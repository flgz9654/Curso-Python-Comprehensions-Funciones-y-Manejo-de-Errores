import  random

def choose_option():
    
    options = ('piedra', 'papel', 'tijera')
    user = input('Elige: piedra, papel o tijera => ')
    user = user.lower()
    
    if not user in options:
        print('Esa opcion no es valida')
        # continue
        return None, None
    
    computer_option = random.choice(options)
    print('User Option =>', user)
    print('Computer Option =>', computer_option)
    return user, computer_option

def check_rules(user, computer_option, user_wins, computer_wins):
    if user  == computer_option:
        print('\nEmpate!')
        
    elif user == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('\nGanaste! 🎉')
            user_wins += 1
        else:
            print('papel gana a piedra')
            print('\nComputer Gano! 🥲')
            computer_wins += 1
            
    elif user == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('\nGanaste! 🎉')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('\nComputer Gano! 🥲')
            computer_wins += 1
            
    elif user == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('\nGanaste! 🎉')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('\nComputer Gano! 🥲')
            computer_wins += 1
    return user_wins, computer_wins


def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        
        print('\n')
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)
        print('Puntuacion: ')
        print('computer_wins', computer_wins)
        print('user_wins', user_wins)
        rounds += 1

        user, computer_option = choose_option()
        user_wins, computer_wins = check_rules(user, computer_option, user_wins, computer_wins)

            
        if computer_wins == 2:
            print('\nEl ganador final es Computer')
            break
        
        if user_wins == 2:
            print('\nEl ganador final es User')
            break

run_game()