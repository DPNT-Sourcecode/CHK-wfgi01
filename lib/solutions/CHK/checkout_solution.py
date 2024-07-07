

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

    for k, v in basket.items():
        if k == 'A':
            if v >= 3:
                result += min(((v // 3) * 130), ((v // 5) * 200)) + ((v % 3) * 50)
            else:
                result += v * 50
        elif k == 'B':
            if v >= 2:
                result += ((v // 2) * 45) + ((v % 2) * 30)
            else:
                result += v * 30
        elif k == 'C':
            result += v * 20
        elif k == 'D':
            result += v * 15
        elif k == 'E':
            if v >= 2:
                result += ((v // 2) * 30) + (v * 40)
            else:
                result += v * 40


    return result



