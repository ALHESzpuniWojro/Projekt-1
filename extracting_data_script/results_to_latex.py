import re
import statistics



PATH_MOD = 'home\\wojciech\\Desktop\\all_data\\result_out_mod\\'
PATH_REF = 'home\\wojciech\\Desktop\\all_data\\result_out_ref\\'

TERMINATIONS = ['maxfevals', 'condition', 'tolfun', 'tolx']

MIN_VALUES = []
temp = -1400
for i in range(1,29):
    MIN_VALUES.append(temp)
    temp += 100
    if temp == 0:
        temp = 100

filenames = []





def process_data(filename, iteration_arr, fvalue_arr, termination_arr, solution_arr):
    try:
        rfile = open(filename, "r")

        filenames.append(filename)

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

        filename = PATH_REF + str(k) + "_dim_" + str(dim) + "_cec_" + str(i) + "_tourcand_2_data"

        process_data(filename, iteration_arr=cec_iter_arr, fvalue_arr=cec_fvalue_arr, termination_arr=cec_term_arr,
                     solution_arr=cec_sol_arr)

    dim5_fvalue_arr.append(cec_fvalue_arr)
    dim5_termination_arr.append(cec_term_arr)
    dim5_solution_arr.append(cec_sol_arr)
    dim5_iteration_arr.append(cec_iter_arr)




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

        filename = PATH_REF + str(k) + "_dim_" + str(dim) + "_cec_" + str(i) + "_tourcand_2_data"

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

        filename = PATH_REF + str(k) + "_dim_" + str(dim) + "_cec_" + str(i) + "_tourcand_2_data"

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

        filename = PATH_REF + str(k) + "_dim_" + str(dim) + "_cec_" + str(i) + "_tourcand_2_data"

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

    for j in range(1, 9):  # for every size of tournament

        tour_fvalue_arr = []
        tour_iter_arr = []
        tour_term_arr = []
        tour_sol_arr = []
        for k in range(51):  # for every point

            filename = PATH_MOD +str(k) + "_dim_" + str(dim) + "_cec_" + str(i) + "_tourcand_" + str(j) + "_data"

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

    for j in range(1, 9):  # for every size of tournament

        tour_fvalue_arr = []
        tour_iter_arr = []
        tour_term_arr = []
        tour_sol_arr = []
        for k in range(51):  # for every point

            filename = PATH_MOD +str(k) + "_dim_" + str(dim) + "_cec_" + str(i) + "_tourcand_" + str(j) + "_data"

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

    for j in range(1, 9):  # for every size of tournament

        tour_fvalue_arr = []
        tour_iter_arr = []
        tour_term_arr = []
        tour_sol_arr = []
        for k in range(51):  # for every point

            filename = PATH_MOD +str(k) + "_dim_" + str(dim) + "_cec_" + str(i) + "_tourcand_" + str(j) + "_data"

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

    for j in range(1, 9):  # for every size of tournament

        tour_fvalue_arr = []
        tour_iter_arr = []
        tour_term_arr = []
        tour_sol_arr = []
        for k in range(51):  # for every point

            filename = PATH_MOD +str(k) + "_dim_" + str(dim) + "_cec_" + str(i) + "_tourcand_" + str(j) + "_data"

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



REF_FVALUES = [dim5_fvalue_arr, dim10_fvalue_arr, dim20_fvalue_arr, dim30_fvalue_arr]
REF_ITERATIONS = [dim5_iteration_arr, dim10_iteration_arr, dim20_iteration_arr, dim30_iteration_arr]
REF_TERMINATIONS = [dim5_termination_arr, dim10_termination_arr, dim20_termination_arr, dim30_termination_arr]
REF_SOLUTIONS = [dim5_solution_arr, dim10_solution_arr, dim20_solution_arr, dim30_solution_arr]

MOD_FVALUES = [m_dim5_fvalue_arr, m_dim10_fvalue_arr, m_dim20_fvalue_arr, m_dim30_fvalue_arr]
MOD_ITERATIONS = [m_dim5_iteration_arr, m_dim10_iteration_arr, m_dim20_iteration_arr, m_dim30_iteration_arr]
MOD_TERMINATIONS = [m_dim5_termination_arr, m_dim10_termination_arr, m_dim20_termination_arr, m_dim30_termination_arr]
MOD_SOLUTIONS = [m_dim5_solution_arr, m_dim10_solution_arr, m_dim20_solution_arr, m_dim30_solution_arr]



### FORMATING PART ###



# /min/ /max/ /mean/ /var/ /stdev/ /kwartyl/ /? turniej/
NUM_OF_COLLUMS = 12
REF_COLLUMNS = 5
MOD_COLLUMNS = 6


f= open("RESULTS.txt","w+")

OUTPUT = ''
turniej = 1
#for dim in [5,10,20]:
for turniej in range (6,9):
    i = 0
    for dim in [5,10]:
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
            ref_str = ''

            rfv = REF_FVALUES[i][cec]
            if rfv:
                ref_str = str(cec+1) + ' & '+  str("%.5g" % (min(rfv) - MIN_VALUES[cec])) + ' & '+  str( "%.5g" % (max(rfv) - MIN_VALUES[cec])) + ' & '+  str("%.5g" % (statistics.mean(rfv) - MIN_VALUES[cec])) + ' & '+  str("%.5g" % statistics.variance(rfv)) + ' & '+ str("%.5g" % statistics.stdev(rfv)) + ' & '
            mfv = MOD_FVALUES[i][cec][turniej - 1]
            mod_str = ' & & & & & & \\\\ \n'
            if mfv:
                mod_str = str(turniej) + ' & ' + str("%.5g" % (min(mfv) - MIN_VALUES[cec])) + ' & ' + str("%.5g" % (max(mfv) - MIN_VALUES[cec]))+ ' & ' +  str("%.5g" % (statistics.mean(mfv) - MIN_VALUES[cec])) + ' & ' + str("%.5g" % statistics.variance(mfv)) + ' & ' +  str("%.5g" % statistics.stdev(mfv)) + '\\\\ \n'
            output_str += (ref_str + mod_str)

        output_str += '\\hline ' \
                      '\\end{tabular}\\end{adjustbox}\n' \
                      '\\end{table}\n'
        i+=1
        OUTPUT += output_str
print(OUTPUT)
f.write(OUTPUT)

'''

#'F-cja CEC &  Oryginalny CMAES &  CMAES z turniejem: 2 & CMAES z turniejem: 3 & CMAES z turniejem: 4 & CMAES z turniejem: 5 & CMAES z turniejem: 6 \\\\ \n \\hline \n'

'''
def most_frequent(List):
    return max(set(List), key = List.count)


OUTPUT = ''
NUM_OF_COLLUMS = 5
i = 2
for dim in [20]:

    output_str = '\\begin{table}[H] \n' \
                 '\\centering \n' \
                 '\\begin{adjustbox}{width=1\\textwidth}\n' \
                 '\\small\n' \
                 '\\begin{tabular}{lllll} \n' \
                 '\\hline \n' \
                 '\\multicolumn{' + str(NUM_OF_COLLUMS)+ '}{|c|}{Wymiar = ' + str(dim) + '} \\\\ \n \\hline \n' \
                 'F-cja CEC &  Oryginalny CMAES &  CMAES z porównaniem parami & CMAES z turniejem: 2 & CMAES z turniejem: 3 \\\\ \n \\hline \n'

    for cec in range (0,28):
        output_str += str(cec+1) + ' & '
        if REF_TERMINATIONS[i][cec]:
            output_str += most_frequent(REF_TERMINATIONS[i][cec])
        output_str += ' & '
        for turn in range(0,3):
            if MOD_TERMINATIONS[i][cec][turn]:
                output_str += most_frequent(MOD_TERMINATIONS[i][cec][turn])
            if turn != 2:
                output_str += ' & '
            else:
                output_str += ' \\\\ \n'

    output_str += '\\hline ' \
                  '\\end{tabular}\\end{adjustbox}\n' \
                  '\\end{table}\n'
    i+=1
    OUTPUT += output_str
print(OUTPUT)
'''



OUTPUT = ''
NUM_OF_COLLUMS = 5
i = 2
for dim in [20, 30]:

    output_str = '\\begin{table}[H] \n' \
                 '\\centering \n' \
                 '\\begin{adjustbox}{width=1\\textwidth}\n' \
                 '\\small\n' \
                 '\\begin{tabular}{lllll} \n' \
                 '\\hline \n' \
                 '\\multicolumn{' + str(NUM_OF_COLLUMS)+ '}{|c|}{Wymiar = ' + str(dim) + '} \\\\ \n \\hline \n' \
                 'F-cja CEC &  Oryginalny CMAES &  CMAES z porównaniem parami & CMAES z turniejem: 2 & CMAES z turniejem: 3 \\\\ \n \\hline \n'

    for cec in range (0,28):
        output_str += str(cec+1) + ' & '
        if REF_ITERATIONS[i][cec]:
            output_str += str("%.5g" % statistics.mean(REF_ITERATIONS[i][cec]))
        output_str += ' & '
        for turn in range(0,3):
            if MOD_ITERATIONS[i][cec][turn]:
                output_str += str("%.5g" % statistics.mean(MOD_ITERATIONS[i][cec][turn]))
            if turn != 2:
                output_str += ' & '
            else:
                output_str += ' \\\\ \n'



    output_str += '\\hline ' \
                  '\\end{tabular}\\end{adjustbox}\n' \
                  '\\end{table}\n'

    i += 1
    OUTPUT += output_str
print(OUTPUT)
'''

