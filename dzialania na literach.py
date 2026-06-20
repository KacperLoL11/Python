TEXT_SIZE = 80


def to_lower(text):
    result = ""

    for char in text:
        if "A" <= char <= "Z":
            result += chr(ord(char) + (ord("a") - ord("A")))
        else:
            result += char

    return result


def to_upper(text):
    result = ""

    for char in text:
        if "a" <= char <= "z":
            result += chr(ord(char) - (ord("a") - ord("A")))
        else:
            result += char

    return result


def text_size(text):
    size = 0

    for char in text:
        size += 1

    return size


def main():
    print("Dzialania na slowach")
    print("Wpisz pusty tekst, aby zakonczyc program.")
    print()

    while True:
        text = input("Podaj tekst: ")

        if text == "":
            break

        if text_size(text) >= TEXT_SIZE:
            text = text[:TEXT_SIZE - 1]

        print(f"Tekst oryginalny: {text}")
        print(f"Male litery: {to_lower(text)}")
        print(f"Duze litery: {to_upper(text)}")
        print(f"Dlugosc tekstu: {text_size(text)}")
        print("------------------------------")


if __name__ == "__main__":
    main()