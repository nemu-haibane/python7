from bank import bank
import os, shutil
while True:
    do = input('что желаете сделать?')
    if do == 'создать папку':
        try:
            os.mkdir(input('введите название папки'))
        except:
            pass
    if do == 'удалить (файл/папку)':
        file_or_dir = input('введите название папки или файла')
        try:
            os.remove(file_or_dir)
        except:
            os.rmdir(file_or_dir)
    if do == 'копировать (файл/папку)':
        src = input('введите название папки/файла')
        dst = input('новое название папки/файла')
        try:
            shutil.copyfile(src, dst)
        except:
            shutil.copytree(src, dst)
    if do == 'просмотр содержимого рабочей директории':
        print(os.listdir())
    if do == 'посмотреть только папки':
        print([item for item in os.listdir() if os.path.isdir(item)])
    if do == 'посмотреть только файлы':
        print([item for item in os.listdir() if os.path.isfile(item)])
    if do == 'сохранить содержимое рабочей директории в файл':
        with open('listdir.txt', 'w') as f:
            f.write('files: ' + ', '.join([item for item in os.listdir() if os.path.isfile(item)]))
            f.write('\ndirs: ' + ', '.join([item for item in os.listdir() if os.path.isdir(item)]))
    if do == 'просмотр информации об операционной системе':
        print(os.uname())
    if do == 'создатель программы':
        print('this program is created by amirov sergey nemu.haibane@gmail.com')
    if do == 'мой банковский счет':
        bank()
    if do == 'смена рабочей директории':
        os.chdir(input('введите полный /home/user/... или относительный user/my/... путь'))
    if do == 'выход':
        break