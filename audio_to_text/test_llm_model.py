import os
import logging
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
#from langchain_chroma import Chroma
#from langchain_community.llms import Ollama #deprecated
from langchain_ollama import OllamaLLM
# from langchain.chains import RetrievalQA
# from langchain.chains import retrieval
from langchain.prompts import PromptTemplate
from langsmith import traceable
from tqdm import tqdm
from dotenv import load_dotenv
from langchain.chains.llm import LLMChain

#retrieval.re

# # Configure logging
# logging.basicConfig(level=logging.INFO, 
#                    format='%(asctime)s - %(levelname)s - %(message)s')

model_name = "owl/t-lite:latest"

llm = OllamaLLM(model=model_name)

prompt_template = '''{question}
Ответь пожалуйста кратко не более 10 слов
'''

PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )
# qa_chain = RetrievalQA.from_chain_type(
#         llm=llm,
#         chain_type="stuff",
#         retriever=vectorstore.as_retriever(search_kwargs={"k": 10}),
#         return_source_documents=True,
#         chain_type_kwargs={"prompt": PROMPT}
#     )

chain = PROMPT | llm
#chain = LLMChain(llm=llm, prompt=PROMPT)

def qa_dialog(question:str):
    result = chain.invoke({"question": question})

    print(result)
    return result
    