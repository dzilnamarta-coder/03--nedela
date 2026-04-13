# --- Saraksti ---
# 1. Izveido sarakstu ar vismaz 5 skaitļiem
skaitli = [4, 8, 12, 16, 20, 24, 28, 32, 36]
print(f"Saraksts: {skaitli}")

skaitli.append(40)
print(f"Saraksts pēc pievienošanas: {skaitli}")

skaitli.pop()
print(f"Saraksts pēc noņemšanas: {skaitli}")

kopsumma = 0
skaitu_daudzums = 0
for sk in skaitli:
    kopsumma += sk
    skaitu_daudzums += 1
print(f"Summa: {kopsumma}, Vidējais: {kopsumma/skaitu_daudzums}")

# Summa = 4 + 8 + 12 + 16 + 20 + 24 + 28 + 32 + 36 = 180
# Vidējais = 180 / 9 = 20.0

para_skaitli = []
for sk in skaitli:
    if sk % 2 == 0:
        para_skaitli.append(sk)
print(f"Pāra skaitļi: {para_skaitli}")

# Pāra skaitļi: [4, 8, 12, 16, 20, 24, 28, 32, 36]

pirmie_tris = skaitli[:3]
pedejie_tris = skaitli[-3:]
katrs_otrais = skaitli[::2]
print(f"Pirmie 3 skaitļi: {pirmie_tris}")
print(f"Pēdējie 3 skaitļi: {pedejie_tris}")
print(f"Katrs otrais elements: {katrs_otrais}")

# Pirmie 3 skaitļi: [4, 8, 12]
# Pēdējie 3 skaitļi: [28, 32, 36]
# Katrs otrais elements: [4, 12, 20, 28, 36]


# --- Vārdnīcas ---

# 1. Izveidojo vārdnīcu ar 3+ studentiem
studenti = {"Anna": 85, "Jānis": 72, "Līga": 95}
print(f"Sākotnējā vārdnīca: {studenti}")

# Sākotnējā vārdnīca: {'Anna': 85, 'Jānis': 72, 'Līga': 95}


# 2. Pievienoju jaunu studentu un mainām esošu atzīmi
studenti["Māris"] = 90
studenti["Anna"] = 78
print(f"Atjauninātā vārdnīca: {studenti}")

# Atjauninātā vārdnīca: {'Anna': 78, 'Jānis': 72, 'Līga': 95, 'Māris': 90}


# 3. Iterēu (ejam cauri) vārdnīcai ar for un .items()
print("Studentu saraksts un atzīmes:")
for name, grade in studenti.items():
    print(f"Students: {name}, Atzīme: {grade}")

# Studentu saraksts un atzīmes:
# Students: Anna, Atzīme: 78
# Students: Jānis, Atzīme: 72
# Students: Līga, Atzīme: 95
# Students: Māris, Atzīme: 90

# 4. Atrodu studentu ar augstāko atzīmi (ar for ciklu)
augstaka_atzime = 0
students_ar_augstako_atzimi = []
for name, grade in studenti.items():
    if grade > augstaka_atzime:
        augstaka_atzime = grade
        students_ar_augstako_atzimi = [name]
    elif grade == augstaka_atzime:
        students_ar_augstako_atzimi.append(name)
print(f"Augstākā atzīme: {augstaka_atzime}, Studenti ar augstāko atzīmi: {students_ar_augstako_atzimi}")

# Augstākā atzīme: 95, Studenti ar augstāko atzīmi: ['Līga']

# 1. Izveidoju sarakstu ar vārdnīcām (katra vārdnīca ir viens students)
studentu_saraksts = [
    {"vards": "Anna", "atzime": 78},
    {"vards": "Jānis", "atzime": 72},
    {"vards": "Līga", "atzime": 95},
    {"vards": "Māris", "atzime": 90}
]
print(f"Saraksts ar vārdnīcām: {studentu_saraksts}")

# Saraksts ar vārdnīcām: [{'vards': 'Anna', 'atzime': 78}, {'vards': 'Jānis', 'atzime': 72},
# {'vards': 'Līga', 'atzime': 95}, {'vards': 'Māris', 'atzime': 90}]

# 2. Filtrēju: izveidojam jaunu sarakstu tikai ar tiem, kam atzīme >= 80
studenti_ar_augstako_atzimi = []
for student in studentu_saraksts:
    if student["atzime"] >= 80:
        studenti_ar_augstako_atzimi.append(student)
print(f"Studenti ar atzīmi >= 80: {studenti_ar_augstako_atzimi}")

# Studenti ar atzīmi >= 80: [{'vards': 'Līga', 'atzime': 95}, {'vards': 'Māris', 'atzime': 90}]

# 3. Izmantoju enumerate() un f-strings formatētai izvadei
for i, students in enumerate(studenti_ar_augstako_atzimi, start=1):
    vards = students["vards"]
    atzime = students["atzime"]
    print(f"{i}. {vards} — {atzime}")

# Studenti ar atzīmi >= 80: [{'vards': 'Līga', 'atzime': 95}, {'vards': 'Māris', 'atzime': 90}]
# 1. Līga — 95
# 2. Māris — 90'
