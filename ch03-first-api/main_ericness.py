import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get('/api/calculate')
def calculate():
    result = 2 + 2
    return {
        "value": result
    }


uvicorn.run(api, port=8000, host="127.0.0.1")
