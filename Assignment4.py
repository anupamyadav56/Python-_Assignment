# List handling function and methods.
'''
       #min()
#1.Find the smallest number.
numbers = [12, 45, 7, 89, 23]
print(min(numbers))
#2.Print the minimum mark.
marks = [56, 78, 91, 45, 67]
print(min(marks))
#3.Find the lowest price.
prices = [299, 150, 499, 199, 99]
print(min(prices))

#      max()
#1.Find the largest number
numbers = [10, 55, 78, 32, 91]
print(max(numbers))
#2.Print the highest mark.
marks = [67, 81, 93, 88, 74]
print(max(marks))
#3.Find the highest salary.
salary = [25000, 32000, 28000, 45000]
print(max(salary))
         #len()
#1.Find the length of the list.
fruits = ["apple", "banana", "mango"]
print(len(fruits))
#2.Print the total number of elements.
numbers = [10, 20, 30, 40, 50, 60]
print(len(numbers))
#3.Find the list length.
letters = ["A", "B", "C", "D", "E"]
print(len(letters))

        #append()
#1.Add 40.
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)
#2.Add "mango".
fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)
#3.Add "green".
colors = ["red", "blue"]
colors.append("green")
print(colors)

            # index()
#1.Find the index of "mango".
fruits = ["apple", "banana", "mango", "orange"]
print(fruits.index("mango"))
#2.Find the index of 20.
numbers = [10, 20, 30, 40]
print(numbers.index(20))
#3.Find the position of "blue".
colors = ["red", "green", "blue"]
print(colors.index("blue"))

              #insert()
#1.insert 30 at index 2.
numbers = [10, 20, 40]
numbers.insert(2,30)
print(numbers)
#2.Insert "banana" at index 1.
fruits = ["apple", "mango"]
fruits.insert(1,"banana")
print(fruits)
#3.Insert "B" at index 1.
letters = ["A", "C", "D"]
letters.insert(1,"b")
print(letters)

                 #extend().
#1.Join both lists.
list1 = [1, 2]
list2 = [3, 4]
list1.extend(list2)
print(list1)
#2.Combine the lists
fruits = ["apple", "banana"]
more = ["mango", "orange"]
fruits.extend(more)
print(fruits)
                  # pop().
#1.Remove the last element.
numbers = [10, 20, 30, 40]
numbers.pop()
print(numbers)
#2.Remove the last fruit.
fruits = ["apple", "banana", "mango"]
fruits.pop()
print(fruits)
#3.Remove the element at index 1.
colors = ["red", "blue", "green"]
colors.pop(1)
print(colors)

                  #remove().
#1.Remove 20.
numbers = [10, 20, 30, 40]
numbers.remove(20)
print(numbers)
#2.Remove "banana"
fruits = ["apple", "banana", "mango"]
fruits.remove("banana")
print(fruits)
#3.Remove "B".
letters = ["A", "B", "C"]
letters.remove("B")
print(letters)

                   #reverse()
#1.Reverse each list.
numbers = [10, 20, 30, 40]
numbers.reverse()
print(numbers)
#2.Reverse each list.
fruits = ["apple", "banana", "mango"]
fruits.reverse()
print(fruits)

                       #sort().
#1.Sort in ascending order.
numbers = [45, 12, 89, 23, 67]
numbers.sort()
print(numbers)
#2.Sort in descending order.
numbers = [45, 12, 89, 23, 67]
numbers.sort(reverse=True)
print(numbers)
#3.Sort alphabetically.
fruits = ["mango", "apple", "banana", "orange"]
fruits.sort()
print(fruits)

                       #clear().
#1.Remove all elements.
numbers = [10, 20, 30]
numbers.clear()
print(numbers)
#2.Make the list empty
fruits = ["apple", "banana"]
fruits.clear()
print(fruits)

                 #⭐ Bonus Challenge (Mix All Methods).
numbers = [25, 10, 45, 30, 15]
#Perform the following in order:
#Find the minimum value.
print(min(numbers))
#Find the maximum value.
print(max(numbers))
#Find the length of the list.
print(len(numbers))
#Append 50.
numbers.append(50)
print(numbers)
#Insert 20 at index 2.
numbers.insert(2,20)
print(numbers)
#Remove 30.
numbers.remove(30)
print(numbers)
#Pop the last element.
numbers.pop()
print(numbers)
#Reverse the list.
numbers.reverse()
print(numbers)
#Sort the list in ascending order.
numbers.sort()
print(numbers)
#Count how many times 10 appears.
print(numbers.count(10))
#Find the index of 45.
print(numbers.index(45))
'''