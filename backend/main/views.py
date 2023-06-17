import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .utils import MongoDB
from .models import Client, Employee, Game, Dish
from bson.json_util import dumps


@csrf_exempt
def create_client(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mongo_db = MongoDB()
        client = Client(data['userId'], data['firstName'], data['lastName'],
                        data['dateOfBirth'], data['email'], data['phone'],
                        data['address'])
        client_dict = client.__dict__
        result = mongo_db.insert_one('Clients', client_dict)
        return JsonResponse({"inserted_id": str(result)})

    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def create_game(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mongo_db = MongoDB()
        game = Game(**data)
        game_dict = game.__dict__
        result = mongo_db.insert_one('Games', game_dict)
        return JsonResponse({"inserted_id": str(result)})
    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def create_employee(request):
    if request.method == 'POST':
        data = json.loads(request.body)
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
        dish = Dish(data['dishId'], data['dishType'], data['description'], data['dishPrice'])
        dish_dict = dish.__dict__
        mongo_db = MongoDB()
        result = mongo_db.insert_one('Menu', dish_dict)
        return JsonResponse({"inserted_id": str(result)})
    else:
        return JsonResponse({"error": "Invalid method"})


@csrf_exempt
def find_client(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mongo_db = MongoDB()
        client = mongo_db.find_one('Clients', {'userId': data['userId']})
        return JsonResponse(client)
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
