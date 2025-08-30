import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

load_dotenv("config/.env")


# Try both possible env variable names for compatibility
geminiapi_key = os.getenv("geminiapi_key") or os.getenv("GOOGLE_API_KEY")

# Raise error if API key is missing
if not geminiapi_key:
    raise ValueError("Google Gemini API key not found in environment variables.")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=geminiapi_key,
    temperature=0.7
)

def generate_name(cuisine):
    # Prompt 1 → Generate restaurant name
    prompt_temp = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. "
                 "Suggest a catchy name for the restaurant."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_temp, output_key='restaurant_name')

    # Prompt 2 → Generate menu items based on restaurant name
    prompt_temp_item = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some popular menu items for a restaurant named {restaurant_name}."
    )
    item_chain = LLMChain(llm=llm, prompt=prompt_temp_item, output_key='menu_items')

    # Sequential Chain
    chain = SequentialChain(
        chains=[name_chain, item_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items'],
        verbose=True
    )

    # Call the chain with a dictionary input
    response = chain({"cuisine": cuisine})
    return response
