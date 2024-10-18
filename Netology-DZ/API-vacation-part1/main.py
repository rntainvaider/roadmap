import requests


def find_uk_city(coordinates:list) -> str:
    """Ваш код здесь"""
    url = f"https://geocode.maps.co/reverse"
    api_key = "66d9a3f5c4319937392825zyf4dbcfb"
    uk_cities = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']
    for latitude, longitude in coordinates:
        params = {"lat": latitude, "lon": longitude, api_key: api_key}
        response = requests.get(url, params=params).json()
        city = response.get("address").get("city")
        if city in uk_cities:
            return city

if __name__ == '__main__':
    coordinates = [
        ('55.7514952', '37.618153095505875'),
        ('52.3727598', '4.8936041'),
        ('53.4071991', '-2.99168')
    ]
    assert find_uk_city(coordinates) == 'Liverpool'