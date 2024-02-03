def count_words(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()

            word_counts = {}

            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

            for word, count in sorted(word_counts.items()):
                print(f'{word}: {count}')

    except FileNotFoundError:
        print(f'Error: File "{filename}" not found.')

count_words('your_file.txt')