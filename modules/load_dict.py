import json
import os

def load_dict():
    path = os.path.abspath('dictionary.json')
    with open('modules/dictionary.json', 'r') as f:
        return json.load(f)


def update_dict(new_dict):
    with open('modules/dictionary.json', 'w') as f:
        to_save = json.dumps(new_dict, ensure_ascii=False)
        f.write(to_save)
