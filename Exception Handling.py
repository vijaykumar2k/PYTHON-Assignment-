'''
exception : unwanted conditon that arises during the execution of a program
jiski wajh se your program may give you different results or may stop working


'''
x= ""
# try:
#     print("hey")
#     print(x)
#     print("hello")
# except Exception as e:  #Exception is a class where all exceptions are defined
    
#     print("Error generated",e)

# exception - programing language


# try:
#     print("hey")
#     print(x)
# except NameError as e: 
#     print("Error generated",e)

# try:
#     print("hey", str(10) + "a")
#     print(x)
# except (NameError, TypeError) as e:
#     print("Error=>", e)


# try:
#     print("asdf.txt")
#     print("hey", 10+"a")
#     print(x)
# except (NameError,  TypeError) as e:
#     print("Error=>",e)
# except Exception as f:
#     print("all exception =>",f)


# try:
#     try:
#         open("text.txt")
#     except:    
#         print("file  not found")
#     print("heyy")
# except Exception as f:
#     print("all exception=>",f)



# try:
#     try:
#         open("text22.txt")
#     except:    
#         print("file  not found")
#     print("heyy",x1)
#     print(x)


# except Exception as f:
#     print("all exception=>",f)
# else:
#     print("else block here")


# try:
#     print("heyy")

# except Exception as f:
#     print("all exception=>",f)
# finally:
#     print("finally block here")


try:
    a=int(input("Enter number:") )
    if(a>100):
        print("Welcome with value of a",a)
    else:
        raise ValueError("A value is less than 100")
except ValueError as e:
    print("Raised exception is e",e)