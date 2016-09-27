import sys

def main():
    try:
        box_w = float(input())
        box_h = float(input())
        box_d = float(input())
        packages_filename = input()
        return 0
    except:
        print("INVALID INPUT")

def _load_packages(input_filename):

    with open(input_filename, encoding='utf-8') as f:
        pass


if __name__ == '__main__':
    sys.exit(main())