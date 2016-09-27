import sys
import math

def main():
    try:
        p = float(input())
        a = float(input())
        b = float(input())
        c = float(input())
        if p <= 0 or a <= 0 or b <= 0 or c <= 0 :
            print('INVALID INPUT')
        else:
            box_size = 2*(a*b + a*c + b*c)/p
            res = box_size/100*109.8
            resultat = math.ceil(res)
        print(resultat)
    except:
        print("INVALID INPUT")

if __name__ == "__main__":
    sys.exit(int(main() or 0))