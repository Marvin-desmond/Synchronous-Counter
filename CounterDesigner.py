import math


def toBinary(a):
    b = format(a, "b")
    return b


def toInt(a):
    b = int(a, 2)
    return b


def UpCounter(what):
    up = []
    for i in range(len(what)):
        temp = 1 + toInt(what[i])
        # print(temp, end=" ")
        temp = format(temp, "b")
        up.append(temp)
    return up


def DownCounter(what):
    down = []
    for i in range(len(what)):
        down.append(what[i])
    down.reverse()
    temp = down[1:]
    print("The counter is a down counter")
    temp.reverse()
    for i in range(1, len(down)):
        down[i] = temp[i-1]
    return down


def FlipFlops(a, b, ab):
    if ab == "JK" or ab == "SR":
        if a == 0 and b == 0:
            j = 0
            k = 'X'
            return j, k
        elif a == 0 and b == 1:
            if ab == "SR":
                j = 1
                k = 0
            else:
                j = 1
                k = 'X'
            return j, k
        elif a == 1 and b == 0:
            if ab == "SR":
                j = 0
                k = 1
            else:
                j = 'X'
                k = 1
            return j, k
        elif a == 1 and b == 1:
            j = 'X'
            k = 0
            return j, k


def remaining(suppose, states, first, second):
    rem = suppose-states
    value = states
    for i in range(rem):
        app = toBinary(value)
        first.append(app)
        if suppose ==4:
            k='2'
        elif suppose ==8:
            k = '3'
        elif suppose == 16:
            k='4'
        k = '0'+k+'b'
        second.append(format(0, k))
        value = value + 1
    return first, second


def ex(a):
    b = []
    for i in range(0, a):
        c = toBinary(i)
        b.append(c)
        d = list(c)
        i = 0
        while i < len(d):
            # print(d[i])
            i = i + 1
    return b


if __name__ == '__main__':
    print('a module')
