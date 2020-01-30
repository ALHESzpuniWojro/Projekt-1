# Extracting and carrying out statistics on results data


rfile = open(r"test.txt", "w+")
ss = ["ssss\n", "xxxx\n", "aaaa\n"]
rfile.writelines(ss)
rfile.write("No siemanko")
rfile.close()

rfile = open(r"test.txt", "r")
k = rfile.readlines()

print(k)

rfile.close()

rfile = open(r"0_dim_30_cec_1_tourcand_3_data", "r")
content = rfile.readlines()

mean_iterations = ''
mean_iterations = content[len(content)-3]
print(mean_iterations[mean_iterations.find("=")+2:len(mean_iterations)])

mean_fvalue = ''
mean_fvalue = content[len(content)-2]
print(mean_fvalue[mean_fvalue.find("=")+2:len(mean_fvalue)])

mean_solution = ''
mean_solution = content[len(content)-1]
print(mean_solution[mean_solution.find("=")+2:len(mean_solution)])

TERMINATIONS = ['maxfevals', 'condition', 'tolfun']

reason_line = content[len(content) - 4]
reason = ''
for t in TERMINATIONS:
    if t in reason_line:
        reason = t
        break

print(reason)

solution_line = content[len(content) - 1]
solution_str = solution_line[solution_line.find("=") + 2:len(solution_line)]
solution = eval(solution_str)

print(solution[0])

rfile.close()

# if l[0] == 'e' then ... , if l[0] == 'S' then ...

c = content[5].split(' ')
print(float(c[len(c)-1]))

wfile = open(r"summary", "w+")
wfile.write(mean_iterations[mean_iterations.find("=")+2:len(mean_iterations)])
wfile.write(mean_fvalue[mean_fvalue.find("=")+2:len(mean_fvalue)])
wfile.write(mean_solution[mean_solution.find("=")+2:len(mean_solution)])
wfile.close()

'''
# For reference results
dim = 5
for i in range(1, 29): # for every CEC test function 1-28 (i)
    for k in range(51): # for every point
        filename = str(k) + "_dim_" + str(dim) + "_cec_" + i + "_tourcand_2_data"
        file = open(filename, "r")
        file.close()
dim = 10
for i in range(1, 29): # for every CEC test function 1-28 (i)
    for k in range(51): # for every point
        
dim = 20
for i in range(1, 29): # for every CEC test function 1-28 (i)
    for k in range(51): # for every point

dim = 30
for i in range(1, 29): # for every CEC test function 1-28 (i)
    for k in range(51): # for every point
        

# For modified results
dim = 5
for i in range(1, 29): # for every CEC test function 1-28 (i)
    for j in range(2, 7): # for every size of tournament
        for k in range(51): # for every point
            filename = str(k) + "_dim_" + str(dim) + "_cec_" + i + "_tourcand_" + j + "_data"
            file = open(filename, "r")
            file.close()
dim = 10
for i in range(14, 29): # for every CEC test function 1-28 (i)
    for j in range(2, 7): # for every size of tournament
        for k in range(51): # for every point
            
dim = 20
for i in range(1, 29): # for every CEC test function 1-28 (i)
    for j in range(2, 7): # for every size of tournament
        for k in range(51): # for every point
           
dim = 30
for i in range(1, 29): # for every CEC test function 1-28 (i)
    for j in range(2, 7): # for every size of tournament
        for k in range(51): # for every point
'''