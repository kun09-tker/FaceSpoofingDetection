import uvicorn
if __name__ == "__main__":
    uvicorn.run("FastAPI.FastAPI_Server:app", host="localhost", port=3000, reload=True)

