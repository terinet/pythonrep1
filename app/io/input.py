import pandas as pd

def input_text_from_console():
    """
    Функція для вводу тексту з консолі.
    """
    text = input("Введіть текст з консолі: ")
    return text

def read_file_with_builtin(filename):
    """
    Функція для зчитування з файлу за допомогою вбудованих можливостей Python.
    """
    try:
        with open(filename, 'r') as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
        return None
    except Exception as e:
        print(f"Виникла помилка при зчитуванні файлу '{filename}': {e}")
        return None

def read_file_with_pandas(filename):
    """
    Функція для зчитування з файлу за допомогою бібліотеки pandas.
    """
    try:
        dataframe = pd.read_csv(filename)
        file_content = dataframe.to_string(index=False)
        return file_content
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
        return None
    except Exception as e:
        print(f"Виникла помилка при зчитуванні файлу '{filename}': {e}")
        return None
