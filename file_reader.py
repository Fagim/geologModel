import os

def read_data_from_folder(folder_path):
    files = os.listdir(folder_path)

    if len(files) >= 2:
        file1_path = os.path.join(folder_path, files[0])
        file2_path = os.path.join(folder_path, files[1])

        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            content1 = file1.read().splitlines()
            content2 = file2.read().splitlines()

        return content1, content2
    else:
        return None
