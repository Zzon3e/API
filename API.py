import requests
from pokemon import pokemon

lenkeTilApi = "http://api.open-notify.org/astros.json"

def main():
    ting = input("Hva ønsker du å gjøre vær, catfact eller pokeapi")

    if ting == "vær":
        vær = hentData("https://api.openweathermap.or") ["26c9ad7e0adb187c0a7f698500326784"]
    elif ting == "catfact":
        catfact = hentData("https://catfact.ninja/fact")["fact"]
    elif ting == "pokeapi":
        pokemon()


def hentData(link):
    hentetApi = requests.get(link)
    if hentetApi.status_code == 200:
        return hentetApi.json()
    else:
        print ("All ok med kode"+(hentetApi.status_code))