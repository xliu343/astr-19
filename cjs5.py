import numpy as np
import math
def main():
    x_values = np.linspace(0, 2, 1000)
    print("x\t\tsin(x)")
    print("----------------------")
    for x in x_values:
        print(f"{x:.6f}\t{math.sin(x):.6f}")
if __name__ == '__main__':
    main()