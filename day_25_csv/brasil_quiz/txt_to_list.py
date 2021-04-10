def txt_to_list(file_name: str) -> list:
    with open(file_name, mode="r", encoding="utf-8") as file:
        lines = file.readlines()

    listA = []
    for line in lines:
        line = line.strip()
        listA.append(line.split(sep=" "))

    return listA

def get_mouse_click_coord(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coord)

turtle.mainloop()
