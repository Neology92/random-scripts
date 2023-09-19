import sys


def set_bit(val, idx, new_bin_val):
    mask = 1 << idx - 1
    val &= ~mask
    val |= (new_bin_val << idx - 1)
    return val


def main():
    val = int(sys.argv[1], 2)
    idx = int(sys.argv[2])
    new_bin_val = int(sys.argv[3], 2)

    new_val = set_bit(val, idx, new_bin_val)

    print("")
    print("Your updated value is:")
    print(bin(new_val)[2:])
    print("")


if __name__ == "__main__":
    main()
