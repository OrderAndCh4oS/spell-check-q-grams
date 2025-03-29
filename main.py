from rapidfuzz.distance.Levenshtein import distance


def extract_q_grams(word, q):
    q_grams = []
    for i in range(len(word) - q + 1):
        q_grams.append(word[i:i + q])
    return q_grams

def extract_all_q_grams(words, q):
    all_q_grams = {}

    for word in words:
        q_grams = extract_q_grams(word, q)
        for q_gram in q_grams:
            if q_gram in all_q_grams:
                all_q_grams[q_gram].add(word)
            else:
                all_q_grams[q_gram] = set([word])
    return all_q_grams

def find_closet_matches(q_grams, word, q):
    matches = {}
    input_q_grams = extract_q_grams(word, q)
    for q_gram in input_q_grams:
        for w in q_grams.get(q_gram, []):
            matches[w] = matches.get(w, 0) + 1
    closest_matches = sorted(matches, key=matches.get, reverse=True)[:100]

    return sorted(closest_matches, key=lambda m: distance(word, m))[:5]


if __name__ == '__main__':
    words = []
    with open('333333_words', 'r') as file:
        for line in file:
            stripped = line.strip()
            if stripped:
                words.append(stripped)
    print(words)
    q = 3
    print(extract_all_q_grams(words, q))
    q_grams = extract_all_q_grams(words, q)
    closest_matches = find_closet_matches(q_grams, 'sweatbread', q)

    print(closest_matches)
