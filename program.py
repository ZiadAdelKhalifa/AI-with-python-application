from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI
load_dotenv()

loader=TextLoader('questions.txt',encoding='utf-8')
index=VectorstoreIndexCreator().from_loaders([loader])

userinput=input('user: ')

response=index.query(question=userinput,llm=ChatOpenAI())