import random, json

with open('data/inventory.json', 'r') as open_file:
    OPTIONS = json.load(open_file)

def get_inventory(seed, is_mature):
    random.seed(str(seed))
    if is_mature:
        return random.choice(OPTIONS)
    else:
        return '--'