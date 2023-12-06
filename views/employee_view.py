from prettytable import PrettyTable


class EmployeeView:
    def display_table(self, employees):
        if employees:
            table = PrettyTable()
            table.field_names = ["ID", "First Name", "Last Name", "Email", "Phone", "Gender", "Age",
                                 "Job Title", "Years of Experience", "Salary", "Department"]

            for employee in employees:
                table.add_row([
                    employee["id"],
                    employee["first_name"],
                    employee["last_name"],
                    employee["email"],
                    employee["phone"],
                    employee["gender"],
                    employee["age"],
                    employee["job_title"],
                    employee["years_of_experience"],
                    employee["salary"],
                    employee["department"]
                ])

            print(table)
        else:
            print("No employees found.")
