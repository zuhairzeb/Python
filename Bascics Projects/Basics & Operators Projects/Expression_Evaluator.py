####  Expression Evaluator

def evaluate_expression():
    expr = input("Enter an arithmetic expression: ")
    try:
        result = eval(expr)
        print("Result:", result)
    except:
        print("Invalid expression!")

evaluate_expression()