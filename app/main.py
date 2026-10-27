from fastapi import FastAPI


app = FastAPI()


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/version")
def version():
    return {"version": "0.1.0"}
