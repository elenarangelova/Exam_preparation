import sys

def main():
    try:
        input_filename = input()
        x = 0
        y = 0

        with open(input_filename, encoding='utf-8') as f:
            for row in f:
                if row == '\n':
                    continue
                words = row.split()
                if len(words) == 2:
                    direction = words[0]
                    interval = float(words[1])

                    if direction == 'up':
                        y += interval
                    elif direction == 'down':
                        y -= interval
                    elif direction == 'left':
                        x -= interval
                    elif direction == 'right':
                        x += interval
                else:
                    continue
            print("X " "{:.3f}".format(x))
            print("Y " "{:.3f}".format(y))


    except:
        print("INVALID INPUT")


if __name__ == '__main__':
    sys.exit(main())