import requests

url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'
token = 'dict.1.1.20240904T125102Z.166aa9983bc9e2ba.4f0bfb992f813c14864952dd1815d97961941bd1'


def translate_word(word: str) -> str:
    params = {"key": token, "lang": 'ru-en', "text": word}
    response = requests.get(url, params=params)
    result = response.json()
    trans_word = result.get('def')[0]['tr'][0]['text']
    
    return trans_word

if __name__ == '__main__':
    word = 'Производитель'
    print(translate_word(word))
