import math

from file_reader import read_data_from_folder


def calculate_bayes():
    result = read_data_from_folder("dataBayes")

    if result:
        data1, data2 = result

        print(data2[0])

        if len(data1) != len(data2):
            print("Error: Length.")
            print(len(data1))
            print(len(data2))
            return None

        total_count = len(data1)

        max_reliability = 0.0  # Максимальное значение достоверности
        selected_indexes = []  # Индексы скважин с максимальной достоверностью

        for i in range(total_count):
            P_j_H1_Bk = float(data1[i])
            P_i_Bk1_H1 = float(data2[i])
            q_i_H1_Bk = 1.0 - P_j_H1_Bk
            q_i_Bk1_H1 = 1.0 - P_i_Bk1_H1

            reliability = (P_j_H1_Bk * P_i_Bk1_H1) / (P_j_H1_Bk * P_i_Bk1_H1 + q_i_H1_Bk * q_i_Bk1_H1)
            print("Dostovernost {}: {}".format(i + 1, reliability))

            if reliability > max_reliability:
                max_reliability = reliability
                selected_indexes = [i + 1]
            elif math.isclose(reliability, max_reliability, rel_tol=1e-9):
                selected_indexes.append(i)

        return max_reliability

