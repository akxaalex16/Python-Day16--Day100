piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
print(piano_keys[2:5])
# this gives you ["c", "d", "e"], starts at second position but does not include the 5th position

print(piano_keys[2:])
# this gives you ['c', 'd', 'e', 'f', 'g'], starts at second position and goes until the end of the list

print(piano_keys[:5])
# this gives you ['a', 'b', 'c', 'd', 'e'], starts at the beginning of the list and includes the 4th position

print(piano_keys[2:5:2])
# this gives you ['c', 'e'], slicing from 2 to 4, but skipping in between
# third value is the increment value

print(piano_keys[::2])
# gets everything in the list, but skips every other item
# gives you ['a', 'c', 'e', 'g']

print(piano_keys[::-1])
# this reverses the list
# gives you ['g', 'f', 'e', 'd', 'c', 'b', 'a']

piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")
print(piano_tuple[2:5])
# this gives you ('mi', 'fa', 'so'),