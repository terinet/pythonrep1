import pandas as pd

def output_text_to_console(text):
    """
    Виводить текст у консоль.

    :param text: Текст для виводу у консоль.
    :type text: str
    """
    print(text)

def write_to_file_with_builtin(filename, content):
    """
    Записує текст у файл, використовуючи вбудовані можливості Python.

    :param filename: Ім'я файлу, у який потрібно записати текст.
    :type filename: str
    :param text: Текст, який потрібно записати у файл.
    :type text: str
    """
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Дані успішно записано у файл '{filename}'.")
    except Exception as e:
        print(f"Виникла помилка при записі до файлу '{filename}': {e}")

def write_to_file_with_pandas(filename, content):
    """
    Записує дані у файл, використовуючи бібліотеку pandas.

    :param filename: Ім'я файлу, у який потрібно записати дані.
    :type filename: str
    :param data: Дані, які потрібно записати у файл (DataFrame).
    :type data: pandas.DataFrame
    """
    try:
        dataframe = pd.DataFrame(content)
        dataframe.to_csv(filename, index=False)
        print(f"Дані успішно записано у файл '{filename}' за допомогою бібліотеки pandas.")
    except Exception as e:
        print(f"Виникла помилка при записі до файлу '{filename}' за допомогою бібліотеки pandas: {e}")
