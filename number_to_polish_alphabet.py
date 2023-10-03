
alphabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"


def number_to_polish_alphabet(number):
    index = number - 1  # list index starts from 0, instead of 1
    return alphabet[index]


def main(numbers):
    for number in numbers.split():
        print(number_to_polish_alphabet(int(number)), end=" ")

    print(" ")


if __name__ == "__main__":
    first_string = "13 7 24 26 7 25"
    second_string = "28"
    thrid_string = "22 20 23 30 2 6 14 27"

    print("alphabet length: ", len(alphabet))

    main(first_string)
    main(second_string)
    main(thrid_string)
