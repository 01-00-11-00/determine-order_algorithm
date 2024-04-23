# ---------------------------- Libraries ------------------------------- #

import math


# ---------------------------- CONSTANTS ------------------------------- #

LOGO = """
 ____       _                      _             
|  _ \  ___| |_ ___ _ __ _ __ ___ (_)_ __   ___  
| | | |/ _ \ __/ _ \ '__| '_ ` _ \| | '_ \ / _ \ 
| |_| |  __/ ||  __/ |  | | | | | | | | | |  __/ 
|____/ \___|\__\___|_|  |_| |_| |_|_|_| |_|\___| 
 / _ \ _ __ __| | ___ _ __                       
| | | | '__/ _` |/ _ \ '__|                      
| |_| | | | (_| |  __/ |                         
 \___/|_|  \__,_|\___|_|
"""


# ---------------------------- Functions ------------------------------- #

def print_logo():
    """
    Print the logo of the program to the console.
    :return: None
    """

    print()
    print(LOGO)
    print()


def validate_user_input(prompt: str) -> int:
    """
    Validate the user input.
    :param str prompt: The prompt message to display to the user.
    :return: The validated integer input from the user.
    """

    while True:
        user_input = input(prompt)
        print()

        try:
            value = int(user_input)

            if value <= 0:
                raise ValueError("Invalid Input: Please enter a positive number.")
            break

        except ValueError:
            print("Invalid Input: Please enter a positiv number.")

    return value


def find_divisors(n: int) -> list:
    """
    Find all divisors of a given number.
    :param int n: The number to find divisors for.
    :return: A sorted list of all divisors of the given number.
    """

    divisors = []

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n / i == i:
                divisors.append(i)

            else:
                divisors.extend([i, n // i])

    return sorted(divisors)


def montgomery_ladder(base: int, exponent: int, modulo: int) -> int:
    """
    Perform the Montgomery Ladder algorithm.
    :param int base: The base number for the calculation.
    :param int exponent: The exponent for the calculation.
    :param int modulo: The modulo for the calculation.
    :return: The result of the Montgomery Ladder calculation.
    """

    x = 1
    y = base % modulo
    exponent_in_bit = bin(exponent)[2:]

    for bit in exponent_in_bit:
        if bit == "1":
            x = (x * y) % modulo
            y = (y ** 2) % modulo
        else:
            y = (x * y) % modulo
            x = (x ** 2) % modulo

    return x


def determine_order(g: int, p: int) -> int:
    """
    Determine the order of an element in a prime field.
    :param int g: The element whose order is to be determined.
    :param int p: The prime field in which the operation is to be carried out.
    :return: The order of the element in the field, or -1 if no order is found.
    """

    order_of_p = p - 1
    divisors = find_divisors(order_of_p)

    for divisor in divisors:
        if montgomery_ladder(g, divisor, p) == 1:
            return divisor

    return -1


def main():
    """
    Main function of the program.
    :return: None
    """

    # Header
    print_logo()
    print()

    # Variables
    g = validate_user_input("Please enter the element whose order you would like to determine.\nElement: ")
    p = validate_user_input("Please enter the prime field in which the operation is to be carried out.\nField: ")

    # Body
    order_of_g = determine_order(g, p)
    print("-" * 50)
    print()
    print(f"The order of {g} in the field of {p} is: {order_of_g}")


# ------------------------------ Main ---------------------------------- #

if __name__ == "__main__":
    main()
