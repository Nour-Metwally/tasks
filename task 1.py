#!/usr/bin/env python
# coding: utf-8

# **1-Write a Python program to calculate the length of a string using 2 ways

# In[16]:


def calculate_length_using_len(string):
    return len(string)
my_string = "Hello, World!"

# Calculate length using len() function
length_using_len = calculate_length_using_len(my_string)
print("Length using len() function:", length_using_len)


# In[17]:


def calculate_length_using_iteration(string):
    count = 0
    for char in string:
        count += 1
    return count

my_string = "Hello, World!"

length_using_iteration = calculate_length_using_iteration(my_string)
print("Length using iteration:", length_using_iteration)


# **2-Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead ("##Sample String : 'w3resource'
# Expected Result : 'w3ce'
# ##Sample String : 'w3'
# Expected Result : 'w3w3'
# ##Sample String : ' w'
# Expected Result : Empty String)

# In[10]:


def get_first_and_last_two_chars(string):
    if len(string) >= 2:
        return string[:2] + string[-2:]
    else:
        return ""

# Example 
sample_strings = ['w3resource', 'w3', ' w']

for sample in sample_strings:
    result = get_first_and_last_two_chars(sample)
    print(f"Sample String: '{sample}'  Result: '{result}'")


# **3-Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. (Sample String : 'abc'
# Expected Result : 'abcing')

# In[11]:


def add_ing_ly(string):
    if len(string) < 3:
        return string
    elif string.endswith('ing'):
        return string + 'ly'
    else:
        return string + 'ing'

# Example usage:
sample_strings = ['abc', 'testing', 'read']

for sample in sample_strings:
    result = add_ing_ly(sample)
    print(f"Sample String: '{sample}'  Result: '{result}'")


# **4-Write a Python function that takes a list of words and return the longest word and the length of the longest one
# (Longest word: Exercises
# Length of the longest word: 9)

# In[12]:


def longest_word_and_length(word_list):
    if not word_list:
        return None, 0

    longest_word = ""
    max_length = 0

    for word in word_list:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)

    return longest_word, max_length

# Example usage:
word_list = ['Python', 'programming', 'is', 'fun', 'for', 'everyone']
longest_word, length = longest_word_and_length(word_list)
print("Longest word:", longest_word)
print("Length of the longest word:", length)


# **5-Write a Python program to change a given string to a newly string where the first and last chars have been exchanged using 2 ways (Sample String:abca  Expected Result:ebce)

# In[19]:


def exchange_chars_direct(string):
    if len(string) < 2:
        return string
    return string[-1] + string[1:-1] + string[0]
#
sample_string = "abca"
#
result_direct = exchange_chars_direct(sample_string)
print("Result using direct manipulation:", result_direct)


# In[20]:


def exchange_chars_slicing(string):
    if len(string) < 2:
        return string
    return string[-1] + string[1:-1] + string[0]
#
sample_string = "abca"
#
result_slicing = exchange_chars_slicing(sample_string)
print("Result using slicing and concatenating:", result_slicing)


# **6-Write a Python program to remove characters that have odd index values in a given string (Sample String:abca Expected Result:ac)

# In[ ]:


def remove_odd_index_chars(string):
    return ''.join([char for index, char in enumerate(string) if index % 2 == 0])

# Sample string
sample_string = "abca"

# Remove characters with odd index values
result = remove_odd_index_chars(sample_string)
print("Result:", result)


# **7-Write a Python program to count the occurrences of each word in a given sentence (Sample String:amr and ahmed are frindes but amr is the tallest Expected Result:2)

# In[21]:


def count_word_occurrences(sentence):
    word_count = {}
    words = sentence.split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# Sample sentence
sample_sentence = "amr and ahmed are friends but amr is the tallest"

# Count occurrences of each word
word_occurrences = count_word_occurrences(sample_sentence)
print("Occurrences of each word:")
for word, count in word_occurrences.items():
    print(f"{word}: {count}")


# **8-Write a Python script that takes input from the user and displays that input back in upper and lower cases

# In[ ]:


user_input = input("Enter a string: ")

# Display input back in upper case
print("Input in upper case:", user_input.upper())

# Display input back in lower case
print("Input in lower case:", user_input.lower())


# **9-Write a Python function to reverse a string if its length is a multiple of 4

# In[22]:


def reverse_string_if_multiple_of_4(input_string):
    # Check if the length of the string is a multiple of 4
    if len(input_string) % 4 == 0:
        # Reverse the string and return
        return input_string[::-1]
    else:
        
        return input_string

# Example usage:
input_string = "python"
result = reverse_string_if_multiple_of_4(input_string)
print("Result:", result) 
input_string = "reverse"
result = reverse_string_if_multiple_of_4(input_string)
print("Result:", result)  


# **10- Write a Python program to remove a newline in Python

# In[23]:


def remove_newline_with_replace(string_with_newline):
    return string_with_newline.replace('\n', '')

# Example usage:
string_with_newline = "Hello\nWorld\n"
result = remove_newline_with_replace(string_with_newline)
print("Result:", result)


# **11-Write a Python program to check whether a string starts with specified characters

# In[24]:


def starts_with_specified_characters(string, characters):
    return string.startswith(characters)

# Example usage:
input_string = "Python is awesome"
specified_characters = "Pyt"
result = starts_with_specified_characters(input_string, specified_characters)
print("Does the string start with specified characters?", result)  # Output will be True


# **12- Write a Python program to add prefix text to all of the lines in a string

# In[25]:


def add_prefix_to_lines(input_string, prefix):
    lines = input_string.split('\n')  # Split the string into lines
    prefixed_lines = [prefix + line for line in lines]  # Add prefix to each line
    return '\n'.join(prefixed_lines) 

# Example usage:
input_string = "Hello\nWorld\nPython"
prefix = "Prefix: "
result = add_prefix_to_lines(input_string, prefix)
print("Result:")
print(result)


# **13-Write a Python program to print the following numbers up to 2 decimal places

# In[ ]:


numbers = [3.141592653589793, 2.718281828459045, 1.618033988749895]

# Print numbers up to 2 decimal places
for number in numbers:
    print("{:.2f}".format(number))


# **14-Write a Python program to print the following numbers up to 2 decimal places with a sign

# In[26]:


numbers = [3.141592653589793, -2.718281828459045, 1.618033988749895]

# Print numbers up to 2 decimal places with sign
for number in numbers:
    if number >= 0:
        print("+{:.2f}".format(number))
    else:
        print("{:.2f}".format(number))


# **15-Write a Python program to display a number with a comma separator

# In[27]:


number = 1000000

# Display the number with comma separator
print("{:,}".format(number))


# **16-Write a Python program to reverse a string using 2 ways

# In[ ]:


def reverse_string_slicing(input_string):
    return input_string[::-1]

# Example usage:
input_string = "hello"
reversed_string = reverse_string_slicing(input_string)
print("Reversed string:", reversed_string)


# In[ ]:


def reverse_string_iteration(input_string):
    reversed_str = ''
    for char in input_string:
        reversed_str = char + reversed_str
    return reversed_str

# Example usage:
input_string = "hello"
reversed_string = reverse_string_iteration(input_string)
print("Reversed string:", reversed_string)


#  **17-Write a Python program to count repeated characters in a string (hint:use dictionary)

# In[40]:


def count_repeated_characters(input_string):
    # Initialize an empty dictionary to store character counts
    char_count = {}

   
    for char in input_string:
        
        char_count[char] = char_count.get(char, 0) + 1

    # Filter out characters with count greater than 1
    repeated_characters = {char: count for char, count in char_count.items() if count > 1}

    return repeated_characters

# Example usage:
input_string = "hello"
repeated_chars = count_repeated_characters(input_string)
print("Repeated characters:", repeated_chars)


# **18-Write a Python program to find the first non-repeating character in a given string

# In[41]:


def first_non_repeating_char(input_string):
    # Initialize an empty dictionary to store character counts
    char_count = {}


    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1

    
    for char in input_string:
        if char_count[char] == 1:
            return char

    # Return None if there is no non-repeating character
    return None

# Example usage:
input_string = "hello"
non_repeating_char = first_non_repeating_char(input_string)
if non_repeating_char:
    print("First non-repeating character:", non_repeating_char)
else:
    print("No non-repeating character found")


# **19-Write a Python program to remove spaces from a given string

# In[42]:


def remove_spaces(input_string):
    return input_string.replace(" ", "")

# Example usage:
input_string = "hello world"
result = remove_spaces(input_string)
print("Result:", result)


# **20-Write a Python program to count the number of non-empty substrings of a given string

# In[44]:


def count_non_empty_substrings(input_string):
    count = 0
    n = len(input_string)
#
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = input_string[i:j]
            # Check if the substring is non-empty
            if substring:
                count += 1

    return count

# Example usage:
input_string = "abc"
result = count_non_empty_substrings(input_string)
print("Number of non-empty substrings:", result)


# **21-write a Python program to swap first and last element of any list.

# In[45]:


def swap_first_last(lst):
    if len(lst) < 2:
        return lst  
    
    # Swap the first and last elements using a temporary variable
    temp = lst[0]
    lst[0] = lst[-1]
    lst[-1] = temp

    return lst

# Example usage:
my_list = [1, 2, 3, 4, 5]
result = swap_first_last(my_list)
print("List after swapping first and last elements:", result)


# **22-Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. (Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90])

# In[46]:


def swap_elements(lst, pos1, pos2):
    # Check if the positions are valid
    if pos1 < 0 or pos1 >= len(lst) or pos2 < 0 or pos2 >= len(lst):
        print("Invalid positions.")
        return lst

    # Swap the elements at the given positions
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]

    return lst

# Example usage:
my_list = [23, 65, 19, 90]
position1 = 1
position2 = 3
result = swap_elements(my_list, position1, position2)
print("List after swapping elements at positions {} and {}: {}".format(position1, position2, result))


# **23- search for the all ways to know the length of the list

# In[ ]:


**24-write a Python code to find the Maximum number of list of numbers.


# In[47]:


def find_maximum(numbers):
    # Check if the list is empty
    if not numbers:
        return None
    
    # Find the maximum number 
    maximum = max(numbers)
    
    return maximum

# Example usage:
numbers = [23, 65, 19, 90]
max_number = find_maximum(numbers)
print("Maximum number:", max_number)


# In[ ]:


**25-write a Python code to find the Minimum number of list of numbers.


# In[48]:


def find_minimum(numbers):
  
    if not numbers:
        return None
    
    # Find the minimum number in the list
    minimum = min(numbers)
    
    return minimum

# Example usage:
numbers = [23, 65, 19, 90]
min_number = find_minimum(numbers)
print("Minimum number:", min_number)


# **26-search for if an elem is existing in list

# In[49]:


def search_element_in_list(lst, elem):
    return elem in lst

# Example usage:
my_list = [1, 2, 3, 4, 5]
element_to_search = 3
exists = search_element_in_list(my_list, element_to_search)
if exists:
    print(f"{element_to_search} exists in the list.")
else:
    print(f"{element_to_search} does not exist in the list.")


# **27- clear python list using different ways

# In[50]:


my_list = [1, 2, 3, 4, 5]
my_list.clear()
print("List after clearing using clear() method:", my_list)


# **28-remove duplicated elements from a list

# In[51]:


def remove_duplicates(lst):
    unique_list = list(set(lst))
    return unique_list

# Example usage:
my_list = [1, 2, 3, 4, 2, 5, 3]
result = remove_duplicates(my_list)
print("List after removing duplicates:", result)


# **29-Given list values and keys list, convert these values to key value pairs in form of list of dictionaries. (Input : test_list = [“Gfg”, 3, “is”, 8], key_list = [“name”, “id”]
# Output : [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}])

# In[52]:


def convert_to_key_value_pairs(test_list, key_list):
    result = []
    
    for i in range(0, len(test_list), len(key_list)):
        # Construct a dictionary with keys from key_list and corresponding values from test_list
        temp_dict = {key_list[j]: test_list[i+j] for j in range(len(key_list))}
        result.append(temp_dict)
    
    return result

# Example usage:
test_list = ["Gfg", 3, "is", 8]
key_list = ["name", "id"]
result = convert_to_key_value_pairs(test_list, key_list)
print("Output:", result)


# **30-write a python program to count unique values inside a list using different ways

# In[53]:


def count_unique_values(lst):
    unique_values = set(lst)
    return len(unique_values)

# Example usage:
my_list = [1, 2, 3, 4, 2, 5, 3]
result = count_unique_values(my_list)
print("Number of unique values:", result)


# **31-write a python program Extract all elements with Frequency greater than K (Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3 
# Output : [4, 3] )

# In[54]:


def extract_elements_with_frequency_greater_than_K(test_list, K):
    
    count_dict = {}
    for elem in test_list:
        count_dict[elem] = count_dict.get(elem, 0) + 1
    
    result = [elem for elem, count in count_dict.items() if count > K]
    
    return result

# Example usage:
test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
K = 3
result = extract_elements_with_frequency_greater_than_K(test_list, K)
print("Output:", result)


# **32-write a python program to find the Strongest Neighbour (Input: 1 2 2 3 4 5
# Output: 2 2 3 4 5)

# In[55]:


def find_strongest_neighbor(arr):
    n = len(arr)
    result = []
    for i in range(n):
        if i == 0:
            result.append(arr[i+1])
        elif i == n-1:
            result.append(arr[i-1])
        else:
            strongest_neighbor = max(arr[i-1], arr[i+1])
            result.append(strongest_neighbor)
    return result

# Example usage:
input_list = [1, 2, 2, 3, 4, 5]
strongest_neighbors = find_strongest_neighbor(input_list)
print("Strongest Neighbors:", strongest_neighbors)


# **33-write a Python Program to print all Possible Combinations from the three Digits (Input: [1, 2, 3]
# Output:
# 1 2 3 ##
# 1 3 2 ##
# 2 1 3 ##
# 2 3 1 ##
# 3 1 2 ##
# 3 2 1)

# In[56]:


from itertools import permutations

def print_all_combinations(digits):
   
    perm = permutations(digits)
    
    for p in perm:
        print("##", *p)

# Example usage:
input_digits = [1, 2, 3]
print_all_combinations(input_digits)


# **34-write a Python program to find all the Combinations in the list with the given condition (Input: test_list = [1,2,3] 
# Output: 
#  [1], [1, 2], [1, 2, 3], [1, 3]
#  [2], [2, 3], [3])

# In[57]:


def find_combinations(test_list):
    n = len(test_list)
    result = []
    for i in range(n):
        for j in range(i, n):
            result.append(test_list[i:j+1])
    return result

# Example usage:
test_list = [1, 2, 3]
result = find_combinations(test_list)
print("Output:", result)



# **35-write a Python program to get all unique combinations of two Lists (List_1 = ["a","b"]
# List_2 = [1,2]
# Unique_combination = [[('a',1),('b',2)],[('a',2),('b',1)]] )

# In[58]:


from itertools import product

def get_unique_combinations(list_1, list_2):
   
    combinations = product(list_1, list_2)
    
    unique_combinations = [list(comb) for comb in combinations]
    
    return unique_combinations

# Example usage:
List_1 = ["a", "b"]
List_2 = [1, 2]
Unique_combination = get_unique_combinations(List_1, List_2)
print("Unique combinations:", Unique_combination)


# **36-Remove all the occurrences of an element from a list in Python (Input : 1 1 2 3 4 5 1 2 1 
# 
# **Output : 2 3 4 5 2)

# In[59]:


def remove_all_occurrences(input_list, element):
    
    new_list = [x for x in input_list if x != element]
    return new_list

# Example usage:
input_list = [1, 1, 2, 3, 4, 5, 1, 2, 1]
element_to_remove = 1
result = remove_all_occurrences(input_list, element_to_remove)
print("List after removing all occurrences of {}: {}".format(element_to_remove, result))


# **37-write a python program to Replace index elements with elements in Other List (The original list 1 is : [‘Gfg’, ‘is’, ‘best’] The original list 2 is : [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0] The lists after index elements replacements is : [‘Gfg’, ‘is’, ‘best’, ‘is’, ‘Gfg’, ‘Gfg’, ‘Gfg’, ‘best’, ‘is’, ‘is’, ‘best’, ‘Gfg’])

# In[65]:


def replace_index_elements(original_list, index_list):
    # Create a copy of the original list to avoid modifying it directly
    modified_list = original_list[:]

    # Replace elements at specified indices with elements from original_list
    modified_list = [original_list[index] for index in index_list]

    return modified_list

# Example usage:
original_list_1 = ['Gfg', 'is', 'best']
original_list_2 = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]
result = replace_index_elements(original_list_1, original_list_2)
print("The lists after index elements replacements:", result)


# **38- write python program to Retain records with N occurrences of K(Input : test_list = [(4, 5, 5, 4), (5, 4, 3)], K = 5, N = 2 
# Output : [(4, 5, 5, 4)]
# Input : test_list = [(4, 5, 5, 4), (5, 4, 3)], K = 5, N = 3 
# Output : [] )

# In[66]:


def retain_records_with_N_occurrences(test_list, K, N):

    result = [tup for tup in test_list if tup.count(K) == N]
    return result

# Example usage:
test_list = [(4, 5, 5, 4), (5, 4, 3)]
K = 5
N = 2
output = retain_records_with_N_occurrences(test_list, K, N)
print("Output:", output)

test_list = [(4, 5, 5, 4), (5, 4, 3)]
K = 5
N = 3
output = retain_records_with_N_occurrences(test_list, K, N)
print("Output:", output)


# **39-write a Python Program to Sort the list according to the column using lambda
# array = [[1, 3, 3], [2, 1, 2], [3, 2, 1]]
# Output :
# Sorted array specific to column 0, [[1, 3, 3], [2, 1, 2], [3, 2, 1]]
# Sorted array specific to column 1, [[2, 1, 2], [3, 2, 1], [1, 3, 3]]
# Sorted array specific to column 2, [[3, 2, 1], [2, 1, 2], [1, 3, 3]]

# In[67]:


def sort_list_by_column(array, column):
    # Sort the list according to the specified column
    sorted_array = sorted(array, key=lambda x: x[column])
    return sorted_array

# Example usage:
array = [[1, 3, 3], [2, 1, 2], [3, 2, 1]]

# Sort the array according to column 0
sorted_column_0 = sort_list_by_column(array, 0)
print("Sorted array specific to column 0:", sorted_column_0)

# Sort the array according to column 1
sorted_column_1 = sort_list_by_column(array, 1)
print("Sorted array specific to column 1:", sorted_column_1)

# Sort the array according to column 2
sorted_column_2 = sort_list_by_column(array, 2)
print("Sorted array specific to column 2:", sorted_column_2)


# In[ ]:


**40- write a program to Sort Python Dictionaries by Key or Value
Input:
{'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

Output: 
{'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}


# In[1]:


def sort_dict_by_key(dictionary):
    return {k: v for k, v in sorted(dictionary.items())}

def sort_dict_by_value(dictionary):
    return {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])}


input_dict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

sorted_by_key = sort_dict_by_key(input_dict)
print("Sorted by Key:", sorted_by_key)

sorted_by_value = sort_dict_by_value(input_dict)
print("Sorted by Value:", sorted_by_value)


# **41-write python program to Remove keys with Values Greater than K ( Including mixed values )
# nput : test_dict = {‘Gfg’ : 3, ‘is’ : 7, ‘best’ : 10, ‘for’ : 6, ‘geeks’ : ‘CS’},
# K = 7 
# Output : {‘Gfg’ : 3, ‘for’ : 6, ‘geeks’ : ‘CS’}

# In[5]:


def remove_keys_with_greater_values(dictionary, k):
    return {key: value for key, value in dictionary.items() if not (isinstance(value, int) and value > k)}

# Sample input dictionary
test_dict = {'Gfg': 3, 'is': 7, 'best': 10, 'for': 6, 'geeks': 'CS'}
K = 7

# Remove keys with values greater than K
output_dict = remove_keys_with_greater_values(test_dict, K)
print("Output:", output_dict)


# **42-Write a Python program to concatenate the following dictionaries to create a new one
# 
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# In[7]:


# Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create a new dictionary and concatenate the sample dictionaries
result_dict = {}
result_dict.update(dic1)
result_dict.update(dic2)
result_dict.update(dic3)

print("Concatenated Dictionary:", result_dict)


# **43-Write a Python program to iterate over dictionaries using for loops

# In[6]:


my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Iterate over keys
print("Iterating over keys:")
for key in my_dict:
    print(key)


# **44- Write a Python script to merge two Python dictionaries

# In[39]:


def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

# Sample dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge the dictionaries
result = merge_dictionaries(dict1, dict2)
print("Merged dictionary:", result)


# **45-Write a Python program to get the maximum and minimum values of a dictionary values

# In[38]:


def get_max_min_values(dictionary):
    # Use dictionary comprehension to extract values
    values = [value for value in dictionary.values() if value is not None]

    # Check if the dictionary is not empty
    if values:
        # Return the maximum and minimum values
        return max(values), min(values)
    else:
        return None, None  

# Sample dictionary
sample_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 30}

# Get the maximum and minimum values
max_value, min_value = get_max_min_values(sample_dict)

# Print the results
print("Maximum value:", max_value)
print("Minimum value:", min_value)


# **46- Write a Python program to drop empty items from a given dictionary.
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

# In[37]:


def drop_empty_items(original_dict):
    return {key: value for key, value in original_dict.items() if value is not None}

# Original Dictionary
original_dict = {'c1': 'Red', 'c2': 'Green', 'c3': None}

# New Dictionary after dropping empty items
new_dict = drop_empty_items(original_dict)
print("New Dictionary after dropping empty items:", new_dict)


# **47-Write a Python program to create a tuple of numbers and print one item

# In[36]:


# Create a tuple of numbers
numbers_tuple = (1, 2, 3, 4, 5)

# Print one item from the tuple
print("One item from the tuple:", numbers_tuple[2])  # Prints the third item (index 2)


# **48-Write a Python program to unpack a tuple into several variables

# In[35]:


# Define a tuple
my_tuple = (1, 2, 3)

# Unpack the tuple into separate variables
a, b, c = my_tuple

# Print the values of the variables
print("a:", a)
print("b:", b)
print("c:", c)


# **49-Write a Python program to add an item to a tuple

# In[34]:


def add_item_to_tuple(input_tuple, item):
    return input_tuple + (item,)

# Sample tuple
sample_tuple = (1, 2, 3, 4, 5)
item_to_add = 6

# Add an item to the tuple
result_tuple = add_item_to_tuple(sample_tuple, item_to_add)
print("Modified tuple:", result_tuple)


# **50-Write a Python program to convert a tuple to a string

# In[33]:


def tuple_to_string(input_tuple):
    return ''.join(str(elem) for elem in input_tuple)

# Sample tuple
sample_tuple = (1, 2, 3, 4, 5)

# Convert the tuple to a string
result_string = tuple_to_string(sample_tuple)
print("Converted string:", result_string)


# **51-Write a Python program to convert a list to a tuple

# In[32]:


def list_to_tuple(input_list):
    return tuple(input_list)

# Sample list
sample_list = [1, 2, 3, 4, 5]

# Convert the list to a tuple
result_tuple = list_to_tuple(sample_list)
print("Converted tuple:", result_tuple)


# **52-Write a Python program to reverse a tuple

# In[31]:


def reverse_tuple(input_tuple):
    return input_tuple[::-1]

# Sample tuple
sample_tuple = (1, 2, 3, 4, 5)

# Reverse the tuple
reversed_tuple = reverse_tuple(sample_tuple)
print("Reversed tuple:", reversed_tuple)


# **53-Write a Python program to replace the last value of tuples in a list.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

# In[30]:


def replace_last_value(tuple_list, new_value):
    updated_list = []
    for tup in tuple_list:
        updated_tup = list(tup)
        updated_tup[-1] = new_value
        updated_list.append(tuple(updated_tup))
    return updated_list

# Sample list
sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_value = 100

# Replace the last value in each tuple
result = replace_last_value(sample_list, new_value)
print("Expected Output:", result)


# **54-Write a Python program to convert a given string list to a tuple
# Original string: python 3.0
# <class 'str'>
# Convert the said string to a tuple:
# ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')

# In[29]:


def string_list_to_tuple(string_list):
    # Concatenate all strings in the list into a single string
    concatenated_string = ''.join(string_list)
    
    # Convert the concatenated string into a tuple of characters
    char_tuple = tuple(concatenated_string)
    return char_tuple

# Example usage:
original_string_list = ['python', ' ', '3.0', ' ', '<class', ' ', "'str'"]
result_tuple = string_list_to_tuple(original_string_list)
print("Convert the said string to a tuple:", result_tuple)


# **55-Write a Python program to calculate the average value of the numbers in a given tuple of tuples

# In[28]:


def average_value(tuple_of_tuples):
    # Flatten the tuple of tuples into a single list
    flattened_list = [num for inner_tuple in tuple_of_tuples for num in inner_tuple]

    # Calculate the average value
    average = sum(flattened_list) / len(flattened_list)
    return average

# Example usage:
tuple_of_tuples = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
average = average_value(tuple_of_tuples)
print("Average value:", average)


# **56-Write a Python program to add member(s) to a set.

# In[15]:


def add_members_to_set(my_set, *members):
    # Using add() method to add a single member
    for member in members:
        my_set.add(member)
    print("Members added successfully.")

# Sample set
my_set = {1, 2, 3, 4}

# Add a single member to the set
add_members_to_set(my_set, 5)
print("Updated Set:", my_set)

# Add multiple members to the set
my_set.update([6, 7, 8])
print("Updated Set:", my_set)


# **57-Write a Python program to remove an item from a set if it is present in the set.

# In[14]:


def remove_item_from_set(my_set, item):
    # Using remove() method
    if item in my_set:
        my_set.remove(item)
        print(f"Item '{item}' removed from the set.")
    else:
        print(f"Item '{item}' not found in the set.")

# Sample set
my_set = {1, 2, 3, 4, 5}

# Remove item 3 from the set
remove_item_from_set(my_set, 3)
print("Updated Set:", my_set)

# Try to remove item 6 (not present) from the set
remove_item_from_set(my_set, 6)
print("Updated Set:", my_set)


# **58-Write a Python program to create an intersection,union,difference and symmetric difference of sets

# In[13]:


# Sample sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Intersection
intersection = set1.intersection(set2)
print("Intersection:", intersection)

# Union
union = set1.union(set2)
print("Union:", union)

# Difference (elements in set1 but not in set2)
difference = set1.difference(set2)
print("Difference (set1 - set2):", difference)

# Symmetric Difference (elements in either set1 or set2 but not both)
symmetric_difference = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference)


# **59-Write a Python program to find the maximum and minimum values in a set

# In[8]:


my_set = {10, 20, 30, 40, 50}

# Find maximum value
max_value = max(my_set)
print("Maximum value:", max_value)

# Find minimum value
min_value = min(my_set)
print("Minimum value:", min_value)


# **60- Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

# In[9]:


def find_pairs_with_sum(lst, target_sum):
    pairs = []
    seen = set()

    for num in lst:
        complement = target_sum - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)

    return pairs

# Example usage:
my_list = [1, 2, 3, 4, 5, 6]
target = 7
result = find_pairs_with_sum(my_list, target)

print("Pairs with sum equal to", target, "are:", result)


# In[ ]:




