fr = input("введите имя файла для чтения")
fw = input("введите имя файла для записи")
try:
    file_fr = open(fr)
    s = file_fr.readlines()
    file_fr.close()
except FileNotFoundError:
    print("файл не найден")

try:
    file_fw = open(fw, "w")
    count = 0
    l = len(s)
    while count < l:
        count += 1
        file_fw.writelines(f"{count}: {s[(count - 1)]}")
    file_fw.close()
except FileNotFoundError:
    print("файл не найден")
