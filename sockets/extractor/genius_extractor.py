import http.client
from env import env
import json

def extractor(request):

    conn = http.client.HTTPSConnection('genius-song-lyrics1.p.rapidapi.com')

    headers = {
            'X-RapidAPI-Key': f"{env('GENIUS_KEY')}",
            'X-RapidAPI-Host': 'genius-song-lyrics1.p.rapidapi.com'
    }

    requestRoutes = {
        "info": "/artist/details/",
        "álbuns": "/artist/albums/",
        "música": "/artist/songs/",
        "letras": "/song/lyrics/"
    }

    if request['type'] != "letras":

        conn.request("GET",f"/search/?q={request['param'].replace(' ','%20')}&per_page=2&page=1",headers=headers)
        artistRes = conn.getresponse()
        artistData = json.loads(artistRes.read().decode("utf-8"))
        Id = artistData['hits'][0]['result']['primary_artist']['id']

    else:
        Id = request['param']

    url = f"{requestRoutes[request['type']]}?id={Id}"

    if request['type'] ==  "letras" or request['type'] == "info": url += "&text_format=html"
    if request['type'] == "música": url += "&sort=popularity"

    conn.request("GET",url,headers=headers)
    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))
    returnString = ""

    # tratamentos de retorno:
    if request['type'] == "info":
        returnString += 'Nomes alternativos:\n'
        for i in data['artist']['alternate_names']:returnString += f'{i}\n'
        returnString += f"\nDescrição:\n{data['artist']['description']['html']}"
    if request['type'] == "álbuns":
        returnString += "Álbuns:\n"
        for i in data['albums']:
            returnString += f"{i['full_title']}\n"
    if request['type'] == "música":
        returnString += "Algumas das músicas mais populares:\n"
        for i in data['songs']:
            returnString += f"{i['full_title']} - {i['id']}\n"
    if request['type'] == "letras":
        returnString = f"Letras de {data['lyrics']['tracking_data']['title']}:\n\n"
        returnString += data['lyrics']['lyrics']['body']['html']
    
    return returnString