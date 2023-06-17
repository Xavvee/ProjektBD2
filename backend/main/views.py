import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .utils import MongoDB
from .models import Client, Employee, Game, Dish, Reservation
from bson.json_util import dumps
from bson import ObjectId
from datetime import datetime
import uuid


@csrf_exempt
def create_client(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data['userId'] = str(uuid.uuid4())  # auto-generate userId
        mongo_db = MongoDB()
        client = Client(**data)
        client_dict = client.__dict__
        result = mongo_db.insert_one('Clients', client_dict)
        return JsonResponse({"inserted_id": str(result)})
    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def create_game(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data['gameId'] = str(uuid.uuid4())  # auto-generate gameId
        mongo_db = MongoDB()
        game = Game(**data)
        game_dict = game.__dict__
        result = mongo_db.insert_one('Games', game_dict)
        return JsonResponse({"inserted_id": str(result)})
    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def add_table_to_game(request):
    if request.method == 'POST':
        # Create a MongoDB object
        mongo_db = MongoDB()

        # Parse JSON data from the request body
        data = json.loads(request.body)

        # Extract game name and table data from the request body
        game_id = data.get('gameId')
        capacity = data.get('capacity')

        # Call add_table method
        if game_id and capacity:
            mongo_db.add_table(game_id, capacity)
            return JsonResponse({'status': 'success'}, status=200)
        else:
            return JsonResponse({'status': 'failure', 'error': 'Missing game_name or table_data'}, status=400)
    else:
        return JsonResponse({'status': 'failure', 'error': 'Invalid request method'}, status=405)


@csrf_exempt
def create_employee(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data['employeeId'] = str(uuid.uuid4())  # auto-generate employeeId
        mongo_db = MongoDB()
        employee = Employee(**data)
        employee_dict = employee.__dict__
        result = mongo_db.insert_one('Employees', employee_dict)
        return JsonResponse({"inserted_id": str(result)})
    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def create_dish(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data['dishId'] = str(uuid.uuid4())  # auto-generate dishId
        dish = Dish(**data)
        dish_dict = dish.__dict__
        mongo_db = MongoDB()
        result = mongo_db.insert_one('Menu', dish_dict)
        return JsonResponse({"inserted_id": str(result)})
    else:
        return JsonResponse({"error": "Invalid method"})


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


@csrf_exempt
def find_client(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mongo_db = MongoDB()
        client_doc = mongo_db.find_one('Clients', {'userId': data['userId']})
        if client_doc:
            client = Client(client_doc)
            return JsonResponse(client.__dict__)
        else:
            return JsonResponse({"error": "Client not found"}, status=404)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)


@csrf_exempt
def delete_client(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mongo_db = MongoDB()
        result = mongo_db.delete_one('Clients', {'userId': data['userId']})
        return JsonResponse({"deleted_count": result.deleted_count})
    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def find_dish(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mongo_db = MongoDB()
        dish_doc = mongo_db.find_one('Menu', {'dishId': data['dishId']})
        if dish_doc:
            dish = Dish(dish_doc)
            return JsonResponse(dish.__dict__)
        else:
            return JsonResponse({"error": "Dish not found"}, status=404)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)


@csrf_exempt
def delete_dish(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mongo_db = MongoDB()
        result = mongo_db.delete_one('Menu', {'dishId': data['dishId']})
        return JsonResponse({"deleted_count": result.deleted_count})
    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def find_game(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mongo_db = MongoDB()
        game_doc = mongo_db.find_one('Games', {'gameId': data['gameId']})

        if game_doc:
            game = Game(game_doc)
            return JsonResponse(game.__dict__)
        else:
            return JsonResponse({"error": "Game not found"}, status=404)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)


@csrf_exempt
def delete_game(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mongo_db = MongoDB()
        result = mongo_db.delete_one('Games', {'gameId': data['gameId']})
        return JsonResponse({"deleted_count": result.deleted_count})
    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def find_employee(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mongo_db = MongoDB()
        employee_doc = mongo_db.find_one('Employees', {'employeeId': data['employeeId']})

        if employee_doc:
            employee = Employee(employee_doc)
            return JsonResponse(employee.__dict__)
        else:
            return JsonResponse({"error": "Employee not found"}, status=404)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)


@csrf_exempt
def delete_employee(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mongo_db = MongoDB()
        result = mongo_db.delete_one('Employees', {'employeeId': data['employeeId']})
        return JsonResponse({"deleted_count": result.deleted_count})
    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def update_client(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mongo_db = MongoDB()
        client_id = data.pop('userId')
        result = mongo_db.update_one('Clients', {'userId': client_id}, data)
        return JsonResponse({"modified_count": result.modified_count})
    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def update_game(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mongo_db = MongoDB()
        game_id = data.pop('gameId')
        result = mongo_db.update_one('Games', {'gameId': game_id}, data)
        return JsonResponse({"modified_count": result.modified_count})
    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def update_employee(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mongo_db = MongoDB()
        employee_id = data.pop('employeeId')
        result = mongo_db.update_one('Employees', {'employeeId': employee_id}, data)
        return JsonResponse({"modified_count": result.modified_count})
    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def update_dish(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mongo_db = MongoDB()
        dish_id = data.pop('dishId')
        result = mongo_db.update_one('Menu', {'dishId': dish_id}, data)
        return JsonResponse({"modified_count": result.modified_count})
    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def find_all_clients(request):
    if request.method == 'GET':
        mongo_db = MongoDB()
        clients = mongo_db.find_all('Clients')
        return JsonResponse({"clients": json.loads(dumps(clients))})
    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def find_all_games(request):
    if request.method == 'GET':
        mongo_db = MongoDB()
        games = mongo_db.find_all('Games')
        return JsonResponse({"games": json.loads(dumps(games))})
    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def find_all_employees(request):
    if request.method == 'GET':
        mongo_db = MongoDB()
        employees = mongo_db.find_all('Employees')
        return JsonResponse({"employees": json.loads(dumps(employees))})
    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def find_all_dishes(request):
    if request.method == 'GET':
        mongo_db = MongoDB()
        dishes = mongo_db.find_all('Menu')
        return JsonResponse({"dishes": json.loads(dumps(dishes))})
    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def create_reservation(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # create a new MongoDB connection
        mongo_db = MongoDB()

        # retrieve the client and game using their respective IDs
        client = mongo_db.find_one('Clients', {'userId': data['userId']})
        game = mongo_db.find_one('Games', {'gameId': data['gameId']})

        if client is None or game is None:
            return JsonResponse({"error": "Client or game not found"})

        # convert string dates into datetime objects
        start_date = datetime.strptime(data['startDate'], '%Y-%m-%dT%H:%M:%S.%f%z')
        end_date = datetime.strptime(data['endDate'], '%Y-%m-%dT%H:%M:%S.%f%z')
        order_date = datetime.now()
        final_price, dish_list = get_price_and_dishes(data['dishes'], mongo_db)

        # create a minimal game object with only required fields
        minimal_game = {
            'gameId': game['gameId'],
            'gameType': game['gameType'],
            'pricePerHour': game['pricePerHour'],
            'tables': [{'tableId': table['tableId']} for table in game['tables'] if table['tableId'] in data['tables']]
        }

        # create a new reservation
        reservation = Reservation(reservationId=str(uuid.uuid4()), reservationStatus='Pending',
                                  peopleCount=data['peopleCount'], startDate=start_date, endDate=end_date,
                                  orderDate=order_date, games=[minimal_game], orders=[
                {'orderId': str(uuid.uuid4()), 'dishes': dish_list, 'finalPrice': final_price}])

        reservation_dict = reservation.__dict__

        # add the new reservation to the client's reservations
        client['reservations'].append(reservation_dict)
        mongo_db.update_one('Clients', {'userId': data['userId']}, {'reservations': client['reservations']})

        # add the new reservation to the game's tables
        for table in game['tables']:
            if table['tableId'] in data['tables']:
                table['reservedDates'].append({'startDate': start_date, 'endDate': end_date})
                mongo_db.update_one('Games', {'gameId': data['gameId']}, {'tables': game['tables']})

        return JsonResponse({'status': 'success'}, status=200)
    else:
        return JsonResponse({"error": "Invalid method"})


def get_price_and_dishes(dishes, mongo_db):
    total_price = 0.0
    dish_list = []
    for dishId in dishes:
        # find the dish in the Menu collection
        dish = mongo_db.find_one('Menu', {'dishId': dishId})
        dish_list.append(dish)

        if dish is not None:
            # add the dish price to the total price
            total_price += float(dish['dishPrice'])

    # return the total price as a string
    return str(total_price), dish_list


@csrf_exempt
def update_reservation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mongo_db = MongoDB()
        client = mongo_db.find_one('Clients', {'userId': data['userId']})
        if client is None:
            return JsonResponse({"error": "Client not found"})

        for reservation in client['reservations']:
            if reservation['reservationId'] == data['reservationId']:
                if 'reservationStatus' in data:
                    reservation['reservationStatus'] = data['reservationStatus']
                    if data['reservationStatus'] == 'Canceled':
                        handle_cancellation(reservation)
                if 'peopleCount' in data:
                    reservation['peopleCount'] = data['peopleCount']
                if 'startDate' in data:
                    reservation['startDate'] = datetime.strptime(data['startDate'], '%Y-%m-%dT%H:%M:%S.%f%z')
                if 'endDate' in data:
                    reservation['endDate'] = datetime.strptime(data['endDate'], '%Y-%m-%dT%H:%M:%S.%f%z')
                if 'dishes' in data:
                    reservation['orders'][0]['dishes'] = data['dishes']
                    reservation['orders'][0]['finalPrice'] = get_price_from_dishes(data['dishes'], mongo_db)
                if 'gameId' in data:
                    new_game = mongo_db.find_one('Games', {'gameId': data['gameId']})
                    if new_game is not None:
                        reservation['games'] = [new_game]
                    else:
                        return JsonResponse({"error": "Game not found"})

                break

        mongo_db.update_one('Clients', {'userId': data['userId']}, {'reservations': client['reservations']})
        return JsonResponse({"message": "Reservation updated"})
    else:
        return JsonResponse({"error": "Invalid method"})


def handle_cancellation(reservation):
    mongo_db = MongoDB()
    start_date = reservation['startDate']
    end_date = reservation['endDate']
    for game in reservation['games']:
        game_document = mongo_db.find_one('Games', {'gameId': game['gameId']})
        for table in game_document['tables']:
            table['reservedDates'] = [date for date in table['reservedDates'] if
                                      date['startDate'] != start_date and date['endDate'] != end_date]
        mongo_db.update_one('Games', {'gameId': game['gameId']}, {'tables': game_document['tables']})

    return JsonResponse({"message": "Reserved dates removed"})


@csrf_exempt
def filter_menu_by_dish_type(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        dish_type = data.get('dishType')

        if dish_type:
            # create a new MongoDB connection
            mongo_db = MongoDB()

            # Query the dishes from the MongoDB Menu collection
            dishes = mongo_db.find_all('Menu', {'dishType': dish_type})

            return JsonResponse({"dishes": json.loads(dumps(dishes))})
        else:
            return JsonResponse({"error": "No dishType provided"}, status=400)
    else:
        return JsonResponse({"error": "Invalid method"}, status=400)
