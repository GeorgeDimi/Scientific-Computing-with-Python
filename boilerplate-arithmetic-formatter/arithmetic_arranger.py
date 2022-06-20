import operator
def arithmetic_arranger(problems, show=False):
    arranged_problems = ""
    ops = { "+": operator.add, "-": operator.sub }


    if len(problems) > 5:
        return "Error: Too many problems"

    for problem in problems:
        problem_list = problem.split()

        # check inputs
        if problem_list[1] not in ops.keys():
            return "Error: Operator must be '+' or '-'"  
        if not problem_list[0].isnumeric() or not problem_list[2].isnumeric:
            return "Error: Numbers must only contain digits"
        if len(problem_list[0]) > 4 or  len(problem_list[2]) > 4:
            return "Error: Numbers cannot be more than four digits"
        first_value = int(problem_list[0])
        second_value = int(problem_list[2])
        problem_list__with_results = problem_list.append(ops[problem_list[1]](first_value,second_value))
              
        line_up = line_up + ' {:>8}'.format(first_value)
        second_line = second_line +  '{}{:>8}'.format(problem_list[1], first_value)

    
        
    return arranged_problems