from fastapi import FastAPI
from openai import OpenAI
import urllib.parse
import json
import os
from elasticsearch import Elasticsearch
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv


load_dotenv()

# Environment vars
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ES_USER = os.getenv('ES_USER')
ES_PW = os.getenv('ES_PW')
ES_CERT = os.getenv('ES_CERT')

# Connect to openAI API
client = OpenAI(api_key=OPENAI_API_KEY)

# Function to get the text embedding of a users input


def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding


# Connect to elasticsearch
es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=(ES_USER, ES_PW),
    ca_certs=ES_CERT
)


def extract_source_data(response):
    result = []
    for item in response:
        if "_source" in item:
            result.append(item["_source"])
    return result


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.get('/listings')
async def filter_listings(filter: str):
    nl_string = urllib.parse.unquote(filter)
    vector_of_input_keyword = get_embedding(nl_string)

    my_prompt = f"""
        bedrooms can be anything from 0 to 20
        bathrooms can be any integer from 0.0 to 20.0
        based on user's search query. give me json output as follows
        {{
            "pets" : "it should be a boolean true or false whether or not the user specified for pets to be allowed, this includes specific pets such as cats and dogs"
            "type" : "it should be an array of strings where the possible values are house, townhouse, apartment, or condo, or any conbination if no preference is mentioned return an array with all possible values"
            "bedrooms": "it should be what the user wants if not mentioned give 0"
            "bathrooms": "it should be what the user wants if not mentioned give 0.0"
            "min_price": "it should be what the user wants if not mentioned give 0"
            "max_price": "it should be what the user wants if not mentioned give 100000"
        }}

        users query : {nl_string}
        """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output only in JSON format. No other text or explaination."},
            {"role": "user", "content": my_prompt}
        ]
    )

    filter_map = json.loads(response.choices[0].message.content)

    print('Filter map ➡️ ', filter_map)

    query = {
        "knn": {
            "field": "naturalDescriptionVector",
            "query_vector": vector_of_input_keyword,
            "k": 10,
            "num_candidates": 100,
        },
        "_source": ["address", "bedrooms", "bathrooms", "size", "type", "neighbourhood", "description", "price", "image", "sponsored", "pets"]
    }

    filter_query = {
        "bool": {
            "must": [
                {
                    "range": {
                        "bedrooms": {
                            "gte": filter_map["bedrooms"] if filter_map["bedrooms"] != 0 else 0,
                            "lte": filter_map["bedrooms"] if filter_map["bedrooms"] != 0 else 20
                        }
                    }
                },
                {
                    "range": {
                        "bathrooms": {
                            "gte": filter_map["bathrooms"] if filter_map["bathrooms"] != 0 else 0.0,
                            "lte": filter_map["bathrooms"] if filter_map["bathrooms"] != 0 else 20.0
                        }
                    }
                },
                {
                    "range": {
                        "price": {
                            "lte": filter_map["max_price"],
                            "gte": filter_map["min_price"]
                        }
                    }
                },
                {
                    "terms": {
                        "type": filter_map["type"]
                    }
                },
            ]
        }
    }

    if filter_map.get("pets") is True:
        filter_query["bool"]["must"].append({
            "match": {
                "pets": "true"
            }
        })

    res = es.knn_search(index="listings",
                        body=query,
                        request_timeout=5000,
                        filter=filter_query)

    return extract_source_data(res["hits"]["hits"])
