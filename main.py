import yaml
import os
import sys
import random
import platform

host_platform = platform.system()
clear_screen_command = ''
if host_platform == 'Windows':
    clear_screen_command = 'cls'
else:
    clear_screen_command = 'clear'

def clear_screen():
    os.system(clear_screen_command)
    print('''
     __  __ ___ __  __             _   
    |  \/  | __|  \/  |___ ___ _ _| |_ 
    | |\/| | _|| |\/| (_-</ -_) '_|  _|
    |_|  |_|___|_|  |_/__/\___|_|  \__|
                                       ''')


if os.path.exists('sources') == False:
    print('X| Sources folder is missing!')
    sys.exit(1)

clear_screen()

while True:
    active_source_name = input("Choose a source (without .yaml): ")

    if not os.path.exists(f"sources/{active_source_name}.yaml"):
        print('This source file doesn\'t exists')
    else: break

source_file = open(f"sources/{active_source_name}.yaml", encoding='UTF-8')
source_raw = source_file.read()
source_d = yaml.load(source_raw, yaml.Loader)
## source = {k for k,v in source_d.items()}
## print(source)
# source = list(source_d)
source_file.close()
# source_rev = [v for k,v in source_d.items()]
# source_rev = list(source_rev)
learn_words = source_d['learn']
# learn_answers = {v:k for k,v in learn_words.items()}
learn_words = list([k for k,v in learn_words.items()])
learn_answers = list([v for k,v in source_d['learn'].items()])
test_words = list([k for k,v in source_d['test'].items()])
test_answers = list([v for k,v in source_d['test'].items()])

for _ in learn_words: test_words.append(_)
for _ in learn_answers: test_answers.append(_)

clear_screen()

working = True
while working:
    print('(P)ractice or (L)earn?')
    ans = input('? ')
    clear_screen()
    if ans.lower() == 'l':
        print('Press ENTER every time when you need to go next')
        # for _ in range(len(learn_words)):
        #     while True:
        #         input(f"{learn_words[_]} = {learn_words_rev[_]}")
        #         ans = input(f'What\'s {learn_words[_]}? ')
        #         if ans == learn_words_rev[_]:
        #             break
        #         else:
        #             print('Incorrect! Let\'s try again.')
        for _ in range(len(learn_words)):
            while True:
                input(f"{learn_words[_]} = {learn_answers[_]}")
                clear_screen()
                ans = input(f'What\'s {learn_words[_]}? ')
                if ans == learn_answers[_]:
                    print('Yes, it\'s right!')
                    break
                else:
                    print('Wrong! Let\'s try again.')
    if ans.lower() == 'p':
        message = None
        correct = 0
        incorrect = 0
        ready = []
        for _ in range(len(test_words)):
            while True:
                r = random.randint(0, len(test_words)-1)
                if not r in ready: break
            selected = test_words[r]
            selected_rev = test_answers[r]
            print(f"{correct} right | {incorrect} wrong")
            if message: print(f"{message}")
            else: print('===== ------ ====')
            ans = input(f"{selected}: ")
            clear_screen()
            if ans == selected_rev:
                message = '===== Right! ===='
                correct += 1
            else:
                message = '=== Wrong! It\'s ' + selected_rev
                incorrect += 1
            ready.append(r)

        print(f'{correct} right answers and {incorrect} wrong')
        if incorrect == 0:
            print('You\'re a CHAMPION! Don\'t stop to be the best!')
        elif correct == 0:
            print('It\'s sad, but it seems that language learning isn\'t very interesting for you')
        elif correct < incorrect:
            print('You need to learn a more...')
        elif correct == incorrect:
            print('You have a result!')
        elif correct > incorrect:
            print('Nice result! You\'re learning good!')