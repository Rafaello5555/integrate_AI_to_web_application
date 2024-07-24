from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models import ModelInference


#Project credentials
#ENDPOINT url
#The following URL represents the base URLs for the watsonx.ai API endpoints. When you call the API, use the URL and add the path for each method to form the complete API endpoint for your requests.
credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": ""
 
}


project_id = "c31bf9af-7319-429d-9a09-ed3b00280b9f"


#Tokenazitation
""" Word Tokenaziation,
    Character tokenization 
    
    
    
    
    The primary goal of tokenization is to represent text in a manner that's meaningful for machines without losing its context. 
    By converting text into tokens, algorithms can more easily identify patterns. This pattern recognition is crucial because it makes it possible for machines to understand and respond to human input. 
    For instance, when a machine encounters the word "running", it doesn't see it as a singular entity but rather as a combination of tokens that it can analyze and derive meaning from. """


# Segt up LLM parameters 
#Decoding is process of  choosing highest probability of token in genrated output
parameters = {
    GenParams.DECODING_METHOD: "greedy",
    GenParams.MAX_NEW_TOKENS: 256,
    GenParams.TEMPERATURE:0.1
}


#Setup model objects

llama2_model_id = ModelTypes.LLAMA_2_70B_CHAT


llama2_model = ModelInference(
    model_id=llama2_model_id,
    params=parameters,
    credentials=credentials,
    project_id=project_id)




