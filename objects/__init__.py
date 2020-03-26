from objects.village import Village as VObject
import time

# Hey there! This is the generator's "password".
PASSWORD = "CHANGE-ME"
# The idea is that two users will only generate the exact same towns
# if they use the exact same PASSWORD value.
# Very useful if you're a DM and you don't want your players
# to look up any data: if they use a different PASSWORD,
# they'll generate a different city, even if they use
# the same name and the same size.

MANAGER = {}
TIMES = {}

def Village(name, size):
    seed = f"{name}-{size}"
    TIMES[seed] = time.time()

    if seed not in MANAGER:
        MANAGER[seed] = VObject(name, size, PASSWORD)
    
    return MANAGER[seed]

def clean_tree():
    # Clean memory: remove villages that haven't been inspected for a while.
    to_remove = []

    for seed in MANAGER:
        if (time.time() - TIMES[seed]) > 1: #(5 * 60):
            to_remove.append(seed)
    
    for seed in to_remove:
        print(f'Removing {seed}!')
        del MANAGER[seed]
        del TIMES[seed]