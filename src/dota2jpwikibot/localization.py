import requests


def _get(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to get localization file")
    return response.json()


print('Downloading localization files...')
dota = _get("https://raw.githubusercontent.com/nihongoka/dota2/master/main/resource/localization/dota_japanese.txt.json") # noqa
