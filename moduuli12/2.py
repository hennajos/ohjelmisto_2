import requests

paikkakunta = input("Anna paikkakunta")
pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&units=metric&appid=d5617b002ed2b89c33043122a30586b8"

print(pyyntö)

try:

    vastaus = requests.get(pyyntö)

    if vastaus.status_code==200:

        json_vastaus=vastaus.json()
        print(f"Lämpötila: {json_vastaus ['main'] ['temp']}")
        print(f"Säätila: {json_vastaus ['weather'] [0] ['description']}")


except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa")