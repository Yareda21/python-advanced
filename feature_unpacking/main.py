# basic unpacking 
a, b, c = [1,2,3]

print(f"a: {a}, b: {b}, c: {c}")

# extended iterable unpacking with *
a, b, *c = [1, 2, 3, 4, 5]
print(f"a: {a}, b: {b}, c: {c}")

# ignoring values 
a, _, c = [1, 2, 3]
print(f"a: {a}, c: {c}")


# Unpacking nested structures 
name, (age, gender) = ["Yared", (28, "Male")]
print(f"Name : {name} \nAge: {age} \nGender: {gender}")

# Unpacking in a function - helps to receive many arguments 
def printing_names(*names): 
    """
    Print each name provided as an argument.

    Args:
        *names: A variable number of name strings to be printed.
    """
    for name in names:
        print(name)

printing_names("Abebe", "Kebede", "Chala")

# combining Lists with unpacking 
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Combine two lists into one using unpacking
combined_list = [*list1, *list2]

# combining dictionaries with unpacking
dict1 = {"name": "A", "age": 22, "address": "CMC"}
dict2 = {"name": "B", "age": 23, "address": "DMD"}

# Combine two dictionaries into one using unpacking
combined_dicts = {**dict1, **dict2}

# value swapping without using an additional variable 
x = 10
y = 20
print(f"Before swapping:  x = {x} and y = {y}")

# Swap values of x and y
x, y = y, x 
print(f"After swapping:  x = {x} and y = {y}")
