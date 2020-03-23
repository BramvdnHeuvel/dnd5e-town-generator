import random, json

with open('data/inventory.json', 'r') as open_file:
    OPTIONS = json.load(open_file)

def get_inventory(seed):
    random.seed(str(seed))
    return random.choice(OPTIONS)
