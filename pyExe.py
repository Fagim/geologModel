import math
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import OK, showinfo

import numpy as np
from matplotlib import pyplot as plt

from deleteFile import clear_data_bayes_folder
from write_list_to_file import write_list_to_file
from calculateBayes import calculate_bayes


def select_variant():
    window = Tk()
    window.title("Выбор варианта")
    window.geometry("250x200")
    label1 = Label(window, text="Выберите вариант")
    label1.pack(anchor="w")

    # выбор варианта для загрузки данных
    def select_var1():
        with open('варианты/вариант1.txt') as file:
            ValueOf = file.read()
        window.destroy()
        print(ValueOf)
        show_message(ValueOf)

    def select_var2():
        with open('варианты/вариант2.txt') as file:
            ValueOf = file.read()
        window.destroy()
        print(ValueOf)
        show_message(ValueOf)

    def select_var3():
        with open('варианты/вариант3.txt') as file:
            ValueOf = file.read()
        window.destroy()
        print(ValueOf)
        show_message(ValueOf)

    # инициализация кнопок вариантов

    btn1 = ttk.Button(window, text="Вариант1", command=select_var1)
    btn1.pack(anchor=NW, padx=6, pady=6)

    btn2 = ttk.Button(window, text="Вариант2", command=select_var2)
    btn2.pack(anchor=NW, padx=6, pady=6)

    btn3 = ttk.Button(window, text="Вариант3", command=select_var3)
    btn3.pack(anchor=NW, padx=6, pady=6)


# основное окно

def show_message(Valueof):
    String_F = label_6["text"] = char_editor.get("1.0", "end")  # получаем введенный текст
    if len(String_F) == 1:
        String_F = Valueof
    print(String_F)
    string_a = entry_1.get()
    string_σ = entry_2.get()
    string_L = entry_3.get()
    print(String_F)
    print(string_a)
    print(string_σ)
    print(string_L)
    print(type(String_F))

    a = int(float(string_a))
    σ = int(float(string_σ))
    L = int(float(string_L))

    line = String_F.split('\n')
    print(type(line))
    print(line)

    int_line = []
    for i in range(len(line)):
        try:
            int_line.append(float(line[i]))
        except:
            print(line[i], 'не число')
            showinfo(title="ОКНО", message="Вы ввели не число, пожалуйста вводите только числа", default=OK)
            exit()
        continue

    len_massive = len(int_line)

    int_line2 = []

    # подсчёт вероятности
    for i in range(len(int_line)):
        int_line2.append((int_line[i] * 2 - a) * a)

    avg_list = []

    for i in range(len(int_line2)):
        avg_value = sum(int_line2[i:i + L]) / L
        avg_list.append(avg_value)

    fa_list_exp = []

    for i in avg_list:
        fa_list_exp.append(math.exp(i / (2 * σ ** 2)))

    fa_list_lamda = []

    for i in fa_list_exp:
        fa_list_lamda.append(i / (i + 1))

    # запись в файл результатов вычисления

    write_list_to_file(fa_list_lamda, "dataBayes")

    figure, axis = plt.subplots(2)

    x = np.zeros(len_massive)

    figure.tight_layout(h_pad=3)

    axis[0].set_title('Исходные данные')
    axis[0].set_xlabel('X axis')
    axis[0].set_ylabel('P вероятность')
    axis[0].plot(int_line, label='F graphic')
    axis[1].set_title('модель продуктивного пласта')
    axis[1].set_xlabel('X axis')
    axis[1].set_ylabel('P вероятность')
    axis[1].plot(fa_list_lamda, label='λ/λ+1 graphic')
    axis[1].plot(x + 0.5, label='x = 0.5')

    print("data output")

    print(fa_list_lamda)

    plt.show()


def calculate_bayes_and_insert():
    entry_4.delete(0, END)  # Очистка поля entry_4

    # Проверка наличия двух файлов в папке dataBayes
    file_count = count_files_in_directory("dataBayes")
    if file_count == 2:
        entry_4.insert(0, str(calculate_bayes()))
    else:
        showinfo(title="Ошибка", message="Отсутствуют два файла в папке dataBayes")


def count_files_in_directory(directory):
    import os
    if os.path.exists(directory) and os.path.isdir(directory):
        return len(os.listdir(directory))
    return 0


def draw_with_data_set():
    String_F = label_6["text"] = char_editor.get("1.0", "end")  # получаем введенный текст
    string_a = entry_1.get()
    string_σ = entry_2.get()
    string_L = entry_3.get()
    print(String_F)
    print(string_a)
    print(string_σ)
    print(string_L)
    print(type(String_F))

    a = int(float(string_a))
    σ = int(float(string_σ))
    L = int(float(string_L))

    line = String_F.split('\n')
    print(type(line))
    print(line)

    int_line = []
    for i in range(len(line) - 1):
        try:
            int_line.append(float(line[i]))
        except:
            print(line[i], 'не число')
            showinfo(title="ОКНО", message="Вы ввели не число, пожалуйста вводите только числа", default=OK)
            exit()
        continue

    len_massive = len(int_line)

    int_line2 = []
    for i in range(len(int_line)):
        int_line2.append((int_line[i] * 2 - a) * a)

    avg_list = []

    for i in range(len(int_line2)):
        avg_value = sum(int_line2[i:i + L]) / L
        avg_list.append(avg_value)

    fa_list_exp = []

    for i in avg_list:
        fa_list_exp.append(math.exp(i / (2 * σ ** 2)))

    fa_list_lamda = []

    for i in fa_list_exp:
        fa_list_lamda.append(i / (i + 1))

    figure, axis = plt.subplots(2)

    x = np.zeros(len_massive)

    figure.tight_layout(h_pad=3)

    axis[0].set_title('Исходные данные')
    axis[0].set_xlabel('X axis')
    axis[0].set_ylabel('Y axis')
    axis[0].plot(int_line, label='F graphic')
    axis[1].set_title('λ/λ+1 graphic')
    axis[1].set_xlabel('X axis')
    axis[1].set_ylabel('Y axis')

    axis[1].plot(x + 0.5, label='x = 0.5')
    axis[1].plot(fa_list_lamda, label='λ/λ+1 graphic')

    plt.show()


root = Tk()
root.title("Продуктивный пласт")
sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)
root.geometry("720x600")

label_1 = Label(text="Построение математической модели продуктивного пласта на основе "
                     "Байесовской стратегии", font=("Arial", 12))
label_1.pack()

label_2 = Label(text="Введите данные для F= ")
label_2.pack(anchor="w")

char_editor = Text(height=10, width=30, wrap="char")
char_editor.pack(anchor="w", fill="y")

label_3 = Label(text="Введите данные для параметра a=")  # создаем текстовую метку
label_3.pack(anchor="w")

entry_1 = ttk.Entry()
entry_1.insert(0, "-13")
entry_1.pack(anchor="w", padx=6, pady=6)

label_4 = Label(text="Введите данные для параметра σ=")  # создаем текстовую метку
label_4.pack(anchor="w")

entry_2 = ttk.Entry()
entry_2.insert(0, "5")
entry_2.pack(anchor="w", padx=6, pady=6)

label_5 = Label(text="Введите данные для параметра L=")  # создаем текстовую метку
label_5.pack(anchor="w")

entry_3 = ttk.Entry()
entry_3.insert(0, "5")
entry_3.pack(anchor="w", padx=6, pady=6)

label_6 = Label()  # label, Отвечающий за вывод введенных данных
label_6.place(x=380, y=45)

label_7 = Label(text="Введённые данные F=")  # создаем текстовую метку
label_7.place(x=250, y=45)

btn = ttk.Button(text="Ввод", command=draw_with_data_set)
btn.pack(anchor=NW, padx=6, pady=6)

btn = ttk.Button(text="Выбрать вариант", command=select_variant)
btn.pack(anchor=NW, padx=6, pady=6)

label_8 = Label(text="Перед запуском проверки достоверности убедитесь,"
                     "что в папке 'dataBayes' имеется 2 файла с данными по скважинам")
label_8.pack(anchor="w")

entry_4 = ttk.Entry()
entry_4.insert(0, "0.0")
entry_4.pack(anchor="w", padx=6, pady=6)

btn = ttk.Button(text="Подсчёт достоверности", command=lambda: calculate_bayes_and_insert())
btn.pack(anchor=NW, padx=6, pady=6)

btn = ttk.Button(text="Очистить dataBayes", command=clear_data_bayes_folder)
btn.pack(anchor=NW, padx=6, pady=6)

root.mainloop()
