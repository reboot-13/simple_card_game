class Player (object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ': \n' + str (self.score)
        return  rep


def yes_or_no(question):
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

if __name__ == '__main__':
    print('Вы запустили этот модуль напрямую, а не имортировали его.')
