with open("standard.txt", "r") as file:
    lines = file.readlines()

start = 289
end = 289 + 8
pattern = lines[start:end]

for line in pattern:
    print(line, end="")