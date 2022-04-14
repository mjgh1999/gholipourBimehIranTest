from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from jalali_date import datetime2jalali, date2jalali

fee = 0.1


class User(AbstractUser):
    USER_CHOICES = (
        (0, 'admin'),
        (100, "branch1"),
        (101, "branch2"),
        (102, "branch3"),
    )
    username = models.CharField(max_length=100, null=True, blank=True, unique=True, verbose_name='نام کاربری')
    password = models.CharField(max_length=100, null=True, blank=True,verbose_name='رمز عبور')
    email = models.EmailField(null=True, blank=True)
    branch = models.SmallIntegerField(choices=USER_CHOICES, null=True, blank=True)

    class Meta:
        permissions = (("admin", "See every thing"),
                       ("user1", "See branch1 data"),
                       ("user2", "See branch2 data"),
                       ("user3", "See branch3 data"),
                       )


class Data(models.Model):
    BRANCH_CHOICES = (
        (100, "100"),
        (101, "101"),
        (102, "102"),
    )
    maxTransactionLimitChar = 20
    idNumber = models.PositiveBigIntegerField(verbose_name="شماره ملی")
    branchCode = models.PositiveSmallIntegerField(choices=BRANCH_CHOICES, verbose_name="شعبه")
    transactionValue = models.PositiveBigIntegerField(verbose_name="ارزش معامله")
    dateAndTime = models.DateTimeField(auto_now_add=True)

    def get_jalai_datatime(self):
        return datetime2jalali(self.dateAndTime)
