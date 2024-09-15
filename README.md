# Fuzzy-Logic_Shower

# Fuzzy Sets

 - # Inputs:

     ### INITIAL WATER TEMP 
    -  Cold Water: 2°C - 20°C
    - Mid-Temperature Water: 17°C - 35°C
    - Warm Water: 32°C - 50°C


     ## WATER PRESSURE
    - Low Pressure: 20-45 psi
    - Mid Pressure: 40-65 psi
    - High Pressure: 60-85 psi


     ## HEATER TEMP
    - Low Heater Temperature: 0°C - 25°C
    - Mid Heater Temperature: 20°C - 45°C
    - High Heater Temperature: 35°C - 60°C
    ---
    ---
  - # Outputs:

     ## SHOWER WATER
    - Cold: Below 10°C
    - Chilly: 10°C - 20°C
    - Mid: 20°C - 30°C
    - Warm: 30°C - 40°C
    - Hot: 40°C - 50°C
---
---
# Fuzzy Rules

- ## Conditions

    ---
  ### 1. IF Initial Water Temp is Cold
    ---
    - **And Water Pressure is Low**
    - WHILE Heater Temp is Low THEN Shower Water is Cold
    - WHILE Heater Temp is Mid THEN Shower Water is Chilly
    - WHILE Heater Temp is High THEN Shower Water is Mid

    - **And Water Pressure is Mid**
    - WHILE Heater Temp is Low THEN Shower Water is Chilly
    - WHILE Heater Temp is Mid THEN Shower Water is Mid
    - WHILE Heater Temp is High THEN Shower Water is Warm

    - **And Water Pressure is High**
    - WHILE Heater Temp is Low THEN Shower Water is Chilly
    - WHILE Heater Temp is Mid THEN Shower Water is Warm
    - WHILE Heater Temp is High THEN Shower Water is Hot
    ---
    ---
    ### 2. IF Initial Water Temp is Mid-Temperature
    ---
    - **And Water Pressure is Low**
    - WHILE Heater Temp is Low THEN Shower Water is Chilly
    - WHILE Heater Temp is Mid THEN Shower Water is Mid
    - WHILE Heater Temp is High THEN Shower Water is Warm

    - **And Water Pressure is Mid**
    - WHILE Heater Temp is Low THEN Shower Water is Mid
    - WHILE Heater Temp is Mid THEN Shower Water is Warm
    - WHILE Heater Temp is High THEN Shower Water is Hot

    - **And Water Pressure is High**
    - WHILE Heater Temp is Low THEN Shower Water is Mid
    - WHILE Heater Temp is Mid THEN Shower Water is Hot
    - WHILE Heater Temp is High THEN Shower Water is Hot
    ---
    ---
    ### 3. IF Initial Water Temp is Warm
    ---

    - **And Water Pressure is Low**
    - WHILE Heater Temp is Low THEN Shower Water is Mid
    - WHILE Heater Temp is Mid THEN Shower Water is Warm
    - WHILE Heater Temp is High THEN Shower Water is Hot

    - **And Water Pressure is Mid**
    - WHILE Heater Temp is Low THEN Shower Water is Warm
    - WHILE Heater Temp is Mid THEN Shower Water is Hot
    - WHILE Heater Temp is High THEN Shower Water is Hot

    - **And Water Pressure is High**
    - WHILE Heater Temp is Low THEN Shower Water is Warm
    - WHILE Heater Temp is Mid THEN Shower Water is Hot
    - WHILE Heater Temp is High THEN Shower Water is Hot
    ---
---