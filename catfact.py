from API import hentData
def catfact():
    catfact = hentData("https://catfact.ninja/fact")["fact"]
    print(catfact)