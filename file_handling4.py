f = open("index.txt", "a")
f.write(" enzo john")
f.close()

# reading the file

f = open("index.txt", "r")
print(f.read())