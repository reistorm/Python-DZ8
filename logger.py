import pandas as pd

def logger_pupil(string_pupil):
    with open('pupil.csv', 'a', encoding='utf-8') as file:
        file.writelines(f'{string_pupil}\n')
    print('Запись добавлена')

def logger_class(string_class):
    with open('class.csv', 'a', encoding='utf-8') as file:
        file.writelines(f'{string_class}\n')
    print('Запись добавлена')

def logger_delete_pupil():
    del_pupil = int(input('Какую строку вы хотите удалить? '))
    data = pd.read_csv('pupil.csv')
    data.index += 1
    data.drop(labels=[del_pupil])
    with open('pupil.csv', 'w', encoding='utf-8') as file:
        file.writelines(f'{data}\n')
    print('Запись удалена')