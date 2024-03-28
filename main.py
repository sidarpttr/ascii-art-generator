import search
import os

devam = True

serit = ["--" for _ in range(30)]

def get_prompt(text = ""):
    try:
        result = int(input(text))
        return result
    except ValueError:
        print("sadece sayi!!")
    except KeyboardInterrupt:
        os.remove("./image.jpg")
        quit()

while devam:
    print(*serit)
    print("MENU")
    print("1. ciz\t|\t2. yaz\t|\t3. ikisi de\t|\t0. çıkış")

    menu_secenek = get_prompt()


    while menu_secenek == 1:
        prompt = input("ne çizeyim: ")
        icon = search.Icon(prompt)

        while 1:
            print(*serit)
            print("1. degistir\t|\t2. ters düz et\t|\t3. yeni cizim\t|\t4. boyutlandır\t|\t5. menu\t|\t0. çıkış")
            icon_secenek = get_prompt()
            print(*serit)
            if icon_secenek == 1:
                icon.resim_degis()
            elif icon_secenek == 2:
                icon.reverse_color()
            elif icon_secenek == 3:
                break
            elif icon_secenek == 4:
                print(f"mevcut boyut: {icon.size[0]}")
                icon.set_size = get_prompt("boyut: ")
            elif icon_secenek == 5:
                menu_secenek = None
                break 
            elif icon_secenek == 0:
                menu_secenek = None
                devam = 0
                break
        
    while menu_secenek == 2:
        prompt = input("ne yazayım: ")
        text = search.Text(prompt)

        while 1:
            print(*serit)
            print("1. yeni text\t2. ters duz et\t3. menu\t0.çıkış ")
            text_secenek = get_prompt()
            print(*serit)
            if text_secenek == 1:
                break
            elif text_secenek == 2:
                text.reverse_color()
                break
            elif text_secenek == 3:
                menu_secenek = None
                break
            elif text_secenek == 0:
                menu_secenek = None
                devam = False
                break

    if menu_secenek == 3:
        icon_prompt = input("çizilecek:  ")
        text_prompt = input("yazılacak: ")
        search.Icon(icon_prompt)
        search.Text(text_prompt)
    if menu_secenek == 0:
        break
    
    os.remove("./image.jpg")

    