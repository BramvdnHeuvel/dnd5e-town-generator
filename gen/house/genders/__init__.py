import random

GENDERS = ["Male", "Female"]

def get_genders(seed, size):
    random.seed(str(seed))

    if size == 1:
        return [random.choice(GENDERS)]

    gen = ['Male', 'Female']
    random.shuffle(gen)

    if random.random() < 0.1:
        # Gay family
        gen[0] = gen[1]
    
    for _ in range(size-2):
        gen.append(random.choice(GENDERS))