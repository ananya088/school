# ==================================================
# TOPIC 6: SETS IN PYTHON
# ==================================================

# 1. Set
# Definition:
# A set is a collection of unique elements.
# Sets are unordered, mutable, and do not allow duplicates.

# Example:
numbers = {10, 20, 30, 10, 20}
print(numbers)

# Output:
# {10, 20, 30}

# Explanation:
# Duplicate values are automatically removed.
# The order of elements in a set is not guaranteed.


# ==================================================
# 2. Creating a Set
# ==================================================

# Definition:
# A set is created using curly braces {} or set().

# Example:
fruits = {"apple", "banana", "mango"}
print(fruits)

# Output:
# Contains apple, banana, and mango.
# The display order may vary.

# Creating an empty set:
empty_set = set()
print(type(empty_set))

# Output:
# <class 'set'>

# Remember:
# {} creates an empty dictionary, not an empty set.


# ==================================================
# 3. add() Method
# ==================================================

# Definition:
# add() adds one element to a set.

# Example:
numbers = {10, 20, 30}
numbers.add(40)

print(numbers)

# Output:
# Contains 10, 20, 30, and 40.
# The display order may vary.


# ==================================================
# 4. update() Method
# ==================================================

# Definition:
# update() adds multiple elements from an iterable to a set.

# Example:
numbers = {10, 20}
numbers.update([30, 40, 50])

print(numbers)

# Output:
# Contains 10, 20, 30, 40, and 50.
# The display order may vary.


# ==================================================
# 5. remove() Method
# ==================================================

# Definition:
# remove() deletes a specified element from a set.
# It raises a KeyError if the element does not exist.

# Example:
numbers = {10, 20, 30}
numbers.remove(20)

print(numbers)

# Output:
# {10, 30}


# ==================================================
# 6. discard() Method
# ==================================================

# Definition:
# discard() removes an element if it exists.
# It does not raise an error if the element is missing.

# Example:
numbers = {10, 20, 30}
numbers.discard(20)
numbers.discard(50)

print(numbers)

# Output:
# {10, 30}

# Explanation:
# 20 is removed.
# 50 is missing, but no error occurs.


# ==================================================
# 7. pop() Method
# ==================================================

# Definition:
# pop() removes and returns an arbitrary element from a set.

# Example:
numbers = {10, 20, 30}
removed = numbers.pop()

print("Removed:", removed)
print("Remaining:", numbers)

# Output:
# The removed element may vary.
# The remaining set contains the other elements.

# Remember:
# Sets are unordered, so do not expect a specific
# element to be removed.


# ==================================================
# 8. clear() Method
# ==================================================

# Definition:
# clear() removes all elements from a set.

# Example:
numbers = {10, 20, 30}
numbers.clear()

print(numbers)

# Output:
# set()


# ==================================================
# 9. len() Function
# ==================================================

# Definition:
# len() returns the number of unique elements in a set.

# Example:
numbers = {10, 20, 30, 10}
print(len(numbers))

# Output:
# 3


# ==================================================
# 10. Union of Sets
# ==================================================

# Definition:
# Union combines all unique elements from two sets.

# Operator:
# |

# Method:
# union()

# Example:
a = {10, 20, 30}
b = {30, 40, 50}

print(a | b)

# Output:
# Contains 10, 20, 30, 40, and 50.


# ==================================================
# 11. Intersection of Sets
# ==================================================

# Definition:
# Intersection returns the elements common to both sets.

# Operator:
# &

# Method:
# intersection()

# Example:
a = {10, 20, 30}
b = {20, 30, 40}

print(a & b)

# Output:
# {20, 30}


# ==================================================
# 12. Difference of Sets
# ==================================================

# Definition:
# Difference returns elements present in the first set
# but not in the second set.

# Operator:
# -

# Method:
# difference()

# Example:
a = {10, 20, 30}
b = {20, 30, 40}

print(a - b)

# Output:
# {10}


# ==================================================
# 13. Symmetric Difference
# ==================================================

# Definition:
# Symmetric difference returns elements that are in
# either set, but not in both sets.

# Operator:
# ^

# Method:
# symmetric_difference()

# Example:
a = {10, 20, 30}
b = {20, 30, 40}

print(a ^ b)

# Output:
# {10, 40}


# ==================================================
# 14. Membership Operators
# ==================================================

# Definition:
# in checks whether an element exists in a set.
# not in checks whether an element does not exist.

# Example:
numbers = {10, 20, 30}

print(20 in numbers)
print(50 not in numbers)

# Output:
# True
# True


# ==================================================
# 15. issubset() Method
# ==================================================

# Definition:
# issubset() checks whether all elements of one set
# are present in another set.

# Example:
a = {10, 20}
b = {10, 20, 30, 40}

print(a.issubset(b))

# Output:
# True


# ==================================================
# 16. issuperset() Method
# ==================================================

# Definition:
# issuperset() checks whether a set contains all
# elements of another set.

# Example:
a = {10, 20, 30}
b = {10, 20}

print(a.issuperset(b))

# Output:
# True


# ==================================================
# 17. isdisjoint() Method
# ==================================================

# Definition:
# isdisjoint() returns True if two sets have no
# common elements.

# Example:
a = {10, 20}
b = {30, 40}

print(a.isdisjoint(b))

# Output:
# True


# ==================================================
# 18. Removing Duplicates from a List
# ==================================================

# Definition:
# A set can be used to remove duplicate values from a list.

# Example:
numbers = [10, 20, 10, 30, 20]
unique_numbers = set(numbers)

print(unique_numbers)

# Output:
# Contains 10, 20, and 30.
# The display order may vary.


# ==================================================
# 19. Important Points to Remember
# ==================================================

# 1. Sets use curly braces {} with elements inside.
# 2. Sets do not allow duplicate values.
# 3. Sets are unordered.
# 4. Sets are mutable.
# 5. Set elements must be hashable.
# 6. add() adds one element.
# 7. update() adds multiple elements.
# 8. remove() raises an error if the element is missing.
# 9. discard() does not raise an error if it is missing.
# 10. Union combines unique elements.
# 11. Intersection finds common elements.
# 12. Difference finds elements in the first set only.
# 13. Use set() to create an empty set.


# ==================================================
# 20. Difference Between remove() and discard()
# ==================================================

# remove():
# Removes an element.
# Raises KeyError if the element is missing.

# discard():
# Removes an element if present.
# Does not raise an error if the element is missing.


# ==================================================
# 21. Practical Questions
# ==================================================

# Easy:
# 1. Create a set of five numbers and print it.
s = {10, 20, 30, 40, 50}
print(s)
# 2. Add an element using add().
s = {10, 20, 30, 40, 50}
s.add(60)
print(s)
# 3. Remove an element using discard().
s = {10, 20, 30, 40, 50}
s.remove(50)
print(s)

# Medium:
# 4. Find the union of two sets.
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
# 5. Find the intersection of two sets.
a = {1, 2, 3}
b = {3, 4, 5}

print(a.intersection(b))
# 6. Remove duplicates from a list using a set.
numbers = [1, 2, 2, 3, 4, 4, 5]
s = set(numbers)
print(s)

# Hard:
# 7. Find the difference between two sets.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.difference(b))
# 8. Check whether one set is a subset of another.
a = {1, 2}
b = {1, 2, 3, 4}

if a.issubset(b):
    print("A is a subset of B")
else:
    print("A is not a subset of B")
# 9. Find the symmetric difference of two sets.
a = {1, 2, 3}
b = {3, 4, 5}

print(a.symmetric_difference(b))

# -------------------------------------------------------------------------------------------

























































# s=set() 
# s=(1,2,4,5)
# # ///////////////////
# s.add(1)
# print(s)
# s.update({5,7,3,55})
# # //////////////////////
# s.clear()
# s.pop()
# s.remove()
# ///////////////////////
# s={1,2,3,4,6,7}
# s1={1,2,3}
# print(s.difference(s1))
# print(s.intersection(s1))
# print(s.issubset(s1))
# print(s.issuperset(s1))
# print(s.symmetric_difference(s1))
# print(s.difference_update(s1))
# print(s)

# //////////////////////////////////////////////////

# s=set()
# s=1,2,3,4,5
# print(s)

# s={20,30,50,40}
# s.add(60)
# print(s)

# s={20,30,50,40}
# s.remove(50)
# print(s)


# s = {10, 20, 30, 40, 50}
# print(len(s))

# s = {10, 20, 30, 40, 50}
# s.clear()
# print(s)

# s = {10, 20, 30, 40, 50}
# s1={10,20,30,40,50,60,70}
# print(s.intersection(s1))


# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a.union(b))

# # a = {1, 2, 3, 4}
# # b = {3, 4, 5, 6}
# # print(a.difference(b))

# s = {1, 2, 3, 4}
# s1 = {3, 4, 5, 6}
# print(s.symmetric_difference(s1))

# s= {1, 2}
# s1= {1, 2, 3, 4}
# print(s.issubset(s1))


# s= {1, 2, 3}
# s1= {1,2 ,4, 5, 6}
# print(s.isdisjoint(s1))

# s= {1, 2, 3}
# s1= {1, 2, 4, 5, 6}
# ****************************************



