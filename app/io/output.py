import pandas as pd

def output_text_to_console(text):
    """
    Функція для виводу тексту у консоль.
    """
    print(text)

def write_to_file_with_builtin(filename, content):
    """
    Функція для запису до файлу за допомогою вбудованих можливостей Python.
    """
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Дані успішно записано у файл '{filename}'.")
    except Exception as e:
        print(f"Виникла помилка при записі до файлу '{filename}': {e}")

def write_to_file_with_pandas(filename, content):
    """
    Функція для запису до файлу за допомогою бібліотеки pandas.
    """
    try:
        dataframe = pd.DataFrame(content)
        dataframe.to_csv(filename, index=False)
        print(f"Дані успішно записано у файл '{filename}' за допомогою бібліотеки pandas.")
    except Exception as e:
        print(f"Виникла помилка при записі до файлу '{filename}' за допомогою бібліотеки pandas: {e}")
