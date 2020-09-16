import basilica
from basilica import Connection

import os
from dotenv import load_dotenv

load_dotenv()

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY")  # TODO use env var

# with basilica.Connection(BASILICA_API_KEY) as c:

#     print("CONNECTION", type(c))
#     # embeddings = c.embed_sentences(["Hello world!", "How are you?"])

#     sentences = [
#         'This is a sentence!',
#         "this is a similar sentence!",
#         "I don't think this sentence is very similar at all..."
#     ]
#     embeddings = c.embed_sentences(sentences)

#     print(list(embeddings))  # [[0.8556405305862427, ...], ...]

#     embedding = c.embed_sentence("Hello World!!!")
#     breakpoint()

]

    connection = Connection(BASILICA_API_KEY)
    print("CONNECTION", type(connection))


    if __name__ == "__main__":

    sentences = [
'This is a sentence!',
"this is a similar sentence!",
"I don't think this sentence is very similar at all..."
embeddings = connection.embed_sentences(sentences)

print(list(embeddings))  # [[0.8556405305862427, ...], ...]

embedding = connection.embed_sentence("Hello World!!!", model="twitter")
print(type(embedding))  # <class 'list'>
print(type(embedding[0]))  # <class "float">
print(len(embedding))  # 768

breakpoint()
