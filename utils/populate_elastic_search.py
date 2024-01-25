from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
from utils.indexMapping import indexMapping
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()

# Environment vars
ES_USER = os.getenv('ES_USER')
ES_PW = os.getenv('ES_PW')
ES_CERT = os.getenv('ES_CERT')

es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=(ES_USER, ES_PW),
    ca_certs=ES_CERT
)


def add_data_to_elasticsearch():
    # es.indices.create(index="listings", mappings=indexMapping)

    embedding_df = pd.read_csv("../data/embedded.csv", index_col=0)
    embedding_df.drop(columns=['Unnamed: 0'], inplace=True)
    embedding_df['naturalDescriptionVector'] = embedding_df.naturalDescriptionVector.apply(
        eval).apply(np.array)
    docs = embedding_df.to_dict("records")
    print('Creating docs...\n')
    for doc in docs:
        try:
            es.index(index="listings", document=doc, id=doc["id"])
        except Exception as e:
            print('err: ', e)

    print('-------------------------')


def main():
    # es.indices.delete(index='listings')
    add_data_to_elasticsearch()
    print('Added data to elastic search ✅')
    print(es.count(index="listings"))


if __name__ == "__main__":
    main()
