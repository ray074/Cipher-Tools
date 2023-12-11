def binaryConverter(cipherText):
    alpha, final = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), []
    binary = [16, 8, 4, 2, 1]
    
    for block in cipherText:
        total = 0
        for i in range(5):
            total += binary[i] * int(block[i])
        final.append(alpha[total])
    plaintext = "".join(final)
    return plaintext

        
def main():
    cipherText = input("Enter 5-Bit Binary Numbers: ").split()
    plaintext = binaryConverter(cipherText)
    print("\nPlaintext: \n\n", plaintext)
    

if __name__ == "__main__":
    main()
