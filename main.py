from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import httpx

load_dotenv()

api_key = os.getenv('OPENWEATHER_API_KEY')  
api_url = os.getenv('OPENWEATHER_API_URL')

app = FastAPI(title='Weather API Proxy')

origins = [
    'http://localhost:3000',
    'http://localhost:5173',
    'https://weather-app-sep.vercel.app'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],   
    allow_headers=["*"],   
)

@app.get('/weather')
async def get_weather(city: str):

    url = f'{api_url}/weather?q={city}&appid={api_key}&lang=pt_br'
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    return response.json()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        app=app,
    )