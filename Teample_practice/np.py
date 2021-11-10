import numpy as np

size_of_board = 7
board_array = np.zeros([size_of_board, size_of_board])

max_turn = size_of_board * size_of_board

for i in range(max_turn):

    if i % 2 == 0:
        position = input("흑돌 차례입니다 : ")

        sub_p = position.split(" ")
        pos_H = int(sub_p[0])
        pos_W = int(sub_p[1])

        board_array[pos_H, pos_W] = 1

    else: 
        position = input("백돌 차례입니다 : ")

        sub_p = position.split(" ")
        pos_H = int(sub_p[0])
        pos_W = int(sub_p[1])

        board_array[pos_H, pos_W] = 2

    print(board_array)