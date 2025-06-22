this is my content

# file handling?
# files => store in hdd
# permanenet storage / secondary storage
# file handling => read / write
'''
file handling => file open
read ya write operation
file close
'''

# fileobj = open ("filehandling.txt")
# print( fileobj.read(s) )
# fileobj.close() 


# fileobj = open ("filehandling.txt", "w")
# fileobj.write("$$$$")
# fileobj.close() 


# fileobj = open ("filehandling.txt", "r+")
# print(fileobj.read())
# fileobj.write("!@!")
# fileobj.close() 



# fileobj = open ("filehandling.txt", "w+")
# fileobj.write("hello")
# print(fileobj.read())

# fileobj.close()


# fileobj = open("filehandling.txt", "w+")
# print("Cursor1:" , fileobj.tell())
# fileobj.write("hello")
# print("Cursor2:", fileobj.tell())

# print(fileobj.read())



# fileobj = open("filehandling.txt", "w+")
# print("Cursor1:" , fileobj.tell())
# fileobj.write("hello")
# print("Cursor2:", fileobj.tell())

# fileobj.seek(2)
# print("Cursor3:" , fileobj.tell())

# print(fileobj.read())
# print("Cursor1:", fileobj.tell())






# #older
# with open("filehandling.txt", "r") as f:
#     print(f.read())
#     #no close here



# with open("filehandling.txt", "r") as f:
#     print(f.readline() )
#     print(f.readline() )


#     #no close here





# with open("filehandling.txt", "r") as f:
#     for i in f:
#         print(i)

#     #no close here





# with open("filehandling.txt", "r") as f:
#     print(f.readline() )    #[line1, line2, line3]




# with open("filehandling.txt", "r") as f:
#     for line in f.readline():
#         print(line)



# import csv
# f=open("filehandling.txt")
# csvf=csv.reader(f)
# for i in csvf:
#     print(i)



'''

