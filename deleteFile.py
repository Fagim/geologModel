import os
from tkinter.messagebox import showinfo


def clear_data_bayes_folder():
    folder_path = "dataBayes"  # Путь к папке dataBayes

    # Получаем список файлов в папке
    file_list = os.listdir(folder_path)

    # Перебираем файлы и удаляем каждый
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
    showinfo("Очистка папки", "Папка dataBayes очищена.")

