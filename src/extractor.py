import json

with open('data/occupations.json', 'r') as open_file:
    occup_dic = json.load(open_file)
    CLASS_WITH_COMMONERS = [occup for occup in occup_dic if occup_dic[occup]['family'] or occup == 'Commoner']

def iter_over_people(village, class_name, skip_to_page=-1):
    people_left = 50*skip_to_page
    skip_at_all = skip_to_page == -1

    def people_gen(p, class_name):
        for n in village.neighbourhoods:
            if class_name=='Commoner':
                for class_name in CLASS_WITH_COMMONERS:
                    for house in n.houses[class_name]:
                        for person in house.inhabitants:
                            if person.class_name == 'Commoner':
                                p += -1
                                if p < 0:
                                    yield person
            else:
                for house in n.houses[class_name]:
                    p += -1
                    if p < 0:
                        yield house.inhabitants[0]

    
    return [person for person, _ in zip(people_gen(people_left, class_name), range(50))]
        