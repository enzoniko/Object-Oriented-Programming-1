def leds(num):
    leds = 0
    for x in range(len(num)):
        if num[x] == '1':
            leds += 2
        elif num[x] == '2' or num[x] == '3' or num[x] == '5':
            leds += 5
        elif num[x] == '4':
            leds += 4
        elif num[x] == '7':
            leds += 3
        elif num[x] == '6' or num[x] == '9' or num[x] == '0':
            leds += 6
        elif num[x] == '8':
            leds += 7
    return leds

casos = int(input())
for caso in range(casos):
    num = input()
    print(f'{leds(num)} leds')
