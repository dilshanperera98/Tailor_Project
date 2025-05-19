import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain          

# Load API keys and DB URI    bhchf
load_dotenv()  
openai_api_key = os.getenv("OPENAI_API_KEY")  gr
mysql_uri = os.getenv("MYSQL_URI")  

# Connect to the MySQL database    
db = SQLDatabase.from_uri(mysql_uri)

# Load the language model
llm = ChatOpenAI(openai_api_key=openai_api_key, model="gpt-4", temperature=0)
  
                  
# Create the LangChain SQL agent
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

# Prompt the user for a financial question
while True:
    question = input("\n💬 Ask a financial question (type 'exit' to quit): ")
    if question.lower() == 'exit':
        break
    response = db_chain.run(question)
    print(f"\n🤖 Answer:\n{response}")  
