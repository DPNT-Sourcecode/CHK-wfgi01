

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
        'F': 10,
        'G': 20,
        'H': 10,
        '5H': 45,
        '10H': 80,
        'I': 35,
        'J': 60,
        'K': 80,
        '2K': 150,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        '5P': 200,
        'Q': 30,
        '3Q': 80,
        'R': 50,
        'S': 30,
        'T': 20,
        'U': 40,
        'V': 50,
        '2V': 90,
        '3V': 130,
        'W': 20,
        'X': 90,
        'Y': 10,
        'Z': 50
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
        if basket['F'] >= 3:
            basket['F'] -= (basket['F'] // 3)


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
        elif k in ('B', 'K'):
            if v >= 2:
                result += ((v // 2) * items['2B']) + ((v % 2) * items['B'])
            else:
                result += v * items[k]
        elif k == 'H':
            if v >= 5:
                result += (v // 10) * items['10H']
                rem = v % 10
                result += (rem // 5) * items['5H']
                rem1 = v % 5
                result += rem1 * items['H']
            else:
                result += v * items['H']
        else:
            result += v * items[k]

    return result


