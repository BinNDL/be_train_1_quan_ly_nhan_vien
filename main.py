from models.employee_model import EmployeeModel
from views.employee_view import EmployeeView
from controllers.employee_controller import EmployeeController
from prettytable import PrettyTable


if __name__ == "__main__":
    try:
        file_path = "employees.json"
        if not file_path.endswith('.json'):
            raise Exception(f"File '{file_path}' phải là 1 file json.")
        model = EmployeeModel(file_path)
        view = EmployeeView()
        controller = EmployeeController(model, view)
        controller.run()
    except Exception as e:
        print(f"Error: {e}")
