from random import randrange
import sys


def play():
    print("=============================")
    print("|      Binary trainer       |")
    print("=============================\n")
    print("Input the decimal number corresponding to the binary number shown.\n")
    print("Press Ctrl+C to quit.\n\n")
    game_loop()


def game_loop():
    while True:
        num = randrange(0, 15)
        reply = input("Input {:0>4} decimally: ".format(bin(num)[2:]))
        if reply == str(num):
            print("Correct!")
        else:
            print("Wrong!")

        print("\n")


if __name__ == "__main__":
    try:
        play()
    except KeyboardInterrupt:
        sys.exit(0)
