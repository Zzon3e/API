from API import hentData
def vær():
    vær = hentData("https://api.openweathermap.org/data/3.0/onecall?lat=60&lon=10&appid=26c9ad7e0adb187c0a7f698500326784")
    data = vær["main"]["temp"]
    print(data)