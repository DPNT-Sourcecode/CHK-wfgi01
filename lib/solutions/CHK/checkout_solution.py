

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items = {'A', 'B', 'C', 'D', 'E'}
    basket = {}
    result = 0

    for i in skus:
        if i in items:
            if i not in basket:
                basket[i] = 1
            else:
                basket[i] += 1
        else:
            return -1

    print(basket['E'])

    for k, v in basket.items():
        if k == 'A':
            if v >= 3:
                result += (v // 5) * 200
                rem = v % 5
                result += (rem // 3) * 130
                rem1 = rem % 3
                result += rem1 * 50
            else:
                result += v * 50
        elif k == 'E':
            if v >= 2:
                if 'B' in basket:
                    print(basket)
                    basket['B'] -= (v // 2)
                    print(basket)
            result += v * 40
        elif k == 'B':
            print(basket)
            print(v)
            if v >= 2:
                result += ((v // 2) * 45) + ((v % 2) * 30)
            else:
                result += v * 30
        elif k == 'C':
            result += v * 20
        elif k == 'D':
            result += v * 15


    return result


