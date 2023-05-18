def solve_math_problem(problem):
    try:
        result = eval(problem)
        print(f"The solution to {problem} is {result}")
    except:
        print("Invalid input. Please enter a valid math problem.")

problem = input("Enter a math problem: ")
solve_math_problem(problem)
