# Import necessary FastAPI components and libraries
from fastapi import FastAPI, File, UploadFile, HTTPException, Query
import pandas as pd
import io

# Initialize FastAPI application
app = FastAPI()

# Global variable to store DataFrame
data = None

# Welcome message endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI Data Analysis API!"}

# Endpoint for file upload
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    global data
    try:
        # Read the contents of the uploaded file
        contents = await file.read()
        
        # Convert CSV content to a Pandas DataFrame
        data = pd.read_csv(io.StringIO(contents.decode("utf-8")))
        
        # Return a success message
        return {"message": "File uploaded successfully!"}
    except Exception as e:
        # Handle exceptions and raise HTTPException with an appropriate status code and detail message
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint for retrieving summary statistics of the DataFrame
@app.get("/summary/")
async def get_summary():
    global data
    if data is not None:
        # Return summary statistics as a dictionary
        return {"summary": data.describe().to_dict()}
    else:
        # Raise HTTPException if DataFrame is not found
        raise HTTPException(status_code=404, detail="DataFrame not found.")

# Endpoint for retrieving information about the DataFrame
@app.get("/info/")
async def get_info():
    global data
    if data is not None:
        # Capture info in a dictionary
        info_dict = {
            "columns": list(data.columns),
            "dtypes": data.dtypes.apply(lambda x: x.name).to_dict(),
            "non-null count": data.count().to_dict(),
        }
        # Return the info dictionary
        return {"info": info_dict}
    else:
        # Raise HTTPException if DataFrame is not found
        raise HTTPException(status_code=404, detail="DataFrame not found.")

# Endpoint for retrieving the tail of the DataFrame
@app.get("/tail/")
async def get_tail():
    global data
    if data is not None:
        # Return the tail of the DataFrame as a dictionary
        return {"tail": data.tail().to_dict(orient="records")}
    else:
        # Raise HTTPException if DataFrame is not found
        raise HTTPException(status_code=404, detail="DataFrame not found.")

# Endpoint for retrieving the head of the DataFrame
@app.get("/head/")
async def get_head(start: int = Query(0, title="Start Index"), end: int = Query(5, title="End Index")):
    global data
    if data is not None:
        # Return the head of the DataFrame as a dictionary
        return {"head": data.iloc[start:end].to_dict(orient="records")}
    else:
        # Raise HTTPException if DataFrame is not found
        raise HTTPException(status_code=404, detail="DataFrame not found.")

# Endpoint for retrieving descriptive statistics of the DataFrame
@app.get("/describe/")
async def get_describe():
    global data
    if data is not None:
        # Return descriptive statistics as a dictionary
        return {"describe": data.describe().to_dict()}
    else:
        # Raise HTTPException if DataFrame is not found
        raise HTTPException(status_code=404, detail="DataFrame not found.")

if __name__ == "__main__":
    import uvicorn
    # Run FastAPI application using Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
