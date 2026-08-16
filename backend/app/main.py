from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import tools

app = FastAPI(title="Cognodb AI Tools Graph API", version="1.0.0")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tools.router)

@app.get("/")
def root():
    return {
        "message": "Welcome to the Cognodb AI Tools Graph API!"
        }
    
@app.get("/cap2")
def cap2(tools):
    return {
        "name": tools.cap2
        }
    
@app.get("/cap1")
def cap1(tools):
    return {
        "name": tools.cap1
        }

@app.get("/domain")
def domain(tools):
    return {
        "name": tools.domain
        }
    
@app.get("/integration")
def integration(tools):
    return {
        "name": tools.integration
        }