def get_count_char(str_):
    all_sign_dict = {}
    for sign in str_.lower():
        if sign.isalpha():
            if sign in all_sign_dict:
                all_sign_dict[sign] += 1
            else:
                all_sign_dict[sign] = 1

    return all_sign_dict


def persentage_in_dict(all_sign_dict):
    prove = 0
    i = 0
    persents_dict = {}
    for letter in all_sign_dict:
        i += all_sign_dict.get(letter)
    for letter in all_sign_dict:
        persents_dict[letter] = round(all_sign_dict.get(letter) / i) * 100, 2
    for letter in persents_dict:
        prove += persents_dict.get(letter)
    return persents_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова.
    В качестве разделителя для встроенного метода split будет выбран символ пробела.
    На выходе мы получим список отдельных слов.
    Далее нужно отсортировать слова в алфавитном порядке,
    а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
