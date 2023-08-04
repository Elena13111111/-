import shutil
# создаем файл
def create_file(file_name):
    with open(file_name, "w") as file:
        for i in range(1, 1000):
            file.write(f" Number : {i}\n")

create_file('../venv/text_files/text_text2.txt')

#копировать файл
#import shutil
#for i in range(1, 1000):
#   shutil.copyfile('text_files/text_text2.txt',f'text_files/text_text2_{i}.txt' )

# сжимаем файл - 14,1 МБ  МБ весит папка
shutil.make_archive('compressed_file', 'zip', '../venv/text_files')  # 2,15 МБ