from datetime import datetime, date
from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':

    print(date.today())

    calculate_salary()

    get_employees()