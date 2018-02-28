import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from controller import Controller
controller = Controller("","")
controller.authorize_client('client_secret.json')

@csrf_exempt
def get_accounts(request):
    sheet_id = str(request.GET['sheet_id'])
    sheet_name = str(request.GET['sheet_name'])
    # print controller.getSheet(sheet_id, sheet_name)
    return JsonResponse(controller.getSheet(sheet_id, sheet_name))

@csrf_exempt
def put_account(request):
    sheet_id =str(request.GET['sheet_id'])
    sheet_name = str(request.GET['sheet_name'])
    # sheet_name = str(json.loads(request.body)['sheet_name'])
    accounts = json.loads(request.body)
    controller.postSheet(sheet_id, sheet_name, accounts)
    # print
    return JsonResponse({'update': 'success'})