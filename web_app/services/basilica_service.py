
# python web_app/services/basilica_service.py

import basilica
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BASCILICA_API_KEY")

connection = basilica.Connection(API_KEY)

if __name__ == "__main__":
    print(type(connection))
    print("----------")


    sentence = "Hello again!"
    print(sentence)
    embeddings = connection.embed_sentence(sentence)
    print("----------")


    sentences = ["Hello world!", "How are you?"]
    print(sentences)
    embeddings = connection.embed_sentences(sentences)
    print(list(embeddings)) # [[0.8556405305862427, ...], ...]