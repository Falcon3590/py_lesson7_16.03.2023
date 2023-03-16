def changes(fio, all_str, numb):
    temp = all_str.split(": ")
    if fio.lower() in temp[0].lower():
        temp[1] = numb
        return ": ".join(temp) + "\n"
    else:
        return all_str


def delete1(fio, all_str):
    if fio.lower() in all_str.lower():
        return ""
    else:
        return all_str
