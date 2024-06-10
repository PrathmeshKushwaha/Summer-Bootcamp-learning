fruits = ['orange', 'mango', 'papaya', 'grape', 'watermelon']

fruits.append('kiwi')
print("Q1.1 - After appending 'kiwi':", fruits)

fruits.insert(2, 'pear')
print("Q1.2 - After inserting 'pear' at index 2:", fruits)

fruits.remove('mango')
print("Q1.3 - After removing 'mango':", fruits)

first_fruit = fruits[0]
last_fruit = fruits[-1]
print("Q1.4 - First and last fruit:", first_fruit, last_fruit)

even_numbers = [x for x in range(21) if x % 2 == 0]
print("Q4.1 - Even numbers:", even_numbers)

squares = [x ** 2 for x in range(1, 11)]
print("Q4.2 - Squares from 1 to 10:", squares)

words = ['hello', 'world', 'python', 'lists']
uppercased_words = [word.upper() for word in words]
print("Q4.3 - Uppercased words:", uppercased_words)

nested_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = [item for sublist in nested_list for item in sublist]
print("Q4.4 - Flattened list from nested list:", flattened_list)

from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Q6.1 - Sum of numbers using reduce:", sum_of_numbers)

cubes = list(map(lambda x: x ** 3, numbers))
print("Q6.2 - Cubes of numbers using map:", cubes)

even_numbers_filtered = list(filter(lambda x: x % 2 == 0, numbers))
print("Q6.3 - Even numbers using filter:", even_numbers_filtered)

names = ['David', 'Eva', 'Frank']
scores = [88, 90, 85]
zipped_names_scores = list(zip(names, scores))
print("Q6.4 - Zipped names and scores:", zipped_names_scores)

num_list = [1, 2, 3, 4, 5]

num_list.append(7)
print("Q3.1 - After appending 7:", num_list)

num_list.insert(0, 0)
print("Q3.2 - After inserting 0 at the beginning:", num_list)

last_element = num_list.pop()
print("Q3.3 - Last element popped:", last_element, "Remaining list:", num_list)

count_of_2 = num_list.count(2)
print("Q3.4 - Count of '2':", count_of_2)

index_of_3 = num_list.index(3)
print("Q3.5 - Index of '3':", index_of_3)

num_list.reverse()
print("Q3.6 - After reversing:", num_list)

#sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1.union(set2)
print("Union of sets:", union_set)

intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)

difference_set = set1.difference(set2)
print("Difference between sets:", difference_set)

symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference between sets:", symmetric_difference_set)

set3 = {1, 2, 3}

set3.add(4)
print("Adding element 4 to the set:", set3)

set3.remove(2)
print("Removing element 2 from the set:", set3)

set3.discard(3)
print("Discarding element 3 from the set:", set3)

set3.clear()
print("Clearing the set:", set3)

set4 = {1, 2, 3}
set5 = set4.copy()
print("Copying set4 to set5:", set5)

set6 = {1, 2}
set7 = {1, 2, 3, 4}
is_subset = set6.issubset(set7)
is_superset = set7.issuperset(set6)
print("Is set6 a subset of set7?", is_subset)
print("Is set7 a superset of set6?", is_superset)

set8 = {1, 2, 3}
set9 = {4, 5, 6}
is_disjoint = set8.isdisjoint(set9)
print("Are set8 and set9 disjoint?", is_disjoint)

#tules

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

concatenated_tuple = tuple1 + tuple2
print("Concatenation of tuples:", concatenated_tuple)

repeated_tuple = tuple1 * 3
print("Repetition of tuple1:", repeated_tuple)

print("First element of tuple1:", tuple1[0])
print("Last element of tuple2:", tuple2[-1])

tuple3 = (3, 1, 2, 5, 4)

count_2 = tuple3.count(2)
print("Count of '2' in tuple3:", count_2)

index_5 = tuple3.index(5)
print("Index of '5' in tuple3:", index_5)

#dict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 4, 'd': 5, 'e': 6}

merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)

print("Value associated with key 'b':", dict1['b'])
print("Value associated with key 'd':", dict2.get('d'))

dict1['f'] = 7
print("Adding key-value pair 'f':", dict1)

removed_value = dict1.pop('b')
print("Removed value associated with key 'b':", removed_value, "Updated dictionary:", dict1)

keys = dict2.keys()
values = dict2.values()
print("Keys of dict2:", keys)
print("Values of dict2:", values)

is_key_present = 'c' in dict1
print("Is key 'c' present in dict1?", is_key_present)
