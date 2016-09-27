#Като входни данни са подадени размерите на кашон
# (правоъгълен паралелепипед) - w, h, d, и име на файл,
# в който на всеки ред за записани име на лекарство и 3 числа -
# размери на опаковки на лекарства, които също са правоъгълни паралелепипеди.
#Празните редове от файла не бива да се обработват.
#От подадения файл, изведете на отделен ред името на всяко лекарство,
# което може самостоятелно да се побере в кашона.
#Имайте предвид, че при поставяне в кашона можете да завъртате
# лекарствата на всички посоки.
#Ако входните данни не са валидни, трябва да изведете "INVALID INPUT"
#Пример:
#ВХОД:
#1.23
#0.80
#0.50
#packages.txt
#Примерно съдържание на packages.txt
#Аналгин,0.10,0.15,0.25
#Памук,1.25,0.40,0.60
#Лекарство 3,0.30,0.05,0.12
#РЕЗУЛТАТ:
#Аналгин
#Лекарство 3

import sys
import csv

def main():
    try:
        box_w = float(input())
        box_h = float(input())
        box_d = float(input())
        packages_filename = input()

        box_dimensions = sorted((box_w, box_h, box_d))

        packages = _load_packages(packages_filename)
        for name, dimensions in packages: #name = value[0]#dimensions = value[1]
            can_fit = True
            for dim_idx in range(3):
                if dimensions[dim_idx > box_dimensions[dim_idx]:
                    can_fit = False
                 break
            if can_fit:
                print(name)
        return 0
    except:
        print("INVALID INPUT")

def _load_packages(input_filename):

    result = []
    with open(input_filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            name = row[0]
            dimensions = [float(row[1]), float(row[2]), float(row[3])]
            result.append(
                (
                    name,
                    sorted(dimensions)
                )
            )
    return result

if __name__ == '__main__':
    sys.exit(main())