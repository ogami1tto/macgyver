#! /usr/bin/env python3
# coding: utf-8

class Laby:
    # X
    # Y
    # 1 => SOL | 2 => MUR
    # Item...
    # etc...
    Coordonnees = [
    []*100,
    []*100,
    []*100
    ]

    def MethodeIncrementTest(self, test):
        test += 1
        return test

    def ChargeLaby(self):
        Coordonnees = [
    [0]*100,
    [0]*100,
    [0]*100,
    ]
        d = sorted(Coordonnees)
        d[0][0] = 1 # x
        d[1][0] = 1 # y
        d[2][0] = 1 # type de sol
        return d

if __name__ == '__main__':

    test = 0
    Coordonnees = [
    []*100,
    []*100,
    []*100
    ]
    test = Laby.MethodeIncrementTest()
    Coordonnees = Laby.ChargeLaby(Coordonnees)

    print(Coordonnees)
