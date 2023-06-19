import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .utils import MongoDB
from .models import Client, Employee, Game, Dish, Reservation
from bson.json_util import dumps
from bson import ObjectId
from datetime import datetime
import uuid
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


@csrf_exempt
def create_client(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data['userId'] = str(uuid.uuid4())  # auto-generate userId
        mongo_db = MongoDB()
        client = Client.from_dict(data)
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
        if isinstance(o, datetime):
            return o.isoformat()
        return super().default(o)


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
        return JsonResponse({"dishes": json.loads(dumps(dishes))}, safe=False)
    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def create_reservation(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # create a new MongoDB connection
        mongo_db = MongoDB()

        # retrieve the client and game using their respective IDs
        client = mongo_db.find_one('Clients', {'email': data['email']})
        game = mongo_db.find_one('Games', {'gameId': data['gameId']})

        if client is None or game is None:
            return JsonResponse({"error": "Client or game not found"})

        # convert string dates into datetime objects
        start_date = datetime.strptime(data['startDate'], '%Y-%m-%dT%H:%M:%SZ')
        end_date = datetime.strptime(data['endDate'], '%Y-%m-%dT%H:%M:%SZ')
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
        mongo_db.update_one('Clients', {'email': data['email']}, {'reservations': client['reservations']})

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
        client = mongo_db.find_one('Clients', {'email': data['email']})
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
                    reservation['orders'][0]['finalPrice'], reservation['orders'][0]['dishes'] = get_price_and_dishes(
                        data['dishes'], mongo_db)
                if 'gameId' in data:
                    new_game = mongo_db.find_one('Games', {'gameId': data['gameId']})
                    if new_game is not None:
                        reservation['games'] = [new_game]
                    else:
                        return JsonResponse({"error": "Game not found"})

                break

        mongo_db.update_one('Clients', {'email': data['email']}, {'reservations': client['reservations']})
        return JsonResponse({"message": "Reservation updated"})
    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def find_client_reservations(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mongo_db = MongoDB()
        client_doc = mongo_db.find_one('Clients', {'userId': data['userId']})
        if client_doc:
            reservations = client_doc.get('reservations', [])
            return JsonResponse(reservations, safe=False)
        else:
            return JsonResponse({"error": "Client not found"}, status=404)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)


@csrf_exempt
def find_future_client_reservations(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mongo_db = MongoDB()
        client_doc = mongo_db.find_one('Clients', {'userId': data['userId']})
        if client_doc:
            current_date = datetime.datetime.now()
            reservations = client_doc.get('reservations', [])
            future_reservations = [reservation for reservation in reservations if
                                   reservation['startDate'] > current_date]
            return JsonResponse(future_reservations, safe=False)
        else:
            return JsonResponse({"error": "Client not found"}, status=404)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)


@csrf_exempt
def find_past_client_reservations(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mongo_db = MongoDB()
        client_doc = mongo_db.find_one('Clients', {'userId': data['userId']})
        if client_doc:
            current_date = datetime.datetime.now()
            reservations = client_doc.get('reservations', [])
            past_reservations = [reservation for reservation in reservations if reservation['startDate'] < current_date]
            return JsonResponse(past_reservations, safe=False)
        else:
            return JsonResponse({"error": "Client not found"}, status=404)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)


@csrf_exempt
def find_reservation_by_param(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mongo_db = MongoDB()

        search_param = {}
        if 'userId' in data:
            search_param = {'userId': data['userId']}
        elif 'email' in data:
            search_param = {'email': data['email']}

        if not search_param:
            return JsonResponse({"error": "Missing search parameter (userId or email)"}, status=400)

        client_doc = mongo_db.find_one('Clients', search_param)

        if client_doc:
            reservations = client_doc.get('reservations', [])
            if data.get('reservationId'):
                reservations = [reservation for reservation in reservations if
                                    reservation['reservationId'] == data.get('reservationId')]
            reservations = json.dumps(reservations, cls=JSONEncoder)
            return HttpResponse(reservations, content_type='application/json')
        else:
            return JsonResponse({"error": "Client not found"}, status=404)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)


def find_tables_for_game(gameId):
    mongo_db = MongoDB()
    tables = mongo_db.find_one('Games', {'gameId': gameId})['tables']
    return tables;


@csrf_exempt
def check_if_free_date(request):
    if request.method == 'GET':
        date_format = '%Y-%m-%dT%H:%M:%SZ'
        gameId = request.GET.get('gameId')
        startDate = datetime.strptime(request.GET.get('startDate'), date_format)
        endDate = datetime.strptime(request.GET.get('endDate'), date_format)
        # data = json.loads(request.body)
        # startDate = datetime.strptime(data.pop('startDate'), date_format)
        # endDate = datetime.strptime(data.pop('endDate'), date_format)
        # gameId = data.pop('gameId')
        tables = find_tables_for_game(gameId)
        for table in tables:
            if table['reservedDates'] != []:
                for dates in table['reservedDates']:
                    if not (dates['startDate'] >= endDate or dates['endDate'] <= startDate):
                        return JsonResponse({"response": False})
        return JsonResponse({"response": True})
    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def display_tables_for_game(request):
    if request.method == 'GET':
        # data = json.loads(request.body)
        # gameId = data.pop('gameId')
        gameId = request.GET.get('gameId')
        tables = find_tables_for_game(gameId)
        return JsonResponse({"games": json.loads(dumps(tables))})
    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def show_clients_ordered_dishes(request):
    if request.method == 'GET':
        mongo_db = MongoDB()
        data = json.loads(request.body)
        user_Id = data.pop('userId')
        dishes = mongo_db.find_one('Clients', {'userId': user_Id})['reservations'][0]['orders'][0]['dishes']
        return JsonResponse({"dishes": json.loads(dumps(dishes))})
    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def calculate_recipe(request):
    if request.method == 'POST':
        mongo_db = MongoDB()
        data = json.loads(request.body)
        user_Id = data.pop('userId')
        reservations = mongo_db.find_one('Clients', {'userId': user_Id})['reservations']
        if reservations == []:
            return JsonResponse({"error": "Client has no reservations."})
        startDate = reservations[0]['startDate']
        endDate = reservations[0]['endDate']
        time = endDate - startDate
        hours = time.total_seconds() / 3600
        total_price = 0
        for game in reservations[0]['games']:
            total_price += float(game['pricePerHour']) * hours
        total_price += float(reservations[0]['orders'][0]['finalPrice'])
        return JsonResponse({"total_price": json.loads(dumps(total_price))})
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
            mongo_db = MongoDB()
            dishes = mongo_db.find_all('Menu', {'dishType': dish_type})

            return JsonResponse({"dishes": json.loads(dumps(dishes))})
        else:
            return JsonResponse({"error": "No dishType provided"}, status=400)
    else:
        return JsonResponse({"error": "Invalid method"}, status=400)


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = authenticate(request, username=data.get('email'), password=data.get('password'))
        if user is not None:
            login(request, user)
            return JsonResponse({'user_id': user.id, 'email': user.email})
        else:
            return JsonResponse({'error': 'Invalid login credentials'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=400)


@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.create_user(username=data.get('email'), password=data.get('password'))
        user.save()
        return JsonResponse({'user_id': user.id, 'email': user.email})
    else:
        return JsonResponse({'error': 'Invalid method'}, status=400)


def get_roles_view(request, userId):
    # if request.method == 'GET':
    #     try:
    #         # user = User.objects.get(pk=userId)
    #         # roles = Roles.objects.get(user=user)
    #         # return JsonResponse({'roles': roles.roles})
    #     except User.DoesNotExist:
    #         return JsonResponse({'error': 'User does not exist'}, status=400)
    # else:
    return JsonResponse({'error': 'Invalid method'}, status=400)
