import random


def randomize_in_place(a: list):
    for i in range(len(a)):
        rand = random.randrange(i, len(a))
        a[i], a[rand] = a[rand], a[i]
    return a


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    a = randomize_in_place(a)
    print(a)
