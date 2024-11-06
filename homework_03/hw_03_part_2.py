
def requires_access(func):
    def wrapper(*args, **kwargs):
        security_system = args[0]
        employee = args[1] if len(args) > 1 else kwargs["employee"]
        zone = args[2] if len(args) > 2 else kwargs["zone"]

        if zone in employee.access_zones or zone in security_system.open_zones:
            security_system.add_employee_at_granted(employee, zone)
            return func(*args, **kwargs)
        else:
            security_system.add_employee_at_denied(employee, zone)
            print("Request was rejected!")

    return wrapper


def log_access(is_granted):
    def decorator(func):
        def wrapper(*args, **kwargs):
            employee = args[1] if len(args) > 1 else kwargs["employee"]
            zone = args[2] if len(args) > 2 else kwargs["zone"]
            if is_granted:
                print(f"To an employee by name {employee.name} access was allowed to {zone}")
            else:
                print(f"To an employee by name {employee.name} access denied to {zone}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


class Employee:
    def __init__(self, name: str, access_zones: list):
        self.__name = name
        self.__access_zones = access_zones

    def __str__(self):
        return self.__name

    @property
    def name(self) -> str:
        return self.__name

    @property
    def access_zones(self) -> list:
        return self.__access_zones


class SecuritySystem:
    def __init__(self, open_zones):
        self.__open_zones = open_zones
        self.__access_granted = []
        self.__access_denied = []

    @property
    def open_zones(self) -> list:
        return self.__open_zones

    @requires_access
    def enter_zone(self, employee, zone):
        pass

    @log_access(True)
    def add_employee_at_granted(self, employee: Employee, zone: str):
        self.__access_granted.append(f"{zone}, {employee}")

    @log_access(False)
    def add_employee_at_denied(self, employee: Employee, zone: str):
        self.__access_denied.append(f"{zone}, {employee}")


employee_1 = Employee("emp1", access_zones=["Office", "Library", "Lab"])
employee_2 = Employee("emp2", access_zones=["Office", "Lab"])
security = SecuritySystem(open_zones=["Lobby", "Cafeteria"])

security.enter_zone(employee_1, "Library")
security.enter_zone(employee_2, "Library")
security.enter_zone(employee_2, "Lobby")


