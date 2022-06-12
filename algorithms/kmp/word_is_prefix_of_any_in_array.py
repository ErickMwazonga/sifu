'''
1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

Given a sentence that consists of some words separated by a single space, and a searchWord,
check if searchWord is a prefix of any word in sentence.

Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word.
If searchWord is a prefix of more than one word, return the index of the first word (minimum index).
If there is no such word return -1.

A prefix of a string s is any leading contiguous substring of s.

Examples:
1. sentence = 'i love eating burger', searchWord = 'burg' => 4
    Explanation: 'burg' is prefix of 'burger' which is the 4th word in the sentence.
2. sentence = 'this problem is an easy problem', searchWord = 'pro' => 2
    Explanation: 'pro' is prefix of 'problem' which is the 2nd and the 6th word in the sentence, but we return 2 as it's the minimal index.
'''


def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    sentence = sentence.split(' ')

    for idx, word in enumerate(sentence):
        if searchWord == word[:len(searchWord)]:
            return idx + 1

    return -1


def isPrefixOfWord2(sentence: str, searchWord: str) -> int:
    sentence = sentence.split(' ')

    for i, word in enumerate(sentence):
        if word.startswith(searchWord):
            return i+1

    return -1
