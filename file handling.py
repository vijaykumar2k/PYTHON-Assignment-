# File Handling
# Mechanism to read and write the file

# To save data parmanently into file

# File Handling
#     open function
#         read or write
# close

# a=open("text.txt", "r+")      #a story memory address
# by default it opens in read mode

# out=a.read()
# a.close()
# print("out->", out)
# print('cursor 1:', a.tell())  # tell function tells the current position of cursor
# a.write("##")
# print('cursor 2:', a.tell())

# out=a.read()
# a.seek(4)
# print('cursor 3:', a.tell())
# a.close()   
# print("out->", out)

# a=open("text.txt", "r+")      #a story memory address

# with open("text.txt", "r+") as a:
#     out=a.read()

# print(out)


# with open("text.txt", "r") as a:
#     print( a.readlines() )   # readlines function reads all the lines and gives in the form of list
    

# line by line read
with open("text.txt", "r") as a:
    for line in a:
       for word in line.split():
           print(word)