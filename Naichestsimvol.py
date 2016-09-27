#Задача: 102. 102 - Най-често срещан символ в str
# Назад
#От подаден str, изведете най-често срещания символ.
#Ако подаденият стринг е празен или съдържа само whitespace
# (нов ред, интервал, табулация), трябва да изведете "INVALID INPUT".
#Примери:
#ВХОД:
#Пазете си решенията на всяка задача.
#РЕЗУЛТАТ:
#а
import sys
INPUT_STRING = 'Пазете си  решенията на всяка задача.'

def main():
    input_string = input()
    input_string = input_string.strip()
    if input_string:
        symbols_counts = {}
        for c in input_string:
            if c not in symbols_counts:
                symbols_counts[c] = 1
            else:
                symbols_counts[c] += 1

        symbols_counts = list(symbols_counts.items())
        symbols_counts.sort(key=lambda item: item[1], reverse=True)
        print(symbols_counts[0][0])
    else:
        print("INVALID INPUT")

    return 0

if __name__ == '__main__':
    sys.exit(main())














