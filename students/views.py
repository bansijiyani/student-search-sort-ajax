from django.shortcuts import render
from .models import Student
from django.http import JsonResponse

def student_search(request):
    return render(request, 'students/search.html')

def search_results(request):
    query_type = request.GET.get('query_type')
    query = request.GET.get('query')

    if query_type == 'name':
        results = Student.objects.filter(name__icontains=query)
    elif query_type == 'nationality':
        results = Student.objects.filter(nationality__icontains=query)
    elif query_type == 'city':
        results = Student.objects.filter(city__icontains=query)
    else:
        results = Student.objects.none()

    data = list(results.values())
    return JsonResponse(data, safe=False)
