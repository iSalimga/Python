import math


def fun(z, y, x):
    f1 = (math.log(math.fabs(x)) ** 4
          + 81 * (x ** 3 / 6 + y ** 2 + 56 * z) ** 7) \
         / (82 * x ** 2 - (86 * z ** 2 - z - 89 * y ** 3))
    f2 = ((1 - 49 * y ** 2 - 30 * x) ** 2 +
          75 * (z - 1)) / ((z + 46) ** 6 -
                           12 * (y ** 2 + 42 * x))
    f = f1 + f2
    return f


def fun12(n, b, a, p):
    result = 0
    for k in range(1, a + 1):
        for j in range(1, b + 1):
            for c in range(1, n + 1):
                result += math.sqrt(1 + c ** 2 + 41 * k) + \
                          63 * (math.tan(j)) ** 4 + \
                          56 * (math.asin(p)) ** 5
    return result


def masdfasdf(z, y, x):
    result = 0
    for i in range(1, len(z) + 1):
        result += (math.acos(68 * y[math.ceil((i - 1) / 3)] ** 2 +
                             z[math.ceil((i - 1) / 2)] ** 3) +
                   x[math.ceil((i - 1) / 3)]) ** 5 / 80
    result = result * 96
    return result


def makmnkmn(x):
    dict42 = {'SMALI': 7, 'P4': 8, 'TWIG': 9}
    dict41 = {'OOC': 2, 'GENIE': 3, 'NSIS': 4}
    dict31 = {'ARC': 0, 'GOSU': 1, 'LLVM': dict41[x[0]]}
    dict21 = {'SMALI': dict31[x[2]], 'P4': 5, 'TWIG': 6}
    dict32 = {'OOC': dict42[x[1]], 'GENIE': 10, 'NSIS': 11}
    dict22 = {'ARC': dict32[x[0]], 'GOSU': 12, 'LLVM': 13}
    dict1 = {2011: dict21[x[1]], 1984: dict22[x[2]], 2003: 14}
    return dict1[x[4]]


def maikjhn(x):
    a = x * 0b1111_1111_1111_1
    b = (x >> 13) * 0b1111_1111_1111_11
    c = (x >> 27) * 0b11
    d = (x >> 29) * 0b1
    e = (x >> 30) * 0b11
    a = a >> 3
    b = b >> 5
    c = c << 24
    d = d << 28
    e = e << 14
    return b | e | a | c | d


def asdfasdf(x):
    a1 = []
    s1 = []
    a = x.replace(" ", "").replace('\n', '').split("end;do")
    for i in range(0, len(a)):
        string = a[i]
        pos1 = a[i].find("@\"")
        pos2 = a[i].find("option")
        pos3 = a[i].find("\".")
        pos4 = a[i].find("->")
        s1.append(int(string[pos2 + 6: pos4]))
        a1.append(string[pos1 + 2: pos3])
    dict1 = dict(zip(a1, s1))
    return dict1


class StateMachine:
    state = 'A'

    def scan(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'C':
            self.state = 'D'
            return 2
        elif self.state == 'E':
            self.state = 'F'
            return 5
        elif self.state == 'H':
            return 10
        else:
            raise KeyError

    def draw(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'G'
            return 3
        elif self.state == 'F':
            self.state = 'C'
            return 8
        elif self.state == 'G':
            self.state = 'H'
            return 9
        else:
            raise KeyError

    def chip(self):
        if self.state == 'D':
            self.state = 'E'
            return 4
        elif self.state == 'F':
            return 7
        elif self.state == 'H':
            self.state = 'A'
            return 11
        else:
            raise KeyError

    def load(self):
        if self.state == 'F':
            self.state = 'G'
            return 6
        else:
            raise KeyError


def main():
    return StateMachine()
