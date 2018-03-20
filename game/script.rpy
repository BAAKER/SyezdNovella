# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Троцкая', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:

init 1:
    $ social_pol = 0
label start:

    scene lenin

    show trotskey angry

    e "Итак, выбирай."

    e "Геи люди?"
    
    menu:
        "Да":
            $ social_pol += 2
            jump socialpol1
        "Нет":
            $ social_pol += 1
            jump socialpol2
    label socialpol1:
        if social_pol == 2:
            "Социальная политика = 1"
            return
    label socialpol2:
        if social_pol ==2:
            "Социальная политика = -1"
        else:
            "Неверно"
            return
    return
