

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
        'X': 17,
        'Y': 20,
        'Z': 21
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

    if 'N' in basket:
        if basket['N'] >= 3:
            if 'M' in basket:
                basket['M'] -= (basket['N'] // 3)

    if 'R' in basket:
        if basket['R'] >= 3:
            if 'Q' in basket:
                basket['Q'] -= (basket['R'] // 3)

    if 'U' in basket:
        if basket['U'] >= 4:
            basket['U'] -= (basket['U'] // 4)

    for k, v in basket.items():
        if k == 'A':
            if v >= 3:
                result += (v // 5) * items['5'+k]
                rem = v % 5
                result += (rem // 3) * items['3'+k]
                rem1 = rem % 3
                result += rem1 * items[k]
            else:
                result += v * items[k]
        elif k in ('B', 'K'):
            if v >= 2:
                result += ((v // 2) * items['2'+k]) + ((v % 2) * items[k])
            else:
                result += v * items[k]
        elif k == 'H':
            if v >= 5:
                result += (v // 10) * items['10'+k]
                rem = v % 10
                result += (rem // 5) * items['5'+k]
                rem1 = rem % 5
                result += rem1 * items[k]
            else:
                result += v * items[k]
        elif k == 'P':
            if v >= 5:
                result += ((v // 5) * items['5'+k]) + ((v % 5) * items[k])
            else:
                result += v * items[k]
        elif k == 'Q':
            if v >= 3:
                result += ((v // 3) * items['3'+k]) + ((v % 3) * items[k])
            else:
                result += v * items[k]
        elif k == 'V':
            if v >= 2:
                result += (v // 3) * items['3'+k]
                rem = v % 3
                result += (rem // 2) * items['2'+k]
                rem1 = rem % 2
                result += rem1 * items[k]
            else:
                result += v * items[k]
        else:
            result += v * items[k]

    return result

