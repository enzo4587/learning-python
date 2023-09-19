f = open("index.txt", "w")
f.write("oops deleted!")
f.close()

# reading the file

f = open("index.txt", "r")
print(f.read())