


def show_menu():
    print('1. Citire lista')
    print('2. Afisare numere negative')
    print('3. Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.')
    print('4. Afișarea tuturor numerelor din listă care sunt superprime.')
    print('5. Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au '
             'fost înlocuite cu CMMDC-ul lor și numerele negative au cifrele în ordine inversă.')
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


def get_lowest(digit, lst):
    """
    Cautarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.
    :param digit: cifra dorita
    :param lst: Lista citita
    :return: Numarul obtinut

    """
    result = []
    for n in lst:
        if n % 10 == digit:
            result.append(n)

    mini = result[0]
    for num in result:
        if num < mini:
            mini = num
    return mini


def test_get_lowest():
    assert get_lowest(3, [10, 20, 33]) == 33
    assert get_lowest(5, [5, 55, 555]) == 5
    assert get_lowest(7, [50, 623, 62, 7, 53267]) == 7


def is_prime(n):
    """

    :param n: int
    :return:  true daca n este prim si false daca nu.
    """

    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def test_isprime():
    assert is_prime(10) is False
    assert is_prime(13) is True
    assert is_prime(11) is True
    assert is_prime(17) is True
    assert is_prime(18) is False


def is_superprime(n):
    """

    :param n: Este de tipul int
    :return: Returneaza True daca numarul este superprim, False in caz contrar

    Functia inverseaza numarul, si dupa construieste unul nou din invers, cifra cu cifra
    In timpul constructiei acesta verifica daca numarul curent este prim
    Primalitatea este verificata cu ajutorul functiei is_prime(n)

    """
    nr = n
    invers = 0

    # prima inversiune
    while nr > 0:
        digit = nr % 10
        invers = invers * 10 + digit
        nr = nr // 10

    # reinitializarea variabilelor
    nr = invers
    invers = 0
    gresit = 1

    # a doua inversiune + verificare primalitate la fiecare pas
    while nr > 0 and gresit == 1:
        digit = nr % 10
        invers = invers * 10 + digit
        if is_prime(invers) == False:
            gresit = 0
        nr = nr // 10

    if gresit == 1:
        return True
    else:
        return False


def test_is_superprime():
    assert is_superprime(233) is True
    assert is_superprime(237) is False

def get_all_superprime(lst: list[int]) -> list[int]:
    """
    Verifica numerele superprime din lista
    :param lst: lista in care se cauta subsecventa
    :return: subsecventa gasita
    """

    result = []
    for n in lst:
        if is_superprime(n) is True and n > 0:
            result.append(n)

    return result

def get_cmmdc(lst):
    """
    gaseste cel mai mic div comun dintre nr pozitive
    :param lst: lista
    :return: cmmdc
    """
    maxi = -1
    for n in lst:
        if n > maxi:
            maxi = n
    while maxi != 0:
        gasit = 1
        for i in lst:
            if i > -1 and i % maxi != 0:
                gasit = 0
        if gasit == 1:
            return maxi
        maxi -= 1

def invers(nr):
    """
    determina inversul nr
    :param nr: numarul dorit
    :return: inversul
    """

    n = nr
    n *= -1
    num = 0
    while n != 0:
        num = num * 10 + (n % 10)
        n = n // 10

    return -1*num

def modifica(rez, cmmdc):
    """

    :param rez:
    :param cmmdc:
    :return:
    """
    n = len(rez)
    print(cmmdc)
    for i in range (0,n):
        if rez[i] >= 0:
            rez[i] = cmmdc
        else:
            rez[i] = invers(rez[i])

    return rez

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
        elif option == '3':
            cifra = int(input("Introduceti cifra dorita: "))
            numar = get_lowest(cifra, lst)
            print("Cel mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură este: ", numar)
        elif option == '4':
            res = get_all_superprime(lst)
            print("Numerele superprime din lista sunt: ", res)
        elif option == '5':
            cmmdc = get_cmmdc(lst)
            res = modifica(lst, cmmdc)
            print("Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu "
                  "CMMDC-ul lor și numerele negative au cifrele în ordine inversă este: ", res)

        elif option == 'x':
            break
        else:
            print("Optiune invalida! Reincercati!")




if __name__ == '__main__':
    test_get_negative()
    test_get_lowest()
    test_is_superprime()
    test_isprime()
    main()