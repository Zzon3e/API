from API import hentData
def pokemon():
    pokeapi = hentData("https://pokeapi.co/api/v2/pokemon/pikachu")
    vekt = pokeapi["weight"]
    høyde = pokeapi["height"]
    print (vekt)
    print (høyde)
    

