import requests
from pokemon import pokemon
from vær import vær
from catfact import catfact
lenkeTilApi = "http://api.open-notify.org/astros.json"

def main():
    ting = input("Hva ønsker du å gjøre vær, catfact eller pokeapi")

    if ting == "vær":
        vær()
    elif ting == "catfact":
        catfact()
    elif ting == "pokeapi":
        pokemon()


def hentData(link):
    hentetApi = requests.get(link)
    if hentetApi.status_code == 200:
        return hentetApi.json()
    else:
        print ("All ok med kode"+(hentetApi.status_code))