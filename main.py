import os
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter, TokenTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Qdrant
from langchain.schema import Document
import openai
from sklearn.feature_extraction.text import CountVectorizer

# Load medical documents from the specified directory
documents = []
txt_files = os.listdir("/content/drive/MyDrive/HouseArch/pubmed/files")
for filename in txt_files:
    with open(os.path.join("/content/drive/MyDrive/HouseArch/pubmed/files", filename), "r", encoding='latin-1') as f:
        documents.append(f.read())

# Convert the list of strings to a list of Document objects
documents = [Document(page_content=text) for text in documents]

# Split documents into smaller chunks
CHUNK_SIZE = 1500
CHUNK_OVERLAP = 30
text_splitter = CharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
docs = text_splitter.split_documents(documents)

# Embed the text chunks and store them in a Qdrant database
embeddings = OpenAIEmbeddings(model='text-embedding-ada-002')
qdrant = Qdrant.from_documents(docs, embeddings, path="/tmp/local_qdrant", collection_name="housearch", force_recreate=True)

# Perform a similarity search on the vector database
query = "leukemia"
found_docs = qdrant.similarity_search(query, k=2)

# Prepare the prompt for the language model
prompt = f"""
You are a medical assistant. You have a transcript of a consultation between a doctor and a patient. The doctor is diagnosing the patient, who has been feeling very tired and weak. Here is the transcript:

{diarised_transcript}

Based on the transcript and the following relevant medical information, provide a detailed response to help the doctor with the diagnosis and treatment plan:

{found_docs[0].page_content}

Response:
"""

# Generate the response using OpenAI's language model
prompt_json = [{'role': 'user', 'content': prompt}]
model = 'gpt-3.5-turbo-0613'
chat_completion = openai.ChatCompletion.create(model=model, messages=prompt_json, temperature=0, max_tokens=512)
prompt_output = chat_completion.choices[0].message.content

print(prompt_output)
