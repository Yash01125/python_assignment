#81) Write a Python program to write a list to a file.

def write_list(file_path, data_list):
    with open(file_path, "w") as file:
        for item in data_list:
            file.write(f"{item}\n")

file_path = "output.txt"
data_list = ["apple", "banana", "cherry", "date"]
write_list(file_path, data_list)

print("List has been written to the file.")
