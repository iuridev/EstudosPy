import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent
print(ROOT_PATH)

try:
    os.mkdir(ROOT_PATH / "new_directory")
except FileExistsError as err:
    print(f"Ops! diretorio ja existente!")
    print(err)

try:
    new_file = open(ROOT_PATH / 'new_File.txt', 'w')
    new_file.close()
except FileExistsError:
    print(f"Ops! file ja existente!")

try:
    os.rename(ROOT_PATH / 'new_File.txt', ROOT_PATH / 'File_renamed.txt')
except FileExistsError as err:
    print("Já exite um arqivo com esse nome")
    print(err)

try:
    new_file = open(ROOT_PATH / 'File.txt', 'w')
    new_file.close()
except FileExistsError:
    print(f"Ops! file ja existente!")

try:
    os.remove(ROOT_PATH / 'File.txt')
except ValueError:
    print(ValueError)

try:
    shutil.move(ROOT_PATH / "File_renamed.txt", ROOT_PATH / "new_directory" / "File_renamed.txt")
except FileNotFoundError:
    print("Não Existe arquivo com esse nome.")

