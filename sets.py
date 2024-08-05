# =========================================
# This is the Header
# =========================================

# Define the lists
my_list1 = [1, 5, 9, 0]
my_list2 = [3, 0, 2, 9]

# Create a set from my_list1 for O(1) lookups
set1 = set(my_list1)
set2 = set(my_list2)

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set2.difference(set1)
sym_diff_set = set2.symmetric_difference(set1)

print(union_set)
print(intersection_set)
print(difference_set)
print(sym_diff_set)
