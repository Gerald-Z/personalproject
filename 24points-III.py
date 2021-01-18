def main():
    print("Enter the four integers!")
    int1 = int(input("What is the first integer?"))
    int2 = int(input("What is the second integer?"))
    int3 = int(input("What is the third integer?"))
    int4 = int(input("What is the fourth integer?"))

    testall(int1, int2, int3, int4)

    if counter == 0:
        print("It is impossible for the four numbers to be computed to 24.")
    else:
        print("There are " + str(counter) + " ways to turn the four numbers into 24!")
    

counter = 0

def testall(a, b, c, d):
    printf(evaluate([[a, str(a)]], [[b, str(b)], [c, str(c)], [d, str(d)]]))
    printf(evaluate([[a, str(a)]], [[b, str(b)], [d, str(d)], [c, str(c)]]))
    printf(evaluate([[a, str(a)]], [[c, str(c)], [b, str(b)], [d, str(d)]]))
    printf(evaluate([[a, str(a)]], [[c, str(c)], [d, str(d)], [b, str(b)]]))
    printf(evaluate([[a, str(a)]], [[d, str(d)], [b, str(b)], [c, str(c)]]))
    printf(evaluate([[a, str(a)]], [[d, str(d)], [c, str(c)], [b, str(b)]]))

    printf(evaluate([[b, str(b)]], [[a, str(a)], [c, str(c)], [d, str(d)]]))
    printf(evaluate([[b, str(b)]], [[a, str(a)], [d, str(d)], [c, str(c)]]))
    printf(evaluate([[b, str(b)]], [[c, str(c)], [a, str(a)], [d, str(d)]]))
    printf(evaluate([[b, str(b)]], [[c, str(c)], [d, str(d)], [a, str(a)]]))
    printf(evaluate([[b, str(b)]], [[d, str(d)], [a, str(a)], [c, str(c)]]))
    printf(evaluate([[b, str(b)]], [[d, str(d)], [c, str(c)], [a, str(a)]]))

    printf(evaluate([[c, str(c)]], [[b, str(b)], [a, str(a)], [d, str(d)]]))
    printf(evaluate([[c, str(c)]], [[b, str(b)], [d, str(d)], [a, str(a)]]))
    printf(evaluate([[c, str(c)]], [[a, str(a)], [b, str(b)], [d, str(d)]]))
    printf(evaluate([[c, str(c)]], [[a, str(a)], [d, str(d)], [b, str(b)]]))
    printf(evaluate([[c, str(c)]], [[d, str(d)], [b, str(b)], [a, str(a)]]))
    printf(evaluate([[c, str(c)]], [[d, str(d)], [a, str(a)], [b, str(b)]]))

    printf(evaluate([[d, str(d)]], [[b, str(b)], [c, str(c)], [a, str(a)]]))
    printf(evaluate([[d, str(d)]], [[b, str(b)], [a, str(a)], [c, str(c)]]))
    printf(evaluate([[d, str(d)]], [[c, str(c)], [b, str(b)], [a, str(a)]]))
    printf(evaluate([[d, str(d)]], [[c, str(c)], [a, str(a)], [b, str(b)]]))
    printf(evaluate([[d, str(d)]], [[a, str(a)], [b, str(b)], [c, str(c)]]))
    printf(evaluate([[d, str(d)]], [[a, str(a)], [c, str(c)], [b, str(b)]]))


def printf(string):
    if (len(string) == 0):
        print("", end= '')
    else:
        print(string)


def evaluate(lst1, lst2):
    if (len(lst2) == 0):
        return (present(lst1))
    else:
        return evaluate((addtolst(lst1, lst2[0])), lst2[1:])


def present(lst):
    for i in lst:
        if i[0] == 24: 
            global counter
            counter += 1
            return i[1] + " = 24   " + str(counter)
    return ""

def addtolst(lst, element):
    returned = []
    for i in lst:
        returned.append([i[0]+element[0], i[1] + " + " + element[1]])
        returned.append([i[0]-element[0], i[1] + " - " + element[1]])
        returned.append([i[0]*element[0], i[1] + " * " + element[1]])
        if (element[0] != 0):
            returned.append([i[0]/element[0], i[1] + " / " + element[1]])
    return returned

main()