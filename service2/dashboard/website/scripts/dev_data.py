"""
    Runs all the other scripts
    run: python manage.py runscript dev_data
"""

from water_meter.scripts import gen_goals
from water_meter.scripts import gen_hcsr04
from water_meter.scripts import gen_yfs201

from sabesp.scripts import gen_sabesp


def run():
    gen_yfs201.run()
    gen_hcsr04.run()
    gen_goals.run()
    gen_sabesp.run()
