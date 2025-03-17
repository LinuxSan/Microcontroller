# 🔌 Modul 06: Læs Sensor-Data via Seriel Port

## 📌 Hvad lærer du i dette modul?
✔️ Hvordan du **læser data fra en seriel port** (f.eks. fra en ESP32 eller Arduino)  
✔️ Hvordan du **visualiserer real-time data fra en sensor**  
✔️ Hvordan du **filtrerer data for bedre læsbarhed**  

---

## 📌 Trin 1: Krav til seriel forbindelse
For at læse sensor-data fra en enhed som en **ESP32** eller **Arduino**, skal vi bruge en **USB-seriel forbindelse**.

### 🔧 **Forudsætninger**
✅ En enhed, der sender seriel data (ESP32, Arduino, etc.)  
✅ En sensor, f.eks. en **DHT22** (temperatur og fugtighed)  
✅ `pyserial`-biblioteket installeret:
```bash
pip install pyserial
```

---

## 📌 Trin 2: Hvad forventer vi af seriel data?
Vi forventer, at enheden sender JSON-data i dette format:
```json
{"temperature": 22.5, "humidity": 48.0}
```

Hvis din enhed sender en anden struktur, skal vi **tilpasse Python-koden**.

---

## 📌 Trin 3: Læs og Visualiser Sensor-Data i Real-Time
Nedenstående kode **læser real-time data fra seriel porten** og **animerer plottet**.

```python
import serial
import json
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Åbn seriel port (tilpas denne til din enheds port)
# Ved Linux udskift COM3 med /dev/ttyUSB0
ser = serial.Serial('COM3', 115200, timeout=1)

# Opret figur og akse
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(15, 30)  # Temperaturinterval

xdata, ydata = [], []
ln, = ax.plot([], [], 'r-', label="Temperatur")

def init():
    ln.set_data([], [])
    return ln,

def update(frame):
    line = ser.readline().decode(errors='ignore').strip()
    try:
        data = json.loads(line)  # Konverter JSON-streng til Python-dictionary
        xdata.append(frame)
        ydata.append(data["temperature"])
        ln.set_data(xdata[-100:], ydata[-100:])  # Vis kun de seneste 100 målinger
    except:
        pass
    return ln,

# Opret animation
ani = FuncAnimation(fig, update, frames=range(1000), init_func=init, interval=500, blit=False)

plt.legend()
plt.show()
```

---

## 🔥 Hvordan fungerer koden?
1️⃣ **Vi åbner den serielle port:**  
   ```python
   ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
   ```
   - Porten `/dev/ttyUSB0` bruges til Linux/Mac, på Windows kan den være `COM3` eller `COM4`.  
   - Baudraten er `115200` (afhængig af din enhed).  

2️⃣ **Vi læser data fra den serielle port:**  
   ```python
   line = ser.readline().decode(errors='ignore').strip()
   ```
   - Dette læser **én linje ad gangen** fra enheden.  
   - `decode(errors='ignore')` sikrer, at fejl ikke bryder programmet.  

3️⃣ **Vi parser JSON-data:**  
   ```python
   data = json.loads(line)
   ```
   - Hvis enheden sender `{ "temperature": 22.5, "humidity": 48.0 }`, gemmes det som en Python-dictionary.

4️⃣ **Vi opdaterer plottet i realtid:**  
   ```python
   ln.set_data(xdata[-100:], ydata[-100:])
   ```
   - Vi **holder kun de seneste 100 målinger** for at holde grafen ren.  

---

## ✅ Opgaver
1️⃣ Kør koden og se real-time temperaturgrafen.  
2️⃣ Tilføj en **blå linje for fugtighedsmålinger**.  
3️⃣ Tilpas `timeout=1` i `serial.Serial()` – hvad sker der?  
4️⃣ Gem dataene i en **CSV-fil** i realtid.  

---

🔹 **Når du har forstået dette, er du klar til næste modul! 🚀**
