#!/home/scholarisadmin/public_html/ws/env34/bin/python

import os
os.environ.setdefault("PYTHONPATH",
"/home/scholarisadmin/public_html/ws/garage21/service/dashboard")

from wsgiref.handlers import CGIHandler
from sensor_data import app

CGIHandler().run(app)
