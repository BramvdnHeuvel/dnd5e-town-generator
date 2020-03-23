import random, json

with open('gen/name/adjective.txt', 'r') as reader:
    ADJECTIVES = [line.rstrip() for line in json.load(reader)]
    
with open('gen/name/noun.txt', 'r') as reader:
    NOUNS = [line.rstrip() for line in json.load(reader)]

def get_house_name(seed):
    random.seed(str(seed))
    return random.choice(ADJECTIVES) + ' ' + random.choice(NOUNS)