import json, random

def race_dict(race):
    return json.load(open('gen/age/ages.json', 'r'))[race]

def get_adult(dic):
    return random.randint(dic["maturesAt"], dic["livesUntil"])

def get_partner(age, dic, min_age, max_age):
    if min_age == max_age:
        max_age += 1

    min_age = max(min_age, dic["maturesAt"])
    max_age = min(max_age, dic["livesUntil"])

    p = (age - min_age) / (max_age - min_age)

    return min_age + sum([1 for _ in range(max_age - min_age) if random.random() < p])

def get_parent(dic, children):
    return random.randint(dic["maturesAt"] + max(children), dic["becomesParentUntil"] + min(children))

def get_child(dic):
    return random.randint(0, dic["maturesAt"])

def get_family_ages(size, race):
    dic = race_dict(race)

    if size == 1:
        yield get_adult(dic)
    
    elif size == 2:
        p1 = get_adult(dic)
        p2 = get_partner(p1, dic, p1 // 2 + 7, 2 * (p1 - 7))

        yield p1
        yield p2

    else:
        # They are parents, with at least one child.
        children = [get_child(dic) for _ in range(size - 2)]
        children.sort(reverse=True)
        
        p1 = get_parent(dic, children)
        p2 = get_partner(p1, dic, dic["maturesAt"] + max(children), dic["becomesParentUntil"] + min(children))

        yield p1
        yield p2
        yield from children


if __name__ == '__main__':
    print([p for p in get_family_ages(1, 'Elf')])