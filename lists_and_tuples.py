# -*- coding: utf-8 -*-
"""Lists_and_Tuples.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XDt9HHU9rsOE9sPHbXPnmTYlKuDrhqi-
"""

fruits = ["apple", "banana", "orange"]
more_fruits = ["mango", "grape"]
fruits.extend(more_fruits)
print(fruits)

my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 6)
print(my_list)

my_list = [10, 20, 30, 40, 50]
print(my_list.pop(1))
print(my_list)

my_list = [10,20,30,40,50]
print(my_list.pop())
my_list

my_list = [10,20,30,40,50]
my_list.remove(40)
print(my_list)

list = [6,5,7,9,2]
list.reverse()
print(list)

my_list = [1, 2, 3, 4, 5]
print(my_list[::3])
my_list.sort(reverse = True)
print(my_list)

fruits = ("apple", "banana", "apple", "orange")
fruits.count("apple")

fruits[1]

numbers = (10,20,5,30)
print(sum(numbers))

print(min(numbers))
print(max(numbers))

fruits = ("apple","banana","orange")
print(len(fruits))

[1,2,3]+[1,2,3]

B=[1,2,[3,'a'],[4,'b']]
B[3][1]

A = [1]
A.append([2,3,4,5])
A

A = [1]
A.extend([2,3,4,5])
A