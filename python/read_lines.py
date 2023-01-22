file = open('file.txt', 'r')
lines = []
for i in range(2):
    lines.append(file.readline())


print(lines)

file.close()
