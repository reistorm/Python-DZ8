import pandas as pd

def print_pupil():
    data = pd.read_csv('pupil.csv')
    data.index += 1
    print(data)

def print_class():
    with open('class.csv', 'r', encoding='utf-8') as file:
        data = file.read()
        print(data)