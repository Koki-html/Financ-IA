from Src.models.dbmodels import User
from Src.connector.database import SessionLocal
from Src.models.PModels import User as UserSchema
from sqlalchemy.orm import Session
import uuid
# Función para obtener todos los usuarios
def get_users():
    db: Session = SessionLocal()

    try:
        users = db.query(User).all()
        user_list = [UserSchema(**{
            "id": user.id.hex(),
            "run": user.run,
            "name": user.name,
            "last_name": user.last_name,
            "password": user.password,
            "email": user.email,
            "phone": user.phone,
            "birthdate": user.birthdate
        }) for user in users]

        return user_list
    finally:
        db.close()

def create_users(user_data:UserSchema):
    db: Session = SessionLocal()

    try:
        new_user = User(
            id=uuid.uuid4().bytes,
            run=user_data.run,
            name=user_data.name,
            last_name=user_data.last_name,
            password=user_data.password,
            email=user_data.email,
            phone=user_data.phone,
            birthdate=user_data.birthdate
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {
            "id": new_user.id.hex(),
            "run": new_user.run,
            "name": new_user.name,
            "last_name": new_user.last_name,
            "password": new_user.password,
            "email": new_user.email,
            "phone": new_user.phone,
            "birthdate": str(new_user.birthdate)
        }
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()