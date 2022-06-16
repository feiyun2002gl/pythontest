# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Employee import Employee
from Employee2 import Employee2


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    "创建 Employee 类的第一个对象"
    emp1 = Employee("Zara", 2000)
    "创建 Employee 类的第二个对象"
    emp2 = Employee("Manni", 5000)
    emp1.displayEmployee()
    emp1.displayCount()
    emp3 = Employee2()
    emp3.displayEmployee()
    emp3.displayCount()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
