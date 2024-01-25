# Assignment 5 - Exercise 10
# Create a new list from two list using the following condition
# Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list 
# and even numbers from the second list.

# Merge the lists
# Make new two new lists, odd numbers of list 1 and even numbers of list 2

def merge_list(list_1, list_2):
    result_list = [num for num in list_1 if num % 2 != 0] + [num for num in list_2 if num % 2 == 0]
    return result_list

list_1 = [10, 20, 25, 30, 35]
list_2 = [40, 45, 60, 75, 90]

# Print output

print("Result List:", merge_list(list_1, list_2))