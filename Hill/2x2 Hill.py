from trigrams import trigrams

def get_determinant(matrix):
    return ((matrix[0] * matrix[3]) - (matrix[1] * matrix[2]))


def get_adjacency_matrix(matrix):
    return [matrix[3], -matrix[1], -matrix[2], matrix[0]]


def get_multiplicative_inverse(determinant):
    determinant = determinant % 26
    
    if determinant not in [0,2,4,6,8,10,12,13,14,16,18,20,22,24]:
        for n in range(0, 26):
            if (determinant * n) % 26 == 1:
                return n
        
    else:
        return 0


def get_matrix_inverse(matrix):
    determinant = get_determinant(matrix)
    multiplicative_inverse = get_multiplicative_inverse(determinant)
    adjacency = get_adjacency_matrix(matrix)
    adjacency = [(x % 26) for x in adjacency]
    final = [(y * multiplicative_inverse) for y in adjacency]
    inverse = [(z % 26) for z in final]

    return inverse


def multiply_matricies_and_reduce(M1, M2):
    multiplied = [
        (M1[0] * M2[0]) + (M1[1] * M2[1]),
        (M1[2] * M2[0]) + (M1[3] * M2[1])
    ]

    return [x % 26 for x in multiplied]


def create_all_key_matrices():
    start, nums, exit = list(range(1000)), [], [] #7
    for num in start:
        length = len(str(num))
        zero_count = 4 - length
        value = zero_count * "0" + str(num)
        value_list = list(value)
        final = [int(x) for x in value_list]
        nums.append(final)
    
    for n in range(1000, 10000):
        val = list(str(n))
        proper = [int(x) for x in val]
        nums.append(proper)
        
    for matrix in nums:
        if get_determinant(matrix) not in [0,2,4,6,8,10,12,13,14,16,18,20,22,24]:
            exit.append(matrix)

    return exit


def fitness(clean_text):
    final_score = 0
    try:
        for i in range(0, len(clean_text), 3):
            final_score += trigrams[clean_text[i:i+3]]
    except KeyError:
        pass
    
    return final_score


def find_best(arr):
    return (arr.index(max(arr)))


def main():
    alpha_dict = {chr(i): str(i - 65) for i in range(65, 91)}
    number_dict = {x: y for y, x in alpha_dict.items()}

    cipher_text = input("\nEnter cipher text: ")
    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    spaces_gone = "".join([l for l in list(cipher_text) if l in alpha])
    matrices, clean, final, exit, trigram_checker, fitness_list = create_all_key_matrices(), [], [], "", [], []

    for i in range(0, len(spaces_gone), 2):
        temp = [int(alpha_dict[spaces_gone[i]]), int(alpha_dict[spaces_gone[i+1]])]
        clean.append(temp)

    for matrix in matrices:
        inverse = get_matrix_inverse(matrix)
        for block in clean:
            final.append(multiply_matricies_and_reduce(inverse, block))

        for chunk in final:
            exit += number_dict[str(chunk[0])]
            exit += number_dict[str(chunk[1])]

        trigram_checker.append(exit)
        final.clear()
        exit = ""

    for text in trigram_checker:
        fitness_list.append(fitness(text))

    print("\n", trigram_checker[find_best(fitness_list)], "\n", sep="")
    print(f"Key Matrix: {matrices[find_best(fitness_list)]} \n ")


if __name__ == "__main__":
    main()
  
