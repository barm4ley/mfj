from flask import render_template, request, jsonify
from app import app
from flask_jsonschema import JsonSchema, ValidationError

jsonschema = JsonSchema(app)

@app.errorhandler(ValidationError)
def on_validation_error(e):
    return "error"

@app.route('/reports', methods = ['POST'])
@jsonschema.validate('reports', 'create')
def reports():
    # Get json body of request
    data = request.get_json()
    # Get Mongo reports collection handle
    reports = app.config['REPORTS_COLL']
    # Insert just received json data to db
    ins_res = reports.save(data)
    # Send db responce back to user
    return jsonify({"_id":str(ins_res)})
