from fastapi import FastAPI
from api_routes import router  # Ensure api_routes is in the same directory as main.py
import uvicorn


app = FastAPI()

# Include the API routes
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
