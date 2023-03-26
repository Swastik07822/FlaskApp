import requests
from customize import customize

def get_weather(place):
    i = requests.get("http://api.weatherstack.com/current?access_key=ccf2d3b290bd33c9be211b4605cb254d&query="+place+"'").json()
    i,j,k = customize(i)
    
    return i,j,k

    
    
