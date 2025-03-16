# ⏱ Modul 6: Realtidsdataanalyse i Pandas

## 📌 **Introduktion**
I automationssystemer kan vi arbejde med **løbende opdateringer af sensordata**.  
Dette modul viser, hvordan vi **læser, behandler og analyserer data i realtid** i Pandas.

🔗 **Forrige modul:** [05-time-series.md](05-time-series.md)  
🔜 **Næste modul:** [07-visualization.md](07-visualization.md)  

---

## ✅ **Trin 1: Simulér en strøm af realtidsdata**
Vi kan simulere en strøm af **måledata** med Pandas.

```python
import pandas as pd
import numpy as np
import time

# Opret en tom DataFrame til at gemme data
df = pd.DataFrame(columns=["Tidspunkt", "Måling"])

# Simulér realtidsmålinger
for i in range(10):
    ny_tid = pd.Timestamp.now()
    ny_måling = np.random.uniform(20, 25)  # Simuleret temperatur
    ny_række = pd.DataFrame({"Tidspunkt": [ny_tid], "Måling": [ny_måling]})
    
    df = pd.concat([df, ny_række], ignore_index=True)  # Tilføj ny måling
    
    print(df.tail(1))  # Vis den nyeste måling
    time.sleep(1)  # Simulér realtidsforsinkelse
```

✅ **Nu genererer vi realtidsdata!**  

---

## 🔄 **Trin 2: Glidende gennemsnit af realtidsdata**
Når vi arbejder med realtidsmålinger, kan vi **udglatte data for at reducere støj**.

```python
df["Glidende Gennemsnit"] = df["Måling"].rolling(window=3).mean()
print(df.tail(5))  # Vis de seneste 5 målinger
```

✅ **Nu kan vi analysere realtidsdata med et glidende gennemsnit!**  

---

## 📤 **Trin 3: Gem realtidsdata løbende**
Vi kan gemme vores målinger **efterhånden som vi indsamler dem**.

```python
df.to_csv("realtids_data.csv", index=False, mode="a", header=False)
print("Data gemt til realtids_data.csv!")
```

✅ **Nu gemmer vi realtidsmålinger i en CSV-fil!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Simuleret en **løbende strøm af realtidsmålinger**  
✔️ Anvendt **glidende gennemsnit** på realtidsdata  
✔️ Lært at **gemme realtidsmålinger løbende**  

🔜 **Fortsæt til næste modul:** [07-visualization.md](07-visualization.md), hvor vi lærer **at visualisere data med Pandas og Matplotlib**!  
