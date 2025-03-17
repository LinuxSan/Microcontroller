# 🔄 **Modul 5: Glidende gennemsnit i realtid**

## 📌 **1️⃣ Hvad er et glidende gennemsnit?**
Når vi arbejder med realtidsmålinger fra **DHT22**, kan data variere på grund af **sensorstøj**.  
Et **glidende gennemsnit** hjælper med at **udglatte data**, så vi ser en mere stabil temperatur- og fugtighedskurve.

**Matematisk formel for glidende gennemsnit:**  
\(G_i = \frac{V_{i} + V_{i-1} + ... + V_{i-n}}{n}\)

✅ **Vi tager gennemsnittet af de seneste *n* målinger for at reducere støj.**  

---

## 📌 **2️⃣ Forstå `plt.ion()` - Interaktiv tilstand**
Når vi tegner en realtidsgraf, skal den **opdateres løbende** uden at blokere programmet.  
Dette gør vi med **`plt.ion()`**, som aktiverer **interaktiv tilstand** i Matplotlib.

🔹 **`plt.ion()` gør det muligt at opdatere grafer uden at stoppe programmet.**  
🔹 **`plt.ioff()` slår interaktiv tilstand fra, hvis vi vil stoppe opdateringen.**  

**Eksempel:**
```python
plt.ion()  # Slår interaktiv tilstand til
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()  # Vis grafen, som nu kan opdateres løbende
```

✅ **Nu forstår vi, hvorfor `plt.ion()` er nødvendig i realtidsplotning!**  

---

## 📌 **3️⃣ Tilføj glidende gennemsnit til realtidsgrafen**
Vi kan **tilføje en ekstra kurve** i vores plot, der viser det glidende gennemsnit.  

**Opdater din Python-kode med denne sektion:**  

```python
import serial
import pandas as pd
import matplotlib.pyplot as plt

ser = serial.Serial("COM3", 115200)  # Udskift med din serielle port
df = pd.DataFrame(columns=["Tid", "Temperatur", "Fugtighed"])

plt.ion()  # Aktiver interaktiv tilstand

while True:
    try:
        linje = ser.readline().decode("utf-8").strip().split(",")
        df.loc[len(df)] = [int(linje[0]), float(linje[1]), float(linje[2])]

        # Beregn glidende gennemsnit (vindue = 5 målinger)
        df["Glidende Temp"] = df["Temperatur"].rolling(window=5).mean()
        df["Glidende Fugt"] = df["Fugtighed"].rolling(window=5).mean()

        plt.clf()  # Rens grafen før vi tegner igen
        plt.plot(df["Tid"], df["Temperatur"], marker="o", linestyle="-", label="Temperatur")
        plt.plot(df["Tid"], df["Glidende Temp"], linestyle="--", label="Glidende Temp (5)")
        plt.plot(df["Tid"], df["Fugtighed"], marker="s", linestyle="-.", label="Fugtighed")
        plt.plot(df["Tid"], df["Glidende Fugt"], linestyle="--", label="Glidende Fugt (5)")

        plt.xlabel("Tid")
        plt.ylabel("Målinger")
        plt.title("DHT22: Temperatur og Fugtighed med Glidende Gennemsnit")
        plt.legend()
        plt.pause(1)  # Opdater grafen hvert sekund

    except Exception as e:
        print("Fejl ved læsning af data:", e)
```

✅ **Nu ser vi både rå data og en glattere gennemsnitskurve!**  

---

## 📌 **4️⃣ Hvad betyder det at rense grafen?**
I realtidsgrafer skal vi **slette den tidligere graf**, så vi ikke tegner ovenpå gamle data.  
Dette gør vi med **`plt.clf()`**, som **rydder grafen før vi tegner en ny version**.

🔹 **Uden `plt.clf()`** → Gamle data bliver stående og grafer overlapper.  
🔹 **Med `plt.clf()`** → Kun de nyeste målinger vises, og grafen forbliver ren.  

**Eksempel:**
```python
plt.clf()  # Ryd grafen for gamle data
plt.plot(df["Tid"], df["Temperatur"], label="Temperatur")
plt.legend()
plt.pause(1)  # Vent 1 sekund før næste opdatering
```

✅ **Nu forstår vi hvorfor `plt.clf()` er nødvendig i realtidsplotning!**  

---

## 📌 **5️⃣ Justér vinduet for glidende gennemsnit**
Vil du have **mindre støj men mere forsinkelse?** Øg vinduet!  
Vil du have **hurtigere respons men mere støj?** Reducér vinduet!  

Eksempel:  
```python
df["Glidende Temp"] = df["Temperatur"].rolling(window=10).mean()  # Vindue på 10 målinger
```

✅ **Tilpas grafens udglatning efter behov!**  

---

## 📌 **6️⃣ Fejlfinding**
🔹 **"Glidende gennemsnit viser NaN"**  
➡️ De første *n* målinger har ikke nok værdier til at beregne gennemsnit. Brug `min_periods=1`:  
```python
df["Glidende Temp"] = df["Temperatur"].rolling(window=5, min_periods=1).mean()
```

🔹 **"Grafen opdateres for langsomt"**  
➡️ Prøv et mindre vindue (`window=3`).  

🔹 **"Kurven er stadig for støjende"**  
➡️ Brug **eksponentiel glatning** (`ewm()`):
```python
df["Eksponentiel Temp"] = df["Temperatur"].ewm(alpha=0.3).mean()
```

✅ **Nu er vores realtidsgraf optimeret med glidende gennemsnit!**  

🚀 **Fortsæt til næste modul: [06-multiple-sensors.md](06-multiple-sensors.md)**  
