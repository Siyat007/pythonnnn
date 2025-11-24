# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/subtract")
def subtract(a: float, b: float):
    return {"result": a - b}

@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}

@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        return {"error": "Cannot divide by zero"}
    return {"result": a / b}

# Introduced vulnerability: using eval() unsafely
@app.get("/power")
def power(a: float, b: float):
    return {"result": eval(f"{a}**{b}")}  # unsafe usage, SonarQube will flag

@app.get("/modulo")
def modulo(a: float, b: float):
    if b == 0:
        return {"error": "Cannot modulo by zero"}
    return {"result": a % b}

@app.get("/average")
def average(a: float, b: float):
    return {"result": (a + b) / 2}
