import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .utils import MongoDB
from .models import Client, Employee, Game, Dish, Reservation
from bson.json_util import dumps
from bson import ObjectId
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
        game_dict = game.__dict__Games
        result = mongo_db.insert_one('', game_dict)
        return JsonResponse({"inserted_id": str(result)})
    else:
        return JsonResponse({"error": "Invalid method"})


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
        client_id = ObjectId(data['_id'])
        client = mongo_db.find_one('Clients', {'_id': client_id})
        client_json = JSONEncoder().encode(client)
        return JsonResponse(client_json, safe=False)
    else:
        return JsonResponse({"error": "Invalid method"})


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
        dish = mongo_db.find_one('Menu', {'dishId': data['dishId']})
        return JsonResponse(dish)
    else:
        return JsonResponse({"error": "Invalid method"})


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
        game = mongo_db.find_one('Games', {'gameId': data['gameId']})
        return JsonResponse(game)
    else:
        return JsonResponse({"error": "Invalid method"})


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
        employee = mongo_db.find_one('Employees', {'employeeId': data['employeeId']})
        return JsonResponse(employee)
    else:
        return JsonResponse({"error": "Invalid method"})


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
        data['reservationId'] = str(uuid.uuid4())  # auto-generate reservationId
        mongo_db = MongoDB()

        # ensure gameId exists
        game = mongo_db.find_one('Games', {'gameId': data['games'][0]['gameId']})
        if game is None:
            return JsonResponse({"error": "Game does not exist"})

        # ensure tableId exists within game
        table_exists = False
        for table in game['tables']:
            if table['tableId'] == data['games'][0]['tables'][0]['tableId']:
                table_exists = True
                break
        if not table_exists:
            return JsonResponse({"error": "Table does not exist in the provided game"})

        reservation = Reservation(**data)
        reservation_dict = reservation.__dict__

        # update the client's reservations
        client = mongo_db.find_one('Clients', {'userId': data['userId']})
        if client is not None:
            if 'reservations' in client:
                client['reservations'].append(reservation_dict)
            else:
                client['reservations'] = [reservation_dict]
            mongo_db.update_one('Clients', {'userId': data['userId']}, client)

        return JsonResponse({"message": "Reservation created successfully"})
    else:
        return JsonResponse({"error": "Invalid method"})

