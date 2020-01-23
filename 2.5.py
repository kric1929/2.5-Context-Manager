import datetime

class MyOpen:

    def __init__(self, path, method):
        self.path = path
        self.method = method

    def __enter__(self):
        self.start_time = datetime.datetime.now()
        print(self.start_time)
        self.file = open(self.path, self.method, encoding='utf8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.exit_time = datetime.datetime.now()
        print(self.exit_time)
        dif_time = self.exit_time - self.start_time
        print(dif_time)

if __name__ == '__main__':

    with MyOpen('recipes.txt', 'r') as f:
        cook_book = {}
        while True:
            dish = f.readline().strip()
            cook_book[dish] = []
            person = f.readline().strip()
            i = 0
            while i < int(person):
                ingredients = f.readline().strip().split(' | ')
                cook_book[dish].append({'ingredient_name': ingredients[0], 'quantity': int(ingredients[1]),
                                        'measure': ingredients[2]})
                i += 1
            if f.readline() == '\n':
                continue
            else:
                break
