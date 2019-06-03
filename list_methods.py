

# Python List Methods (11)
#
# .append(), .copy(), .count(), .extend(), .index(), .insert(), .pop(), .remove(), .reverse(), .sort() and .clear()
#
# by Kerem Kandıralı
# https://twitter.com/keremkandirali
# https://github.com/keremkandirali


my_list = ['Apple', 'Orange', 'Banana']


my_list.append('Peach')  # my_list.append(x*)
# Adds a new item to the list.
# ['Apple', 'Orange', 'Banana', 'Peach']


my_list.copy()  # my_new_list = my_list.copy()
# Copies the list.
# ['Apple', 'Orange', 'Banana']


my_list.count('Apple')  # my_list.count(x*)
# Counts an item in the list.
# 1


my_list.extend(['Kiwi', 'Cherry'])  # my_list.extend(iterable*)
# Merges the list with another list, set, tuple, string or any other iterable.
# ['Apple', 'Orange', 'Banana', 'Kiwi', 'Cherry']


my_list.index('Banana')  # my_list.index(x*)
# Finds the index of the item in the list. Raises ValueError if not found.
# 2
my_list.index('Banana', 1, 3)  # my_list.index(x*, start, end)
# Finds the index of the item in the list in the given slice. Raises ValueError if not found.
# 2


my_list.insert(2, 'Peach')  # my_list.insert(i*, x*)
# Adds an item to a specific index in the list.
# ['Apple', 'Orange', 'Peach', 'Banana']


my_list.pop()
# Drops the latest item from the list. After executing this method, my_list now returns ['Apple', 'Banana'].
# 'Orange'
my_list.pop(1)  # my_list.pop(i)
# Drops the item in the given index from the list. After executing this method, my_list now returns ['Apple', 'Banana'].
# 'Orange'


my_list.remove('Banana')  # my_list.remove(x*)
# Removes an item from the list.
# ['Apple', 'Orange']


my_list.reverse()
# Reverses the ordering of the items in the list.
# ['Banana', 'Orange', 'Apple']


my_list.sort()
# Sorts the items in the list.
# ['Apple', 'Banana', 'Orange']
my_list.sort(key=None, reverse=False)
# Sorts the items in the list based on the given parameters. key stands for a function. key=None and reverse=False by default.
# An example for the .sort() method with parameters:
def second_item_of_tuple(elem):
    return elem[1]

example_list = [(3, 9), (0, 1), (8, 5)]
example_list.sort(key=second_item_of_tuple, reverse=False)
print('Example list after .sort() method:', example_list)
# Sorts the list according to the second items of the tuples it holds.
# [(0, 1), (8, 5), (3, 9)]


my_list.clear()
# Removes all items from the list.
# []


# (*) required
