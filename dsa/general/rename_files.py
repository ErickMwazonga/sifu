import os


def renumber_files(path):
    os.chdir(path)
    renamed_files_count = 0

    for filename in os.listdir(path):
        if str(filename).startswith('y2mate.com'):
            _, name = filename.split(' - ')

            try:
                os.rename(filename, name)
                renamed_files_count += 1
                print(f'File renamed from {filename} to {name}')
            except:
                print(f'Unexpected error while renaming {filename}')

    print(f'Renamed {renamed_files_count}')
    os.scandir(path).close()


DIR = r'C:\Users\emwazonga\Downloads'
renumber_files(DIR)
