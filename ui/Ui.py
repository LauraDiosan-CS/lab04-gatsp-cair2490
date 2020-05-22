from repository.Repo import Repo
from service.GA import calculateFitness
from service.Service import Service
from ui.RunGA import RunGA
from utils.Utils import modularity


class UI:
    def __init__(self, service):
        self.__service = service

    def run(self):
        self.__service.solve()


# repository = Repo("E:\\AI\\Lab2\\input.txt")
# service = Service(repository)
# UI(service).run()


def runGA():
    file = input("Introduceti numele fisierului:")
    pop = input("Introduceti populatia initiala:")
    gen = input("Introduceti numarul de generatii:")
    repository = Repo("E:\\AI\\Lab2\\"+file+".txt")
    data = repository.get_input()
    network = {"noNodes": len(data.get_mat()), "mat": data.get_mat()}
    RunGA(int(pop), int(gen), modularity, network)

runGA()