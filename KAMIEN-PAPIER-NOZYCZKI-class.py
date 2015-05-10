#to do: ramka - mnozenie str
import random
import os
import userchoice
from userchoice import user_input

def check_choices(user_choice, computer_choice, optionslist, game_output):
    if user_choice + computer_choice in optionslist:
        print ('Wynik rozgrywki: ' + game_output + '\n')
        return True
    return False

def computer_level_choice():
    os.system ('cls')
    user_choice_level = user_input ('Wybierz poziom trudnosci komputera:\nA - Sprytny komputer\nB - Mniej sprytny komputer\n', 'AB')
    if user_choice_level == 'A':
        os.system ('cls')
        print ('Wybrales SPRYTNY komputer.\n') 
    if user_choice_level == 'B':
        os.system ('cls')
        print ('Wybrales MNIEJ SPRYTNY komputer.\n')     
    return user_choice_level       

def game_over_YN():
    game_over_choice = 'NNNT'
    game_over = random.choice (game_over_choice)      
    user_choice_continue = user_input ('Czy chcesz grac dalej? T/N: ', 'TN')
    if user_choice_continue == 'N':
        if game_over == 'N':
            return True
        else:
            os.system('cls')
            print ('Nie!? Tak łatwo mi się nie wymkniesz! Gramy dalej!')
    else:
        os.system ('cls')
    return False

def computer_random_choice(user_choice_level, options_available):
    if user_choice_level == 'A':
        computer_choice = random.choice (options_available)    
    if user_choice_level == 'B':
        double_element = random.choice(options_available)
        all_elements = double_element + options_available
        computer_choice = random.choice(all_elements)
    return computer_choice


class Game():

    def __init__(self, first_screen, possible_choices,choice_screen, remis, win, loss):
        self.first_screen = first_screen
        self.possible_choices = possible_choices
        self.choice_screen = choice_screen
        self.remis = remis
        self.win = win
        self.loss = loss

    def play(self):
        user_choice_welcome = user_input(self.first_screen, 'SPQ')
        os.system ('cls')
        if user_choice_welcome == 'Q':
            print ('Wybrales BRAK rozgrywki.')
          
        if user_choice_welcome == 'P':
            user_choice_level = computer_level_choice()

        if user_choice_welcome == 'S':
            os.system ('cls')
            print ('Brak mozliwosci wyboru poziomu trudnosci. Grasz ze SPRYTNYM komputerem.\n')
            
        while user_choice_welcome == 'S' or user_choice_welcome == 'P':
            user_choice = user_input(self.choice_screen, self.possible_choices)
           
            if user_choice_welcome == 'P':
                computer_choice = computer_random_choice(user_choice_level, self.possible_choices)
           
            if user_choice_welcome == 'S':
                computer_choice = random.choice (self.possible_choices)
            os.system ('cls')
            
            print ('Twoj wybor: ', user_choice)
            print ('Wybor komputera: ', computer_choice)

            if check_choices(user_choice, computer_choice, self.remis, 'REMIS'):
                data.append('remis')


            if check_choices(user_choice, computer_choice, self.loss, ' Twoja PRZEGRANA'):
                data.append('P')

            if check_choices(user_choice, computer_choice, self.win, 'Twoja WYGRANA'):
                data.append('W')       
           
            if game_over_YN():
                break

user_win = 0
user_loss = 0
data = []

os.system('cls')
print('WITAJ W GRZE!\nW jaka gre chcesz zagrac?\n') 

user_choice_game = user_input ('Wybierz:\n1 - KAMIEN-PAPIER-NOZYCZKI\n2 - KAMIEN-PAPIER-NOZYCZKI-LIZARD-SPOCK\nQ - wyjscie\n', '12Q')

os.system ('cls')
if user_choice_game == 'Q':
        print ('Wybrales BRAK rozgrywki.')

#KAMIEN-PAPIER-NOZYCZKI
if user_choice_game == '1':
    game = Game(
        first_screen='Wybrales KPN .......',
        possible_choices='KPN',
        choice_screen = 'Podaj swoj wybor: \nK - kamien \nP - papier \nN - nozyczki\n',
        remis = ['KK', 'PP', 'NN'],
        win = ['PK', 'NP', 'KN'],
        loss = ['KP', 'PN', 'NK']

    )
    game.play()
    
#KAMIEN-PAPIER-NOZYCZKI-LIZARD-SPOCK
elif user_choice_game == '2':
    game = Game(
        first_screen='Wybrales KPNLS .....',
        possible_choices='KPNLS',
        choice_screen = 'Podaj swoj wybor: \nK - kamien \nP - papier \nN - nozyczki\n L - lizard\n S - spock',
        remis = ['KK', 'PP', 'NN', 'LL', 'SS'],
        win = ['PK', 'NP', 'KN', 'SK', 'LP', 'SN', 'NL', 'KL', 'PS', 'LS'], 
        loss = ['KP', 'PN', 'NK', 'KS', 'PL', 'NS', 'LN', 'LK', 'SP', 'SL']
    )

    game.play()


if data == []:
    print ('KONIEC GRY\n')
else:
    import CC
    a = CC.win_loss_sequence(data, 'W')
    b = len(data)
    c = CC.win_loss_sequence(data, 'P')
    print ('wyniki rozgrywek: ', data)

    print ('ilosc WYGRANYCH uzytkownika: ', data.count('W'))
    print ('ilosc PRZEGRANYCH uzytkownika: ', data.count('P'))

   # jesli W = 0  i P = 0 => ZeroDivisionError (np. dla data = ['remis', 'remis'] dlatego:
    if (data.count('W') + data.count('P')) > 0:
        print ('ilosc WYGRANYCH uzytkownika w %: ', data.count('W')/(data.count('W') + data.count('P'))*100, '%')
        print ('ilosc PRZEGRANYCH uzytkownika w %: ', data.count('P')/(data.count('W') + data.count('P'))*100, '%')
    else:
        print ('ilosc WYGRANYCH uzytkownika w %: 0\nilosc PRZEGRANYCH uzytkownika w %: 0')

    print ('najdluzsza sekwencja WYGRANYCH uzytkownika:', a)
    print ('najdluzsza sekwencja PRZEGRANYCH uzytkownika:', c)

    print ('\nKONIEC GRY')












