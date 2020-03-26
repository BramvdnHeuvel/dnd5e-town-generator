from objects.village import Village as VObject
from config import SECRET as PASSWORD
import time

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