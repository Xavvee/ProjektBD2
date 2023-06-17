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
        self.registerDate = registerDate if registerDate else datetime.now().strftime("%Y-%m-%d")
        self.reservations = reservations

    def __init__(self, data):
        self._id = str(data.get('_id', ''))
        self.firstName = data.get('firstName', '')
        self.lastName = data.get('lastName', '')
        self.dateOfBirth = data.get('dateOfBirth', '')
        self.email = data.get('email', '')
        self.phone = data.get('phone', '')
        self.address = data.get('address', '')
        self.registerDate = data.get('registerDate', '')
        self.reservations = data.get('reservations', [])


class Employee:
    def __init__(self, employeeId, employeeType, firstName, lastName, dateOfBirth, email, phone, registerDate=None):
        self.employeeId = employeeId
        self.employeeType = employeeType
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.email = email
        self.phone = phone
        self.registerDate = registerDate if registerDate else datetime.now().strftime("%Y-%m-%d")

    def __init__(self, data):
        self._id = str(data.get('_id', ''))
        self.employeeType = data.get('employeeType', '')
        self.firstName = data.get('firstName', '')
        self.lastName = data.get('lastName', '')
        self.dateOfBirth = data.get('dateOfBirth', '')
        self.email = data.get('email', '')
        self.phone = data.get('phone', '')
        self.registerDate = data.get('registerDate', '')


class Game:
    def __init__(self, gameId, gameType, capacity, pricePerHour, tables=[]):
        self.gameId = gameId
        self.gameType = gameType
        self.capacity = capacity
        self.pricePerHour = pricePerHour
        self.tables = tables

    def __init__(self, data):
        self._id = str(data.get('_id', ''))
        self.gameType = data.get('gameType', '')
        self.capacity = data.get('capacity', '')
        self.pricePerHour = data.get('pricePerHour', '')
        self.tables = data.get('tables', [])


class Dish:
    def __init__(self, dishId, dishType, description, dishPrice):
        self.dishId = dishId
        self.dishType = dishType
        self.description = description
        self.dishPrice = dishPrice

    def __init__(self, data):
        self._id = str(data.get('_id', ''))
        self.dishType = data.get('dishType', '')
        self.description = data.get('description', '')
        self.dishPrice = data.get('dishPrice', '')


class Reservation:
    def __init__(self, reservationId, reservationStatus, peopleCount, startDate, endDate, orderDate, games, orders):
        self.reservationId = reservationId
        self.reservationStatus = reservationStatus
        self.peopleCount = peopleCount
        self.startDate = startDate
        self.endDate = endDate
        self.orderDate = orderDate
        self.games = games
        self.orders = orders
