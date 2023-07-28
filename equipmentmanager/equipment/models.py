from django.db import models
from django_extensions.db.models import TimeStampedModel

from django.utils.timezone import timezone

from autoslug import AutoSlugField


class Equipment(TimeStampedModel):

    class InstrumentType():
        NAGADO = "Nagado"
        SHIME  = "Shime"
        OKEDO  = "Okedo"
        HIRA   = "Hira"
        UCHIWA = "Uchiwa daiko"
        CHAPPA = "Chappa"
        KANE   = "Atarigane (kane)"
        FUE    = "Fue"
        
    class StandType():
        NAGADO = "Nagado"
        TACHI  = "Shime (tachi)"
        SUWARI = "Shime (suwari)"
        OKEDO  = "Okedo"
        HIRA   = "Hira"
        NANAME = "Naname"

    class InstrumentSize():
        ONEFOUR = "1.4"
        ONEFIVE = "1.5"
        ONESIX  = "1.6"
        
    INSTRUMENT_CHOICES = [
        (InstrumentType.NAGADO, InstrumentType.NAGADO),
        (InstrumentType.SHIME, InstrumentType.SHIME),
        (InstrumentType.OKEDO, InstrumentType.OKEDO),
        (InstrumentType.HIRA, InstrumentType.HIRA),
        (InstrumentType.UCHIWA, InstrumentType.UCHIWA), 
        (InstrumentType.CHAPPA, InstrumentType.CHAPPA),
        (InstrumentType.KANE, InstrumentType.KANE),
        (InstrumentType.FUE, InstrumentType.FUE)
    ]

    STAND_CHOICES = [
        StandType.NAGADO,
        StandType.TACHI, 
        StandType.SUWARI,
        StandType.OKEDO,
        StandType.HIRA, 
        StandType.NANAME
    ]

    SIZE_CHOICES = [
        (InstrumentSize.ONEFOUR, InstrumentSize.ONEFOUR),
        (InstrumentSize.ONEFIVE, InstrumentSize.ONEFIVE),
        (InstrumentSize.ONESIX, InstrumentSize.ONESIX)
    ]

    instrument_type = models.CharField(max_length=50, choices=INSTRUMENT_CHOICES, null=False, blank=False)

    number = models.IntegerField(unique=True, null=True, blank=True)
    size   = models.CharField(max_length=20, choices=SIZE_CHOICES, null=True, blank=True)

    stand    = models.ForeignKey('Equipment', null=True, blank=True, on_delete=models.CASCADE)
    owner    = models.ForeignKey('Member', null=True, blank=True, related_name="owner", on_delete=models.CASCADE)
    location = models.ForeignKey('Member', null=True, blank=True, related_name="location", on_delete=models.CASCADE)

    def __str__(self):
        return '{0} {1} #{2}'.format(self.instrument_type, self.size, self.number)

class Member(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name
    
class Group(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name

class GroupMember(models.Model):
    member = models.ForeignKey('Member', null=False, blank=False, on_delete=models.CASCADE)
    group = models.ForeignKey('Group', null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} ({1})'.format(self.member.name, self.group.name)

class Performance(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    date = models.DateTimeField(blank=True, null=True)
    slug = AutoSlugField("Performance URL", unique=True, always_update=False, populate_from="name")

    def __str__(self):
        return self.name
    
class PerformanceEquipment():
    equipment_item = models.ForeignKey('Equipment', null=False, blank=False, on_delete=models.CASCADE)
    performance = models.ForeignKey('Performance', null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} ({1})'.format(self.equipment_item.to_string(), self.performance.name)