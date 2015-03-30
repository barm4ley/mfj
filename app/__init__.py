from flask import Flask
import os
import pymongo

app = Flask(__name__)
app.config['JSONSCHEMA_DIR'] = os.path.join(app.root_path, 'schemas')

#DB connection
connection = pymongo.MongoClient("mongodb://localhost")
db = connection.mfj
reports = db.reports
# Save reports collection handle to global config variable
app.config['REPORTS_COLL'] = reports

from app import views
