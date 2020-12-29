from enum import Enum

from django.db import models


class InitiativeStatus(Enum):
    """Enum for Initiative status field"""

    APPROVED = 'APPROVED'
    DECLINED = 'DECLINED'

    @classmethod
    def choices(cls):
        """Enum choices"""
        return tuple((i.name, i.value) for i in cls)


class Config(models.Model):
    """Config model"""

    required_signature_amount = models.IntegerField('Required signature amount for submission',
                                                    default=10)
    resubmission_attempts = models.IntegerField(
        'Permitted amount of initiative resubmission attempts', default=3)
    petition_longevity = models.IntegerField('Amount of days petition can last', default=2)


class Initiative(models.Model):
    """Initiative model"""

    initiator = models.ForeignKey('Initiator', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    edition = models.IntegerField(default=1)
    status = models.CharField(choices=InitiativeStatus.choices(), max_length=100)


class Initiator(models.Model):
    """Initiator model"""

    name = models.CharField(max_length=200)
    surnname = models.CharField(max_length=200)


class Committee(models.Model):
    """Committee model"""

    name = models.CharField(max_length=200)
    surnname = models.CharField(max_length=200)


class Petition(models.Model):
    """Petition model"""
    initiative = models.ForeignKey('Initiative', on_delete=models.CASCADE)
    date_created = models.DateTimeField('Date petition created')
    date_closed = models.DateTimeField('Date petition closed')

    def signature_count(self):
        """Return signatures count for petition"""
        return self.petitionsignature_set.count()

    def is_closed(self):
        """Return is petition was closed"""
        return self.date_closed is not None


class PetitionSignature(models.Model):
    """Petition Signature model"""
    petition = models.ForeignKey('Petition', on_delete=models.CASCADE)
    citizen_code = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
