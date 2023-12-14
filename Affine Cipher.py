from sympy import mod_inverse

def affineConverter(cipherText, a, b):
    alpha, final = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), []
    
    for letter in list(cipherText):
        if letter in alpha:
            letterVal = alpha.index(letter)
            result = (mod_inverse(a, 26) * (letterVal - b)) % 26
            final.append(alpha[result])
        else:
            final.append(letter)

    plainText = "".join(final)
    return plainText
            
def calculateMostProbable(cipherText):
    alpha, final = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), []
    coprimes = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    letterDistributions = [
      8.55, 1.60, 3.16, 3.87, 12.10, 2.18, 2.09, 4.96, 7.33, 0.22, 0.81, 4.21, 2.53,
      7.17, 7.47, 2.07, 0.10, 6.33, 6.73, 8.94, 2.68, 1.06, 1.83, 0.19, 1.72, 0.11
    ]
    
    for a in coprimes:
        for b in range(26):
            result = affineConverter(cipherText, a, b)
            absDiffs, counts = 0, {}
            
            for letter in alpha:
                value = (result.count(letter) / len(result)) * 100
                counts[letter] = round(value, 4)
            
            for expected, real in zip(letterDistributions, counts.values()):
                absDiffs += abs(expected - real)
                
            final.append(absDiffs)
            
    minIndex = final.index(min(final))
    aValue = coprimes[minIndex // 26]
    bValue = minIndex % 26
    
    return (affineConverter(cipherText, aValue, bValue), aValue, bValue)
            

def main():
    cipherText = input("Enter text encrypted with an Affine Cipher: ").upper()
    plainText, a, b, = calculateMostProbable(cipherText)
    print(f"\n Plaintext: \n\n {plainText} \n\n A VALUE: {a} \n B VALUE: {b} \n\n")
    
    searching = True
    while searching:
        validation = input("Continue with Affine Decryption? (y/n) ").lower()
        if validation == "y" or validation == "yes":
            newA = int(input("Enter New A Value: "))
            newB = int(input("Enter New B Value: "))
            newPlaintext = affineConverter(cipherText, newA, newB)
            print(f"\nNew Plaintext: {newPlaintext} \n\n")
        else:
            searching = False

if __name__ == "__main__":
    main()
