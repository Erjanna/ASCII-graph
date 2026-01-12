import math

def graph(width = 60, height = 25, x_min = -10, x_max = 10):
    func = input("Enter your function: ").replace("^", "**").replace("sin", "math.sin").replace("cos", "math.cos").replace("tan", "math.tan").replace("ln", "math.log")

    for y in range(height, -height, -1):
        line = ""
        for x in range(-width, width):
            x_temp = x / width * (x_max - x_min)
            epsilon = 0
            replace = {"x": x_temp + epsilon, "math": math, "e": math.e, "pi": math.pi}
            try:
                y_temp = eval(func, replace)
            except ValueError:
                y_temp = None
            try:
                if y + 1 > round(y_temp) > y - 1:
                    epsilon = 0.01
                    approx_derivative = (eval(func, {"x": x_temp + epsilon, "math": math, "e": math.e, "pi": math.pi}) - y_temp) / 0.01
                    if approx_derivative > 5:
                        line += "\033[1;33m|\033[0m"
                    elif approx_derivative > 1:
                        line += "\033[1;33m/\033[0m"
                    elif approx_derivative >= -1:
                        line += "\033[1;33m-\033[0m"
                    elif approx_derivative >= -5:
                        line += "\033[1;33m\\\033[0m"
                    else: line += "\033[1;33m|\033[0m"
                elif x == 0 and y == 0 :
                    line += "+"
                elif x == 0 :
                    line += "|"
                elif y == 0 :
                    line += "-"
                else:
                    line += " "
            except Exception: 
                if x == 0 and y == 0 :
                    line += "\033[31m+\033[0m"
                elif x == 0 :
                    line += "\033[31m|\033[0m"
                elif y == 0 :
                    line += "\033[31m-\033[0m"
                else:
                    line += " "
        print(line)

    action = input("Type 1 to graph a new function, press enter to exit: ")
    if action == "1":
        graph()

if __name__ == "__main__":
    graph()
