import sys


def usage(program_name):
    print(f"Usage: {program_name} number1 operation number2")
    print("Available operations:")
    print("\tadd")
    print("\tsub")
    print("\tmul")
    print("\tdiv")
    print("\tmod")

def main():
    if len(sys.argv) != 4:
        usage(sys.argv[0])
        return 1

    number1 = int(sys.argv[1])
    operation = sys.argv[2]
    number2 = int(sys.argv[3])

    if operation == "add":
        result = number1 + number2
        print(f"{number1} + {number2} = {result}")
        return 0

    if operation == "sub":
        result = number1 - number2
        print(f"{number1} - {number2} = {result}")
        return 0

    if operation == "mul":
        result = number1 * number2
        print(f"{number1} * {number2} = {result}")
        return 0

    if operation == "div":
        if number2 == 0:
            print("Division by zero is not allowed.")
            return 1

        result = number1 / number2
        print(f"{number1} / {number2} = {result:.2f}")
        return 0

    if operation == "mod":
        if number2 == 0:
            print("Modulo by zero is not allowed.")
            return 1

        result = number1 % number2
        print(f"{number1} % {number2} = {result}")
        return 0

    usage(sys.argv[0])
    return 1


if __name__ == "__main__":
    main()