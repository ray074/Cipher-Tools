def polybiusConverter(nums):
    nums, new, final = [int(x) for x in nums], [], [[] for _ in range(6)]
    
    for i in range(len(nums)):
        nums[i] -= 1
    string = "".join(str(x) for x in nums)
    
    for i in range(0, len(string), 2):
        new.append(string[i:i+2])
    
    matrix1 = [["A", "B", "C", "D", "E"],
               ["F", "G", "H", "I", "J"],
               ["K", "L", "M", "N", "O"],
               ["P", "R", "S", "T", "U"],
               ["V", "W", "X", "Y", "Z"]]
              
    matrix2 = [['A', 'B', 'C', 'D', 'E'],
               ['F', 'G', 'H', 'I', 'J'],
               ['K', 'L', 'M', 'N', 'O'],
               ['P', 'Q', 'R', 'S', 'T'],
               ['U', 'V', 'W', 'X', 'Y']]

    matrix3 = [['A', 'B', 'C', 'D', 'E'],
               ['F', 'G', 'H', 'I', 'J'],
               ['K', 'L', 'M', 'N', 'O'],
               ['P', 'Q', 'R', 'S', 'T'],
               ['U', 'V', 'W', 'Y', 'Z']]
    
    matrix4 = [['A', 'B', 'C', 'D', 'E'],
               ['F', 'G', 'H', 'I', 'K'],
               ['L', 'M', 'N', 'O', 'P'],
               ['Q', 'R', 'S', 'T', 'U'],
               ['V', 'W', 'X', 'Y', 'Z']]

    matrix5 = [['A', 'B', 'C', 'D', 'E'],
               ['F', 'G', 'H', 'I', 'J'],
               ['L', 'M', 'N', 'O', 'P'],
               ['Q', 'R', 'S', 'T', 'U'],
               ['V', 'W', 'X', 'Y', 'Z']]
    
    matrix6 = [['A', 'B', 'C', 'D', 'E'],
               ['F', 'G', 'H', 'I', 'J'],
               ['K', 'L', 'M', 'N', 'O'],
               ['P', 'Q', 'R', 'S', 'T'],
               ['U', 'W', 'X', 'Y', 'Z']]
              
    matrices = [matrix1, matrix2, matrix3, matrix4, matrix5, matrix6]
    
    pointer = 0
    for matrix in matrices:
        for block in new:
            row, col = int(block[0]), int(block[1])
            final[pointer].append(matrix[row][col])
        pointer += 1
    
    for p in range(len(final)):
        final[p] = "".join(final[p])
        
    return final

def calcMostProbable(converted):
    letterDistributions = [
      8.55, 1.60, 3.16, 3.87, 12.10, 2.18, 2.09, 4.96, 7.33, 0.22, 0.81, 4.21, 2.53,
      7.17, 7.47, 2.07, 0.10, 6.33, 6.73, 8.94, 2.68, 1.06, 1.83, 0.19, 1.72, 0.11
    ]
    
    alpha, length = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), len(converted[0])
    sumDiffs = []
    
    for block in converted:
        counts = {}
        absDiffs = []
        
        for letter in alpha:
            value = (block.count(letter) / length) * 100
            counts[letter] = round(value, 8)
        
        for expected, real in zip(letterDistributions, counts.values()):
            absDiffs.append(abs(expected - real))
        
        sumDiffs.append(sum(absDiffs))
        absDiffs.clear()
        counts.clear()
    
    minIndex = sumDiffs.index(min(sumDiffs))
    plaintext = converted[minIndex]
    return plaintext


def main():
    nums = list("".join(x for x in input("Enter Polybius Square Numbers: ").split()))
    convertedList = polybiusConverter(nums)
    print("\n", "Plaintext: ", "\n")
    print(calcMostProbable(convertedList))
    
    check = input("\n Display results for all Polybius Squares? (y/n) ").lower()
    if check == "y" or check == "yes":
        for value in convertedList:
            print("\n", value, "\n\n")


if __name__ == "__main__":
    main()
