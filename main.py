import CounterDesigner
global states
print("Enter the counter e.g\n|*** modulo 8 synchronous up counter OR \n3 bit synchronous up counter*******|")

d = input()

if "modulo" in d:
    d = d.split()
    states = int(d[1])
    print("The counter has {0} states. ".format(states))
# print(d)
elif "bit" in d:
    d = d.split()
    states = 2**int(d[0])
    print("The counter is a {0} bit having {1} states".format(d[0], states))

global suppose

if states <= 4:
    suppose = 4
elif states <= 8:
    suppose = 8
elif states <= 16:
    suppose = 16

global ab


if "SR" in d or "sr" in d:
    print("SR in counter")
    ab = "SR"
elif "JK" in d or "jk" in d:
    ab = "JK"

if "up" in d:
    e = CounterDesigner.ex(states)
    up = CounterDesigner.UpCounter(e)
    up[-1] = 0
    print("The counter is an up counter")
    if states != 4 or states != 8 or states != 16:
        e, up = CounterDesigner.remaining(suppose, states, e, up)
    print("Present States : ")
    print(e)
    print("Next States : ")
    print(up)

elif "down" in d:
    e = CounterDesigner.ex(states)
    down = CounterDesigner.DownCounter(e)
    if states != 4 or states != 8 or states != 16:
        e, down = CounterDesigner.remaining(suppose, states, e, down)
    print("Present States : ")
    print(e)
    print("Next States : ")
    print(down)
    for i in range(len(e)):
        m = len(e[i])
        n = len(down[i])
        if m > n:
            res = m-n
            print("dominant PS : ", e[i])
        elif m < n:
            res = n-m
            print("dominant NS : ", down[i])
        else:
            print("Equality")
        print("{0}    {1}\n".format(m, n))


elif "up/down" in d:
    print("The counter is an up/down counter")
else:
    print("By default, it counts up")


# print(e[4][0])
# print(CounterDesigner.toInt(e[-2]))

