# open the file in read mode 
file_read = open("input.txt", "r")
print("File in read Mode -")
print(file_read.read())
file_read.close()

# open the file in write mode
file_write = open("input.txt", "w")

#write in the file
file_write.write("File is write mode ....")
file_write.write("Hi! I am Sudip ")

file_write.close()

#open the file in append mode
file_append = open("input.txt", "a")

#append in the file
file_append.write("File is append mode")
file_append.write("Hi! I am Sudip ")
file_append.close()
