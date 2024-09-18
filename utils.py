import os
import openai
import requests
import os
from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI


load_dotenv()
openai_api_key = os.getenv('api_key')



# Specify an embedding model
embedding_model = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Load documents and create an index with the embedding model
loader = TextLoader('questions.txt', encoding='utf-8')
index = VectorstoreIndexCreator(embedding=embedding_model).from_loaders([loader])

def modify_gpt(user_input):
    # Using ChatOpenAI with the loaded API key
    llm = ChatOpenAI(openai_api_key=openai_api_key)
    response = index.query(question=user_input, llm=llm)
    return response


from dotenv import load_dotenv
stablediffusion_api_key = os.getenv('DREAMSTUDIO_KEY')
engine_id = "stable-diffusion-xl-1024-v1-0"
api_host = 'https://api.stability.ai'

def diffusion(prompt):
    import os
    from dotenv import load_dotenv
    load_dotenv()
    stablediffusion_api_key = os.getenv('DREAMSTUDIO_KEY')
    engine_id = "stable-diffusion-xl-1024-v1-0"
    api_host = 'https://api.stability.ai'

    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {stablediffusion_api_key}"
        },
        json={
            "text_prompts": [
                {
                    "text": prompt
                }
            ],
            "cfg_scale": 7,
            "height": 1024,
            "width": 1024,
            "samples": 1,
            "steps": 30,
        },
    )

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        print("Response:", response.json())
        return None

    data = response.json()

    # Check if 'artifacts' key exists in the response
    if 'artifacts' not in data or not data['artifacts']:
        print("Error: 'artifacts' key not found in the response")
        print("Response:", data)
        return None

    return data['artifacts'][0]['base64']




def chatgpt(user_input, system_settings,chunk):
    if chunk:
        content=split_string_into_chunks(user_input,3000)
    else:
        content=[user_input]
    
    for x in content:

        response=openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role':'system','content':system_settings},{'role':'user','content':x}],
            stream=True
        )
        
        for y in response:
            if y.choices[0].finish_reason !='stop':
                yield y.choices[0].delta.content
        if len(content)!=1 and content[-1] !=x:
            yield '\n'
            

    

def split_string_into_chunks(user_input,chunk_size):
    chunks=[]
    string_length=len(user_input)
    for i in range(0,string_length,chunk_size):
        if (i+chunk_size)<=string_length:
            chunks.append(user_input[i:i+chunk_size])
        else:
            chunks.append(user_input[i:string_length])
    return chunks

def translate_keywords(user_input):
    load_dotenv()


    openai.api_key=os.getenv('api_key')
    response=openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role':'system','content':'you will be given a set of keywords . transelate them into english'},{'role':'user','content':user_input}],
        )
    return response['choices'][0]['message']['content']

def transcribe_function(path):
    with open(path,'rb') as audio_file:
        transcript=openai.Audio.transcribe('whisper-1',audio_file)

    return transcript['text']