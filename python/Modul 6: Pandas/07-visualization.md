# 📊 Modul 7: Visualisering af data med Pandas og Matplotlib

## 📌 **Introduktion**
For at forstå måledata bedre er det ofte en god idé at **visualisere dem**.  
I dette modul lærer vi at **plotte data med Pandas og Matplotlib**.

🔗 **Forrige modul:** [06-realtime-processing.md](06-realtime-processing.md)  
🔜 **Næste modul:** [08-next-steps.md](08-next-steps.md)  

---

## ✅ **Trin 1: Opret en simpel graf**
Vi kan bruge **Matplotlib** til at plotte en Pandas DataFrame.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Simuler nogle måledata
data = {
    "Tidspunkt": pd.date_range(start="2024-03-01", periods=10, freq="D"),
    "Måling": [20, 21, 22, 21, 23, 24, 25, 26, 27, 28]
}

df = pd.DataFrame(data)

# Plot data
plt.plot(df["Tidspunkt"], df["Måling"], marker="o", linestyle="-")
plt.xlabel("Tid")
plt.ylabel("Temperatur (°C)")
plt.title("Temperaturmålinger over tid")
plt.grid(True)
plt.show()
```

✅ **Nu har vi plottet en simpel tidsserie!**  

---

## 🔄 **Trin 2: Glidende gennemsnit i et plot**
For at **udglatte data** kan vi tilføje en **glidende gennemsnitskurve**.

```python
df["Glidende Gennemsnit"] = df["Måling"].rolling(window=3).mean()

plt.plot(df["Tidspunkt"], df["Måling"], marker="o", linestyle="-", label="Rå data")
plt.plot(df["Tidspunkt"], df["Glidende Gennemsnit"], linestyle="--", label="Glidende gennemsnit")
plt.xlabel("Tid")
plt.ylabel("Temperatur (°C)")
plt.title("Temperatur med glidende gennemsnit")
plt.legend()
plt.grid(True)
plt.show()
```

✅ **Nu kan vi vise både rå data og en glidende gennemsnitskurve!**  

---

## 📊 **Trin 3: Histogram af måledata**
Hvis vi vil **se fordelingen af måledata**, kan vi bruge et histogram.

```python
plt.hist(df["Måling"], bins=5, edgecolor="black")
plt.xlabel("Temperatur (°C)")
plt.ylabel("Antal målinger")
plt.title("Histogram over temperaturmålinger")
plt.grid(True)
plt.show()
```

✅ **Nu kan vi se fordelingen af måledata!**  

---

## ✅ **Hvad har vi opnået?**
✔️ Plottet **måledata over tid**  
✔️ Tilføjet **glidende gennemsnit til et plot**  
✔️ Visualiseret **fordelingen af måledata med et histogram**  

🔜 **Fortsæt til næste modul:** [08-next-steps.md](08-next-steps.md), hvor vi udforsker **avancerede anvendelser og næste skridt**!  
