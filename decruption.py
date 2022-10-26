import pyAesCrypt
import os


# функция дешифрования файла
def decryption(file, password):
    # задаём размер буфера
    buffer_size = 512 * 1024

    # вызываем метод расшифровки
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # чтобы видеть результат выводим на печать имя зашифрованного файла
    print(f'Файл {str(os.path.splitext(file[0]))} дешифрован')

    # удаляем исходный файл
    os.remove(file)


# функция сканирования директорий
def walking_by_dirs(dir, password):

    # перебираем все поддиректории в указанной директории

    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл, то дешифруем его
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директорию, то повторим цикл в поисках файлов
        else:
            walking_by_dirs(path, password)


password = input('Введите пароль для расшифровки: ')
walking_by_dirs("/home/aleksandr/Рабочий стол/123", password)
