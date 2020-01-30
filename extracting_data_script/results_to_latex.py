import re
import statistics
from os import listdir
from os.path import isfile, join
from decimal import Decimal


DIM_30_MOD = 'all_results\\dim_30_mod\\'
DIM_30_REF = 'all_results\\dim_30_ref\\'
DIMS_MOD = 'all_results\\dims_mod\\'
DIMS_REF = 'all_results\\dims_ref\\'

TERMINATIONS = ['maxfevals', 'condition', 'tolfun']


def process_data(filename, iteration_arr, fvalue_arr, termination_arr, solution_arr):
    try:
        rfile = open(filename, "r")
    except FileNotFoundError:
        return
    content = rfile.readlines()

    # ITERATIONS
    if 'Iterations' not in content[len(content) - 3]:
        rfile.close()
        return
    mean_iterations_line = content[len(content) - 3]
    mean_iterations_str = mean_iterations_line[mean_iterations_line.find("=") + 2:len(mean_iterations_line)]
    mean_iterations_str = re.sub('[^(-9e]', '', mean_iterations_str)
    iterations = float(mean_iterations_str)

    # FVALUE
    if 'f-value' not in content[len(content) - 2]:
        rfile.close()
        return
    mean_fvalue_line = content[len(content) - 2]
    mean_fvalue_str = mean_fvalue_line[mean_fvalue_line.find("=") + 2:len(mean_fvalue_line)]
    mean_fvalue_str = re.sub('[^(-9e]', '', mean_fvalue_str)
    fvalue = float(mean_fvalue_str)

    # TERMINATION
    if 'Termination by' not in content[len(content) - 4]:
        rfile.close()
        return
    reason_line = content[len(content) - 4]
    reason = ''
    for t in TERMINATIONS:
        if t in reason_line:
            reason = t
            break

    # SOLUTION
    solution_line = content[len(content) - 1]
    solution_str = solution_line[solution_line.find("=") + 2:len(solution_line)]
    solution = eval(solution_str)

    # ARRAY UPDATING
    iteration_arr.append(iterations)
    fvalue_arr.append(fvalue)
    termination_arr.append(reason)
    solution_arr.append(solution)

    rfile.close()

    #return mean_iterations, mean_fvalue




dim = 5
dim5_fvalue_arr = []
dim5_termination_arr = []
dim5_solution_arr = []
dim5_iteration_arr = []

for i in range(1, 29):  # for every CEC test function 1-28 (i)
    cec_fvalue_arr = []
    cec_iter_arr = []
    cec_term_arr = []
    cec_sol_arr = []

    for k in range(51):  # for every point
        filename = DIMS_REF + str(k) + "_dim_" + str(dim) + "_cec_" + str(i) + "_tourcand_2_data"
        process_data(filename, iteration_arr=cec_iter_arr, fvalue_arr=cec_fvalue_arr, termination_arr=cec_term_arr,
                     solution_arr=cec_sol_arr)

    dim5_fvalue_arr.append(cec_fvalue_arr)
    dim5_termination_arr.append(cec_term_arr)
    dim5_solution_arr.append(cec_sol_arr)
    dim5_iteration_arr.append(cec_iter_arr)

# print(dim5_iteration_arr)
# print(dim5_solution_arr)
# print(dim5_termination_arr)
# print(dim5_fvalue_arr)



dim = 10
dim10_fvalue_arr = []
dim10_termination_arr = []
dim10_solution_arr = []
dim10_iteration_arr = []

for i in range(1, 29):  # for every CEC test function 1-28 (i)
    cec_fvalue_arr = []
    cec_iter_arr = []
    cec_term_arr = []
    cec_sol_arr = []

    for k in range(51):  # for every point
        filename = DIMS_REF + str(k) + "_dim_" + str(dim) + "_cec_" + str(i) + "_tourcand_2_data"
        process_data(filename, iteration_arr=cec_iter_arr, fvalue_arr=cec_fvalue_arr, termination_arr=cec_term_arr,
                     solution_arr=cec_sol_arr)

    dim10_fvalue_arr.append(cec_fvalue_arr)
    dim10_termination_arr.append(cec_term_arr)
    dim10_solution_arr.append(cec_sol_arr)
    dim10_iteration_arr.append(cec_iter_arr)



dim = 20
dim20_fvalue_arr = []
dim20_termination_arr = []
dim20_solution_arr = []
dim20_iteration_arr = []

for i in range(1, 29):  # for every CEC test function 1-28 (i)
    cec_fvalue_arr = []
    cec_iter_arr = []
    cec_term_arr = []
    cec_sol_arr = []

    for k in range(51):  # for every point
        filename = DIMS_REF + str(k) + "_dim_" + str(dim) + "_cec_" + str(i) + "_tourcand_2_data"
        process_data(filename, iteration_arr=cec_iter_arr, fvalue_arr=cec_fvalue_arr, termination_arr=cec_term_arr,
                     solution_arr=cec_sol_arr)

    dim20_fvalue_arr.append(cec_fvalue_arr)
    dim20_termination_arr.append(cec_term_arr)
    dim20_solution_arr.append(cec_sol_arr)
    dim20_iteration_arr.append(cec_iter_arr)


dim = 30
dim30_fvalue_arr = []
dim30_termination_arr = []
dim30_solution_arr = []
dim30_iteration_arr = []

for i in range(1, 29):  # for every CEC test function 1-28 (i)
    cec_fvalue_arr = []
    cec_iter_arr = []
    cec_term_arr = []
    cec_sol_arr = []

    for k in range(51):  # for every point
        filename = DIM_30_REF + str(k) + "_dim_" + str(dim) + "_cec_" + str(i) + "_tourcand_2_data"
        process_data(filename, iteration_arr=cec_iter_arr, fvalue_arr=cec_fvalue_arr, termination_arr=cec_term_arr,
                     solution_arr=cec_sol_arr)

    dim30_fvalue_arr.append(cec_fvalue_arr)
    dim30_termination_arr.append(cec_term_arr)
    dim30_solution_arr.append(cec_sol_arr)
    dim30_iteration_arr.append(cec_iter_arr)






# For modified results
dim = 5
m_dim5_fvalue_arr = []
m_dim5_termination_arr = []
m_dim5_solution_arr = []
m_dim5_iteration_arr = []
for i in range(1, 29):  # for every CEC test function 1-28 (i)
    cec_fvalue_arr = []
    cec_iter_arr = []
    cec_term_arr = []
    cec_sol_arr = []
    for j in range(2, 7):  # for every size of tournament
        tour_fvalue_arr = []
        tour_iter_arr = []
        tour_term_arr = []
        tour_sol_arr = []
        for k in range(51):  # for every point
            filename = DIMS_MOD +str(k) + "_dim_" + str(dim) + "_cec_" + str(i) + "_tourcand_" + str(j) + "_data"
            process_data(filename, iteration_arr=tour_iter_arr, fvalue_arr=tour_fvalue_arr, termination_arr=tour_term_arr,
                         solution_arr=tour_sol_arr)
        cec_fvalue_arr.append(tour_fvalue_arr)
        cec_iter_arr.append(tour_iter_arr)
        cec_term_arr.append(tour_term_arr)
        cec_sol_arr.append(tour_sol_arr)

    m_dim5_fvalue_arr.append(cec_fvalue_arr)
    m_dim5_termination_arr.append(cec_term_arr)
    m_dim5_solution_arr.append(cec_sol_arr)
    m_dim5_iteration_arr.append(cec_iter_arr)


dim = 10
m_dim10_fvalue_arr = []
m_dim10_termination_arr = []
m_dim10_solution_arr = []
m_dim10_iteration_arr = []
for i in range(1, 29):  # for every CEC test function 1-28 (i)
    cec_fvalue_arr = []
    cec_iter_arr = []
    cec_term_arr = []
    cec_sol_arr = []
    for j in range(2, 7):  # for every size of tournament
        tour_fvalue_arr = []
        tour_iter_arr = []
        tour_term_arr = []
        tour_sol_arr = []
        for k in range(51):  # for every point
            filename = DIMS_MOD +str(k) + "_dim_" + str(dim) + "_cec_" + str(i) + "_tourcand_" + str(j) + "_data"
            process_data(filename, iteration_arr=tour_iter_arr, fvalue_arr=tour_fvalue_arr, termination_arr=tour_term_arr,
                         solution_arr=tour_sol_arr)
        cec_fvalue_arr.append(tour_fvalue_arr)
        cec_iter_arr.append(tour_iter_arr)
        cec_term_arr.append(tour_term_arr)
        cec_sol_arr.append(tour_sol_arr)

    m_dim10_fvalue_arr.append(cec_fvalue_arr)
    m_dim10_termination_arr.append(cec_term_arr)
    m_dim10_solution_arr.append(cec_sol_arr)
    m_dim10_iteration_arr.append(cec_iter_arr)


dim = 20
m_dim20_fvalue_arr = []
m_dim20_termination_arr = []
m_dim20_solution_arr = []
m_dim20_iteration_arr = []
for i in range(1, 29):  # for every CEC test function 1-28 (i)
    cec_fvalue_arr = []
    cec_iter_arr = []
    cec_term_arr = []
    cec_sol_arr = []
    for j in range(2, 7):  # for every size of tournament
        tour_fvalue_arr = []
        tour_iter_arr = []
        tour_term_arr = []
        tour_sol_arr = []
        for k in range(51):  # for every point
            filename = DIMS_MOD +str(k) + "_dim_" + str(dim) + "_cec_" + str(i) + "_tourcand_" + str(j) + "_data"
            process_data(filename, iteration_arr=tour_iter_arr, fvalue_arr=tour_fvalue_arr, termination_arr=tour_term_arr,
                         solution_arr=tour_sol_arr)
        cec_fvalue_arr.append(tour_fvalue_arr)
        cec_iter_arr.append(tour_iter_arr)
        cec_term_arr.append(tour_term_arr)
        cec_sol_arr.append(tour_sol_arr)

    m_dim20_fvalue_arr.append(cec_fvalue_arr)
    m_dim20_termination_arr.append(cec_term_arr)
    m_dim20_solution_arr.append(cec_sol_arr)
    m_dim20_iteration_arr.append(cec_iter_arr)


dim = 30
m_dim30_fvalue_arr = []
m_dim30_termination_arr = []
m_dim30_solution_arr = []
m_dim30_iteration_arr = []
for i in range(1, 29):  # for every CEC test function 1-28 (i)
    cec_fvalue_arr = []
    cec_iter_arr = []
    cec_term_arr = []
    cec_sol_arr = []
    for j in range(2, 7):  # for every size of tournament
        tour_fvalue_arr = []
        tour_iter_arr = []
        tour_term_arr = []
        tour_sol_arr = []
        for k in range(51):  # for every point
            filename = DIM_30_MOD +str(k) + "_dim_" + str(dim) + "_cec_" + str(i) + "_tourcand_" + str(j) + "_data"
            process_data(filename, iteration_arr=tour_iter_arr, fvalue_arr=tour_fvalue_arr, termination_arr=tour_term_arr,
                         solution_arr=tour_sol_arr)
        cec_fvalue_arr.append(tour_fvalue_arr)
        cec_iter_arr.append(tour_iter_arr)
        cec_term_arr.append(tour_term_arr)
        cec_sol_arr.append(tour_sol_arr)

    m_dim30_fvalue_arr.append(cec_fvalue_arr)
    m_dim30_termination_arr.append(cec_term_arr)
    m_dim30_solution_arr.append(cec_sol_arr)
    m_dim30_iteration_arr.append(cec_iter_arr)

# print(statistics.stdev(m_dim30_fvalue_arr[0][0]))
# print(dm_string_constructs)
# dr_sting_constructs = []
REF_FVALUES = [dim5_fvalue_arr, dim10_fvalue_arr, dim20_fvalue_arr, dim30_fvalue_arr]
REF_ITERATIONS = [dim5_iteration_arr, dim10_iteration_arr, dim20_iteration_arr, dim30_iteration_arr]
REF_TERMINATIONS = [dim5_termination_arr, dim10_termination_arr, dim20_termination_arr, dim30_termination_arr]
REF_SOLUTIONS = [dim5_solution_arr, dim10_solution_arr, dim20_solution_arr, dim30_solution_arr]

MOD_FVALUES = [m_dim5_fvalue_arr, m_dim10_fvalue_arr, m_dim20_fvalue_arr, m_dim30_fvalue_arr]
MOD_ITERATIONS = [m_dim5_iteration_arr, m_dim10_iteration_arr, m_dim20_iteration_arr, m_dim30_iteration_arr]
MOD_TERMINATIONS = [m_dim5_termination_arr, m_dim10_termination_arr, m_dim20_termination_arr, m_dim30_termination_arr]
MOD_SOLUTIONS = [m_dim5_solution_arr, m_dim10_solution_arr, m_dim20_solution_arr, m_dim30_solution_arr]

### FORMATING PART ###


'''
# /min/ /max/ /mean/ /var/ /stdev/ /kwartyl/ /? turniej/
NUM_OF_COLLUMS = 12
REF_COLLUMNS = 5
MOD_COLLUMNS = 6
i = 0
OUTPUT = ''
turniej = 2
#for dim in [5,10,20]:
for dim in [5,10,20,30]:
    output_str = '\\begin{table}[H] \n' \
                 '\\centering \n' \
                 '\\begin{adjustbox}{width=1\\textwidth}\n' \
                 '\\small\n' \
                 '\\begin{tabular}{llllllllllll} \n' \
                 '\\hline \n' \
                 '\\multicolumn{' + str(NUM_OF_COLLUMS)+ '}{|c|}{Wymiar = ' + str(dim) + '} \\\\ \n \\hline \n' \
                                                                                         'F-cja CEC & \\multicolumn{' + str(REF_COLLUMNS)+ '}{|c|}{Oryginalny CMAES} &  \\multicolumn{' + str(MOD_COLLUMNS)+ '}{|c|}{Zmodyfikowany CMAES} \\\\ \n \\hline \n'
    output_str += ' --- & MIN & MAX & ŚREDNIA & WARIANCJA  & ODCHYLENIE ST  & TURNIEJ & MIN & MAX & ŚREDNIA & WARIANCJA  & ODCHYLENIE ST    \\\\ \n'
    output_str += '\\hline \n'
    for cec in range (0,28):
        # for turn in range (2,7):
        #     ref_str = ''
        #     if turn == 2:
        #         rfv = REF_FVALUES[i][cec]
        #         multirow = '\\multirow{5}{*}{'
        #         if rfv != []:
        #             ref_str = multirow + str(cec) + '} & ' + multirow + str(min(rfv)) + '} & ' +multirow + str(max(rfv)) + '} & ' + multirow + str(statistics.mean(rfv)) + '} & ' + multirow + str(statistics.variance(rfv))+ '} & ' + multirow + str(statistics.stdev(rfv)) + '} & ' + multirow + '} & TEST &'
        #     mfv = MOD_FVALUES[i][cec][turn-2]
        #     mod_str = ' & & & & & & \\\\ \n'
        #     if mfv != []:
        #         mod_str =str(turn) + ' & ' + str(min(mfv)) + ' & ' + str(max(mfv))+ ' & ' +(str(statistics.mean(mfv))) + ' & ' + str(statistics.variance((mfv))) + ' & ' +  str(statistics.stdev(mfv))+ ' & ' + 'TEST' + '\\\\ \n'
        #     output_str += (ref_str + mod_str)
        ref_str = ''

        rfv = REF_FVALUES[i][cec]
        if rfv:
            ref_str = str(cec+1) + ' & '+  str("%.5g" % min(rfv)) + ' & '+  str( "%.5g" % max(rfv)) + ' & '+  str("%.5g" % statistics.mean(rfv)) + ' & '+  str("%.5g" % statistics.variance(rfv)) + ' & '+ str("%.5g" % statistics.stdev(rfv)) + ' & '
        mfv = MOD_FVALUES[i][cec][turniej - 2]
        mod_str = ' & & & & & & \\\\ \n'
        if mfv:
            mod_str = str(turniej) + ' & ' + str("%.5g" % min(mfv)) + ' & ' + str("%.5g" % max(mfv))+ ' & ' +  str("%.5g" % statistics.mean(mfv)) + ' & ' + str("%.5g" % statistics.variance((mfv))) + ' & ' +  str("%.5g" % statistics.stdev(mfv)) + '\\\\ \n'
        output_str += (ref_str + mod_str)

    output_str += '\\hline ' \
                  '\\end{tabular}\\end{adjustbox}\n' \
                  '\\end{table}\n'
    i+=1
    OUTPUT += output_str
print(OUTPUT)
'''

def most_frequent(List):
    return max(set(List), key = List.count)

NUM_OF_COLLUMS = 7
OUTPUT = ''

i = 0
for dim in [5,10,20,30]:
    output_str = '\\begin{table}[H] \n' \
                 '\\centering \n' \
                 '\\begin{adjustbox}{width=1\\textwidth}\n' \
                 '\\small\n' \
                 '\\begin{tabular}{llllllll} \n' \
                 '\\hline \n' \
                 '\\multicolumn{' + str(NUM_OF_COLLUMS)+ '}{|c|}{Wymiar = ' + str(dim) + '} \\\\ \n \\hline \n' \
                 'F-cja CEC &  Oryginalny CMAES &  CMAES z turniejem: 2 & CMAES z turniejem: 3 & CMAES z turniejem: 4 & CMAES z turniejem: 5 & CMAES z turniejem: 6 \\\\ \n \\hline \n'
    for cec in range (0,28):
        output_str += str(cec+1) + ' & '
        if REF_TERMINATIONS[i][cec]:
            output_str += most_frequent(REF_TERMINATIONS[i][cec])
        output_str += ' & '
        for turn in range(0,5):
            if MOD_TERMINATIONS[i][cec][turn]:
                output_str += most_frequent(MOD_TERMINATIONS[i][cec][turn])
            if turn != 4:
                output_str += ' & '
            else:
                output_str += ' \\\\ \n'



    output_str += '\\hline ' \
                  '\\end{tabular}\\end{adjustbox}\n' \
                  '\\end{table}\n'
    i+=1
    OUTPUT += output_str
print(OUTPUT)