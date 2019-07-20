from functions0 import players_list, players_info, level, category, secret_word, round_no, game

players0 = []
players = players_list(players0)
players_info(players)

players_dict = {}
for p in range(0,len(players)):
    players_dict.update({(players[p]):0})

r = round_no()
level = level()


for i in range(r):
    print(f'\n\nRunda {i+1}')
    cat = category()
    secret_words = secret_word((*cat['value']),plen= len(players))  # *2

    for p in players:
        a = secret_words[0]  # *3
        secret_words.remove(a)  # *3
        print(f"\n\nHasło z kategorii {(cat['key']).upper()} zgaduje {p}.")
        score = game(a, level)
        if score == 1:
            players_dict[p] += 1
        else:
            pass
    print(f'\nWyniki po {i+1} rundzie:')
    print(players_dict)


scores_players_dict = sorted(players_dict.items(), key=lambda x: x[1], reverse=True) # *1
print('\nOstateczne wyniki rozgrywki: \n')
for i in range(len(scores_players_dict)):
    print(f'{scores_players_dict[i][0]} : {scores_players_dict[i][1]}')

if scores_players_dict[0][1] == scores_players_dict[1][1]:
    print('\nRemis na pierwszym miejscu!!!')
else:
    print(f'\nGratulacje, {scores_players_dict[0][0]}!!')



# *1 - sortuję słownik players_dict w zależności od wyniku, tak,
#   że aby wyświetlić zwycięzcę w ostatniej linii wystarczy wyświetlić klucz pierwszego elementu

# *2 - od razu generuję listę słów od odgadnięcia z danej kategorii - jedno dla każdego z graczy

# *3 dla pierwszego gracza pierwsze słowo, a potem zostaje ono usunięte.
# w ten sposób niemożliwe jest powtórzenie się hasła dla w jednej rundzie