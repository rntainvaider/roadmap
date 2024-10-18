import requests


def get_the_smartest_superhero() -> str:
    the_smartest_superhero = {"Hulk": 0, "Captain America": 0, "Thanos": 0}
    # ваш код здесь
    URL = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(URL)

    for hero in response.json():
        name = hero.get("name")
        if name in the_smartest_superhero:
            intelligence = hero.get("powerstats").get("intelligence")
            the_smartest_superhero[name] = intelligence

    max_intelligence = 0
    hero = ""
    for key, value in the_smartest_superhero.items():
        if value > max_intelligence:
            max_intelligence = value
            hero = key
    return hero


if __name__ == "__main__":
    print(get_the_smartest_superhero())
