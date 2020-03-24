from objects.village import CLASS_WITH_COMMONERS
import json

def iter_over_people(village, class_name, skip_to_page=-1):
    people_left = 50*skip_to_page
    skip_at_all = skip_to_page == -1

    def people_gen(p, class_name):
        for n in village.neighbourhoods:
            if class_name=='Commoner':
                for clss in CLASS_WITH_COMMONERS:
                    for house in n.houses[clss]:
                            for person in house.inhabitants:
                                if person.class_name == 'Commoner':
                                    p += -1
                                    if p < 0:
                                        yield person
            else:
                for house in n.houses[class_name]:
                    for person in house.inhabitants:
                        if person.class_name == class_name:
                            p += -1
                            if p < 0:
                                yield house.inhabitants[0]

    if not skip_at_all:
        return [person for person, _ in zip(people_gen(people_left, class_name), range(50))]
    else:
        return [person for person in people_gen(people_left, class_name)]    