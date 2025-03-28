import random

def pc_guess_number(x):
    print('====================')
    print('Welcome to the game')
    print('====================')
    print(f'Think of a number between 1 and {x} for the PC to guess')
    
    lower_bound = 1
    upper_bound = x
    answer = ''
    
    while answer != 'c':
        if lower_bound != upper_bound:
            guess = random.randint(lower_bound, upper_bound)
        else:
            guess = lower_bound
            
        answer = input(f"My guess is {guess}. If it's too high, type (H). If it's too low, type (L). If it's correct, type (C): ").lower()
        
        if answer == 'h':
            upper_bound = guess - 1
        elif answer == 'l':
            lower_bound = guess + 1
            
    print(f"WoHoo! The computer guessed your number correctly: {guess}")   
    
pc_guess_number(10)