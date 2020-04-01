import random, json

def get_review(shop):
    with open('data/reviews.json', 'r') as open_file:
        REVIEWS = json.load(open_file)

    try:
        r = random.choice(REVIEWS[shop.occupation])
    except KeyError:
        return None
    else:
        r = shop.name.join(r.split('<SHOP>'))
        r = shop.inhabitants[0].name.join(r.split('<OWNER>'))
        r = shop.seed[1].join(r.split('<TOWN>'))
        return r
