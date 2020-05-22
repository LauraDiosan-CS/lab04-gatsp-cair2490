from domain.Chromosome import Chromosome
from service.GA import GA


def RunGA(popsize, nogen, modularity, network):
    gaParam = {'popSize': popsize, 'noGen': nogen}
    problParam = network

    best = Chromosome(problParam)

    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()

    for g in range(nogen):
        ga.oneGeneration()

        bestChromosome = ga.bestChromosome()

        if bestChromosome.fitness < best.fitness or best.fitness == 0.0:
            best = bestChromosome

        print(
            'Best solution in generation ' + str(g) + ' is: x = ' + str(bestChromosome.repres) + ' modularity = ' + str(
                bestChromosome.fitness))

    print("Best solution overall is: x = " + str(best.repres) + " modularity = " + str(best.fitness))
    # A = np.matrix(network["mat"])
    # G = nx.from_numpy_matrix(A)
    # pos = nx.spring_layout(G)  # compute graph layout
    # plt.figure(figsize=(10, 10))  # image is 8 x 8 inches
    # nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlBu, node_color=communities(best.repres)[1])
    # nx.draw_networkx_edges(G, pos, alpha=0.3)
    # plt.show()