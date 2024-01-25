import pandas as pd
from openai import OpenAI
from utils.indexMapping import indexMapping
import os
from dotenv import load_dotenv

load_dotenv()

# Environment vars
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


# Connect to openAI API
client = OpenAI(api_key=OPENAI_API_KEY)


# Function to get the text embedding of a users input
def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding


def add_pets_description(row):
    if row['pets']:
        return row["naturalDescription"] + 'pets allowed'
    else:
        return row["naturalDescription"] + 'no pets allowed'


# Get embeddings of our csv dataset
def create_embeddings_of_dataset():
    df = pd.read_csv("../data/fake_properties_dataset.csv")
    df.dropna(inplace=True)
    # Create custom column with descriptor data, this is the col we will get vector embeddings of
    df["naturalDescription"] = df["neighbourhood"] + df["description"] + \
        df['bedrooms'].astype(str) + ' bedrooms ' + \
        df["bathrooms"].astype(str) + ' bathrooms '
    df["naturalDescription"] = df.apply(add_pets_description, axis=1)
    df['naturalDescriptionVector'] = df.naturalDescription.apply(
        lambda x: get_embedding(x, model='text-embedding-ada-002'))
    df.to_csv('embedded.csv', index=True)
    print("CSV file saved successfully")
    print(df.head(2))


def main():
    print('Running embedding script...')
    create_embeddings_of_dataset()


if __name__ == "__main__":
    main()
