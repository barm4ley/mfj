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
    data = request.get_json()
    reports = app.config['REPORTS_COLL']
    ins_res = reports.save(data)
    print(type(ins_res))
    return jsonify({"_id":str(ins_res)})
