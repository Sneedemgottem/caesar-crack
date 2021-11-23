from argparse import ArgumentParser

startUpper = 65
endUpper  = 90
startLower = 97
endLower = 122

def shift_char(char, steps) -> str:
    """This function shifts the given character by the given step. Example: shift_char('a', 2) -> c.
    It only shifts to the right"""

    if (len(char)) > 1:
        raise Exception("Input a string not a character")

    if char.isupper():
        if ord(char) + steps > endUpper: # Checks if steps goes past the Z and if so go back to A
            num = (ord(char) + steps) -  endUpper
            return  chr(startUpper - 1 + num)
        else: # If step does not go past Z just add steps to the ascii decimal value and change it back to a string
            return chr(ord(char) + steps)
    else: # Else if letter is lower
        # Same as upper but for lower
        if ord(char) + steps > endLower:
            num = (ord(char) + steps) -  endLower
            return  chr(startLower - 1 + num)
        else:
            return chr(ord(char) + steps)

def shift_word(msg, shift):
    """This function shifts a message by the given shift to the right by shifting every character in the message and returning the new string"""

    if shift < 0: # handle negative numbers
        shift = 26 + shift

    newMsg = ""

    for char in msg:
        if not char.isalnum():
            newMsg += char
        else:
            newMsg += shift_char(char, shift)

    return newMsg


def find_all_shifts(msg, shift = 1) -> None:
    """Prints every possible shift sequence for the inputed cipher text"""

    if shift > 25: return

    if shift == 1:
        print("Original Message: ", msg)

    newMsg = shift_word(msg, shift)

    print("Shift: ", shift, "; Message: ", newMsg)
    find_all_shifts(msg, shift + 1)


# This is the main function
def main():
    parser = ArgumentParser(description="Process inputed strings for caesar cipher text.")
    parser.add_argument("-m", type=str, required=True, help="Input message")
    parser.add_argument("-c", type=int, required=False,help="If given, shift the message to the right by this amount (negative numbers are accepted for left shift).")

    args = parser.parse_args()
    if args.c == None:
        find_all_shifts(args.m)
    else:
        print(shift_word(args.m, args.c))

if __name__ == "__main__":
	main()
