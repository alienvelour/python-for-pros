list = [1, 2, 3, 4, 5]

tup = (1, 2, 3, 4, 5)

set_ = {1, 2, 3, 4, 5}

dict_ = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}

project_names = ["Payments API", "Orders API", "User Management API"]
project_names.append("Inventory API")

newlist = [1, 2, 3] + [4, 5, 6]
newlist.extend([7, 8, 9])

mixed = [1, "two", 3.0, True]  # Don't do this

version = ("alpha", 0.2)  # Immutable

unique_priorities = {"low", "medium", "high", "urgent", "low"}

project = {"name": "Payments API", "archived": False}
project.keys()
project.values()
project.items()  # Key-Value pairs
len(newlist)
len("name")

letters = "A B C D E"
letters.split(" ")  # ['A', 'B', 'C', 'D', 'E']

names = ["Bob", "Alice", "Charlie"]
" ".join(names)  # 'Bob Alice Charlie'
names.sort()  # Sorts the list in alphabetical order ['Alice', 'Bob', 'Charlie']
sorted(names)  # Returns a new sorted list ['Alice', 'Bob', 'Charlie']
