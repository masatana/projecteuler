# -*- coding: utf-8 -*-

def f(n):
    kosu = 10
    keta = 1
    while True:
        if n == 10:
            return 1
        if (kosu * keta) > n:
            print n, (n - ((kosu / 10) * (keta - 1))) / (keta), (n - ((kosu / 10) * (keta - 1))) % (keta)
            l = map(int, list(str((n - ((kosu / 10) * (keta - 1))) / (keta))))
            print l
            a = l[(n - ((kosu / 10) * (keta - 1))) % (keta)]
            print a
            return a
        else:
            kosu *= 10
            keta += 1

def g(n):
    ans = ''
    for i in range(0, 1000001):
        ans += str(i)
    return int(ans[n])

def main():
    l = [1, 10, 100, 1000, 10000, 100000, 1000000]
    ans = 1
    for i in l:
        ans *= g(i)
    print ans

if __name__ == '__main__':
    main()
