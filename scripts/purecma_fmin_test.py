from cma import purecma_modified, ff
res = purecma_modified.fmin(ff.elli, 2 * [0.5], 0.3, verb_disp=100)
print(res[0])
print(res[1].result[1])
res[1].logger.plot()  # needs pylab/matplotlib to be installed