import requests

heroes_dict = {}

def heroes():
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(url).json()
    for hero in response:
        if hero['name'] in ['Hulk', 'Captain America', "Thanos"]:
          heroes_dict.setdefault(hero['name'], hero['powerstats']['intelligence'])
    print(f"Самый умный - {max(heroes_dict)}")

if __name__ == '__main__':
    heroes()