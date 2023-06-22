from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Any
import yaml
import os



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/{project}', response_model=Any)
def get_data(project: str):
    try:
        with open(f'./projects/{project}.yaml') as f:
            data = yaml.safe_load(f)
            return data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f'Project {project} not found')


# @app.put('/{project}')
# def add_or_replace_data(project: str, data: Any):
#     try:
#         with open(f'./projects/{project}.yaml', 'w') as f:
#             yaml.dump(data, f)
#         return {"message": f"Data added or replaced in {project}"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

    
# @app.delete('/{project}')
# def delete_project(project: str):
#     try:
#         file_path = f'./projects/{project}.yaml'
#         if os.path.isfile(file_path):
#             os.remove(file_path)
#             return {"message": f"Project {project} deleted"}
#         else:
#             raise HTTPException(status_code=404, detail=f'Project {project} not found')
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))