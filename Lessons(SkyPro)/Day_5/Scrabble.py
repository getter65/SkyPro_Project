import random


def random_letters_f_s():
    with open('russian_word.txt', 'r', encoding='utf-8') as file_words:
        for words in file_words:
            list_words.append(words.strip())
    for key, word in letters_dict.items():
        random_letter.extend(key)
    random.shuffle(random_letter)
    letters_first_player.extend(random_letter[: 7])
    for value in letters_first_player:
        if value in letters_dict:
            letters_dict[value] -= 1
            if letters_dict[value] == 0:
                del letters_dict[value]
    random.shuffle(random_letter)
    letters_second_player.extend(random_letter[: 7])
    for value in letters_second_player:
        if value in letters_dict:
            letters_dict[value] -= 1
            if letters_dict[value] == 0:
                del letters_dict[value]
    print("Выдаю буквы")
    print(f"Буквы для {first_name_player} - {', '.join(letters_first_player)}")
    print(f"Буквы для {second_name_player} - {', '.join(letters_second_player)}")


def game_first_player():
    print(f"{first_name_player} вот твои буквы\n{', '.join(letters_first_player)}")
    game_input_first = input(f"{first_name_player} вводи слово\n")
    if [i for i in game_input_first if i in letters_first_player]:
        if game_input_first in list_words:
            for letter in game_input_first:
                letters_first_player.remove(letter)
            random.shuffle(random_letter)
            letters_first_player.extend(random_letter[:len(game_input_first) + 1])
            print(letters_first_player)
            score_player_1.append(score_for_answer_list[len(game_input_first) - 1])
            game_second_player()
        else:
            print("Нет такого слова")
            random.shuffle(random_letter)
            letters_first_player.extend(random_letter[:1])
            game_second_player()
    elif game_input_first == "stop":
        score_game()
    else:
        print(f"Нет такой буквы в твоём списке")
        game_first_player()


def game_second_player():
    print(f"{second_name_player} вот твои буквы\n{', '.join(letters_second_player)}")
    game_input_second = input(f"{second_name_player} вводи слово\n")
    if [i for i in game_input_second if i in letters_second_player]:
        if game_input_second in list_words:
            for letter in game_input_second:
                letters_second_player.remove(letter)
            random.shuffle(random_letter)
            letters_second_player.extend(random_letter[:len(game_input_second) + 1])
            print(letters_second_player)
            score_player_2.append(score_for_answer_list[len(game_input_second) - 1])
            game_first_player()
        else:
            print("Нет такого слова")
            random.shuffle(random_letter)
            letters_second_player.extend(random_letter[:1])
            game_first_player()
    elif game_input_second == "stop":
        score_game()
    else:
        print(f"Нет такого слова")
        random.shuffle(random_letter)
        letters_second_player.extend(random_letter[:1])
        game_first_player()


def score_game():
    if sum(score_player_1) > sum(score_player_2):
        print(f"Победил {first_name_player} со счетом\n"
              f"{sum(score_player_1) : {sum(score_player_2)}}")
        quit()
    elif sum(score_player_1) == sum(score_player_2):
        print(f"У нас нечья со счетом\n{sum(score_player_1)} : {sum(score_player_2)}")
        quit()
    else:
        print(f"Победил {second_name_player} со счётом\n"
              f"{sum(score_player_2)} : {sum(score_player_1)}")
        quit()


if __name__ == "__main__":
    letters_dict = {
        'а': 8, 'б': 2, 'в': 4, 'г': 2, 'д': 4,
        'е': 8, 'ё': 1, 'ж': 1, 'з': 2, 'и': 5,
        'й': 1, 'к': 4, 'л': 4, 'м': 3, 'н': 5,
        'о': 10, 'п': 2, 'р': 5, 'с': 5, 'т': 5,
        'у': 4, 'ф': 1, 'х': 1, 'ц': 1, 'ч': 1,
        'ш': 1, 'щ': 1, 'ъ': 1, 'ы': 2, 'ь': 3,
        'э': 1, 'ю': 1, 'я': 2
    }
    first_name_player = input('Привет друг, ты первый игрок представся))): ')
    second_name_player = input('Ты его противник, представся pls: ')
    letters_first_player = []
    letters_second_player = []
    random_letter = []
    list_words = []
    score_for_answer_list = [0, 0, 0, 3, 6, 7, 8, 9]
    score_player_1 = [0]
    score_player_2 = [0]
    print('Давайте начнём игру')
    random_letters_f_s()
    game_first_player()