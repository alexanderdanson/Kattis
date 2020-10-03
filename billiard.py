import math


def calculate_angle(opposite, adjacent):
    angle = math.degrees(math.atan((opposite/adjacent)))
    return angle


def calculate_diagonal(opposite, adjacent):
    hypotenuse = math.sqrt((opposite*opposite) + (adjacent*adjacent))
    return hypotenuse


while True:
    numbers = [int(i) for i in input().split(" ")]
    a = numbers[0]  # horizontal side (inches)
    b = numbers[1]  # vertical side (inches)
    s = numbers[2]  # seconds until ball returns to point from which it was launched
    m = numbers[3]  # number of bounces off vertical sides
    n = numbers[4]  # number of bounces of horizontal sides

    if (a == 0) & (b == 0) & (s == 0) & (m == 0) & (n == 0):
        break

    x_distance = a * m
    y_distance = b * n

    A = format((calculate_angle(y_distance, x_distance)), '.2f')

    distance_travelled = calculate_diagonal(y_distance, x_distance)
    v = format((distance_travelled/s), '.2f')

    #OUTPUT
    print("{} {}".format(A, v))

