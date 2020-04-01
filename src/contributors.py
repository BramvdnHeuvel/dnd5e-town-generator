import json, time, random
from gen.person.name import get_name_from_race
from gen.house.name import get_house_name

def add_review(shop_type, review, author='Unknown'):
    with open('data/contributions/reviews.json', 'r') as open_file:
        REVIEWS = json.load(open_file)
    REVIEWS.append({
        'shop': shop_type,
        'review': review,
        'author': author if author != '' else 'Unknown'
    })
    with open('data/contributions/reviews.json', 'w') as write_file:
        json.dump(REVIEWS, write_file, ensure_ascii=True, indent=4)

def add_food(food_name, squalid, poor, modest, comfortable, wealthy, aristocratic, rarity, author='Unknown'):
    with open('data/contributions/food.json', 'r') as open_file:
        FOOD = json.load(open_file)
    FOOD.append({
        'food': food_name,
        'prices': {
            'Squalid': squalid,
            'Poor': poor,
            'Modest': modest,
            'Comfortable': comfortable,
            'Wealthy': wealthy,
            'Aristocratic': aristocratic
        },
        'rarity': rarity,
        'author': author if author != '' else 'Unknown'
    })
    with open('data/contributions/food.json', 'w') as write_file:
        json.dump(FOOD, write_file, ensure_ascii=True, indent=4)

def add_occupation(occupation, sv, author='Unknown'):
    with open('data/contributions/occupations.json', 'r') as open_file:
        OCCUPATIONS = json.load(open_file)

        if occupation not in OCCUPATIONS:
            OCCUPATIONS[occupation] = {
                'sv': sv,
                'author': author if author != '' else 'Unknown'
            }
        
    with open('data/contributions/occupations.json', 'w') as open_file:
        json.dump(OCCUPATIONS, open_file, indent=4) 

def get_occups():
    with open('data/commoner-occupations.json', 'r') as open_file:
        JOBS = json.load(open_file)
    
    relevant_jobs = {job: JOBS[job] for job in JOBS if (job == 'Baker' or random.random() < 0.25)}

    return relevant_jobs

def get():
    return json.load(open('data/contributions/contributors.json', 'r'))

def random_names():
    random.seed(time.time())

    return {
        'owner': get_name_from_race('Human', ('male_full' if random.random() < 0.5 else 'female_full')),
        'town': 'Hansborough',
        'shop': get_house_name(time.time())
    }