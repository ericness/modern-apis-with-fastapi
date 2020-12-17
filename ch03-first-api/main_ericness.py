from typing import Optional

import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get("/")
def index():
    content = """
    <html>
    <body style='padding: 10px;'>
    <h1>Welcome to the API</h1>
    <div>
    Try it: <a href='/api/calculate?x=7&y=11'>/api/calculate?x=7&y=11</a>
    </div>
    </body>
    </html>
    """

    return fastapi.responses.HTMLResponse(content=content)


@api.get("/api/calculate")
def calculate(x: int, y: int, z: Optional[int] = None):
    if z == 0:
        return fastapi.responses.JSONResponse(
            content={"error": "z cannot be zero"}, status_code=400,
        )

    result = x + y

    if z is not None:
        result = result / z

    return {
        "x": x,
        "y": y,
        "z": z,
        "value": result,
    }


uvicorn.run(api, port=8000, host="127.0.0.1")
