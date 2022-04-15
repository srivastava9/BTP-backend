from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class IndustryChoices(models.TextChoices):
    """Industry Choices."""

    FOOD = "FOOD", _("Agriculture industry")
    AUTOMOBILE = "AUTOMOBILE", _("Automobile Industry")
    AI = "AI", _("Aerospace Industry")
    TI = "TI", _("Transport Industry")
    CI = "CI", _("IT Industry")
    EI = "EI", _("Electronics Industry")
    COI = "COI", _("Construction Industry")
    TLI = "TLI", _("Telecommunication industry")


class Factory(models.Model):
    """Industry Model."""

    name = models.CharField(
        _("Name Of Factory/Shop or Enterprise"), max_length=128, null=False
    )
    user = models.ForeignKey(
        to=User,
        verbose_name=_("Managed by User"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    type = models.CharField(
        _("Type of Indsutry"), max_length=128, choices=IndustryChoices.choices
    )
    address = models.TextField(_("Address of Factory"))
    no_workers = models.IntegerField(_("Number of Workers"), default=0)

    def __str__(self):
        return self.name

    class Meta:
        """Meta Class."""

        verbose_name = "Enterprise/Factory"
        verbose_name_plural = "Enterprises/Factories"


class Products(models.Model):
    name = models.CharField(_("Product to be manufactured/sold"), max_length=128)
    factory = models.ForeignKey(to=Factory, on_delete=models.CASCADE)

    def __str__(self) -> str:

        return self.name


class Employee(models.Model):

    name = models.CharField(_("Name Of Employee"), max_length=128)
    foctory = models.ForeignKey(
        to=Factory, verbose_name="Factory name", on_delete=models.CASCADE
    )
    employee_salary = models.IntegerField(
        _("Enter Salary of Employee(in Rs) per Month"), default=1000
    )
    designation = models.CharField(
        _("Designation of Employees(like manager, accountant etc."), max_length=128
    )
    profile_photo = models.ImageField(_("Image of Employee"), null=True, blank=True)

    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")

    def __str__(self):
        return self.name


class Inventory(models.Model):
    """Inventory Model"""

    name = models.CharField(
        _("Name of Inventory"), max_length=64, null=True, blank=True
    )
    address = models.CharField(_("Address of Inventory"), max_length=128)
    factory = models.ForeignKey(
        to=Factory, verbose_name=_("Enterprise/Factory"), on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Inventories"


class ProductInventory(models.Model):
    product = models.ForeignKey(
        to=Products, on_delete=models.CASCADE, verbose_name="Product Name"
    )
    max_lot_size = models.IntegerField(
        verbose_name="Maximum Volume/Lot size of Product", default=0
    )
    inventory = models.ForeignKey(to=Inventory, on_delete=models.CASCADE)
