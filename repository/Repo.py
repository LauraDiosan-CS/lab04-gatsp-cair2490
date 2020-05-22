from copy import deepcopy

import numpy as np

from domain.Input import Input


class Repo:
    def __init__(self, fileName):
        self.__fileName = fileName
        self.__input = None
        self.__load_from_file()

    def get_input(self):
        return self.__input

    def __euclid_distance(self, xa, ya, xb, yb):
        return np.sqrt((xa-xb) * (xa-xb) + (ya - yb) * (ya - yb))

    def __load_from_file(self):
        with open(self.__fileName, "r") as f:
            admat = []
            mat = []
            for i in range(3):
                f.readline()
            n = int(f.readline().split(":")[1].rstrip())
            for i in range(2):
                f.readline()
            for i in range(n):
                coord = f.readline().split(" ")
                mat.append([int(coord[0]), int(coord[1]), int(coord[2])])

            for i in range(n):
                adj = []
                for j in range(n):
                    adj.append(self.__euclid_distance(mat[i][1], mat[i][2], mat[j][1], mat[j][2]))
                admat.append(deepcopy(adj))
            # for i in range(n):
            #     print(admat[i])
            self.__input = Input(admat, None, None)
