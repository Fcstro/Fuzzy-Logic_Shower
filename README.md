
# Fuzzy Logic System for Shower Water Temperature Control

This system utilizes fuzzy logic to determine the shower water temperature based on three input variables: initial water temperature, water pressure, and heater temperature. It adjusts the shower water temperature to achieve the desired comfort level.

Here's a simplified version of the fuzzy logic system for your Tkinter application, focusing only on the input variables, output variables, and fuzzy logic rules:

---
---
## Input Variables

 ### 1. Initial Water Temperature
  - **Cold**: 2°C - 15°C
  - **Mid-Temperature**: 16°C - 35°C
  - **Warm**: 36°C - 50°C
 ---
 ### 2. Water Pressure
  - **Low**: 20 - 41 psi
  - **Mid**: 42 - 62 psi
  - **High**: 63 - 85 psi
 ---
 ### 3. Heater Temperature
  - **Off**: Below 15°C
  - **Low**: 15°C - 30°C
  - **Mid**: 30°C - 45°C
  - **High**: 45°C - 60°C

 
---
---
## Output Variable

### Shower Water Temperature
- **Cold**: Below 15°C
- **Chilly**: 15°C - 25°C
- **Mid**: 26°C - 35°C
- **Warm**: 36°C - 49°C
- **Hot**: 50°C and above
---
---
## Fuzzy Logic Rules
---
 ### 1. When the Heater is Off (Heater Temp < 15°C):
  - **Cold Water**: Shower Water Temp is **Cold**
  - **Chilly Water**: Shower Water Temp is **Chilly**
  - **Mid Water**: Shower Water Temp is **Mid**
  - **Warm Water**: Shower Water Temp is **Warm**
  - **Hot Water**: Shower Water Temp is **Hot**
 ---
 ### 2. When the Heater is at Low Temperature (15°C - 30°C):
  - **Cold Water** AND **Low Pressure**: Shower Water Temp is **Chilly**
  - **Cold Water** AND **Mid Pressure**: Shower Water Temp is **Cold**
  - **Cold Water** AND **High Pressure**: Shower Water Temp is **Cold**
  - **Mid-Temperature Water** AND **Low Pressure**: Shower Water Temp is **Warm**
  - **Mid-Temperature Water** AND **Mid Pressure**: Shower Water Temp is **Mid**
  - **Mid-Temperature Water** AND **High Pressure**: Shower Water Temp is **Warm**
  - **Warm Water**: Shower Water Temp is **Warm**
 ---
 ### 3. When the Heater is at Mid Temperature (30°C - 45°C):
  - **Cold Water** AND **Low Pressure**: Shower Water Temp is **Warm**
  - **Cold Water** AND **Mid Pressure**: Shower Water Temp is **Mid**
  - **Cold Water** AND **High Pressure**: Shower Water Temp is **Chilly**
  - **Mid-Temperature Water** AND **Low Pressure**: Shower Water Temp is **Warm**
  - **Mid-Temperature Water** AND **Mid Pressure**: Shower Water Temp is **Warm**
  - **Mid-Temperature Water** AND **High Pressure**: Shower Water Temp is **Warm**
  - **Warm Water**: Shower Water Temp is **Hot**
 ---
 ### 4. When the Heater is at High Temperature (45°C - 60°C):
  - **Cold Water** AND **Low Pressure**: Shower Water Temp is **Warm**
  - **Cold Water** AND **Mid Pressure**: Shower Water Temp is **Mid**
  - **Cold Water** AND **High Pressure**: Shower Water Temp is **Chilly**
  - **Mid-Temperature Water** AND **Low Pressure**: Shower Water Temp is **Hot**
  - **Mid-Temperature Water** AND **Mid Pressure**: Shower Water Temp is **Warm**
  - **Mid-Temperature Water** AND **High Pressure**: Shower Water Temp is **Hot**
  - **Warm Water**: Shower Water Temp is **Hot**


---
___

