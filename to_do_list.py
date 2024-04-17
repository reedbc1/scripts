import sys
import os

my_list = []

def main(): 
    
    os.system('cls')

    while True:
        print('To-do List')
        i = 1
        if len(my_list) > 0:
            for item in my_list:
                print(f'{i}\t{item}')
                i += 1

        my_input = input('\ntype number to remove item or type task to add to list: ')
        os.system('cls')

        try:
            my_list.pop(int(my_input)-1)
        except:
            if my_input == 'tv':
                tunnel_vision()
            elif my_input == 'exit':
                sys.exit()
            else:
                my_list.append(my_input)

def tunnel_vision():
    i = 0
    while True:
        if len(my_list) == 0:
            print('You have no items! Returning to main:')
            main()
        elif i == len(my_list):
            i = 0
        else: 
            print('\n')
            print(my_list[i])
            x = input('input: skip, done, exit: ')
            os.system('cls')
            if x == 'skip':
                i += 1
            elif x == 'done':
                my_list.pop(i)
            elif x == 'exit':
                main()
            else:
                print('invalid input')

main()
