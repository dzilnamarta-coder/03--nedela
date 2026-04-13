#---- Utilītu bibliotēka ----

# Virkņu funkcijas 
def capitalize(text):
    """
    Pārvērš pirmo burtu lielo un pārējos mazajos.
    
    Args:
        text (str): Ievades teksts.
        
    Returns:
        str: Teksts ar lielo sākumburtu.
        
    Example:
        >>> capitalize("hello world")
        'Hello world'
    """
    if not text:
        return text
    return text[0].upper() + text[1:].lower()


def truncate(text, max_len=20):
    """
    Saīsina tekstu līdz max_len simboliem, pievienojot '...' ja nepieciešams.
    
    Args:
        text (str): Ievades teksts.
        max_len (int): Maksimālais garums (noklusējums: 20).
        
    Returns:
        str: Saīsinātais teksts.
        
    Example:
        >>> truncate("Sveiki!", 5)
        'Sv...'
    """
    if len(text) <= max_len:
        return text
    return text[:max_len-3] + "..."


def count_words(text, separator=" "):
    """
    Skaita vārdus tekstā, atdalot tos ar norādīto atdalītāju.
    
    Args:
        text (str): Ievades teksts.
        separator (str): Atdalītājs (noklusējums: atstarpe).
        
    Returns:
        int: Vārdu skaits.
        
    Example:
        >>> count_words("Šis ir teksts")
        3
    """
    if not text:
        return 0
    return len(text.split(separator))

# Skaitļu funkcijas

def clamp(num, low, high):
    """
    Ierobežo skaitli norādītajā diapazonā.
    
    Args:
        num (int/float): Skaitlis, ko ierobežot.
        low (int/float): Minimālā robeža.
        high (int/float): Maksimālā robeža.
        
    Returns:
        int/float: Ierobežotā vērtība.
        
    Example:
        >>> clamp(15, 0, 10)
        10
    """
    if num < low:
        return low
    elif num > high:
        return high
    else:
        return num

def is_prime(num):
    """
    Pārbauda, vai skaitlis ir pirmskaitlis (dalās tikai ar 1 un sevi pašu).
    
    Args:
        num (int): Pārbaudāmais skaitlis.
        
    Returns:
        bool: True, ja ir pirmskaitlis, citādi False.
        
    Example:
        >>> is_prime(7)
        True
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def factorial(n):
    """
    Aprēķina skaitļa faktoriālu (n!).
    
    Args:
        n (int): Skaitlis faktoriāla aprēķinam.
        
    Returns:
        int: Faktoriāla vērtība.
        
    Raises:
        ValueError: Ja skaitlis ir negatīvs.
        
    Example:
        >>> factorial(5)
        120
    """
    if n < 0:
        raise ValueError("Faktoriāls nav definēts negatīviem skaitļiem.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    

# --- Sarakstu funkcijas ---

def total(numbers):
    """
    Aprēķina skaitļu saraksta summu, izmantojot for ciklu (bez sum() funkcijas).
    
    Args:
        numbers (list/tuple): Skaitļu saraksts.
        
    Returns:
        int/float: Skaitļu summa.
        
    Example:
        >>> total([1, 2, 3])
        6
    """
    result = 0
    for num in numbers:
        result += num
    return result


def average(numbers):
    """
    Aprēķina saraksta skaitļu vidējo aritmētisko vērtību.
    
    Args:
        numbers (list): Skaitļu saraksts.
        
    Returns:
        float: Vidējā vērtība.
        
    Example:
        >>> average([1, 2, 3, 4, 5])
        3.0
    """
    if not numbers:
        return 0
    return total(numbers) / len(numbers)

# Pārbaude visam utils.py failam

# Hello world
# Python
# Īss teksts: Sveiki!
# Garš teksts: Šis ir ļoti garš tekst...
# Vārdu skaits: 4
# clamp(15, 0, 10) -> 10
# clamp(-3, 0, 100) -> 0
# Is 7 prime? True
# Is 10 prime? False
# 5! = 120
# 0! = 1
# Pārbaudām factorial(-1):
# Error: Faktoriāls nav definēts negatīviem skaitļiem.
# Skaitļu summa: 15
# Skaitļu vidējais: 3.0

if __name__ == "__main__":
    print("--- Pārbaudām capitalize() funkciju ---")
    print(capitalize("hello world")) 
    print(capitalize("PYTHON"))      

#Pārbaude capitalize() funkciju 
# Hello world
# Python


print(f"Īss teksts: {truncate('Sveiki!')}")
print(f"Garš teksts: {truncate('Šis ir ļoti garš teksts, kas jāsaīsina.', max_len=25)}")

# Pārbaude truncate() funkciju 
# Īss teksts: Sveiki!
# Garš teksts: Šis ir ļoti garš tekst...


print(f"Vārdu skaits: {count_words('Šis ir piemērs tekstam.')}")

# Pārbaude count_words() funkciju 
# Vārdu skaits: 4

print(f"clamp(15, 0, 10) -> {clamp(15, 0, 10)}")
print(f"clamp(-3, 0, 100) -> {clamp(-3, 0, 100)}")

# Pārbaude clamp() funkciju 
# clamp(15, 0, 10) -> 10
# clamp(-3, 0, 100) -> 0

print(f"Is 7 prime? {is_prime(7)}")
print(f"Is 10 prime? {is_prime(10)}")

# Pārbaude is_prime() funkciju 
# Is 7 prime? True
# Is 10 prime? False

print(f"5! = {factorial(5)}")
print(f"0! = {factorial(0)}")

# Pārbaude factorial() funkciju
# 5! = 120
# 0! = 1

print("Pārbaudām factorial(-1):")
try:
    factorial(-1)
except ValueError as e:
    print(f"Error: {e}")

# Pārbaudām factorial(-1): 
# Error: Faktoriāls nav definēts negatīviem skaitļiem.

print(f"Skaitļu summa: {total([1, 2, 3, 4, 5])}")

# Pārbaude total() funkciju
# Skaitļu summa: 15


print(f"Skaitļu vidējais: {average([1, 2, 3, 4, 5])}")

# Pārbaude average() funkciju
# Skaitļu vidējais: 3.0