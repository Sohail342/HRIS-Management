from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import (
    Designation, 
    Employee, 
    EmployeeType, 
    Cadre, 
    EmployeeGrade, 
    Branch, 
    Qualification,
)

def employees_view(request):
    employees = Employee.objects.all().order_by('SAP_ID')
    search_query = request.GET.get('search', '')
    employee_type_filter = request.GET.get('employee_type', '')
    designation_filter = request.GET.get('designation', '')
    cadre_filter = request.GET.get('cadre', '')
    employeeGrade_filter = request.GET.get('employeeGrade', '')
    branch_filter = request.GET.get('branch', '')
    qualification_filter = request.GET.get('qualification', '')

     # Apply branch filter
    if branch_filter:
        employees = employees.filter(branch__branch_name=branch_filter)

     # Apply qualification filter
    if qualification_filter:
        employees = employees.filter(qualifications__name=qualification_filter)

    # Apply search filter
    if search_query:
        employees = employees.filter(SAP_ID__icontains=search_query)

    # Apply employee type filter
    if employee_type_filter:
        employees = employees.filter(employee_type=employee_type_filter)

    # Apply cadre filter
    if cadre_filter:
        employees = employees.filter(cadre__name=cadre_filter)

    # Apply designation filter
    if designation_filter:
        employees = employees.filter(designation__title=designation_filter)

    if employeeGrade_filter:
        employees = employees.filter(employee_grade__grade_name=employeeGrade_filter)

    employee_types = EmployeeType.objects.all()
    designations = Designation.objects.all()
    cadre = Cadre.objects.all()
    employeeGrade = EmployeeGrade.objects.all()
    branch = Branch.objects.all()
    qualification = Qualification.objects.all()


    # Handle pagination
    paginator = Paginator(employees, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'employees': [
                {
                    'SAP_ID': emp.SAP_ID,
                    'full_name': emp.full_name,
                    'husband_or_father_name': emp.husband_or_father_name,
                    'employee_type': emp.employee_type.name if emp.employee_type else None,
                    'designation': emp.designation.title if emp.designation else None,
                    'cadre': emp.cadre.name if emp.cadre else None,
                    'employee_grade': emp.employee_grade.grade_name if emp.employee_grade else None,
                    'branch': emp.branch.branch_name if emp.branch else None,
                    'qualifications': [qual.name for qual in emp.qualifications.all()],
                    'mobile_no': emp.mobile_no,
                    'phone_no_official': emp.phone_no_official,
                    'phone_no_emergency_contact': emp.phone_no_emergency_contact,
                    'employee_email': emp.employee_email,
                    'date_of_last_promotion': emp.date_of_last_promotion,
                    'date_current_posting': emp.date_current_posting,
                    'date_current_assignment': emp.date_current_assignment,
                    'date_of_retirement': emp.date_of_retirement,
                }
                for emp in page_obj.object_list
            ],
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
        "designation_filter": designation_filter,
        "employee_types": employee_types,
        "designations": designations, 
        'cadre':cadre,
        'employeeGrade':employeeGrade,
        'branchs':branch,
        'qualifications':qualification
    }

    return render(request, 'core/employee.html', context)




def index(request):
    employess = Employee.objects.count()
    return render(request, 'index.html', {'employess':employess})




def employee_detail_view(request, sap_id):
    employee = get_object_or_404(Employee, SAP_ID=sap_id)
    return render(request, 'core/employee_details.html', {'employee': employee})
