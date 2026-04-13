class EmployeeSalary:
    hourly_payment = 400  

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None and rest_days is not None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        if self.hours is None:
            return 0
        return self.hours * self.hourly_payment


employee = EmployeeSalary(name="Jenya", rest_days=2)
employee = EmployeeSalary.get_hours(employee.name, employee.hours, employee.rest_days, employee.email)
employee = EmployeeSalary.get_email(employee.name, employee.hours, employee.rest_days, employee.email)
print(f"Отработанные часы: {employee.hours} ч")  
print(f"Email: {employee.email}")  
print(f"Зарплата за неделю: {employee.salary()} руб.")  

EmployeeSalary.set_hourly_payment(500)
print(f"Новая зарплата за неделю: {employee.salary()} руб.")  