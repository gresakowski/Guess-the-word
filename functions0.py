import math

# funkcja służąca do stworzenia listy graczy
def players_list(players0):
    while True:
        player = input("Podaj imię gracza: ")
        player = player.capitalize()
        if player not in players0:
            players0.append(player)
        elif player in players0:
            print(f'Gracz o imieniu {player} jest już na liście, podaj inne imię.')
            continue
        if len(players0) >= 2:
            next_player = ' '
            while next_player != 'T' and next_player != 'N':
                next_player = input('Czy chcesz dodać następnego zawodnika? T/N ')
                next_player = next_player.capitalize()
            if next_player == 'N':
                return players0
                break
            elif next_player == 'T':
                continue
            else:
                print('Proszę wprowadzić poprawną wartość T/N')
                continue


# funkcja podająca skład graczy:
def players_info(players0):
    players2 = players0[0:(len(players0) - 2)]
    str1 = ', '.join(players2) + ', ' + players0[len(players0) - 2]
    if len(players0) == 2:
        str = ' oraz '.join(players0)
        print(f'\nW grze biorą udział {str}.')
    else:
        print('\nW grze biorą udział {} oraz {}.'.format(str1, players0[len(players0) - 1]))


# funkcja służąca do ustalenia poziomu trudności:
def level():
    level = ' '
    while level != 'E' and level != 'M' and level != 'H':
        level = input('''\nWybierz poziom trudności:
                        - E - Easy
                        - M - Medium
                        - H - hard
                        Poziom:  ''')
        level = level.capitalize()
    if level == 'E':
        level1 = 'Easy'
    elif level == 'M':
        level1 = 'Medium'
    else:
        level1 ='Hard'
    print('Wybrano poziom {}.'.format(level1))
    return level


# funkcja służąca do ustalenia ilośći rund:
def round_no():
    round_no = ' '
    while True: #type(round_no) is not int:
        round_no = input("\nPodajcie ilość rund: ")
        try:
            round_no = int(round_no)
        except ValueError:
            print('Należy podać liczbę.')
            continue
        if round_no < 1:
            print('\nNależy podać liczbę niemniejszą niż 1.')
            continue
        elif round_no ==1:
            print(f'\nRozegrana zostanie {round_no} runda.')
            return round_no

        elif round_no >= 2 and round_no <= 4:
            print(f'\nRozegrane zostaną {round_no} rundy.')
            return round_no

        else:
            print(f'Rozegranych zostanie {round_no} rund.')
            return round_no


# funkcja służąca do wyboru kategorii
def category():

    categories = [
        {'key': 'zwierzęta',
         'value': 'żyrafa antylopa nosorożec tygrys niedźwiedź sarna jeleń papuga hipopotam krokodyl jeżozwierz'.split(' ')},
        {'key': 'pojazdy',
         'value': 'samochód motocykl motorower samolot helikopter odrzutowiec rower katamaran'.split(' ')},
        {'key': 'państwa',
         'value': 'Wenezuela Brazylia Honduras Mongolia Argentyna Kambodża Wietnam Hiszpania Portoryko'.split(' ')}]
    category = ' '
    while category != 1 and category != 2 and category != 3:
        category = input('''\nWybierzcie kategorię:
                                1 - zwierzęta
                                2 - pojazdy
                                3 - państwa
                                Wybór: ''')
        try:
            category = int(category)
        except ValueError:
            print('Należy podać liczbę z zakresu 1:3.')
            continue
        if category == 1:
            choosen_cat = categories[0]
        elif category == 2:
            choosen_cat = categories[1]
        elif category == 3:
            choosen_cat = categories[2]
        else:
            print('Należy podać liczbę z zakresu 1:3.')
            continue
        return choosen_cat


# wygenerowanie słowa
def secret_word(*category,plen):
    import random
    category = list(category)
    secret_words = []
    for i in range(plen):
        num = len(category)-1
        n = random.randint(0, num)
        secret_word = category[n]
        category.remove(secret_word)
        secret_words.append(secret_word)
    return secret_words


# gra
def game(secret_word, level):
    xx = list('_'*len(secret_word))
    xxx = '_ '*len(secret_word)
    print(xxx)
    swlen = len(secret_word)
    if level == 'E':
        attempt_no = round(swlen/2 + 0.5) # +0.5 żeby zaokrągliło w górę
    elif level == 'M':
        attempt_no = round(swlen/3 + 0.5)
    else:
        attempt_no = round(swlen/4 + 0.5)

    if attempt_no == 1:
        attempt_no = attempt_no + 1 # żeby zawsze były przynajmniej 2 próby
    else:
        attempt_no = attempt_no

    print('Masz {} {} na odgadnięcie litery. Za {} razem musisz odgadnąć hasło. Powodzenia!!.'.format(attempt_no, 'próby' if attempt_no >= 3 else 'prób', attempt_no+1))

    sw_list = []
    for i in range(attempt_no):
        guess = input('Odgadnij literę: ')

        if guess in secret_word or guess.upper() in secret_word:
            print('Trafiłeś!!')
            for x in range(len(secret_word)):
                if secret_word[x] == guess or secret_word[x] == guess.upper():
                    sw_list.append(x)
                for i in sw_list:
                    if xx[i] == '_':
                        xx[i] = guess
                    else:
                        pass
            print(' '.join(xx))
        else:
            print('Pudło..')
            print(' '.join(xx))
        attempt_no = attempt_no -1
        print('Pozostało {} prób.'.format(attempt_no))
    print('Musisz teraz odgadnąć hasło.')
    guess_word = input('Hasło to: ')
    if guess_word == secret_word or guess_word.capitalize() == secret_word:
        print(f'\nGratulacje, hasło to {secret_word}.')
        return 1
    else:
        print('\nNiestety nie udało się.')
        print(f'Poprawne hasło to: {secret_word}')
        return 0

