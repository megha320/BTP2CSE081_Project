# if we open our file in this format, so we don't need to close the file.
with open("note.txt", "r") as f1:
    file = f1.read() # read whole data present at that file in normal format
    data = f1.readline() # read line by line.
    store = f1.readlines() # read whole data present at that file in list.
    # all of these 3 function take indexing as argument.
    print(file)
    print(data)
    print(store)

# another syntax to open a file where we have to close the file after perfoming all operations.
file_obj = open("note") # if we don't pass any mode while opening a file, so it will open in read mode by default.
# do operation on file.
file_obj.close() 
# we have to close the file, so that any of data will never get vanished or go in buffer.