# AI Banking Chatbot

This project is an AI-powered banking assistant chatbot built using **LangChain** and **Azure OpenAI** services. It can handle banking tasks such as checking account balances, reporting card issues, and classifying user intents.

---

## Table of Contents

- [Features](#features)  
- [Project Structure](#project-structure)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Tools](#tools)  
- [Environment Variables](#environment-variables)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Features

- Classifies user intent in banking conversations
- Supports multi-turn conversations with memory
- Checks account balances
- Reports card issues
- Handles unsupported requests gracefully
- Integrates with Azure OpenAI for intelligent responses

---

## Project Structure

AI-AGENT/
│
├── main.py # Entry point: runs the chatbot
├── utils.py # Helper functions and Azure LLM integration
├── Tools.py # Defines tools for agent execution
├── no_llm.py # Placeholder or alternative LLM implementation
├── requirements.txt # Project dependencies
├── .env # Environment variables (not committed)
└── pycache/ # Python cache files

yaml
Copy code

---

## Installation

1. Clone the repository:
```bash
git clone <repository_url>
cd AI-AGENT
Create a virtual environment and activate it:

bash
Copy code
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Add environment variables in .env:

env
Copy code
azure_resource_endpoint=<your_azure_endpoint>
azure_resource_key=<your_azure_key>
model_endpoint=<your_model_endpoint>
model_api_key=<your_model_api_key>
Usage
Run the chatbot:

bash
Copy code
python main.py
Log in with user ID and password (credentials defined in utils.py):

User IDs: Ini, Bolu, Ebuks, Daniel

Passwords: 001, 002, 003, 004

Interact with the bot by typing queries.

Type q or quit to exit.

Example interaction:

pgsql
Copy code
Enter your user ID: Bolu
Enter your password: 002
Welcome Bolu!
You: What is my account balance?
Bot: Your account balance is $420,000
Tools
The chatbot uses the following LangChain tools:

Tool Name	Description
ClassifyIntent	Classifies user intent in banking conversations
CheckBalance	Returns account balance for a given account ID
Report_Card_Issues	Blocks a card and provides next steps
unsupported	Handles unsupported user requests

Environment Variables
azure_resource_endpoint – Azure OpenAI endpoint

azure_resource_key – Azure OpenAI API key

model_endpoint – Endpoint for the intent classification model

model_api_key – API key for the intent classification model

Contributing
Fork the repository

Create a feature branch: git checkout -b feature/my-feature

Commit your changes: git commit -am 'Add new feature'

Push to the branch: git push origin feature/my-feature

Open a pull request

License
--