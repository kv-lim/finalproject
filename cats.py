import csv
import random

cats = []

with open('Cats.csv', 'r') as csv_file:
    spreadsheet=csv.DictReader(csv_file)
    for cat in spreadsheet:
        cats.append(cat)

def random_cat():
    cat_number = random.randint(1, 30)
    return cats[cat_number]

def run():
    my_cat = random_cat()

    print('You were given {}'.format(my_cat['Individual']))
    stat_choice = input('Which stat do you want to use? (Size, Cuteness, Rarity) ')

    opponent_cat = random_cat()
    print('The opponent chose {}'.format(opponent_cat['Individual']))
    my_stat = my_cat[stat_choice]
    opponent_stat = opponent_cat[stat_choice]

    if my_stat > opponent_stat:
        print('You Win!')
    elif my_stat < opponent_stat:
        print('You Lose!')
    else:
        print('Draw!')

run()