import pandas as pd

def input_text_from_console():
    """
    Функція для вводу тексту з консолі.

    :return: Введений користувачем текст з консолі.
    :rtype: str
    """
    text = input("Введіть текст з консолі: ")
    return text

def read_file_with_builtin(filename):
    """
    Зчитує дані з файлу, використовуючи вбудовані можливості Python.

    :param filename: Ім'я файлу, з якого потрібно зчитати дані.
    :type filename: str
    :return: Зчитані дані з файлу.
    :rtype: str
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
    Зчитує дані з файлу, використовуючи бібліотеку pandas.

    :param filename: Ім'я файлу, з якого потрібно зчитати дані.
    :type filename: str
    :return: Зчитані дані з файлу.
    :rtype: pandas.DataFrame
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

if __name__ == "__main__":
    pass