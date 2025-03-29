import csv
import random

def extract_n_sample_words(filepath, n):
    with open(filepath, encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        words = [row[1] for row in reader]

    sample = random.sample(words, min(n, len(words)))
    sample.sort()

    with open(f"{n}_words", 'w', encoding='utf-8') as f:
        for word in sample:
            f.write(f"{word}\n")


if __name__ == '__main__':
    extract_n_sample_words("words_pos.csv", 333333)
