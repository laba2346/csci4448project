from ..models.Animal import *
from ..models.Zoo import *
from ..models.Employee import *
from ..models.Enclosure import *
from ..models.AnimalFactory import *
from ..models.SpeciesInfo import *
from ..models.EmployeeFactory import *
from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, login_required, logout_user
from app.forms import LoginForm
from app import zoo
import random
import json

class ZooController:
    def getZoo(self):
        return zoo

    def constructKeeperChart(self):
        data = {}
        datasets = []
        dataset = {}
        dataPoints = []
        labels = []
        colors = []
        for species in zoo.getSpeciesList():
            speciesName = species.getName()
            labels.append(speciesName)
            colors.append("#%06x" % random.randint(0, 0xFFFFFF))
            count = 0
            for enclosure in zoo.getEnclosures():
                for animal in enclosure.getAnimals():
                    if(animal.getSpeciesInfo().getName() == speciesName):
                        count += 1
            dataPoints.append(count)
        dataset['label'] = 'Animals'
        dataset['backgroundColor'] = colors
        dataset['data'] = dataPoints
        datasets.append(dataset)
        data['labels'] = labels
        data['datasets'] = datasets

        return data

    def constructVetChart(self):
        data = {}
        datasets = []
        dataset = {}
        dataPoints = [0,0]
        labels = ["Healthy","Unhealthy"]
        colors = ['#00ff00', '#ff0000']
        for enclosure in zoo.getEnclosures():
            for animal in enclosure.getAnimals():
                if(animal.getHealthy()):
                    dataPoints[0] += 1
                else:
                    dataPoints[1] += 1
        dataset['label'] = 'Animal health'
        dataset['backgroundColor'] = colors
        dataset['data'] = dataPoints
        datasets.append(dataset)
        data['labels'] = labels
        data['datasets'] = datasets

        return data
