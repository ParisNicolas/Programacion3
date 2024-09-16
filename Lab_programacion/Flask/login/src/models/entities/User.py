from werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id, username, password, fullname="") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
    
    
    


    #generate_password_hash

#print(generate_password_hash("newpass"))

#ejecutar en consola para que nos de el token de hasheo - python .\src\models\entities\User.py