import random, json

with open('gen/house/name/adjective.txt', 'r') as reader:
    ADJECTIVES = [line.rstrip() for line in reader]
    
with open('gen/house/name/noun.txt', 'r') as reader:
    NOUNS = [line.rstrip() for line in reader]

def get_house_name(seed):
    random.seed(str(seed))
    return random.choice(ADJECTIVES).capitalize() + ' ' + random.choice(NOUNS).capitalize()