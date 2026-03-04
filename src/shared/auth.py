from azure.identity import DefaultAzureCredential
import os

def get_token():
    credential = DefaultAzureCredential()
    token = credential.get_token("https://graph.microsoft.com/.default")
    return token.token
