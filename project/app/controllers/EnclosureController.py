from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, login_required, logout_user
from app.forms import LoginForm
from app.models.Enclosure import Enclosure
from app import zoo

class EnclosureController:
    def addEnclosure(self):
        zoo.addEnclosure(Enclosure([], "", ""))
        return redirect(url_for('enclosures'))

    def editEnclosure(self):
        foodType = request.form['foodType']
        cleanliness = request.form['cleanliness']
        enclosureID = int(request.form['enclosureID'])

        for enclosure in zoo.getEnclosures():
            if(enclosure.getID() == enclosureID):
                enclosure.setFoodType(foodType)
                enclosure.setCleanliness(cleanliness)

        return redirect(url_for('enclosures'))

    def deleteEnclosure(self, enclosureID):
        zoo.removeEnclosure(enclosureID)
        return redirect(url_for('enclosures'))
