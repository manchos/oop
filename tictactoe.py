# -*- coding: utf-8 -*-
#import Numeric
import numpy as np

def aconvert(st):
    rez = []
    if type(st) == str:
        for i in st:
            if i == 'X':
                rez.append(1)
            if i == 'O':
                rez.append(-1)
            if i == '.':
                rez.append(0)

    return rez

def checkio(game_result):
    rezsum = {3:'X', -3:'О', 1:'D'}
    game_arr_result = np.zeros((3, 3))
    for i in range(len(game_result)):
        game_arr_result[i] = aconvert(game_result[i])
    v = [sum(game_arr_result[0,:]), sum(game_arr_result[1,:]), sum(game_arr_result[2,:]), sum(game_arr_result[:,0]), sum(game_arr_result[:,1]), sum(game_arr_result[:,2]), sum(game_arr_result.diagonal()), sum(game_arr_result[::-1].diagonal())]

    return rezsum[v.count(3)*3 + (v.count(-3)>0 and v.count(3)>0) + v.count(-3)*-3]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
