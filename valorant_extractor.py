from gpt_api import Gptapi
import requests
import json
import re

"""
request['type'] - tipo da rota
request['id'] - id do objeto de pesquisa (não vem do front)
request['search'] - string de pesquisa
"""

def getGPTRequest(request):
    gpt = Gptapi()
    return gpt.send_message(request['msg'])


def getRequest(request,full=False):

    header = "https://valorant-api.com/v1/"
    
    requestRoutes = {
        "armas": "weapons",
        "mapas": "maps",
        "agentes": "agents"
    }

    #if request['type'] == "chat": 
    #    return Gptapi.send_message(request['msg'])

    url = f"{header}{requestRoutes[request['type']]}"

    if not full:
       url =  f"{url}/{request['uuid']}"

    url = f"{url}?language=pt-BR"

    if request['type'] == "agentes":
        url = f"{url}&isPlayableCharacter=true"
    
    response = requests.get(url)
    return response.json()

def fullExtractor(request):
    return getRequest(request,full=True) 

def singleExtractor(request):
    return getRequest(request,full=False) 

"""
def levenshteinDistance(wordList, searchWord, k):
    lowerSearchWord = searchWord.lower()
    
    # procura palavras similares a palavra de pesquisa com um grau de diferença (k)
    result = [word for word in wordList if Levenshtein.distance(word.lower(), lowerSearchWord) <= k]
    
    return result
"""
"""
def Extractor(request):

    fullResponse = getRequest(request,full=True)
    data = json.load(fullResponse)

    displayNames = []
    for i in data['data']: displayNames.append(i['displayName'])
    nameSearch = levenshteinDistance(displayNames,request['search'],2)

    if nameSearch == []: return 'mensagem de objeto não encontrado'

    #if len(search) > 1: tratamento para search > len de 1

    for i in data['data']: 
        if i['displayName'] == nameSearch: request['id'] = i['uuid']

    finalResponse = getRequest(request,full=True)
    data = json.load(finalResponse)

    # tratamento de retorno de finalResponse
    returnString = ''

    if request['type'] == "agentes":


    return returnString
"""
