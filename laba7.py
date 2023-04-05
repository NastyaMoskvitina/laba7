from PIL import Image, ImageFilter


print("Задача 1")
name_file = "kot1.jpg"
with Image.open(name_file) as img:
    img.load()            #загружает объект из файла
img.show()
width, height = img.size
format = img.format
mode = img.mode
print('Ширина: ', width)
print('Высота: ', height)
print('Формат: ', format)
print('Цветовая модель: ', mode)

def zadacha2():
    print("Задача 2")
    file2 = "kot2.jpg"
    with Image.open(file2) as img:
        img.load()
    img.show()
    new_kartinka = img.resize((img.height // 3, img.width // 3))
    new_kartinka.show()
    new_kartinka.save("novinka_kota2.jpg")

def zadacha3():
    print("Задача 3")
    kartinki = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
    for i in kartinki:
        with Image.open(i) as pic:
            pic.load()
        new_pic = pic.filter(ImageFilter.FIND_EDGES)
        new_pic.show()
        new_pic.save('new_' + i)

def zadacha4():
    print("Задача 4")
    file4 = Image.open("kot2.jpg")
    znak = Image.open("vvodniy_znak.png")
    width = 280
    height = 200
    umenshenie = znak.resize((width,height), Image.LANCZOS)
    file4.paste(umenshenie, (30,10), umenshenie)
    file4.show()
    file4.save("karninka_s_vvodznak.png")


zadacha4()