from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, login_required, logout_user
from app.forms import LoginForm
from app.models.Enclosure import Enclosure
from app import zoo

class EnclosureController:
    def addEnclosure(self):
        """Add an empty enclosure to the zoo

        Args:
            none
        Returns:
            werkzeug.wrappers.Response: Flask response object for redirecting user.

        """
        zoo.addEnclosure(Enclosure([], "", ""))
        return redirect(url_for('enclosures'))

    def editEnclosure(self):
        """Edits existing enclosure with a request's information

        Args:
            none. The Flask request object is implicitly passed however
        Returns:
            werkzeug.wrappers.Response: Flask response object for redirecting user.

        """
        foodType = request.form['foodType']
        cleanliness = request.form['cleanliness']
        enclosureID = int(request.form['enclosureID'])

        for enclosure in zoo.getEnclosures():
            if(enclosure.getID() == enclosureID):
                enclosure.setFoodType(foodType)
                enclosure.setCleanliness(cleanliness)

        return redirect(url_for('enclosures'))

    def deleteEnclosure(self, enclosureID):
        """Deletes existing enclosure specified by user

        Args:
            enclosureID (int): The ID of the enclosure to be deleted
        Returns:
            werkzeug.wrappers.Response: Flask response object for redirecting user.

        """
        zoo.removeEnclosure(enclosureID)
        return redirect(url_for('enclosures'))
