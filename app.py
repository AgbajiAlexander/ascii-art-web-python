def get_char_pattern(char, lines):
    ascii_val = ord(char)
    start = 1 + (ascii_val - 32) * 9
    end = start + 8
    pattern = lines[start:end]
    return pattern

with open("standard.txt", "r") as file:
    lines = file.readlines()

#start = 289
#end = 289 + 8
#pattern = lines[start:end]

#for line in pattern:
#   print(line, end="")

result = get_char_pattern("#", lines)
for line in result:
    print(line, end="")