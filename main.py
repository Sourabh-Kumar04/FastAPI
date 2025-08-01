from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field,  EmailStr
from typing import Annotated, Literal,  List, Optional
import json
from datetime import date

app = FastAPI()

from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, Literal, List, Optional
from datetime import date

class Patient(BaseModel):

    id: Annotated[int, Field(..., ge=1, description="Unique ID of the patient", example=1)]
    name: Annotated[str, Field(..., min_length=1, description="Full name of the patient")]
    age: Annotated[int, Field(..., gt=0, lt=130, description="Age of the patient")]
    gender: Annotated[Literal['Male', 'Female', 'Other'], Field(..., description="Gender of the patient")]
    contact: Annotated[str, Field(..., min_length=10, max_length=15, description="Contact number")]
    email: Annotated[EmailStr, Field(..., description="Email address of the patient")]
    address: Annotated[str, Field(..., description="Residential address")]
    blood_group: Annotated[str, Field(..., pattern=r"^(A|B|AB|O)[+-]$", description="Blood group like A+, O-, AB+ etc.")]
    medical_history: Annotated[List[str], Field(..., description="List of past medical issues")]
    admission_date: Annotated[date, Field(..., description="Date of hospital admission")]
    discharge_date: Annotated[Optional[date], Field(None, description="Date of discharge (if any)")]
    doctor_assigned: Annotated[str, Field(..., description="Name of the doctor assigned")]
    current_status: Annotated[Literal['Admitted', 'Discharged', 'Under Observation'], Field(..., description="Current patient status")]

def load_data():
    with open('patient_dataset.json', 'r') as f:
        data = json.load(f)

    return data

def save_data(data):
    with open('patient_dataset.json', 'w') as f:
        json.dump(data, f)

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
def view_patient(id: int = Path(..., description='ID of the patient in the DB', example=1)):
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

@app.post("/create")
def create_patient(patient: Patient):

    # load data
    data = load_data()

    # check if alredy exist
    for existing in data:
        if existing['id'] == patient.id:
            raise HTTPException(status_code=400, detail='Patient already exists')

    data.append(patient.model_dump())  

    # save into the json file
    save_data(data)

    return JSONResponse(status_code=200, content={'message': 'Patient created successfully'})
