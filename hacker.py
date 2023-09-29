'''
WORD MATCHING

In this challenge, you will be given an array of sentences and an array of queries.
Determine which sentences contain all of the words of a query.
If no sentence contains all of the words, the answer to that query is [-1].

Test shortcuts
sentences = [
    'bob and alice like to text each other',
    'bob does not like to ski but does not like to fall',
    'Alice likes to ski'
]
queries = ['bob alice', 'alice', 'like', 'non occurrence']

The results of the queries are:
Query O. sentences[0] -> [0]
Query 1. sentences[0] -> [0]
Query 2. sentences[0], sentences[1], sentences[1] -> [0, 1, 1]
Query 3. none match -> [-1]

Return a 2-dimensional integer array: [[0], [0], [0, 1, 1], [-1]]

Note: The word like in queries[2] does not match likes in sentences[2].
The word alice does not match Alice in sentence 2. Matches must be exact.
After each query has been processed, add an array of indices of the matching sentences to the answer array.
If all of the words of a query occur multiple times in a sentence,
the index of that sentences[i] should occur that number of times (see result 2 above for an example).
The order of the words' occurrence in the sentence does not matter.

Notes
If there are no matching sentences for queries[i], the response for that query should be [-1].

queries = 'on occurrence'
{
    0: [bob, and, alice, like, to, text, each, other]
    2: [bob does not like to ski but does not like to fall]
    3: [Alice likes to ski]
}

Second intuition
{
    0: { bob: 1, and: 1, alice: 1, like: 1, text: 1, each: 1, other: 1 }
    2: { bob: 1, does: 1, not: 1, like: 2, to: 2, ski: 1, but: 1, does: 1, 'not': 1, 'fall': 1  }
    3: { Alice: 1, likes: 1, 'to': 1,  ski: 1  }
}
'''


class Word_Matching:

    def __init__(self, sentences, queries):
        self.sentences = sentences
        self.queries = queries

    def sentence_freq(self, sentence):
         freq = {}
         for word in sentence.split(' '):
             freq[word] = freq.get(word, 0) + 1
         return freq

    def word_matching(self):
        no_of_queries = len(self.queries)
        results = [[] for _ in range(no_of_queries)]

        for query_idx, query in enumerate(queries):
            found = False
            query_words = query.split(' ')

            for sentence_idx, sentence in enumerate(self.sentences):
                matches = {}
                sentence_freq = self.sentence_freq(sentence)

                for word in query_words:
                    matches[word] = sentence_freq.get(word, 0)

                if not any(matches.values()):
                    continue

                found = True
                min_matches = min(matches.values()) # 2

                curr_matches = [sentence_idx] * min_matches
                results[query_idx].extend(curr_matches)

            if not found:
                results[query_idx].append(-1)

        return results


class Word_Matching_V2:

    def __init__(self, sentences, queries):
        self.sentences = sentences
        self.queries = queries

    def word_matching(self):
        no_of_queries = len(queries)
        results = [[] for _ in range(no_of_queries)] # [[], [], [], []]

        sentences_hashmap = self.build_sentence_hashmap()

        for query_idx, query in enumerate(queries):  # 3, non occurrence
            found = False #
            query_words = query.split(' ') # non occurrence

            for sentence_idx, sentence in sentences_hashmap.items(): # Alice likes to ski
                matches = {} # { non: 0, occurrence: 0 }

                for word in query_words: # [non, occurrence]
                    _count = sentence.count(word) # 0
                     # _count = sentences_hashmap_v2[sentence_idx].get(word, 0)
                    matches[word] = _count

                if not any(matches.values()):
                    continue

                found = True
                min_matches = min(matches.values()) # 2

                curr_matches = [sentence_idx] * min_matches # [1] * 2 = [1, 1]
                results[query_idx].extend(curr_matches) # [[], [], [0, 1, 1], []]

            if not found: # [[], [], [], [-1]]
                results[query_idx].append(-1) # val
                # results[query_idx].extend([-1]) # val

        return results


    def build_sentence_hashmap(self):
        sentences_hashmap = {}

        for i, sentence in enumerate(self.sentences):
            sentence_words = sentence.split(' ')
            sentences_hashmap[i] = sentence_words

        return sentences_hashmap

sentences = [
    'bob and alice like to text each other',
    'bob does not like to ski but does not like to fall',
    'Alice likes to ski'
]
queries = ['bob alice', 'alice', 'like', 'non occurrence']

word_matching = Word_Matching(sentences, queries)
word_matching_v2 = Word_Matching_V2(sentences, queries)

assert word_matching.word_matching() == [[0], [0], [0, 1, 1], [-1]]
assert word_matching_v2.word_matching() == [[0], [0], [0, 1, 1], [-1]]

print(word_matching.word_matching())
print(word_matching_v2.word_matching())


'''
APPROACH
1a. loop every query
    - break the query
    - for every word, count their occurrences`

    1. loop sentences
        every sentence ->
            break it down
            add it in frequency hashmap

            if no match for any words
                return -1


['bob and alice like to text each other', 'bob does not like to ski but does not like to fall', 'Alice likes to ski']

['bob alice', 'alice', 'like', 'non occurrence']

'bob alice' -> bob, alice
    freq = {
        bob: 2
        alice: 5
    }

    'bob and alice like to text each other'

    if any is 0:
        continue

    get the min val  1
        return index * min 1, 1 -> list()

    results = []
'''
