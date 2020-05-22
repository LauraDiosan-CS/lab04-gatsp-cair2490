from domain.Output import Output
from repository.Repo import Repo


class Service:
    def __init__(self, repo):
        self.__repo = repo

    def get_data(self):
        return self.__repo.get_input()

    def solve(self):
        with open("solution.txt", "w") as file:
            pass
        sol1 = self.solve1()
        sol2 = self.solve2()
        self.__print_output(sol1)
        self.__print_output(sol2)

    def solve1(self):
        input = self.__repo.get_input()
        return self.__greedy(input.get_mat(), 0)

    def solve2(self):
        input = self.__repo.get_input()
        return self.__greedy(input.get_mat(), input.get_src() - 1, input.get_dest() - 1)

    def __greedy(self, mat, src, dest = None):
        INF = 2000000000
        node = src
        viz = [node]
        cost = 0
        n = len(mat)
        while dest not in viz and len(viz) < n:
            nodes = [el for el in mat[node]]
            new_node = nodes.index(min(nodes))
            while new_node in viz:
                nodes[new_node] = INF
                new_node = nodes.index(min(nodes))
            cost += min(nodes)
            node = nodes.index(min(nodes))
            viz.append(nodes.index(min(nodes)))
        if dest is None:
            cost += mat[viz[-1]][src]

        return Output(viz, cost)

    def __print_output(self, output):
        with open("solution.txt", "a") as file:
            path = output.get_path()
            value = output.get_value()
            ret = ""
            for el in path:
                ret += str(el + 1) + ","
            ret[:len(ret) - 1] + "\n"
            file.write(str(len(path)))
            file.write("\n")
            file.write(ret)
            file.write("\n")
            file.write(str(value))
            file.write("\n")

