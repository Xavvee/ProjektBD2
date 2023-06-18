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
- 