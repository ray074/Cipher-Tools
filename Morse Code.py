def morseConverter(cipherText):
    cipherText += " "
    symbols = {".", "-"}
    morseDict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
        '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
        '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
        '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0','.----': '1',
        '..---': '2', '...--': '3', '....-': '4', '.....': '5',  '-....': '6', '--...': '7',
        '---..': '8','----.': '9', '.-.-.-': '.', '--..--': ',', '---...': ':', '..--..': '?',
        '-.-.--': '!', '-....-': '-', '-..-.': '/', '.-..-.': '"', '-.--.': '(', '-.--.-': ')',
                        '...-.-': '$', '.--.-.': '@', '.----.': "'", '.-.-.': '+'
    }
    
    temp, final = [], []
    
    for char in cipherText:
        if char in symbols:
            temp.append(char)
        elif char == "/":
            final.append(" ")
        else:
            if len(temp) != 0:
                final.append(morseDict["".join(temp)])
                temp.clear()
    
    plaintext = "".join(final)
    return plaintext


def main():
    cipherText = input("Enter Morse Code: ")
    plaintext = morseConverter(cipherText)
    print("\n", "Plaintext: ", "\n")
    print(plaintext)
    

if __name__ == "__main__":
    main()
    
