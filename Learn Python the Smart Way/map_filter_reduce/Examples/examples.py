from functools import reduce

# Basic number functions
numbers = [1, 2, 3, 4, 5]
total_sum = reduce(lambda x, y: x + y, numbers)
total_product = reduce(lambda x, y: x * y, numbers)
max_number = reduce(lambda x, y: x if x > y else y, numbers)
min_number = reduce(lambda x, y: x if x < y else y, numbers)

assert total_sum == 15
assert total_product == 120
assert max_number == 5
assert min_number == 1

# Concatenate a list of strings into one long string using reduce.
strings = ['Hello', ' ', 'world', '!']
concatenated_string = reduce(lambda x, y: x + y, strings)
assert concatenated_string == 'Hello world!'

# Given a list of integers, create a new list that contains only the even numbers using reduce.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = reduce(lambda acc, num: acc + [num] if num % 2 == 0 else acc, numbers, [])
assert even_numbers == [2, 4, 6, 8, 10]

# Given a list of strings, create a new list that contains only the strings with a length of 3 characters using reduce.
strings = ['hello', 'world', 'foo', 'bar', 'spam', 'eggs']
three_letter_strings = reduce(lambda acc, string: acc + [string] if len(string) == 3 else acc, strings, [])
assert three_letter_strings ==  ['foo', 'bar']

# Given a list of numbers, create a new list that contains the cumulative sum of the numbers using reduce.
numbers = [1, 2, 3, 4, 5]
cumulative_sum = reduce(lambda acc, num: acc + [acc[-1] + num] if acc else [num], numbers, [])
assert cumulative_sum == [1, 3, 6, 10, 15]

# Given a list of tuples containing a name and an age, 
# create a dictionary where the keys are the names and the values are the ages using reduce.
people = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
age_dict = reduce(lambda acc, person: {**acc, person[0]: person[1]}, people, {})
assert age_dict == {'Alice': 25, 'Bob': 30, 'Charlie': 35}

# Given a list of strings, create a dictionary where the keys are the strings and 
# the values are the number of times each string appears in the list using reduce.
strings = ['foo', 'bar', 'foo', 'spam', 'eggs', 'foo']
string_count = reduce(lambda acc, string: {**acc, string: acc.get(string, 0) + 1}, strings, {})
assert string_count == {'foo': 3, 'bar': 1, 'spam': 1, 'eggs': 1}

# Given a list of tuples containing a name and a salary, find the average salary using reduce:
employees = [('Alice', 50000), ('Bob', 60000), ('Charlie', 70000)]
average_salary = reduce(lambda acc, emp: acc + emp[1], employees, 0) / len(employees)
assert average_salary == 60000.0

# Given a list of strings, find the longest string using reduce:
strings = ['foo', 'bar', 'spam', 'eggs', 'hello world']
longest_string = reduce(lambda acc, string: string if len(string) > len(acc) else acc, strings, '')
assert longest_string =='hello world'

# Given a list of strings, create a new list that contains the strings in reverse order using reduce:
strings = ['foo', 'bar', 'spam', 'eggs']
reverse_strings = reduce(lambda acc, string: [string] + acc, strings, [])
assert reverse_strings == ['eggs', 'spam', 'bar', 'foo']

# Given a list of tuples containing a name and a list of scores, create a dictionary where 
# the keys are the names and the values are the average score using reduce:
scores = [('Alice', [80, 90, 95]), ('Bob', [75, 85, 90]), ('Charlie', [90, 95, 100])]
average_scores = reduce(lambda acc, score: {**acc, score[0]: sum(score[1]) / len(score[1])}, scores, {})
assert average_scores == {'Alice': 88.33333333333333, 'Bob': 83.33333333333333, 'Charlie': 95.0}
