import cma

es = cma.CMAEvolutionStrategy(12 * [0], 0.5)
while not es.stop():
    solutions = es.ask()
    es.tell(solutions, [cma.ff.rosen(x) for x in solutions])
    es.logger.add()  # write data to disc to be plotted
    es.disp()

es.result_pretty()
cma.plot()  # shortcut for es.logger.plot()