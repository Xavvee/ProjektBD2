# Dokumentacja
Celem projektu było zrealizowanie aplikacji umożliwiającej dokonywanie rezerwacji oraz zarządzanie salonem gier z funkcjonalnościami pubu.

## Schemat bazy danych
Na bazę składają się 4 kolekcje.

- Clients
  ``` javascript 
  {
    "userId": 1,
    "firstName": "Jan",
    "lastName": "Kowalski",
    "dateOfBirth": "1990-01-01",
    "email": "jan.kowalski@example.com",
    "phone": "123456789",
    "address": "ul. Przykładowa 1, 00-001 Warszawa",
    "registerDate": "2024-01-01",
    "reservations": [
      {
        "reservationId": 1,
        "reservationStatus": "confirmed",
        "peopleCount": 4,
        "startDate": "2024-01-02",
        "endDate": "2024-01-03",
        "games": [
          {
            "gameId": 1,
            "gameType": "Pool",
            "capacity": 4,
            "pricePerHour": "10.00",
            "tables": [
              {
                "tableId": 1,
                "capacity": 2
              }
            ]
          }
        ],
        "orders": [
          {
            "orderId": 1,
            "dishes": [1, 2, 3],
            "orderDate": "2024-01-02",
            "finalPrice": "25.00"
          }
        ]
      }
    ]
  }
  ```
- Games
  ``` javascript
  {
    "_id": {
      "$oid": "648c4fe533baa7342d60cfab"
    },
    "gameId": "a831e76b-5f4f-4a36-bdbd-9ffbc47d9732",
    "gameType": "Bowling",
    "capacity": 20,
    "pricePerHour": "20",
    "tables": [
      {
        "tableId": "1",
        "capacity": 5,
        "reservedDates": [
          {
            "startDate": {
              "$date": "2023-02-01T17:00:00Z"
            },
            "endDate": {
              "$date": "2023-02-01T20:00:00Z"
            }
          }
        ]
      },
      {
        "tableId": "2",
        "capacity": 5
      },
      {
        "tableId": "3",
        "capacity": 5
      },
      {
        "tableId": "4",
        "capacity": 5
      }
    ]
  }
  ```
- Employees
  ``` javascript
  {
    "_id": {
      "$oid": "648c511b33baa7342d60cfb6"
    },
    "employeeId": "2b57c003-5e4a-478b-a14a-b5c03a8f72ff",
    "employeeType": "Waiter",
    "firstName": "Bob",
    "lastName": "Johnson",
    "dateOfBirth": "1987-02-02",
    "email": "bob.johnson@example.com",
    "phone": "4444444444",
    "registerDate": "2023-01-01"
  }
  ```
- Menu
  ``` javascript
  {
  "_id": {
    "$oid": "648c508933baa7342d60cfaf"
  },
  "dishId": "8b231755-8c29-4e3d-94c5-67c8c56b049c",
  "dishType": "Appetizer",
  "description": "Chicken Wings",
  "dishPrice": "10"
  }
  ```