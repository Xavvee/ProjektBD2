import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .utils import MongoDB
from .models import Client, Employee, Game, Dish


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
