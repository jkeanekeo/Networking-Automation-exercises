f = open("test.txt", "w")
f.write("Hello, this is a test file.\n")
f.close()

f = open("test.txt", "r")
text = f.read()
print (text)
f.close