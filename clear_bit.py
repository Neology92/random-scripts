import sys


def clear_bit(val, idx):
    mask = 1 << idx - 1
    val &= ~mask
    return val


def main():
    val = int(sys.argv[1], 2)
    idx = int(sys.argv[2])
    new_val = clear_bit(val, idx)

    print("")
    print("Your number with cleared bit:")
    print(bin(new_val)[2:])
    print("")


if __name__ == "__main__":
    main()
