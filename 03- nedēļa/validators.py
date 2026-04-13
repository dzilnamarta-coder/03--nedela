# Validācijas bibliotēka 

def is_email(text):
    """
    Pārbauda, vai teksts ir derīgs e-pasts (satur '@' un '.').
    
    Args:
        text (str): Pārbaudāmais teksts.
        
    Returns:
        bool: True, ja ir derīgs e-pasts, citādi False.
        
    Example:
        >>> is_email('anna@inbox.lv')
        True
    """
    if not isinstance(text, str):
        return False
    # Visvienkāršākā pārbaude - vai iekšā ir gan @ zīme, gan punkts
    return "@" in text and "." in text

def is_phone_number(text):
    """
    Pārbauda, vai telefona numurs atbilst precīzam Latvijas formātam (+371 XXXXXXXX).
    
    Args:
        text (str): Pārbaudāmais numurs.
        
    Returns:
        bool: True, ja atbilst, citādi False.
        
    Example:
        >>> is_phone_number('+371 26123456')
        True
    """
    if not isinstance(text, str):
        return False
        
    dalas = text.split(" ")
    
    if len(dalas) == 2:
        valsts_kods = dalas[0]
        cipari = dalas[1]
        
        if valsts_kods == "+371" and len(cipari) == 8 and cipari.isdigit():
            return True
            
    return False


def is_valid_age(age):
    """
    Pārbauda, vai vecums ir vesels skaitlis diapazonā no 0 līdz 150.
    
    Args:
        age (int): Pārbaudāmais vecums.
        
    Returns:
        bool: True, ja derīgs, citādi False.
        
    Example:
        >>> is_valid_age(25)
        True
    """
    if not isinstance(age, int):
        return False
    return 0 <= age <= 150

def is_strong_password(text):
    """
    Pārbauda, vai parole ir spēcīga (vismaz 8 simboli, satur burtus UN ciparus).
    
    Args:
        text (str): Pārbaudāmā parole.
        
    Returns:
        bool: True, ja stipra, citādi False.
        
    Example:
        >>> is_strong_password('parole123')
        True
    """
    if not isinstance(text, str) or len(text) < 8:
        return False
    
    has_letter = any(c.isalpha() for c in text)
    has_digit = any(c.isdigit() for c in text)
    
    return has_letter and has_digit

def is_valid_date(text):
    """
    Pārbauda, vai teksts atbilst pamata datuma formātam YYYY-MM-DD.
    
    Args:
        text (str): Pārbaudāmais datums.
        
    Returns:
        bool: True, ja formāts ir pareizs, citādi False.
        
    Example:
        >>> is_valid_date('2023-10-25')
        True
    """
    if not isinstance(text, str):
        return False
    parts = text.split("-")
    if len(parts) == 3:
        year, month, day = parts
        if len(year) == 4 and len(month) == 2 and len(day) == 2:
            if year.isdigit() and month.isdigit() and day.isdigit():
                return True
                
    return False


if __name__ == "__main__":
    print(f"is_email('anna@inbox.lv') -> {is_email('anna@inbox.lv')}") 
    print(f"is_email('anna')          -> {is_email('anna')}")          
    print(f"is_email('anna@')         -> {is_email('anna@')}")
    print(f"is_phone_number('+371 26123456') -> {is_phone_number('+371 26123456')}") 
    print(f"is_phone_number('+371 2612345')  -> {is_phone_number('+371 2612345')}")  
    print(f"is_phone_number('26123456')     -> {is_phone_number('26123456')}") 
    print(f"is_valid_age(25)   -> {is_valid_age(25)}")
    print(f"is_valid_age(-5)   -> {is_valid_age(-5)}")
    print(f"is_valid_age(200)  -> {is_valid_age(200)}")  
    print(f"is_strong_password('parole123') -> {is_strong_password('parole123')}")
    print(f"is_strong_password('parole')     -> {is_strong_password('parole')}")
    print(f"is_strong_password('12345678')   -> {is_strong_password('12345678')}")
    print(f"is_valid_date('2023-10-25') -> {is_valid_date('2023-10-25')}")
    print(f"is_valid_date('2023-10-2')  -> {is_valid_date('2023-10-2')}")
    print(f"is_valid_date('2023/10/25') -> {is_valid_date('2023/10/25')}")

# Pārbaude is_email(text) funkcijai

print(f"is_email('anna@inbox.lv') -> {is_email('anna@inbox.lv')}") 
print(f"is_email('anna')          -> {is_email('anna')}")          
print(f"is_email('anna@')         -> {is_email('anna@')}")

# is_email('anna@inbox.lv') -> True
# is_email('anna')          -> False
# is_email('anna@')         -> False

# Pārbaude is_phone_number(text) funkcijai
print(f"is_phone_number('+371 26123456') -> {is_phone_number('+371 26123456')}") 
print(f"is_phone_number('+371 2612345')  -> {is_phone_number('+371 2612345')}")  
print(f"is_phone_number('26123456')     -> {is_phone_number('26123456')}")     

# is_phone_number('+371 26123456') -> True
# is_phone_number('+371 2612345')  -> False
# is_phone_number('26123456')     -> False

# Pārbaude is_valid_age(age) funkcijai
print(f"is_valid_age(25)   -> {is_valid_age(25)}")
print(f"is_valid_age(-5)   -> {is_valid_age(-5)}")
print(f"is_valid_age(200)  -> {is_valid_age(200)}")

# is_valid_age(25)   -> True
# is_valid_age(-5)   -> False
# is_valid_age(200)  -> False

# Pārbaude is_strong_password(text)funkcijai
print(f"is_strong_password('parole123') -> {is_strong_password('parole123')}")
print(f"is_strong_password('parole')     -> {is_strong_password('parole')}")
print(f"is_strong_password('12345678')   -> {is_strong_password('12345678')}")

# is_strong_password('parole123') -> True
# is_strong_password('parole')     -> False
# is_strong_password('12345678')   -> False


# Pārbaude is_valid_date(text) funkcijai
print(f"is_valid_date('2023-10-25') -> {is_valid_date('2023-10-25')}")
print(f"is_valid_date('2023-10-2')  -> {is_valid_date('2023-10-2')}")
print(f"is_valid_date('2023/10/25') -> {is_valid_date('2023/10/25')}")

# is_valid_date('2023-10-25') -> True
# is_valid_date('2023-10-2')  -> False
# is_valid_date('2023/10/25') -> False


