from models.employee_model import EmployeeModel
from views.employee_view import EmployeeView
from prettytable import PrettyTable


class EmployeeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    # option 1: Tổng số nhân viên
    def number_of_employees(self):
        print("\nTổng số nhân viên: {0}".format(
            len(self.model.employees_data)))

    # option 2: Số nhân viên nữ / số nhân viên nam
    def number_of_female_male(self):
        female = sum(
            1 for e in self.model.employees_data if e["gender"] == "female")
        male = len(self.model.employees_data) - female
        print(
            "\nSố nhân viên nữ / Số nhân viên nam: {0} / {1}".format(female, male))

    # option 3: Nhân viên có lương cao nhất
    def highest_salary_employee(self):
        print_title = "\n\t{} Nhân viên có lương cao nhất:\n"
        max_salary = max(e["salary"] for e in self.model.employees_data)
        highest_salary_employees = [
            e for e in self.model.employees_data if e["salary"] == max_salary]
        print(print_title.format(len(highest_salary_employees)))
        self.view.display_table(highest_salary_employees)

    # option 4: Nhân viên có lương thấp nhất
    def lowest_salary_employee(self):
        print_title = "\n\t{} Nhân viên có lương thấp nhất:\n"
        min_salary = min(e["salary"] for e in self.model.employees_data)
        lowest_salary_employees = [
            e for e in self.model.employees_data if e["salary"] == min_salary]
        print(print_title.format(len(lowest_salary_employees)))
        self.view.display_table(lowest_salary_employees)

    # option 5: Nhân viên có kinh nghiệm nhiều nhất
    def most_exp_employee(self):
        print_title = "\n\t{} Nhân viên có kinh nghiệm nhiều nhất:\n"
        most_exp = max(e["years_of_experience"]
                       for e in self.model.employees_data)
        most_exp_employees = [
            e for e in self.model.employees_data if e["years_of_experience"] == most_exp]
        print(print_title.format(len(most_exp_employees)))
        self.view.display_table(most_exp_employees)

    # option 6: Nhân viên trẻ tuổi nhất và lớn tuổi nhất
    def youngest_oldest_employee(self):
        print_title_youngest = "\n\t{} Nhân viên trẻ tuổi nhất:\n"
        print_title_oldest = "\n\t{} Nhân viên lớn tuổi nhất:\n"

        min_age = min(e["age"] for e in self.model.employees_data)
        max_age = max(e["age"] for e in self.model.employees_data)

        youngest_employees = [
            e for e in self.model.employees_data if e["age"] == min_age]
        oldest_employees = [
            e for e in self.model.employees_data if e["age"] == max_age]

        print(print_title_youngest.format(len(youngest_employees)))
        self.view.display_table(youngest_employees)

        print(print_title_oldest.format(len(oldest_employees)))
        self.view.display_table(oldest_employees)

    # option 7: Tổng số lương phải trả cho tất cả nhân viên
    def total_salary(self):
        print_result = "\n\tTổng số lương phải trả cho tất cả nhân viên: {}\n"
        total_salary = sum(e['salary'] for e in self.model.employees_data)
        print(print_result.format(total_salary))

    # Run system
    def run(self):
        print("\nChào mừng đến với hệ thống quản lý nhân viên!")
        while True:
            print()
            self.show_menu()
            option = input("Nhập lựa chọn của bạn: (0-7) ")
            if not option.isdigit() or int(option) not in range(8):
                print("Lựa chọn không hợp lệ. Nhập vào lựa chọn từ 0 đến 7!")
                continue
            option = int(option)

            if option == 0:
                print("Đã thoát khỏi hệ thống quản lý nhân viên.")
                break
            elif option == 1:
                self.number_of_employees()
            elif option == 2:
                self.number_of_female_male()
            elif option == 3:
                self.highest_salary_employee()
            elif option == 4:
                self.lowest_salary_employee()
            elif option == 5:
                self.most_exp_employee()
            elif option == 6:
                self.youngest_oldest_employee()
            elif option == 7:
                self.total_salary()

    def show_menu(self):
        print("* " * 26)
        print("*              Danh sách chức năng:               *")
        print("* [1] Tổng số nhân viên                           *")
        print("* [2] Số nhân viên nữ / số nhân viên nam          *")
        print("* [3] Nhân viên có lương cao nhất                 *")
        print("* [4] Nhân viên có lương thấp nhất                *")
        print("* [5] Nhân viên có kinh nghiệm nhiều nhất         *")
        print("* [6] Nhân viên trẻ nhất và lớn nhất              *")
        print("* [7] Tổng số lương phải trả cho tất cả nhân viên *")
        print("* [0] Thoát khỏi hệ thống                         *")
        print("* " * 26)
