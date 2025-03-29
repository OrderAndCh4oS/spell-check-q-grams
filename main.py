def extract_q_grams(word, q):
    """
    Returns a list of all contiguous q-grams of length q from the given word.
    """
    q_grams = []
    for i in range(len(word) - q + 1):
        q_grams.append(word[i:i + q])
    return q_grams

def extract_all_q_grams(words, q):
    """
    Returns a dictionary mapping each q-gram to the set of words that contain it.
    """
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
    """
    Returns a list of up to 5 words with the smallest Levenshtein distance to the input word, selected from the top 100 candidates based on shared q-grams.
    """
    matches = {}
    input_q_grams = extract_q_grams(word, q)
    for q_gram in input_q_grams:
        for w in q_grams.get(q_gram, []):
            matches[w] = matches.get(w, 0) + 1
    closest_matches = sorted(matches, key=matches.get, reverse=True)[:100]

    return sorted(closest_matches, key=lambda m: levenshtein_distance(word, m))[:5]

def levenshtein_distance(a, b):
    m = len(a)
    n = len(b)
    matrix = [list(range(0, n + 1))] + [[i] for i in range(1, m + 1)]
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            insert_cost = matrix[i][j - 1] + 1
            delete_cost = matrix[i - 1][j] + 1
            substitution_cost = 0 if a[i - 1] == b[j - 1] else 1
            substitute_cost = matrix[i - 1][j - 1] + substitution_cost
            min_cost = min(insert_cost, delete_cost, substitute_cost)
            matrix[i].insert(j, min_cost)

    return matrix[-1][-1]


if __name__ == '__main__':
    words = []
    with open('333333_words', 'r') as file:
        for line in file:
            stripped = line.strip()
            if stripped:
                words.append(stripped)
    q = 3
    q_grams = extract_all_q_grams(words, q)
    result = find_closet_matches(q_grams, 'sweatbread', q)

    print(result)
