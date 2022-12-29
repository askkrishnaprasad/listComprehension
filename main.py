import pandas

# Find the squares of a list using list comprehension
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
# Another way of using pythons exponents symbol for square
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

# Find even numbers from numbers using list comprehension
even_numbers = [item for item in numbers if item % 2 == 0]
print(even_numbers)

# Compare data from two files and print the common data between each other.
with open("file1.txt") as data_file1:
    file_1 = data_file1.readlines()
with open("file2.txt") as data_file2:
    file_2 = data_file2.readlines()

new_list = [int(item.rstrip()) for item in set(file_1) & set(file_2)]
# new_list = [int(item.rstrip()) for item in file_1 if item in file_2]
print(new_list)

# Example for Dictionary comprehension looping through a list
sentence = "What is the Aspired Velocity of an Unladen Swallow"
sentence_list = sentence.split()
result = {sentence_temp: len(sentence_temp) for sentence_temp in sentence_list}
print(result)

# Example for Dictionary comprehension looping through a dictionary itself
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 21,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}
weather_f = {new_key: (new_value * (9 / 5)) + 32 for (new_key, new_value) in weather_c.items()}
print(weather_f)

# Use the iterrows() pandas function to iterate through the rows of a DataFrame
student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 77, 65]
}
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
for(index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
