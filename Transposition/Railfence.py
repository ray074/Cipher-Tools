from trigrams import trigrams

global alpha
alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def find_best(arr):
    return (arr.index(max(arr)))


def fitness(clean_text):
    final_score = 0
    try:
        for i in range(0, len(clean_text), 3):
            final_score += trigrams[clean_text[i:i+3]]
    except KeyError:
        pass
    
    return final_score


def clean(text):
    text = text.upper()
    final = "".join([l for l in list(text) if l in alpha])
    return final


def create_railfence(depth, cipher_text_length):
    arr = [[] for _ in range(depth)]
    final = []

    for i in range(depth):
        for _ in range(cipher_text_length):
            arr[i].append(0)

    first = list(range(depth))
    second = list(range(depth-2, 0, -1))
    combined = first + second

    for _ in range(cipher_text_length):
        for num in combined:
            final.append(num)

    final = final[0:cipher_text_length]

    for col, row in zip(list(range(cipher_text_length)), final):
        arr[row][col] = "-"

    return arr


def insert(arr, cleaned, depth):
    counter = 0

    for i in range(depth):
        for j in range(len(cleaned)):
            if arr[i][j] == "-":
                arr[i][j] = cleaned[counter]
                counter += 1

    return arr


def read_arr(completed_arr, depth):
    final = ""
    for i in range(len(completed_arr[0])):
        for j in range(depth):
            if completed_arr[j][i] in alpha:
                final += completed_arr[j][i]

    return final


def main():
    cipher_text = input("\nEnter cipher text: ").upper()
    cleaned = clean(cipher_text)
    cleaned_length = len(cleaned)

    possbile_depths = list(range(2, 21)) # bruteforce depth up to 20 (can be increased)
    texts, textual_fitness = [], []

    for depth in possbile_depths:
        railfence = create_railfence(depth, cleaned_length)
        updated_railfence = insert(railfence, cleaned, depth)
        final = read_arr(updated_railfence, depth)
        texts.append(final)

    for text in texts:
        textual_fitness.append(fitness(text))

    optimal_depth = find_best(textual_fitness)
    plaintext = texts[optimal_depth]

    print()
    print(plaintext)
    print()
    print("Depth: ", depth)
    print()

if __name__ == "__main__":
    main()


# offsets are possible, be wary
