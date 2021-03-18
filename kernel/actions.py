from abc import ABCMeta

class Action(metaclass=ABCMeta):
    pass

class Move(Action):
    def __init__(self,speed):
        self.speed = speed

class Turn(Action):
    def __init__(self,speed):
        self.speed = speed
