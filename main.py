


def show_menu():
    print('1. Citire lista')
    print('2. Afisare numere negative')
    print('x. Exit')




def read_list():
    """
    converteste o lista din str la int
    :return: lista int
    """
    num = []
    num_as_str = input('Dati o lista de numere intregi separate prin spatiu: ')
    num_as_list_of_str = num_as_str.split(' ')
    for num_str in num_as_list_of_str:
        num.append(int(num_str))
    print(num)
    return num



def get_negatives(lst) -> list:
    """
    parcurge lista dorita si extrage numerele negative
    :param lst: lista de numere intregi
    :return: lista rezultata
    """
    result = []
    for nr in lst:
        if nr < 0:
            result.append(nr)

    return result

def test_get_negative():
    assert get_negatives([10,20,-10,-4,1,0,-6]) == [-10,-4,-6]
    assert get_negatives([10,20,30,450]) == []
    assert get_negatives([]) == []


def main():
    lst = []
    res = []
    while True:
        show_menu()
        option = input("Alegeti optiunea: ")
        if option == '1':
            lst = read_list()
        elif option == '2':
            res = get_negatives(lst)
            print("Numerele negative din lista sunt: ", res)
        elif option == 'x':
            break
        else:
            print("Optiune invalida! Reincercati!")




if __name__ == '__main__':
    test_get_negative()
    main()