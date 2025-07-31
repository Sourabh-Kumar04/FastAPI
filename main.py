from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open ('patient_dataset.json', 'r') as f:
        data = json.load(f)

    return data

@app.get('/')
def home():
    return {'message': 'Patient Management System API'}

@app.get('/about')
def about():
    return {'message': 'A fully functional API to manage Patients data'}

@app.get('/view')
def view():
    data = load_data()

    return data

@app.get('/patient/{id}')  # add dynamic segement using {}
def view_patient(id: int = Path(..., description='ID of the patient in the DB', example='1')):
    # load all the data
    data = load_data()
    
    for patient in data:
        # check if the patient id matches the one provided in the path
        if patient['id'] == id:
            return patient
    raise HTTPException(status_code=404, detail='Patient not found')

@app.get("/sort")
def sort_patient(sort_by: str = Query(..., description="Sort on the basis of age, name"), order: str = Query('asc', description='Sort in ascending or desc order')):

    valid_fields = ['age', 'name']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail=f'Invalid order select between asc and desc')
    
    data = load_data()
    
    sort_order = True if order=='desc' else False

    # sorted_data = sorted(data.values(), keys=lambda x: x.get(sort_by, 0), reverse=sort_order)
    sorted_data = sorted(data, key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data