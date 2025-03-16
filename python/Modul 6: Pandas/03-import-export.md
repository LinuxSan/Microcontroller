# 📂 Modul 3: Import og eksport af data i Pandas

## 📌 **Introduktion**
Dette modul viser, hvordan du **importerer og eksporterer data i forskellige formater**.  
Vi lærer at arbejde med **CSV, Excel, JSON og SQL-databaser** i Pandas.

🔗 **Forrige modul:** [02-pandas-basics.md](02-pandas-basics.md)  
🔜 **Næste modul:** [04-data-cleaning.md](04-data-cleaning.md)  

---

## ✅ **Trin 1: Importér data fra en CSV-fil**
Pandas gør det nemt at **læse data fra CSV-filer**.

```python
import pandas as pd

# Læs en CSV-fil
df = pd.read_csv("sensor_data.csv")

print(df.head())  # Vis de første 5 rækker
```

✅ **Nu har vi indlæst en CSV-fil i Pandas!**  

---

## 📤 **Trin 2: Eksportér data til CSV**
Når vi har behandlet vores data, kan vi **gemme det igen i en CSV-fil**.

```python
df.to_csv("output.csv", index=False)
print("Data gemt til output.csv")
```

✅ **Nu har vi eksporteret vores data til en CSV-fil!**  

---

## 📥 **Trin 3: Importér data fra Excel**
Pandas understøtter også **Excel-filer**, hvis `openpyxl` er installeret.

```bash
pip install openpyxl  # Installer openpyxl, hvis det ikke er installeret
```

```python
df = pd.read_excel("sensor_data.xlsx")
print(df.head())
```

✅ **Nu har vi åbnet en Excel-fil i Pandas!**  

---

## 📤 **Trin 4: Eksportér data til Excel**
Hvis vi vil **gemme vores DataFrame som en Excel-fil**, kan vi gøre det sådan:

```python
df.to_excel("output.xlsx", index=False)
print("Data gemt til output.xlsx")
```

✅ **Nu har vi gemt data i en Excel-fil!**  

---

## 🌍 **Trin 5: Importér data fra JSON**
JSON bruges ofte i **webapplikationer og API'er**.

```python
df = pd.read_json("sensor_data.json")
print(df.head())
```

✅ **Nu har vi indlæst data fra en JSON-fil!**  

---

## 🛠 **Trin 6: Gem data til JSON**
Hvis vi vil gemme vores Pandas DataFrame i JSON-format, gør vi sådan:

```python
df.to_json("output.json", orient="records")
print("Data gemt til output.json")
```

✅ **Nu har vi gemt data i en JSON-fil!**  

---

## 🏛 **Trin 7: Importér data fra en SQL-database**
Pandas kan også læse data fra en SQL-database.

```python
import sqlite3

# Opret forbindelse til databasen
conn = sqlite3.connect("database.db")

# Læs data fra en tabel
df = pd.read_sql("SELECT * FROM sensors", conn)

print(df.head())
```

✅ **Nu har vi hentet data fra en SQL-database!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Importeret data fra **CSV, Excel, JSON og SQL**  
✔️ Eksporteret data til **CSV, Excel og JSON**  
✔️ Lært at **arbejde med eksterne datakilder i Pandas**  

🔜 **Fortsæt til næste modul:** [04-data-cleaning.md](04-data-cleaning.md), hvor vi lærer **at rense og filtrere måledata**!  
