import os, json, requests
import pickle
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_classic.agents import AgentExecutor, Tool
from langchain_classic.prompts import PromptTemplate
import azure.cognitiveservices.speech as speech
from langchain_classic.agents.mrkl.base import ZeroShotAgent

load_dotenv()

accounts = {
        "001":{"name":"Ini", "balance":200000},
        "002":{"name":"Bolu", "balance":420000},
        "003":{"name":"Ebuks", "balance":3000000},
        "004":{"name":"Daniel", "balance":250000}
    }


def login(user_id:str, password:str):
    users_db = {
        "Ini":{"password":"001"},
        "Bolu":{"password":"002"},
        "Ebuks":{"password":"003"},
        "Daniel":{"password":"004"}
    }

    user = users_db.get(user_id)
    if user and user["password"] == password:
        return {"status":"success", "user_id":user_id, "name":user_id}
    
    else:
        return {"status":"failure", "message":"Invalid credentials."}
    

def classify_intent(text:str, confidence_threshold=0.6):
    model_api_endpoint = os.getenv("model_endpoint")
    model_api_key = os.getenv("model_api_key")

    response = requests.post(
        url=model_api_endpoint,
        json={"text": text},
        headers={"Content-Type":"application/json", "Authorization": f"Bearer {model_api_key}"}
    )

    data = dict(response.json())
    print(data)

    confidence = max(data['probabilities']) 
    predicted_class = data['prediction']
    
    if confidence >= confidence_threshold:
        return predicted_class
    else:
        return "unsupported"



def azure_llm():
    llm = AzureChatOpenAI(
        azure_endpoint=os.getenv("azure_resource_endpoint"),
        api_key=os.getenv("azure_resource_key"),
        api_version="2024-12-01-preview",
        temperature=0,
        azure_deployment="gpt-4o-mini"
    )

    return llm

def extract_account_id(text:str):
    import re
    match = re.search(r'\b(\d{3})\b', text)
    return match.group(1) if match else None

def check_balance(account_id:str):
    global accounts
    acct = accounts.get(extract_account_id(account_id))
    if not acct:
        return {"status":"failure", "message":"Invalid account number"}
    return {"account_id":account_id, "balance":acct["balance"]}
    
def report_card_issues(account_id:str):
    # Simulate blocking card
    return {"status":"blocked", "account_id":account_id, "next_step":"Collect new card in 48 hours"}

def unsupported(text:str=""):
    return {"status":"unsupported"}

