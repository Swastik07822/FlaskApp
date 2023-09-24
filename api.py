import requests
from customize import customize

def get_weather(place):
    i = requests.get("http://api.weatherstack.com/current?access_key=&query="+place+"'").json()
    i,j,k = customize(i)
    
    return i,j,k

    
    
