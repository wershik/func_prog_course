
def is_sorted(list_test) -> bool:
    tmp_list = list_test
    if tmp_list.sort() == list_test:
        return True
    elif tmp_list.sort(reversed = True) == list_test:
        return True
    else:
        return False

listt = []
while True:
    inp = int(input("Ввод:"))
    if inp == 0:
        break
    listt.append(inp)

boo = is_sorted(listt)