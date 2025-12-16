import requests

lenkeTilApi = "http://api.open-notify.org/astros.json"

def main():
    ting = input("Hva ønsker du å gjøre")

    if

    vær = hentData("") #["main"]["temp"]
    catfact = hentData("https://catfact.ninja/fact")["fact"]


def hentData(link):
    hentetApi = requests.get(link)
    if hentetApi.status_code == 200:
        return hentetApi.json()
    else:
        print ("All ok med kode"+(hentetApi.status_code))