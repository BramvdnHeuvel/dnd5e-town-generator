import random

def get_schedule(seed, works_in_tavern=False):
    return [
        (build_time_string(i), s) for i, s in zip(
            range(24), build_schedule(works_in_tavern)
        )
    ]

def translate_schedule(schedule, is_mature, tavern_name):
    def child_filter():
        # Children go to bed early. Yes, even the 99 year old elves!
        for i, s in zip(range(24), schedule):
            if i < 21 or is_mature:
                yield s
            else:
                yield 0

    activity = {
        0: "Asleep",
        1: "Doing nothing in particular",
        2: "At work" if is_mature else "Playing outside",
        3: f"Eating food at the {tavern_name}"
    }
    
    return [(s[0], activity[c]) for s, c in zip(schedule, child_filter())]


def build_schedule(works_in_tavern):
    if works_in_tavern:
        wake_up = random.randint(8, 10)
        work = random.randint(10, 11)
        
        for i in range(24):
            if (i < wake_up and i >= ((wake_up+16)%24)) or i >= wake_up:
                yield 0  # Asleep
            elif i >= work or i < ((work+13)%24):
                yield 2  # At work
            else:
                yield 1  # Doing nothing in particular

    elif random.random() < 0.9:
        # Regular work day
        wake_up = random.randint(5, 8)
        work = random.randint(8, 10)
        lunch = random.randint(11, 14)
        dinner = work + 9

        for i in range(24):
            if i < wake_up or i >= (wake_up + 16):
                yield 0  # Asleep
            elif i in [lunch, dinner]:
                yield 3 # Eating food at the taven
            elif i >= work and i < dinner:
                yield 2 # At work
            else:
                yield 1 # Doing nothing in particular 
    else:
        # A few ones gotta have the messed up rhythm to keep the taverns open.
        wake_up = random.randint(8, 12)
        work = random.randint(13, 15)
        lunch = random.randint(13, 16)
        dinner = work + 7

        for i in range(24):
            if i < wake_up or i >= (wake_up + 16):
                yield 0  # Asleep
            elif i in [lunch, dinner]:
                yield 3 # Eating food at the taven
            elif i >= work and i < dinner:
                yield 2 # At work
            else:
                yield 1 # Doing nothing in particular 

def build_time_string(i):
    early, late = str(i), str((i+1)%24)
    early.zfill(2)
    late.zfill(2)

    return f"{early}:00 - {late}:00"


