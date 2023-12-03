import yaml
import os
import sys
import random

if os.path.exists('source.yaml') == False:
    print('X| Source file is missing!')
    sys.exit(1)

source_file = open('source.yaml', encoding='UTF-8')
source_raw = source_file.read()
source_d = yaml.load(source_raw, yaml.Loader)
# source = {k for k,v in source_d.items()}
# print(source)
source = list(source_d)
source_file.close()
source_rev = [v for k,v in source_d.items()]
source_rev = list(source_rev)
print('''
 __  __ ___ __  __             _   
|  \/  | __|  \/  |___ ___ _ _| |_ 
| |\/| | _|| |\/| (_-</ -_) '_|  _|
|_|  |_|___|_|  |_/__/\___|_|  \__|
                                   ''')
working = True
while working:
    print('(P)ractice or (L)earn?')
    ans = input('? ')
    if ans == 'L':
        print('Press ENTER every time when you need to go next')
        for _ in range(len(source)):
            input(f"{source[_]} = {source_rev[_]}")
    if ans == 'P':
        correct = 0
        incorrect = 0
        ready = []
        for _ in range(len(source)):
            while True:
                r = random.randint(0, len(source)-1)
                if not r in ready: break
            selected = source[r]
            selected_rev = source_rev[r]
            ans = input(f"{selected}: ")
            if ans == selected_rev:
                print('Correct')
                correct += 1
            else:
                print('Incorrect! It\'s ' + selected_rev)
                incorrect += 1
            ready.append(r)
        print(f'{correct} correct, {incorrect} incorrect')