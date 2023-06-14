
# setting up the api key 
import os
from getpass import getpass
os.environ["OPENAI_API_KEY"] = getpass("Paste your OpenAI API key here and hit enter:")

# importing the required libraries 
from langchain.docstore.document import Document
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings

# This part  of the code is already executed 
# # Step 1: Convert PDF to text
# import textract
# doc = textract.process("./cucm_b_troubleshooting-guide-1251-extracted (1).pdf")

# # Step 2: Save to .txt and reopen (helps prevent issues)
# with open('./cucm_b_troubleshooting-guide-1251-extracted.txt', 'w') as f:
#     f.write(doc.decode('utf-8'))

# with open('./cucm_b_troubleshooting-guide-1251-extracted.txt', 'r') as f:
#     text = f.read()

# chunks = text_splitter.split_text(text)
from langchain.vectorstores import Chroma
embeddings = OpenAIEmbeddings()
persist_directory = './db/'
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
# documents = []
# for chunk in chunks:
# #  document = Document(page_content=chunk, metadata={"source": f"{i}-pl"} for i in range(len(chunks))])
#  documents.append(document)

# vectordb = Chroma.from_documents(documents=documents, embedding= embeddings,persist_directory=persist_directory)

# vectordb = Chroma.from_texts(chunks, embeddings, metadatas=[{"source": f"{i}-pl"} for i in range(len(chunks))])

from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

system_template="""Use the following pieces of context to answer the users question.
Take note of the sources and include them in the answer in the format: "SOURCES: source1 source2", use "SOURCES" in capital letters regardless of the number of sources.
If you don't know the answer, just say that "I don't know", don't try to make up an answer.
----------------
{summaries}"""
messages = [
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template("{question}")
]
prompt = ChatPromptTemplate.from_messages(messages)

chain_type_kwargs = {"prompt": prompt}

from langchain.chains import RetrievalQAWithSourcesChain
from langchain import OpenAI

chain = RetrievalQAWithSourcesChain.from_chain_type(OpenAI(model_name="gpt-3.5-turbo",temperature=0), chain_type="stuff", retriever=vectordb.as_retriever(),  return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs)

query = "give the complete procedure  for Extracting and analyzing pertinent data includes performing the following tasks?"
result = chain(query)

print(result['question']+":")
print(result['answer'])