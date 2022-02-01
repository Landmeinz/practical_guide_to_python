
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
