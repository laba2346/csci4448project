class Zoo:
    def __init__(self, enclosures, employees):
        self.enclosures = enclosures
        self.employees = employees

    def addEnclosure(self, enclosure):
        self.enclosures.append(enclosure)

    def removeEnclosure(self, enclosureID):
        for index, enclosure in enumerate(self.enclosures):
            id = enclosure.getID()
            if(id == enclosureID):
                del self.enclosures[index]

    def addEmployee(self, employee):
        self.employees.append(employee)

    def removeEmployee(self, employeeID):
        for index, employee in enumerate(self.employees):
            id = employee.getID()
            if(id == employeeID):
                del self.employees[index]
