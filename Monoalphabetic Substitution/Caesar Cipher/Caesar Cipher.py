def caesarConverter(cipherText, shift):
    
    alpha, final = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), []
    
    for letter in list(cipherText):
        if letter in alpha:
            letterVal = alpha.index(letter)
            newLetter = alpha[(letterVal + shift) % 26]
            final.append(newLetter)
        else:
            final.append(letter)
            
    plainText = "".join(final)
    return plainText


def calculateMostProbable(cipherText):
    
    alpha, plainTexts, absDiffs = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), [], []
    
    letterDistributions = [
      8.55, 1.60, 3.16, 3.87, 12.10, 2.18, 2.09, 4.96, 7.33, 0.22, 0.81, 4.21, 2.53,
      7.17, 7.47, 2.07, 0.10, 6.33, 6.73, 8.94, 2.68, 1.06, 1.83, 0.19, 1.72, 0.11
    ]
    
    for shift in range(1, 26):
        plainTexts.append(caesarConverter(cipherText, shift))
    
    for plainText in plainTexts:
        counts, totalDiff = {}, 0
        
        for letter in alpha:
            counts[letter] = round((plainText.count(letter) / len(plainText)) * 100, 4)
    
        for expected, real in zip(letterDistributions, counts.values()):
            totalDiff += abs(expected - real)
            
        absDiffs.append(round(totalDiff, 4))
        
    bestShift = absDiffs.index(min(absDiffs)) + 1
    return caesarConverter(cipherText, bestShift)


def main():
    
    cipherText = input("\nEnter Text Encrypted with a Caesar Cipher: \n\n").upper()
    result, manual = calculateMostProbable(cipherText), False
    
    print(f"\n Plaintext: \n\n{result}")

    user = input("\nEnter Manual Decryption? (y/n) ").lower()
    if user == "y" or user == "yes":
        manual = True
    
    while manual:
        
        newShift = int(input("Enter Shift Value: (1-25) "))
        newResult = caesarConverter(cipherText, newShift)
        print(f"\n{newResult}")
        
        further = input("\nContinue? (y/n) ").lower()
        
        if further != "y" and further != "yes":
            manual = False
        else:
            manual = True


if __name__ == "__main__":
    main()
