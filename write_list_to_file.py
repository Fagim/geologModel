import datetime


def write_list_to_file(data_list, file_path=''):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")  # Генерируем уникальный временной штамп
    filename = f"fa_list_lamda_{timestamp}.txt"  # Формируем имя файла с учетом временного штампа

    if file_path:
        filename = f"{file_path}/{filename}"

    with open(filename, 'w') as file:
        for item in data_list:
            file.write(str(item) + '\n')
    print("Write successful ", filename)
