from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class FunctionalGroup(models.Model):
    name = models.CharField(max_length=100)
    allias = models.CharField(max_length=100, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, to_field="name", related_name='functional_groups')

    def __str__(self):
        return f'{self.name} - {self.group.name}'


class Division(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True,default=None)
    functional_group = models.ForeignKey(FunctionalGroup, on_delete=models.CASCADE, related_name='divisions')

    def __str__(self):
        return self.name


class Wing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='wings', to_field='name')

    def __str__(self):
        return self.name



class Region(models.Model):
    name = models.CharField(max_length=100)
    region_category = models.CharField(max_length=100, blank=True, null=True)
    functional_group = models.ManyToManyField(FunctionalGroup, related_name='regions')

    def __str__(self):
        return self.name


class Branch(models.Model):
    branch_code = models.IntegerField()
    branch_name = models.CharField(max_length=100, unique=True)
    branch_Category = models.CharField(max_length=100, default=None)
    branch_address = models.TextField(blank=True, null=True)
    branch_region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='branches')

    def __str__(self):
        return self.branch_name


class Designation(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True, default="Null")

    def __str__(self):
        return self.title


class Cadre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class EmployeeType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class EmployeeGrade(models.Model):
    grade_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.grade_name


class Qualification(models.Model):
    QUALIFICATION_TYPE_CHOICES = [
        ('Professional', 'Professional'),
        ('Educational', 'Educational')
    ]
    name = models.CharField(max_length=300, unique=True)
    qualification_type = models.CharField(max_length=20, choices=QUALIFICATION_TYPE_CHOICES, blank=True, null=True, default="Educational")
    institution = models.CharField(max_length=100, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.name} ({self.qualification_type})"


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    cnic_no = models.CharField(max_length=13, unique=True)
    husband_or_father_name = models.CharField(max_length=100)
    SAP_ID = models.IntegerField(default=None, unique=True)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True, to_field='title')
    cadre = models.ForeignKey(Cadre, on_delete=models.SET_NULL, null=True)
    employee_type = models.ForeignKey(EmployeeType, on_delete=models.SET_NULL, null=True, to_field='name')
    employee_grade = models.ForeignKey(EmployeeGrade, on_delete=models.SET_NULL, null=True, to_field="grade_name")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, to_field="branch_name" , related_name='employees', null=True, blank=True)
    qualifications = models.ManyToManyField(Qualification, related_name='employees')
    date_of_last_promotion = models.DateField(max_length=15, default='1900')
    date_current_posting = models.DateField(max_length=15, default='1900')
    date_current_assignment = models.DateField(max_length=15, default='1900')
    mobile_no = models.CharField(max_length=15, null=True, blank=True, default='1111')
    phone_no_official = models.CharField(max_length=15, null=True, blank=True, default='1111')
    phone_no_emergency_contact = models.CharField(max_length=15, null=True, blank=True, default='1111')
    employee_email = models.EmailField(max_length=100, null=True, blank=True, default="aa@aa.aa")
    date_of_retirement = models.DateField(null=True, blank=True, default='1900')

    def __str__(self):
        return self.full_name 

