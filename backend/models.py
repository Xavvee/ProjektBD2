from datetime import datetime


class Client:
    def __init__(self, userId, firstName, lastName, dateOfBirth, email, phone, address, registerDate=None,
                 reservations=[]):
        self.userId = userId
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.email = email
        self.phone = phone
        self.address = address
        self.registerDate = registerDate if registerDate else datetime.now()
        self.reservations = reservations


class Employee:
    def __init__(self, employeeId, employeeType, firstName, lastName, dateOfBirth, email, phone, registerDate=None):
        self.employeeId = employeeId
        self.employeeType = employeeType
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.email = email
        self.phone = phone
        self.registerDate = registerDate if registerDate else datetime.now()


class Game:
    def __init__(self, gameId, gameType, capacity, pricePerHour, tables=[]):
        self.gameId = gameId
        self.gameType = gameType
        self.capacity = capacity
        self.pricePerHour = pricePerHour
        self.tables = tables


class Dish:
    def __init__(self, dishId, dishType, description, dishPrice):
        self.dishId = dishId
        self.dishType = dishType
        self.description = description
        self.dishPrice = dishPrice
