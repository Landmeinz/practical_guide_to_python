
# indintation matters; there are no code blocks with {}

# greetings = ["hello", "hi", "howdy", "hola"]

# for greeting in greetings: 
#     print(f"{greeting}, World!")


colors = ["red", "green", "blue", "orange"]

for color in colors:
    print(f"the color is: {color}")

# color still exists as the last value of color; even outside of the function
# beware of var names

for num in range(3, 7):
    print(num)

enumerate(colors)

print(colors)

color_set = list(enumerate(colors))

print('color_set', color_set)

print(color_set[0])

print(color_set)

for index, color in enumerate(colors):
    print(f"{index}: color: {color}")

hex_colors = {
    "red" :'123',
    "blue" : '456',
    "yellow" : '789'
}

hex_colors_index = set(enumerate(hex_colors))

print(hex_colors_index)

def test_num(number):
    if number < 100:
        print("test_num is a small number")
    elif number == 100: 
        print("right on the money")
    else:
        print("huge number")

test_num(200)

print(colors)

print([len(color) for color in colors])

print([color[0] for color in colors])

print([color for color in colors if len(color)%2==0])
print([color for color in colors if len(color)%2!=0])


# slicing
my_string = "hello, world!"
print(my_string[:5])
print(my_string[:8])
print(my_string[3:])
print(my_string[9:])

# cheat sheet for working with files
# https://practical.learnpython.dev/05_practical_applications/40_working_with_files/

# can use a context managers 
# we can open() and close() files or just use the keyword "with" for that built in functionality


# cities = [{
# 		"name": "New York",
# 		"pop": 8550405
# 	},
# 	{
# 		"name": "Los Angeles",
# 		"pop": 3971883
# 	},
# 	{
# 		"name": "Chicago",
# 		"pop": 2720546
# 	},
# 	{
# 		"name": "Houston",
# 		"pop": 2296224
# 	},
# 	{
# 		"name": "Philadelphia",
# 		"pop": 1567442
# 	}
# ]

# import this via the file structure using HTTP JSON 
# run: brew install wget

# run: wget https://practical.learnpython.dev/code/cities.json to add to project folder

# to put it into a var import json and assign it by opening the json and targeting the data

import json

with open("cities.json") as cities_file:
    cities_data = json.load(cities_file)
    print('--- in open file', cities_data)

print('--- same as above:', cities_data)

# NICE!


# class vs an instance of that class
# if you change an instance it doesn't effect the class itself
# an instance is a specific type within that class

class Car: 
    runs = True








# generator functions reviews



