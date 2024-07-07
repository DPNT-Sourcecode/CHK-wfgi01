

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items = {
        'A': 50,
        '3A': 130,
        '5A': 200,
        'B': 30,
        '2B': 45,
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
                basket['B'] -= (basket['E'] // 2)

    if 'F' in basket:
        if basket['F'] >= 2:
            basket['F'] -= (basket['F'] // 2)


    for k, v in basket.items():
        if k == 'A':
            if v >= 3:
                result += (v // 5) * items['5A']
                rem = v % 5
                result += (rem // 3) * items['3A']
                rem1 = rem % 3
                result += rem1 * items['A']
            else:
                result += v * items['A']
        elif k == 'B':
            if v >= 2:
                result += ((v // 2) * items['2B']) + ((v % 2) * items['B'])
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





