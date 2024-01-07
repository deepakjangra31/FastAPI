This is a mini project to understand the FastAPI framework.

Run the FastAPI application:
uvicorn main:app --reload

The API will be accessible at http://127.0.0.1:8000.

Usage

Upload a file: Use the /uploadfile/ endpoint to upload a CSV file.

Explore Data: Utilize various endpoints such as /summary/, /info/, /head/, /tail/, and /describe/ for comprehensive data analysis.

API Endpoints

Welcome Message: GET / - Welcome message and API status.

File Upload: POST /uploadfile/ - Upload a CSV file.

Data Summary: GET /summary/ - Retrieve summary statistics.

Data Information: GET /info/ - Retrieve detailed information about the DataFrame.

Head of DataFrame: GET /head/ - Retrieve the head of the DataFrame.

Tail of DataFrame: GET /tail/ - Retrieve the tail of the DataFrame.

Descriptive Statistics: GET /describe/ - Retrieve descriptive statistics of the DataFrame.

Error Handling
The API handles exceptions gracefully and provides detailed error messages using HTTP status codes.

Dependencies
FastAPI
Pandas
Uvicorn
