#open a file --> file Handlers

Sam_file=open("File_handlersSample.txt","w")
linenum=1
print("Name of the file  :  ", Sam_file.name)

Sam_file.write("welcome to the world of Python");
Sam_file.write("we are working with files");
Sam_file.write("Hello World");
print ("Closed ? : ", Sam_file.closed)
print("Opening mode : ", Sam_file.mode)
##for text in Sam_file: #iterates over lines of file
##    Sam_file.read()
##    print('\n', "next line1")
##    linenum+=1
##    print(linenum)
#always close opened file
Sam_file.close()
