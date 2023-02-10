# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 10:32:34 2022

@author: SmartBridge-PC
"""

import requests

import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "a4hY8b_3PvNDBVOmekwxAJuLoP_kIRhjOYcUVYwFBQZv"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [['goitre','tumor','hypopituitary','psych','TSH','T3','TT4','T4U','FTI','TBG']], "values": [[0,0,0,0,0.000000,0.0,0.0,1.00,0.0,40.0]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/93c0fb0f-c7b4-4dbd-a280-8fb0bcee2d8d/predictions?version=2022-07-01', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())