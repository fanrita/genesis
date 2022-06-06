import sys


def is_float(side):
    try:
        return float(side)
    except ValueError:
        sys.exit('Triangle side should be float')


def is_triangle_exist(a, b, c):
    return a + b > c and a + c > b and b + c > a;


def get_triangle_type(a, b, c):
    if a == b == c:
        return 'equilateral'
    elif a == b or b == c or a == c:
        return 'isosceles'
    else:
        a, b, c = sorted([a, b, c])
        if a * a + b * b == c * c:
            return 'right-angled'
        else:
            return 'scalene'


if __name__ == '__main__':
    a, b, c = [is_float(input(f"Type triangle side {side}: ")) for side in ['a', 'b', 'c']]

    if is_triangle_exist(a, b, c):
        print(f"SUMMARY: This is {get_triangle_type(a, b, c)} triangle")
    else:
        print("SUMMARY: Triangle does not exist")
