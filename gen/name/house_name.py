import random

class HouseNameBuilder:
    def __init__(self):
        with open('gen/name/adjective.txt', 'r') as reader:
            self.adjc = [line.rstrip() for line in reader]
        with open('gen/name/noun.txt', 'r') as reader:
            self.noun = [line.rstrip() for line in reader]
    
    def create_name(self):
        return (
            random.choice(self.adjc).capitalize()
              + ' ' 
              + random.choice(self.noun).capitalize()
        )

get = HouseNameBuilder().create_name

if __name__ == '__main__':
    for _ in range(5):
        print(get())