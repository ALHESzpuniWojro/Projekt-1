from cma import purecma_modified, ff
from numpy.random import seed
from numpy.random import rand
from numpy.random import uniform

# ps - population size in each of an interation
# n - how many candidates will be tournamented
# mi - how many 'winners' will be picked from the population
# fn - cec testing function number (1-28)
'''def fmin(xstart, sigma,
         args=(),
         maxfevals='1e3 * N**2', ftarget=None,
         verb_disp=100, verb_log=1, verb_save=1000, ps=7, n=2, mi=5, fn=1):'''

'''xs =[]
dim = 5
for i in range(1, 29): # for every CEC test function 1-28 (i)
    for j in range(2, 7):
        for k in range(51):
            x = uniform(low=-80, high=80, size=(dim,))
            xs[k] = x.tolist()
            purecma_modified.fmin(no = k, xstart = xs[k], sigma = 20/3, ps = 4*dim, n = j, mi = 2*dim, fn = i)
'''
'''xs=[]
dim = 2
for i in range(1, 10): # for every CEC test function 1-28 (i)
    for j in range(2, 4):
        for k in range(5):
            x = uniform(low=-80, high=80, size=(dim,))
            xs.append(x)
            purecma_modified.fmin(no = k, xstart = xs[k], sigma = 20/3, ps = 4*dim, n = j, mi = 2*dim, fn = i)
'''
dim = 10
res = purecma_modified.fmin(1, dim * [0.5], sigma = 20/3, ps = 4*dim, n = 4, mi = 2*dim, fn = 1, verb_disp=100)
#res[1].logger.plot()  # needs pylab/matplotlib to be installed