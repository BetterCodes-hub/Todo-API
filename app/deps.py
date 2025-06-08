from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from . import models, database, auth, schemas
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
# Tworzy mechanizm uwierzytelniania 
oatuh2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")
# Zwraca sesję bazy danych i automatycznie ją zamyka po użyciu
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Zwraca aktualnie zalogowanego użytkownika na podstawie tokenu
# Próba dekodowania tokenu JWT i pobrania ID użytkownika.
# Jeśli token jest nieprawidłowy lub użytkownik nie istnieje – zgłaszany jest błąd 401.
def get_current_user(token: str = Depends(oatuh2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(token, auth.SECRET_KEY, algorithms=[auth.ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(models.User).get(user_id)
    if user is None:
        raise credentials_exception
    return user