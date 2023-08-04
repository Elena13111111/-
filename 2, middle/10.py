File_Name ='hi.txt'

with open(File_Name, "w") as file:
        for i in range (1, 10):
             file.write(f" Number : {i}\n")


# Дописываем файл, не удаляя содержимое
with open(File_Name, "a") as file:
    file.write(f" apple\n")
    file.write(f"book\n")
    file.write(f"dog\n")

with open('new_file.mp3', "x") as file:
        file.write(f"XXXXXXXXXXXXXXXXXXX\n")