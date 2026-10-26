# File Handling

# open a file
# f = open("file path", 'mode to open file')

# read mode ('r'): used to read the data from the file, file should exists in the defined path
f = open('file.txt',"r")
a = f.read()
print(a)
f.close()

# write mode('w'): used to write in a file, if the defined file doesnot exist a file is created, if file exist previous data is replaced my new data
f = open('file.txt',"w")
a = f.write("Writing Writing Writing Writing")
print(a)
f.close()

# append mode(a): used to write in a file, if the defined file doesnot exist a file is created, if file exist new data is added at the end of previous data
f = open('file.txt',"a")
a = f.write(" eiditing a file ")
print(a)
f.close()
