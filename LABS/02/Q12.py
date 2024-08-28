# 12. Write a python program that takes any two lists from user having same number of
# elements. Make a dictionary from these two lists in such a way that first element of first list
# will be key and first element of second list will be its associated value and so on and print the result.
# Note: do not use any library. Make logic yourself.


def main():

    list_1 = [1,2,3,4,5,6]
    list_2 = ["Hello", "World", "123", "345", "Rayyan", 3]

    dict = merge_list(list_1, list_2)
    
    print(dict)
    # or
    for i, j in dict.items():
        print(f"{i}: {j}")


def merge_list(list_1, list_2):
    dict = {}

    for i in range(len(list_1)):
        dict[list_1[i]] = list_2[i]

    return dict


main()
