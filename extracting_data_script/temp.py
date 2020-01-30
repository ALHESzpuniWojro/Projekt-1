
NUM_OF_COLLUMS = 14
REF_COLLUMNS = 6
MOD_COLLUMNS = 7

for dim in [5,10,20,30]:
    output_str = '\\begin{table}[ht] \n' \
                 '\\centering \n' \
                 '\\begin{adjustbox}{width=1\\textwidth}\n' \
                 '\\small\n' \
                 '\\begin{tabular}{llllllllllllll} \n' \
                 '\\hline \n' \
                 '\\multicolumn{' + str(NUM_OF_COLLUMS)+ '}{|c|}{Wymiar = ' + str(dim) + '} \\\\ \n \\hline \n' \
                    'F-cja CEC & \\multicolumn{' + str(REF_COLLUMNS)+ '}{|c|}{Oryginalny CMAES} &  \\multicolumn{' + str(MOD_COLLUMNS)+ '}{|c|}{Zmodyfikowany CMAES} \\\\ \n \\hline \n'
    output_str += ' --- & TESTTEST & TESTTEST & TESTTEST & TETESTST  & TETESTST  & TESTESTT & TETESTST & TEST & TEST & TEST & TEST & TEST & TEST  \\\\ \n'

    output_str += '\\hline ' \
                  '\\end{tabular}\\end{adjustbox}\n' \
                  '\\end{table}\n'
    print(output_str)