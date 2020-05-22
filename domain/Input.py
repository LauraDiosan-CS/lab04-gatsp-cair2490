class Input:
    def __init__(self, mat, src, dest):
        self.__mat = mat
        self.__src = src
        self.__dest = dest

    def get_mat(self):
        return self.__mat

    def get_src(self):
        return self.__src

    def get_dest(self):
        return self.__dest

    def set_mat(self, mat):
        self.__mat = mat

    def set_src(self, src):
        self.__src = src

    def set_dest(self, dest):
        self.__dest = dest



