'''
Print all combinations of phrases formed by picking words from each of the given lists

Given N lists of words, print all combinations of phrases that can be
formed by picking one word each from each of the given lists.

input -> arr = [
    ['I', 'You', 'They'],
    ['love', 'hate'],
    ['food', 'games']
]

output ->  [
    'I love food', 'I love games', 'I hate food', 'I hate games',
    'You love food', 'You love games', 'You hate food', 'You hate games',
    'They love food', 'They love games', 'They hate food', 'They hate games'
]
'''


def phrases(arr):
    n = len(arr)

    if n == 0:
        return []
    
    if n == 1:
        return arr[0]
        
    all_combinations = arr[0]
    
    for i in range(1, n):
        current_combinations = []
        current_phrases = arr[i]
        
        for combination in all_combinations:
            for phrase in current_phrases:
                current_combinations.append(f'{combination} {phrase}')
            
        all_combinations = current_combinations
        
    return all_combinations 


def phrases(arr, i=0):
    '''Time and Space O(m^n*ns)'''
    if i == len(arr):
        return ['']
    else:
        fromNext = phrases(arr, i+1)
        output = []

        for word in arr[i]:
            for phrase in fromNext:
                curr_str = (' ' if len(phrase) > 0 else '')
                output.append(word + curr_str + phrase)

        return output
