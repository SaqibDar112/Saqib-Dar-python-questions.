def reverse_string(old_string):
    new_string = ""
    for x in old_string:
        new_string = x + new_string
    return new_string

old_string = "1234abcd"

print("The reverse string is : ", reverse_string(old_string))