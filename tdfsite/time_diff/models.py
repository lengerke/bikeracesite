from django.db import models
from datetime import datetime

class TimeEntry(models.Model):
    user_name = models.CharField(max_length=100, default="Anonymous")  # Field to store the user's name
    user_time = models.TimeField(default=datetime.now)  # Field to store the user's entered time
    time_difference = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)  # Field to store the calculated time difference (in minutes?)
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp when the entry is created

    def __str__(self):
        return f"Name: {self.user_name}, User Time: {self.user_time}, Time Difference: {self.time_difference} minutes"

# class Team(models.Model):
#     """A model of a bike team."""
#
#     name = models.CharField(max_length=100, default="NoTeam")
#     token = models.CharField(max_length=3)
#
#
# class Member(models.Model):
#     """A model of a cyclist."""
#
#     name = models.CharField("Member's name", max_length=100, default="Anonymous")
#     gender = models.CharField(
#         choices=(
#             ("d", "divers"),
#             ("f", "Frau"),
#             ("m", "Mann"),
#         ),
#         max_length=1,
#     )
#     team = models.ForeignKey("Team")
#
# class StageAdmin(models.Model):
#     """A model of a stage (Etappe)"""
#     name = models.CharField(max_length=10, default="Etappe 0")
#     dist_long = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
#     dist_short = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
#     time_start = models.TimeField(default=datetime.now)
#     dist_sprint = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)  # sprint distance in meters
# 
# class StageUser(models.Model):
#     """A model of a stage (Etappe)"""
#     stage = models.ForeignKey("StageAdmin")
#     time_arrival = models.TimeField(default=datetime.now)  # Field to store the user's entered time
#     time_difference = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)  # Field to store the calculated time difference (in minutes?)
#     timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp when the entry is created
#     placement_mount1 = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)
#     placement_mount2 = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)
#     time_sprint = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)  # sprint time in seconds
