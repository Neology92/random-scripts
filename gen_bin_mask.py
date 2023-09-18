import sys


def main():
    num_of_ones = int(sys.argv[1])
    shift_left = int(sys.argv[2])

    mask = 0b1 << num_of_ones
    mask = mask - 1
    mask = mask << shift_left
    print("")
    print("Your mask:")
    print(bin(mask)[2:])
    print("")


if __name__ == "__main__":
    main()
