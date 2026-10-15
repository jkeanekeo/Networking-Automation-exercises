'''
f = open("test.txt", "a")
f.write("Hello, this is a test file.\n")
f.close()

f = open("test.txt", "r")
text = f.read()
print (text)
f.close
'''

with open("test.txt", "a") as f:
    f.write("hello, i am adding another line here. \n")

with open("test.txt", "r") as f:
    text = f.read()
    print(text)
