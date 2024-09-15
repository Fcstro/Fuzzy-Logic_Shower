# Fuzzy-Logic_Shower

# Define Fuzzy Sets

## Inputs:

# INITIAL WATER TEMP 
-  Cold Water: 2°C - 20°C
- Mid-Temperature Water: 17°C - 35°C
- Warm Water: 32°C - 50°C


# WATER PRESSURE
- Low Pressure: 20-45 psi
- Mid Pressure: 40-65 psi
- High Pressure: 60-85 psi


# HEATER TEMP
- Low Heater Temperature: 0°C - 25°C
- Mid Heater Temperature: 20°C - 45°C
- High Heater Temperature: 35°C - 60°C

## Outputs:

# SHOWER WATER
- Cold: Below 10°C
- Chilly: 10°C - 20°C
- Mid: 20°C - 30°C
- Warm: 30°C - 40°C
- Hot: 40°C - 50°C

## Fuzzy Rules

- If Initial Water Temp is Cold and Water Pressure is Low and Heater Temp is Low, then Shower Water is Cold.

- If Initial Water Temp is Cold and Water Pressure is Low and Heater Temp is Mid, then Shower Water is Chilly.

- If Initial Water Temp is Cold and Water Pressure is Low and Heater Temp is High, then Shower Water is Mid.

- If Initial Water Temp is Cold and Water Pressure is Mid and Heater Temp is Low, then Shower Water is Chilly.

- If Initial Water Temp is Cold and Water Pressure is Mid and Heater Temp is Mid, then Shower Water is Mid.

- If Initial Water Temp is Cold and Water Pressure is Mid and Heater Temp is High, then Shower Water is Warm.

- If Initial Water Temp is Cold and Water Pressure is High and Heater Temp is Low, then Shower Water is Mid.

- If Initial Water Temp is Cold and Water Pressure is High and Heater Temp is Mid, then Shower Water is Warm.

- If Initial Water Temp is Cold and Water Pressure is High and Heater Temp is High, then Shower Water is Hot.

- If Initial Water Temp is Mid-Temperature and Water Pressure is Low and Heater Temp is Low, then Shower Water is Chilly.

- If Initial Water Temp is Mid-Temperature and Water Pressure is Low and Heater Temp is Mid, then Shower Water is Mid.

- If Initial Water Temp is Mid-Temperature and Water Pressure is Low and Heater Temp is High, then Shower Water is Warm.

- If Initial Water Temp is Mid-Temperature and Water Pressure is Mid and Heater Temp is Low, then Shower Water is Mid.

- If Initial Water Temp is Mid-Temperature and Water Pressure is Mid and Heater Temp is Mid, then Shower Water is Warm.

- If Initial Water Temp is Mid-Temperature and Water Pressure is Mid and Heater Temp is High, then Shower Water is Hot.

- If Initial Water Temp is Mid-Temperature and Water Pressure is High and Heater Temp is Low, then Shower Water is Warm.

- If Initial Water Temp is Mid-Temperature and Water Pressure is High and Heater Temp is Mid, then Shower Water is Hot.

- If Initial Water Temp is Mid-Temperature and Water Pressure is High and Heater Temp is High, then Shower Water is Hot.

- If Initial Water Temp is Warm and Water Pressure is Low and Heater Temp is Low, then Shower Water is Mid.

- If Initial Water Temp is Warm and Water Pressure is Low and Heater Temp is Mid, then Shower Water is Warm.

- If Initial Water Temp is Warm and Water Pressure is Low and Heater Temp is High, then Shower Water is Hot.

- If Initial Water Temp is Warm and Water Pressure is Mid and Heater Temp is Low, then Shower Water is Warm.

- If Initial Water Temp is Warm and Water Pressure is Mid and Heater Temp is Mid, then Shower Water is Hot.

- If Initial Water Temp is Warm and Water Pressure is Mid and Heater Temp is High, then Shower Water is Hot.

- If Initial Water Temp is Warm and Water Pressure is High and Heater Temp is Low, then Shower Water is Hot.

- If Initial Water Temp is Warm and Water Pressure is High and Heater Temp is Mid, then Shower Water is Hot.

- If Initial Water Temp is Warm and Water Pressure is High and Heater Temp is High, then Shower Water is Hot.