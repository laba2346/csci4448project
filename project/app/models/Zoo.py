class Zoo:
    def __init__(self, enclosures, employees, species):
        self.enclosures = enclosures
        self.employees = employees
        self.species = species

    def addEnclosure(self, enclosure):
        self.enclosures.append(enclosure)

    def removeEnclosure(self, enclosureID):
        for index, enclosure in enumerate(self.enclosures):
            id = enclosure.getID()
            if(id == enclosureID):
                del self.enclosures[index]

    def getEnclosures(self):
        return self.enclosures

    def addAnimalToEnclosure(self, animal, enclosureID):
        for e in self.enclosures:
            if(enclosureID == e.getID()):
                e.addAnimal(animal)

    def removeAnimalFromEnclosure(self, enclosureID, animalID):
        for i in range(0, len(self.enclosures)):
            if(self.enclosures[i].getID() == enclosureID):
                print('lets goo')
                self.enclosures[i].removeAnimal(animalID)


    def addEmployee(self, employee):
        self.employees.append(employee)

    def removeEmployee(self, employeeID):
        for index, employee in enumerate(self.employees):
            id = employee.getID()
            if(id == employeeID):
                del self.employees[index]

    def getSpeciesList(self):
        result = [s.getName() for s in self.species]

        return result

    def getSpeciesObj(self, speciesName):
        for s in self.species:
            if(s.getName() == speciesName):
                return s
        return None
