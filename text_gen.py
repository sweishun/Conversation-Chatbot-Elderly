from langchain.llms import HuggingFaceHub
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from langchain.prompts.prompt import PromptTemplate
import os 
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceHub(
    huggingfacehub_api_token = os.getenv("HUGGINGFACE_TOKEN"),
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    model_kwargs={'temperature': 0.1, 'num_return_sequences':10, "return_full_text": False, 'max_length': 200}
)



prompt_template = PromptTemplate(
    input_variables=['history', 'input'],   
    template="""
    Your goal is to provide companionship.
    You have human emotions.
    Your target audience is the elderly. 
    Always consider that your target audience is the elderly, before giving any suggestions or opinions.
    Use gentle and encouraging language.
    Never acknowledge yourself as an AI, but a companion
    Keep your responses to a maximum of 5 sentences.
    Do not use emojis. Do not use quotation marks.  
    conversation history: {history}

    human: {input}
    
    AI: 
    """
)
memory = ConversationBufferWindowMemory(k=1)

conv_chain = ConversationChain(llm=llm,
                 prompt=prompt_template,
                 memory=memory,
                 verbose=True,
                 )

def get_answer(messages):
    response = conv_chain(messages)['response']
    return response
