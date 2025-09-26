#  Example 1: Sorting tuples by second element
pairs = [(1, 5), (2, 3), (4, 1), (3, 9)]
pairs.sort(key=lambda x: x[1])
print(pairs)  # Output: [(4, 1), (2, 3), (1, 5), (3, 9)]

#  Example 2: Sorting dictionary by values
data = {"apple": 3, "banana": 1, "cherry": 2}
sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))
print(sorted_data)  # Output: {'banana': 1, 'cherry': 2, 'apple': 3}

#  Example 3: Sorting list of dictionaries
people = [
    {"name": "John", "age": 28},
    {"name": "Alice", "age": 22},
    {"name": "Bob", "age": 25}
 ]
sorted_people = sorted(people, key=lambda x: x["age"])
print(sorted_people)
 # [{'name': 'Alice', 'age': 22}, {'name': 'Bob', 'age': 25}, {'name': 'John', 'age': 28}]

#  Example 4: Custom filtering
names = ["Sam", "Samantha", "Alex", "Jonathan", "Jo"]
long_names = list(filter(lambda name: len(name) > 3, names))
print(long_names)  # Output: ['Samantha', 'Alex', 'Jonathan']

# Nested Lambdas
double = lambda x: x * 2
triple = lambda x: x * 3
combine = lambda f, g, x: f(g(x))
print(combine(double, triple, 2))  # Output: 12  (double(triple(2)))

