# 🧹 Modul 4: Rensning og filtrering af måledata

## 📌 **Introduktion**
Rensning af data er vigtigt, især i **industrielle systemer**, hvor vi ofte har **manglende værdier, dubletter eller fejlmålinger**.  
I dette modul lærer vi at **finde, rette og filtrere fejlbehæftede data** i Pandas.

🔗 **Forrige modul:** [03-import-export.md](03-import-export.md)  
🔜 **Næste modul:** [05-time-series.md](05-time-series.md)  

---

## ✅ **Trin 1: Find og håndtér manglende værdier**
Mange datasæt har **manglende værdier**. Vi kan identificere dem med:

```python
import pandas as pd

# Opret et datasæt med manglende værdier
data = {
    "Sensor": ["Temp", "Tryk", "Fugt", "Luft"],
    "Værdi": [22.5, None, 45, 80],
    "Enhed": ["C", "hPa", "%", None]
}

df = pd.DataFrame(data)

print(df.isnull())  # Se hvor værdier mangler
```

🔹 Output:
```
   Sensor  Værdi  Enhed
0   False  False  False
1   False   True  False
2   False  False  False
3   False  False   True
```

✅ **Nu kan vi se, hvilke data der mangler!**  

---

## 🛠 **Trin 2: Erstat manglende værdier**
Vi kan enten **slette** rækker med manglende værdier eller **udfylde dem** med en standardværdi.

```python
df_filled = df.fillna({"Værdi": df["Værdi"].mean(), "Enhed": "N/A"})
print(df_filled)
```

🔹 Output:
```
  Sensor  Værdi Enhed
0   Temp   22.5     C
1   Tryk   49.2   hPa
2   Fugt   45.0     %
3   Luft   80.0   N/A
```

✅ **Nu har vi erstattet de manglende værdier!**  

---

## 🔍 **Trin 3: Fjern dubletter**
Nogle gange har vi **gentagne målinger**, som vi vil fjerne.

```python
df = pd.DataFrame({
    "Sensor": ["Temp", "Tryk", "Fugt", "Temp"],
    "Værdi": [22.5, 1013, 45, 22.5]
})

df_no_duplicates = df.drop_duplicates()
print(df_no_duplicates)
```

✅ **Nu har vi fjernet dubletter!**  

---

## ✂️ **Trin 4: Fjern ekstreme målinger**
Målefejl kan føre til **ekstremt høje eller lave værdier**. Vi kan filtrere dem fra.

```python
df_filtered = df[(df["Værdi"] > 10) & (df["Værdi"] < 1000)]
print(df_filtered)
```

✅ **Nu har vi filtreret ekstreme værdier væk!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Fundet og håndteret **manglende værdier**  
✔️ Fjernet **dubletter** i data  
✔️ Filtreret **ekstreme målinger**  
✔️ Gjort data **klar til analyse**  

🔜 **Fortsæt til næste modul:** [05-time-series.md](05-time-series.md), hvor vi lærer **at håndtere tidsserier og log-data**!  
