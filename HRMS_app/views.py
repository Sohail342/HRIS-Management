from django.shortcuts import render
from .models import Employee
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

def employees_view(request):
    employees = Employee.objects.all().order_by('SAP_ID')
    search_query = request.GET.get('search', '')
    employee_type_filter = request.GET.get('employee_type', '')

    # Apply search filter
    if search_query:
        employees = employees.filter(SAP_ID__icontains=search_query)

    # Apply employee type filter
    if employee_type_filter:
        employees = employees.filter(employee_type=employee_type_filter)

    # Handle pagination
    paginator = Paginator(employees, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'employees': list(page_obj.object_list.values(
                'SAP_ID', 
                'full_name', 
                'husband_or_father_name', 
                'employee_type', 
                'designation', 
                'employee_grade', 
                'mobile_no', 
                'employee_email', 
                'date_of_last_promotion', 
                'date_current_posting', 
                'date_current_assignment', 
                'date_of_retirement'
            )),
            'total_count': paginator.count,
            'has_previous': page_obj.has_previous(),
            'has_next': page_obj.has_next(),
            'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None,
            'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
        }
        return JsonResponse(data)

    # Prepare context for rendering
    context = {
        "page_obj": page_obj,
        "search_query": search_query,
        "employee_type_filter": employee_type_filter,
    }

    return render(request, 'core/employee.html', context)





def index(request):
    employess = Employee.objects.count()
    return render(request, 'index.html', {'employess':employess})




def employee_detail_view(request, sap_id):
    employee = get_object_or_404(Employee, SAP_ID=sap_id)
    return render(request, 'HRMS_app/employee_details.html', {'employee': employee})
