from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .routes import router
from .db import create_table

app = FastAPI(title="Todo API", version="1.0.0")

# Create table on startup
@app.on_event("startup")
def startup():
    create_table()
    print("✅ Database table created!")

# Include routes
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Todo API", "docs": "/docs"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

