import Levenshtein
import requests
import json
import re

# armars
# mapas
# agentes 
# ???


"""
request['type'] - tipo da rota
request['id'] - id do objeto de pesquisa (não vem do front)
request['search'] - string de pesquisa
"""

def getRequest(request,full=False):

    header = "https://valorant-api.com/v1/"
    
    requestRoutes = {
        "armas": "weapons/",
        "mapas": "maps/",
        "agentes": "agents/",
        "": "," # adicionar rota
    }

    url = f"{header}{requestRoutes[request['type']]}"

    if not full:
       url =  f"{url}{request['id']}"


    url = f"{url}/?language=pt-BR"

    if request['type'] == "agentes":
        url = f"{url}&isPlayableCharacter=true"
    
    return requests.get(url).json()

def levenshteinDistance(wordList, searchWord, k):
    lowerSearchWord = searchWord.lower()
    
    # procura palavras similares a palavra de pesquisa com um grau de diferença (k)
    result = [word for word in wordList if Levenshtein.distance(word.lower(), lowerSearchWord) <= k]
    
    return result

def extractor(request):

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
    return returnString