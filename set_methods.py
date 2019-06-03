

# Set Methods (17)
#
# .add(), .copy(), .remove(), .difference(), .difference_update(), .discard(), .pop(), .intersection(), .intersection_update(), .isdisjoint(), .issubset(), .issuperset(), .symmetric_difference(), .symmetric_difference_update(), .union(), .update() and .clear()
#
# by Kerem Kandıralı
# https://twitter.com/keremkandirali
# https://github.com/keremkandirali


my_set = {'Apple', 'Orange', 'Banana'}


my_set.add('Peach')  # my_set.add(elem*)
# Adds a new unordered item to the set.
# {'Orange', 'Apple', 'Peach', 'Banana'}


my_set.copy()  # my_new_set = my_set.copy()
# Copies the set.
# {'Apple', 'Orange', 'Banana'}


my_set.remove('Apple')  # my_set.remove(elem*)
# Removes an item from the set. Raises KeyError if the item doesn't exist.
# {'Banana', 'Orange'}


my_set.difference({'Orange', 'Kiwi'}, {'Apple'})  # my_new_set = my_set.difference(others)
# Returns the items in the set which are different than the items in given set(s).
# {'Banana'}


my_set.difference_update({'Orange', 'Kiwi'}, {'Apple'})  # my_set.difference_update(others)
# Removes the items from the set which are same with the items in given set(s).
# {'Banana'}


my_set.discard('Apple')  # my_set.discard(elem*)
# Removes an item from the set. Returns None if the item doesn't exist.
# {'Banana', 'Orange'}


my_set.pop()
# Drops a random item from the set. After executing this method, my_set now returns the remaining items of the set.
# e.g. 'Orange'


my_set.intersection({'Orange', 'Apple', 'Kiwi'})  # my_new_set = my_set.intersection(others)
# Returns the items in the set which are same with the items in given set(s).
# {'Orange', 'Apple'}


my_set.intersection_update({'Orange', 'Apple', 'Kiwi'})  # my_set.intersection_update(others)
# Removes the items from the set which are different than the items in given set(s).
# {'Orange', 'Apple'}


my_set.isdisjoint({'Pencil', 'Table', 'Paper'})  # my_set.isdisjoint(other*)
# Checks if the set has no common items with the given set.
# True


my_set.issubset({'Apple', 'Orange', 'Banana', 'Peach', 'Kiwi'})  # my_set.issubset(other*)
# Checks if all the items of the set exist in the given set.
# True


my_set.issuperset({'Apple', 'Orange'})  # my_set.issuperset(other*)
# Checks if all the items of the given set exist in the set.
# True


my_set.symmetric_difference({'Apple', 'Kiwi'})  # my_new_set = my_set.symmetric_difference(other*)
# Returns a new set with the items which are not common in the sets.
# {'Orange', 'Banana', 'Kiwi'}


my_set.symmetric_difference_update({'Apple', 'Kiwi'})  # my_set.symmetric_difference_update(other*)
# Updates the set with the items which are not common in the sets.
# {'Orange', 'Banana', 'Kiwi'}


my_set.union({'Apple', 'Cherry'}, {'Banana', 'Kiwi'})  # my_new_set = my_set.union(others*)
# Merges the set with other sets, lists, tuples, strings or any other iterables and returns a new set.
# {'Apple', 'Cherry', 'Orange', 'Kiwi', 'Banana'}


my_set.update({'Apple', 'Cherry'}, {'Banana', 'Kiwi'})  # my_set.update(others*)
# Merges the set with other sets, lists, tuples, strings or any other iterables.
# {'Apple', 'Cherry', 'Orange', 'Kiwi', 'Banana'}


my_set.clear()
# Removes all items from the set.
# set()


# (*) required
