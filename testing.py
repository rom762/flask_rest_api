import requests
from faker import Faker
import uuid
from random import randint


def post_data(item):
    headers = {"Content-type": "application/json"}
    resp = requests.post('http://127.0.0.1:5555', headers=headers, json=item)
    return resp.json()


def make_items(counter: int = 10):
    results = []
    fake = Faker()
    for _ in range(counter):
        results.append(
            {
                'game_id': str(uuid.uuid4()),
                'home_team': fake.company(),
                'home_score': randint(1,10),
                'away_team': fake.company(),
                'away_score': randint(1,10)
            }
        )
    return results


for item in make_items():
    print(item)
    print(post_data(item))
