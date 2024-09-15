# Fuzzy Logic Rules for Heater Control System

## Fuzzy Sets

### Initial Water Temperature
- **Cold Water:** 4°C - 18°C
- **Mid-Temperature Water:** 15°C - 30°C
- **Warm Water:** 27°C - 46°C

### Water Pressure
- **Low Pressure:** 20 - 45 psi
- **Mid Pressure:** 40 - 65 psi
- **High Pressure:** 60 - 85 psi

### Heater Heat
- **Low Heater Temperature:** OFF - 22°C
- **Mid Heater Temperature:** 20°C - 27°C
- **High Heater Temperature:** 25°C - 32°C

### Shower Water Temperature
- **Cold:** below 15°C
- **Chilly:** 16°C - 20°C
- **Mid:** 21°C - 30°C
- **Warm:** 31°C - 40°C
- **Hot:** 41°C - 50°C

## Fuzzy Logic Rules

### When the heater is OFF (below 15°C heater temperature):
- **If Initial Water Temperature is Cold and Pressure is Low:** Shower Water Temperature = Cold
- **If Initial Water Temperature is Cold and Pressure is Mid:** Shower Water Temperature = Chilly
- **If Initial Water Temperature is Cold and Pressure is High:** Shower Water Temperature = Mid
- **If Initial Water Temperature is Mid and Pressure is Low:** Shower Water Temperature = Chilly
- **If Initial Water Temperature is Mid and Pressure is Mid:** Shower Water Temperature = Mid
- **If Initial Water Temperature is Mid and Pressure is High:** Shower Water Temperature = Warm
- **If Initial Water Temperature is Warm and Pressure is Low:** Shower Water Temperature = Mid
- **If Initial Water Temperature is Warm and Pressure is Mid:** Shower Water Temperature = Warm
- **If Initial Water Temperature is Warm and Pressure is High:** Shower Water Temperature = Hot

### When the heater is at Low Temperature (22°C):
- **If Initial Water Temperature is Cold and Pressure is Low:** Shower Water Temperature = Chilly
- **If Initial Water Temperature is Cold and Pressure is Mid:** Shower Water Temperature = Mid
- **If Initial Water Temperature is Cold and Pressure is High:** Shower Water Temperature = Warm
- **If Initial Water Temperature is Mid and Pressure is Low:** Shower Water Temperature = Mid
- **If Initial Water Temperature is Mid and Pressure is Mid:** Shower Water Temperature = Warm
- **If Initial Water Temperature is Mid and Pressure is High:** Shower Water Temperature = Hot
- **If Initial Water Temperature is Warm and Pressure is Low:** Shower Water Temperature = Warm
- **If Initial Water Temperature is Warm and Pressure is Mid:** Shower Water Temperature = Hot
- **If Initial Water Temperature is Warm and Pressure is High:** Shower Water Temperature = Hot

### When the heater is at Mid Temperature (27°C):
- **If Initial Water Temperature is Cold and Pressure is Low:** Shower Water Temperature = Mid
- **If Initial Water Temperature is Cold and Pressure is Mid:** Shower Water Temperature = Warm
- **If Initial Water Temperature is Cold and Pressure is High:** Shower Water Temperature = Warm
- **If Initial Water Temperature is Mid and Pressure is Low:** Shower Water Temperature = Warm
- **If Initial Water Temperature is Mid and Pressure is Mid:** Shower Water Temperature = Hot
- **If Initial Water Temperature is Mid and Pressure is High:** Shower Water Temperature = Hot
- **If Initial Water Temperature is Warm and Pressure is Low:** Shower Water Temperature = Hot
- **If Initial Water Temperature is Warm and Pressure is Mid:** Shower Water Temperature = Hot
- **If Initial Water Temperature is Warm and Pressure is High:** Shower Water Temperature = Hot

### When the heater is at High Temperature (32°C):
- **If Initial Water Temperature is Cold and Pressure is Low:** Shower Water Temperature = Warm
- **If Initial Water Temperature is Cold and Pressure is Mid:** Shower Water Temperature = Warm
- **If Initial Water Temperature is Cold and Pressure is High:** Shower Water Temperature = Hot
- **If Initial Water Temperature is Mid and Pressure is Low:** Shower Water Temperature = Hot
- **If Initial Water Temperature is Mid and Pressure is Mid:** Shower Water Temperature = Hot
- **If Initial Water Temperature is Mid and Pressure is High:** Shower Water Temperature = Hot
- **If Initial Water Temperature is Warm and Pressure is Low:** Shower Water Temperature = Hot
