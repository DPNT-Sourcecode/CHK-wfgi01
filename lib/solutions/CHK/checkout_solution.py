

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10
    }
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

    if 'E' in basket:
        if basket['E'] >= 2:
            if 'B' in basket:
                print(basket)
                basket['B'] -= (basket['E'] // 2)
                print(basket)

    for k, v in basket.items():
        if k == 'A':
            if v >= 3:
                result += (v // 5) * 200
                rem = v % 5
                result += (rem // 3) * 130
                rem1 = rem % 3
                result += rem1 * items['A']
            else:
                result += v * items['A']
        elif k == 'B':
            if v >= 2:
                result += ((v // 2) * 45) + ((v % 2) * items['B'])
            else:
                result += v * items['B']
        elif k == 'C':
            result += v * items['C']
        elif k == 'D':
            result += v * items['D']
        elif k == 'E':
            result += v * items['E']
        elif k == 'F':
            result += v * items['F']

    return result




