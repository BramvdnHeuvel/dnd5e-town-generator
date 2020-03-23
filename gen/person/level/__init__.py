import random

def get_level(seed, class_name, is_mature):
    random.seed(str(seed))

    if class_name == 'Commoner':
        return 1
    
    level = 1
    while random.random() < 0.7 and level < 20:
        level += 1
    
    return level