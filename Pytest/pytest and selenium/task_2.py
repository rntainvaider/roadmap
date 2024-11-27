import requests

URL = "https://cloud-api.yandex.net/v1/disk/resources"
TOKEN = "y0_AgAAAAAsCrTZAAzZwQAAAAEaHCJKAACWjRFOg6BGu65Hq4hMUy1astWjqw"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"OAuth {TOKEN}",
}


def create_folder(path: str) -> requests.Response:
    response = requests.put(f"{URL}?path={path}", headers=HEADERS)
    return response


def get_info_folder(path: str) -> requests.Response:
    response = requests.get(f"{URL}?path={path}", headers=HEADERS)
    return response
