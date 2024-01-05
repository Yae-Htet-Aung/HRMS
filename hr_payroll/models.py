from django.db import models
from django.utils import timezone
# from hr_employee import EmployeeModel
# Create your models here.

class PayrollModel(models.Model):
    payroll = models.CharField(max_length=10, unique=True, verbose_name='Payroll ID')
    # employee_id = models.models.ForeignKey(EmployeeModel, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True, null=True)
    bonus = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True, null=True)
    ot = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True, null=True)
    fine = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True, null=True)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True, null=True)
    remark = models.TextField()

    def __str__(self):
        return self.payroll
