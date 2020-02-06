from cma import purecma_reference_test, ff
from numpy.random import seed
from numpy.random import rand
from numpy.random import uniform

# ps - population size in each of an interation
# n - how many candidates will be tournamented (in this case doesn't matter)
# mi - how many 'winners' will be picked from the population
# fn - cec testing function number (1-28)
'''def fmin(xstart, sigma,
         args=(),
         maxfevals='1e3 * N**2', ftarget=None,
         verb_disp=100, verb_log=1, verb_save=1000, ps=7, n=2, mi=5, fn=1):'''
dim = 5
for i in range(1, 29): # for every CEC test function 1-28 (i)
    for k in range(51):
        x = uniform(low=-80, high=80, size=(dim,))
        purecma_reference_test.fmin(no = k, xstart = x, sigma = 20/3, ps = 4*dim, n = 2, mi = 2*dim, fn = i)
dim = 10
for i in range(1, 29): # for every CEC test function 1-28 (i)
    for k in range(51):
        x = uniform(low=-80, high=80, size=(dim,))
        purecma_reference_test.fmin(no = k, xstart = x, sigma = 20/3, ps = 4*dim, n = 2, mi = 2*dim, fn = i)
dim = 20
for i in range(1, 29): # for every CEC test function 1-28 (i)
    for k in range(51):
        x = uniform(low=-80, high=80, size=(dim,))
        purecma_reference_test.fmin(no = k, xstart = x, sigma = 20/3, ps = 4*dim, n = 2, mi = 2*dim, fn = i)
dim = 30
for i in range(1, 29): # for every CEC test function 1-28 (i)
    for k in range(51):
        x = uniform(low=-80, high=80, size=(dim,))
        purecma_reference_test.fmin(no = k, xstart = x, sigma = 20/3, ps = 4*dim, n = 2, mi = 2*dim, fn = i)

#res[1].logger.plot()  # needs pylab/matplotlib to be installed