# 🔢 Modul 2: Grundlæggende Pandas operationer

## 📌 **Introduktion**
Dette modul introducerer de vigtigste Pandas-funktioner til **databehandling, filtrering og transformation**.  
Vi lærer at **åbne og gemme data**, **slicke**, **flytte kolonner/rækker**, **tilføje/fjerne data**, og **transponere DataFrames**.

🔗 **Forrige modul:** [01-installation.md](01-installation.md)  
🔜 **Næste modul:** [03-import-export.md](03-import-export.md)  

---

## ✅ **Trin 1: Opret og gem en Pandas DataFrame**
Lad os starte med at **oprette en DataFrame og gemme den**.

```python
import pandas as pd

# Opret et datasæt
data = {
    "Sensor": ["Temp", "Tryk", "Fugt"],
    "Værdi": [22.5, 1013, 45],
    "Enhed": ["C", "hPa", "%"]
}

df = pd.DataFrame(data)

# Gem til CSV
df.to_csv("sensor_data.csv", index=False)

print("Data gemt til 'sensor_data.csv'!")
```

✅ **Nu har vi gemt vores første CSV-fil!**  

---

## 📥 **Trin 2: Åbn en CSV-fil i Pandas**
Vi kan nu **åbne CSV-filen** og arbejde videre med dataene.

```python
df = pd.read_csv("sensor_data.csv")
print(df)
```

🔹 Output:
```
  Sensor  Værdi Enhed
0   Temp   22.5     C
1   Tryk  1013  hPa
2   Fugt   45.0     %
```

✅ **Nu har vi indlæst data fra en CSV-fil!**  

---

## 🔍 **Trin 3: Filtrér data**
Vi kan **filtrere rækker**, fx hvis vi kun vil have sensorer med værdier over 100.

```python
filtered_df = df[df["Værdi"] > 100]
print(filtered_df)
```

🔹 Output:
```
  Sensor  Værdi Enhed
1   Tryk  1013  hPa
```

✅ **Nu kan vi filtrere data baseret på værdier!**  

---

## ✂️ **Trin 4: Slice data**
Slicing bruges til **at vælge en del af DataFrame'en**.

```python
subset = df.loc[:, ["Sensor", "Værdi"]]  # Vælg kun Sensor og Værdi-kolonner
print(subset)
```

✅ **Nu har vi udvalgt specifikke kolonner!**  

---

## 🔄 **Trin 5: Flyt kolonner og rækker**
Nogle gange vil vi **ændre rækkefølgen af kolonner eller rækker**.

```python
# Omarranger kolonner
df = df[["Værdi", "Sensor", "Enhed"]]
print(df)
```

✅ **Nu har vi ændret kolonnernes rækkefølge!**  

---

## ➕ **Trin 6: Tilføj og fjern kolonner og rækker**
Vi kan **tilføje eller slette data** dynamisk.

```python
# Tilføj en ny kolonne
df["Kalibreret"] = df["Værdi"] * 1.05

# Fjern en kolonne
df = df.drop(columns=["Enhed"])

print(df)
```

✅ **Nu har vi tilføjet og fjernet kolonner!**  

---

## 🔄 **Trin 7: Transponér en DataFrame**
Vi kan **bytte rækker og kolonner** med `.T`.

```python
df_T = df.T
print(df_T)
```

🔹 Output:
```
              0     1     2
Værdi      22.5  1013  45.0
Sensor    Temp  Tryk  Fugt
Kalibreret  23.6  1063.65  47.25
```

✅ **Nu har vi transponeret en DataFrame!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Åbnet og gemt data i Pandas  
✔️ Filtreret og slicet data  
✔️ Flyttet rækker og kolonner  
✔️ Tilføjet og fjernet kolonner/rækker  
✔️ Transponeret en DataFrame  

🔜 **Fortsæt til næste modul:** [03-import-export.md](03-import-export.md), hvor vi lærer at **arbejde med eksterne datakilder**!  
