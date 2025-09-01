from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()
@app.get("/", response_class=HTMLResponse)
async def home():
    return """
        <html>source venv/bin/activate

            <head>
                <title>SEP</title>
            </head>
            <body style="font-family: Tahoma; text-align: center; margin-top: 450px;">
                <h1>Hello World</h1>
            </body>
        </html>
    """
