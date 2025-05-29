import re
from datetime import *

def is_valid_cpf(cpf):
    pattern = r'^(\d{3}\.\d{3}\.\d{3}-\d{2})$'
    return bool(re.fullmatch(pattern, cpf))
        
    
def is_valid_email(email):
    pattern = r'^([a-z\d.-]+)@([a-z\d-]+)\.([a-z]{2,8})(\.[a-z]{2,8})?$'
    return bool(re.fullmatch(pattern, email))
        
    
def verify_age(x):
    birth = datetime.strptime(x, "%d/%m/%Y")
    age = (datetime.now() - birth).days // 365
    if age >= 16:
        return True
    else: 
        return False
        