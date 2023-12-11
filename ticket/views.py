from django.shortcuts import render

# Create your views here.
@csrf_exempt
def create(request):
    if request.method == 'POST':
        return JsonResponse({'errno': 0, 'msg': "Create Success"})
    else:
        return JsonResponse({'errno': 2, 'msg': "Wrong Request"})
