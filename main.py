from datetime import datetime
from Application import salary as sal
from Application.db import People
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print(datetime.today())
    sal.calculate_salary()
    People.get_employees()
    print("=============")
    plt.plot([1, 3, 2, 6, 1], [2, 1, 3, 6, 5], [4, 7, 9, 5, 7])
    plt.show()
