# A set of List examples

# 1 creating an empty list
empty_list = []


# creating a simple list of strings
students = ["Prince", "Oke", "Gabriel"]
print(students)

# creating a simple list of integers
scores = [33, 67, 9, 5 , 1002, 5, 3, 99, 15, 1, 87, 194, 3, 40, 3, 67, 67]
print(scores)


# 2 counting the number of items in a list (AKA the length of the list)
print("the empty list has ", len(empty_list), " items")
print("the student list has ", len(students), " items")

# 3 appending (adding an item to the end of a list)
empty_list.append("late guy")
print("students")


# 4 pushing an item to the start of a list
print(students)
students.push("first student")
print(students)

# 5 popping (removing an item at the end of a list )
print(scores)

scores.pop(4)
print(scores)

scores.pop(0)
print(scores)


# 6 identifying the position of an item in a list (finding the item's index)
oke_index = students.index("Oke")
prince_index = students.index("Prince")


# 7 adding  a new item to a list at a certain index
print(students)
students.insert(1, "Max")
print(students)


# removing  an item from a list at a certain index
print(scores)
scores.remove(1002)
print(scores)

# count the number of times a variable with the same value is in a list
# for example, how many threes are in the scores list?
num_of_threes = scores.count(3)
print(scores)
print(num_of_threes)