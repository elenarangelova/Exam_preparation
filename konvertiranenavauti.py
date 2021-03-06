#Реализирайте програма, която да конвертира сума от подадена валута към
# български лева (BGN). Резултатите трябва да се закръглят до втория знак
# след десетичната запетая.
#Входни данни:
#име на файл, съдържащ обменни курсове на различни валути към BGN;
# Празните редове във файла не бива да се обработват;
#име на файл, съдържащ на всеки ред сума и валута, в която е сумата;
# Празните редове във файла не бива да се обработват; Имайте предвид,
# че в този файл ще има по няколко суми от една и съща валута;
#Очакван изход: За всеки ред от файла със сумите, трябва да бъде
# изведена на отделен ред съответната сума в български лева.
#Пример:
#Входни данни:                       Резултати:
#exchange.txt
 #  примерно съдържание:
#   AUD 0.79676
#   CAD 0.78761
#   CHF 0.56759
 #  USD 0.57276
#   EUR 0.5111

#amounts.txt
#   примерно съдържание:
#   623.83 USD                       1089.16
#   572.53 EUR                       1120.19
#   12 CHF                           21.14
#   1182.08 AUD                      1483.61
#   24 CHF                           42.28

rates_filename = input()
exchange_rates = {}
with open(rates_filename, encoding='utf-8') as f:
    for line in f:
        if not line.isspace():
            key, exrate, *_ = line.split()
            exchange_rates[key] = float(exrate)
money_file = input()
with open(money_file) as f2:
    for line in f2:
        if not line.isspace():
            amount, valuta, *_ = line.split()
            print("{:.2f}".format(float(amount)/exchange_rates[valuta]))