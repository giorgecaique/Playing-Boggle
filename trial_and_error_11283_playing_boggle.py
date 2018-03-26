# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 15:28:17 2018

@author: giorge.luiz
"""

import pandas as pd

# coordenadas dos movimentos
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

score_table = [0,0,1,1,2,3,5,11,11,11,11,11,11,11,11,11]

letter_table = []
dictionary = []

inpt = """2

TNXO
AAEI
IOSR
BFRH
8
TAXES
RISE
ANNEX
BOAT
OATS
FROSH
HAT
TRASH

FNEI
OBCN
EERI
VSIR
1
BEER""".split('\n')

# sinaliza que a casa já foi preenchida
marks = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]] 

choosen_word = ''
choosen_word_list = []

def trial_and_error(word, step, x, y):
    success = word in dictionary and word not in choosen_word_list
    if success:
        choosen_word_list.append(word)
    k = 0
    while(not success and k < 8):
        u = x + dx[k]
        v = y + dy[k]
        if is_acceptable(u, v):
            marks[u][v] = step
            word = word + letter_table[u][v]
            global choosen_word
            choosen_word = word
            success = trial_and_error(word, step + 1, u, v)
            
            if (not success):
                word = word[:-1]
                marks[u][v] = 0 # no success
        k+=1
    return success
            
def is_acceptable(x, y):
    result = x >= 0 and x < len(letter_table[0])
    result = result and (y >= 0 and y < len(letter_table))
    result = result and (marks[x][y] == 0)
    return result

def run(n_game, x, y):
    marks[x][y] = 1;
    success = trial_and_error(letter_table[x][y], 2, x, y)
    if success:
        return score_table[len(choosen_word) - 1]
    else:
        return 0

    

def main():
    n_games = int(inpt[0])
    j = 2
    global letter_table, dictionary, marks
    for i in range(0,n_games):
        score_sum = 0
        for v in range(j, j+4):
            letter_table.append(inpt[v])
        j +=4
        n_dicts = int(inpt[j])
        j +=1
        for v in range(j, j+n_dicts):
            dictionary.append(inpt[v])
        j += n_dicts+1
        
        for word in dictionary:
            if word not in choosen_word_list:
                for line in range(0,len(letter_table)):
                    for column in range(0, len(letter_table[0])):
                        if word[0] == letter_table[line][column]:
                            score_sum += run(i, line, column)
                            marks = [[0, 0, 0, 0],
                                     [0, 0, 0, 0],
                                     [0, 0, 0, 0],
                                     [0, 0, 0, 0]] 
        print("Score for Boggle game #"+ str(i), score_sum)
        
        letter_table = []
        dictionary = []
        marks = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]] 
main()
