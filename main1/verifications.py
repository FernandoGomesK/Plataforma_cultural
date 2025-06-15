import re
from datetime import *

def is_valid_cpf(cpf):
    """
    Verifies if a given CPF is valid by matching its format with a regular expression.

    Parameters:
        cpf (str): The CPF to be verified.

    Returns:
        bool: True if the CPF is valid, False otherwise.
    """
    pattern = r'^(\d{3}\.\d{3}\.\d{3}-\d{2})$'
    return bool(re.fullmatch(pattern, cpf))
#//////////////////////////////////////////////////////////////////////////////////q        
def is_valid_email(email):
    """
    Validates the format of an email address using a regular expression.

    Parameters:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    pattern = r'^([a-z\d.-]+)@([a-z\d-]+)\.([a-z]{2,8})(\.[a-z]{2,8})?$'
    return bool(re.fullmatch(pattern, email))
 #/////////////////////////////////////////////////////////////////////////////////       
def verify_age(x):
    """
    Verifies if a given age is valid.

    Parameters:
        x (str): A string containing the date of birth in the format DD/MM/YYYY.

    Returns:
        bool: True if the age is 16 or more, False otherwise.
    """
    birth = datetime.strptime(x, "%d/%m/%Y")
    age = (datetime.now() - birth).days // 365
    if age >= 16:
        return True
    else: 
        return False
        