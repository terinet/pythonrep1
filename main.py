from app.io import input
from app.io import output
from tests import input
from tests import output



def main():
    # Введення тексту з консолі
    input_text = input.input_text_from_console()

    # Зчитування з файлу за допомогою вбудованих можливостей Python
    file_text_builtin = input.read_file_with_builtin("example.txt")

    # Зчитування з файлу за допомогою бібліотеки pandas
    file_text_pandas = input.read_file_with_pandas("example.csv")

    # Виведення тексту у консоль
    output.output_text_to_console(input_text)
    output.output_text_to_console(file_text_builtin)
    output.output_text_to_console(file_text_pandas)

    # Запис до файлу за допомогою вбудованих можливостей Python
    output.write_to_file_with_builtin("output.txt", input_text)
    output.write_to_file_with_builtin("output.txt", file_text_builtin)
    output.write_to_file_with_builtin("output.txt", file_text_pandas)

def main():
    pass

if __name__ == "__main__":
    main()


