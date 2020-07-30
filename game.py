# Write your code here
import random

answers = ('rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water',
           'dragon', 'devil', 'lightning', 'gun')
relait = {'rock': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
          'fire': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],
          'scissors': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
          'snake': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
          'human': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
          'tree': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
          'wolf': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
          'sponge': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
          'paper': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
          'air': ['water','dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
          'water': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
           'dragon': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
          'devil': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
          'lightning': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
          'gun': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf']}


def read_rating():
    f_rating = open('rating.txt', 'r', encoding='utf-8')
    if f_rating:
        rating = dict()
        for line in f_rating.readlines():
            scores = line.strip('\n')
            scores = scores.split(' ')
            rating[scores[0]] = int(scores[1])
    else:
        rating = dict()
    f_rating.close()
    return rating


def game_round(user_in, comp_hit):
    if user_in in relait[comp_hit]:
        print(f'Sorry, but computer chose {comp_hit}')
        return -1
    elif comp_hit in relait[user_in]:
        print(f"Well done. Computer chose {comp_hit} and failed")
        return 1
    elif user_in == comp_hit:
        print(f"There is a draw ({user_in})")
        return 0
    else:
        print("Invalid input")


def game_menu():
    name = input("Enter your name: ")
    print(f"Hello, {name}")
    score_table = read_rating()
    if name in score_table:
        print(f"Your rating: {score_table[name]}")
    else:
        score_table[name] = 0
    Gamer(name, score_table[name])


def update_rating(table):
    f_rating = open('rating.txt', 'w', encoding='utf-8')
    for name in table:
        print(name, table[name], file=f_rating)
    f_rating.close()


class Gamer:
    score_table = read_rating()
    options = ['rock', 'scissors', 'paper']

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.options = Gamer.options
        self.another_opt()
        self.user_menu()

    def another_opt(self):
        in_options = input()
        if in_options:
            self.options = [x for x in in_options.split(',')]
        print()
        print("Okay, let's start")

    def user_menu(self):
        action = input()
        if action == '!rating':
            print(f"Your rating: {self.score}")
            self.user_menu()
        elif action == '!exit':
            print("Bye!")
            exit()
        elif action in self.options:
            comp_choise = random.choice(self.options)
            result = game_round(action, comp_choise)
            if result == 1:
                self.score += 100
                Gamer.score_table[self.name] = self.score
                update_rating(Gamer.score_table)
            elif result == 0:
                self.score += 50
                Gamer.score_table[self.name] = self.score
                update_rating(Gamer.score_table)
            else:
                pass
            self.user_menu()
        else:
            print("Invalid input")
            self.user_menu()


game_menu()

