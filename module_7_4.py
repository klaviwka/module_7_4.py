import os
import time


directory = r'C:\pythonlesson\lesson07'


filename = 'module_7_4.py'


filepath = os.path.join(directory, filename)


if os.path.isfile(filepath):
    filetime = os.path.getmtime(filepath)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(filepath)
    parent_dir = os.path.relpath(os.path.dirname(filepath), directory)

    size_str = f"{filesize} байт" if filesize > 0 else "0 байт"


    parent_dir = "." if parent_dir == "." else parent_dir

    print(f'Обнаружен файл: {filename}, Путь: ./{filename}, Размер: {size_str}, Время изменения: {formatted_time}, Родительская директория {parent_dir}')
