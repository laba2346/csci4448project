from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from models.Animal import *
from models.Species import *
from models.Zoo import *
from models.Employee import *
from models.Enclosure import *
import sys

from views.main_window import Ui_MainWindow
from views.new_animal import Ui_Dialog as Form

class App(QMainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.bt_add_animal.clicked.connect(self.open_animal_dialog)
        self.zoo = init()
        self.updateLists()

    def open_animal_dialog(self):
        dialog = QDialog()
        dialog.ui = Form()
        dialog.ui.setupUi(dialog)

        # Fetch lists for dropdowns
        species = self.zoo.getSpeciesList()
        enclosures = self.zoo.getEnclosures()
        dialog.ui.species_selection.addItem('')
        # Populate dropdowns
        for s in species:
            dialog.ui.species_selection.addItem(s)
        for e in enclosures:
            dialog.ui.enclosure_selection.addItem("Enclosure #"+str(e.getID()))
        dialog.ui.sex_selection.addItem("")
        dialog.ui.sex_selection.addItem("M")
        dialog.ui.sex_selection.addItem("F")

        # Run dialog
        dialog.exec_()
        dialog.show()

        # Add animal with info provided in dialog
        name = dialog.ui.name_input.text()
        speciesName = dialog.ui.species_selection.currentText()
        sex = dialog.ui.sex_selection.currentText()
        age = dialog.ui.age_input.text()
        enclosureID = dialog.ui.enclosure_selection.currentIndex()+1
        self.addAnimal(name, speciesName, sex, age, enclosureID)

    def addAnimal(self, name, speciesName, sex, age, enclosureID):
        if(name != ""):
            species = self.zoo.getSpeciesObj(speciesName)
            new_animal = Animal(name, sex, species, age, True)
            self.zoo.addAnimalToEnclosure(new_animal, enclosureID)
            self.updateLists()

    def updateLists(self):
        self.ui.animal_list.clear()
        self.ui.enclosure_list.clear()
        for e in self.zoo.getEnclosures():
            enclosureStr = "Enclosure #" + str(e.getID()) + " has the following animals: "
            for animal in e.getAnimals():
                enclosureStr = enclosureStr + animal.getName() + ", "
                self.ui.animal_list.addItem(animal.getName())
            self.ui.enclosure_list.addItem(enclosureStr)






def main():
    app = QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()

def init():
    monkey = Species("Fruits & nuts", "Monkey", "Very curious and slightly dangerous animal", "Jungle")
    gorilla = Species("Fruits & nuts", "Gorilla", "Big monkey, slightly more dangerous", "Jungle")
    polar_bear = Species("Fish", "Polar Bear", "Very large and cuddly looking bear; prefers the cold.", "Polar")
    species_list = [monkey, gorilla, polar_bear]

    jimbo = Animal("Jimbo", "M", monkey, 3, True)
    max = Animal("Max", "M", monkey, 1.5, True)
    bob = Animal("Bob", "M", gorilla, 3, False)
    pooh = Animal("Pooh", "M", polar_bear, 1, True)

    enclosure_1 = Enclosure([jimbo, max, bob], "Fruit & Nuts", "Clean")
    enclosure_2 = Enclosure([pooh], "Fish", "Clean")

    zoo = Zoo([enclosure_1, enclosure_2],[],[monkey, gorilla, polar_bear])

    return zoo



if(__name__ == "__main__"):
    main()
