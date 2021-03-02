def roots_quadr_eq(a, b, c):
    des = b ** 2 - 4 * a * c
    if des == 0:
        return 1
    elif des < 0:
        return 0
    else:
        return 2


print(roots_quadr_eq(1, 0, 1))