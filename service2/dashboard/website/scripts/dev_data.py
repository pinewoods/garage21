"""
    Runs all the other scripts
    run: python manage.py runscript dev_data
"""

from django.core import management

#from water_meter.scripts import gen_goals
#from water_meter.scripts import gen_hcsr04
#from water_meter.scripts import gen_yfs201
#from sabesp.scripts import gen_sabesp


def run():

    management.call_command(
            "loaddata", "water_meter/fixtures/some_data.json")

    management.call_command(
            "loaddata", "sabesp/fixtures/sabesp_data.json")

    management.call_command(
            "runscript", "gen_yfs201")

    management.call_command(
            "runscript", "gen_hcsr04")

    management.call_command(
            "runscript", "gen_goals")

    management.call_command(
            "runscript", "gen_sabesp")
