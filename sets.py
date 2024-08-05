# =========================================
# This is the Header
# =========================================

# Define the lists
my_list1 = [1, 5, 9, 0]
my_list2 = [3, 0, 2, 9]

# Create a set from my_list1 for O(1) lookups
set1 = set(my_list1)
set2 = set(my_list2)
set3 = set1.copy()

set1.add(2)
#set1.clear()


union_set = set3.union(set2)
intersection_set = set3.intersection(set2)
set2.intersection_update(set3)
difference_set = set1.difference(set2)
#difference_update = set1.difference_update(set2)
sym_diff_set = set2.symmetric_difference(set3)

set1.discard(9)

print(union_set)
print(intersection_set)
print(difference_set)
print(set1)
print(set2)
print(sym_diff_set)
