# The sctipt copies the content of one file to another file.
source_file = input("Please input the name of the source file: ")
destination_file = input("Please input the name of the destination file: ")

file_open = open(source_file, 'r')
read_file = file_open.read()
file_open.close()

file_write = open(destination_file, 'w')
write_to_file = file_write.write(read_file)
file_write.close()