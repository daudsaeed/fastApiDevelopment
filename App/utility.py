from passlib.context import CryptContext


context  = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashPassword(password):
  return context.hash(password)


# verify the password
def passwordVerification(password, hashPassword):
  return context.verify(password, hashPassword)