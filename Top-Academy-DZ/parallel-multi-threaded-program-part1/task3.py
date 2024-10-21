from threading import Thread
from time import sleep

input_existing_directory = input("Введите путь к существующей директории\n") # ФАЙЛ 'to.txt'
input_new_directory = input("Введите путь к новой директории\n") # ФАЙЛ 'after.txt'

def read_and_write_file_contents(path_file: str, output_file: str) -> None:
    with open(path_file, 'r', encoding='UTF-8') as read_file:
        data = [item for item in read_file.readlines()]
        for line in data:
            print(f"Читаем строку из файла - '{line.rstrip()}'")
            sleep(1)

    with open(output_file, 'w', encoding='UTF-8') as write_file:
        for item in data:
            write_file.write(item)
            print(f"Записываем в файл {output_file} строку '{item.strip()}'")
            sleep(1)


thread1 = Thread(target=read_and_write_file_contents(input_existing_directory, input_new_directory))

thread1.start()

thread1.join()
