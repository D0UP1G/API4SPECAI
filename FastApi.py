from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.exceptions import HTTPException
from jose import JWTError, jwt
from typing import Optional

app = FastAPI(redoc_url=None)


app = FastAPI()

SECRET_KEY = "SecretKey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
import datetime

def create_access_token(data: dict, expires_delta: Optional[datetime.timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
    else:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.post("/token")
async def login_for_access_token():
    access_token = create_access_token(data={})
    return {"access_token": access_token, "token_type": "bearer"}

def AI_sign(company:str, model:str, token):
    try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            # Здесь вы можете выполнить проверку токена и получить информацию о пользователе из токена
    except JWTError:
        raise HTTPException(status_code=401, detail="Неверные учетные данные")
    return {
    'Материал':['Nintendo switch', 'https://clck.ru/3B9JqY'],
    'Процессор': ['Intel core i5', 'https://clck.ru/3B9JtM'],
    'ВидеоКарта': [None, 'https://clck.ru/3B9Juf'],
    'Операционная Система':['Linux', 'https://clck.ru/3B9Jxn'],
}

@app.get("/get_sign")
def read_root(token:str, brand:str, model:str):
    
    return AI_sign('Xiaomi', 'Xiaomi Redmi Note mega NFC plus Ultra 5-6G', token=token)
