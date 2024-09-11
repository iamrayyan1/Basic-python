# Two lists are given : list1 = ["Hello ", "take "] , list2 = ["Dear", "Sir"]
# Concatenate these two lists like this : ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

x = zip(list1, list2)

newList = [l1 + l2 for l1 in list1 for l2 in list2]

print(newList)