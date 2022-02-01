
# try and except

# this will throw an exception!
# can use more than one except case

try:
    d = {}
    d["a"]
    int("a")
except ValueError:
    print("A value exception happened")
except KeyError:
    print("A key was not found")
finally:
    print("we get here no matter what")

print("End of the program.")

# Traceback (most recent call last):
#   File "exceptions.py", line 2, in <module>
#     int("a")
# ValueError: invalid literal for int() with base 10: 'a'