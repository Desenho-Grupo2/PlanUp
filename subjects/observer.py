from abc import ABC, abstractmethod
from . import models

class ObserverSubject():

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def attach(self, observer):
        assert isinstance(observer, Observer)

    @abstractmethod
    def update(self):
        pass

class Observer():

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def update(self, subject):
        pass

class SubjectConcreteObserver(Observer):

    def __init__(self):
        self.dangerous_subjects = set()

    def update(self, subject):
        self.dangerous_subjects.add(subject)
