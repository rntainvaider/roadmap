import requests

def get_the_smartest_superhero(superheros: list):
    the_smartest_superhero = ''
    URL = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(URL)
    max_intelligence = 0
    for hero in response.json():
        name = hero.get("name")
        id = hero.get("id")
        intelligence = hero.get('powerstats').get("intelligence")
        if id in superheros:
            if intelligence > max_intelligence:
                max_intelligence = intelligence
                the_smartest_superhero = name
    return the_smartest_superhero
if __name__ == "__main__":
    print(get_the_smartest_superhero([332, 149, 655]))