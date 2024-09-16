
# Fuzzy Logic System for Shower Water Temperature Control

This system utilizes fuzzy logic to determine the shower water temperature based on three input variables: initial water temperature, water pressure, and heater temperature. It adjusts the shower water temperature to achieve the desired comfort level.

## Input Variables

### Initial Water Temperature
- **Cold Water**: 2°C - 20°C
- **Mid-Temperature Water**: 17°C - 35°C
- **Warm Water**: 32°C - 50°C

### Water Pressure
- **Low Pressure**: 20-45 psi
- **Mid Pressure**: 40-65 psi
- **High Pressure**: 60-85 psi

### Heater Temperature
- **Off (Low)**: below 15°C
- **Low Heater Temperature**: 15°C - 25°C
- **Mid Heater Temperature**: 20°C - 45°C
- **High Heater Temperature**: 35°C - 60°C

## Output Variable

### Shower Water Temperature
- **Cold**: Below 15°C
- **Chilly**: 16°C - 25°C
- **Mid**: 26°C - 35°C
- **Warm**: 36°C - 45°C
- **Hot**: 46°C and above

## Fuzzy Logic Rules

### 1. When the Heater is Off (Heater Temp < 15°C):
- **Cold Water** AND **Low Pressure**: Shower Water Temp is **Cold**
- **Cold Water** AND **Mid Pressure**: Shower Water Temp is **Cold**
- **Cold Water** AND **High Pressure**: Shower Water Temp is **Cold**
- **Mid-Temperature Water** AND **Low Pressure**: Shower Water Temp is **Chilly**
- **Mid-Temperature Water** AND **Mid Pressure**: Shower Water Temp is **Chilly**
- **Mid-Temperature Water** AND **High Pressure**: Shower Water Temp is **Chilly**
- **Warm Water** AND **Low Pressure**: Shower Water Temp is **Mid**
- **Warm Water** AND **Mid Pressure**: Shower Water Temp is **Mid**
- **Warm Water** AND **High Pressure**: Shower Water Temp is **Mid**

### 2. When the Heater is at Low Temperature (15°C - 25°C):
- **Cold Water** AND **Low Pressure**: Shower Water Temp is **Chilly**
- **Cold Water** AND **Mid Pressure**: Shower Water Temp is **Chilly**
- **Cold Water** AND **High Pressure**: Shower Water Temp is **Chilly**
- **Mid-Temperature Water** AND **Low Pressure**: Shower Water Temp is **Mid**
- **Mid-Temperature Water** AND **Mid Pressure**: Shower Water Temp is **Mid**
- **Mid-Temperature Water** AND **High Pressure**: Shower Water Temp is **Mid**
- **Warm Water** AND **Low Pressure**: Shower Water Temp is **Warm**
- **Warm Water** AND **Mid Pressure**: Shower Water Temp is **Warm**
- **Warm Water** AND **High Pressure**: Shower Water Temp is **Warm**

### 3. When the Heater is at Mid Temperature (20°C - 45°C):
- **Cold Water** AND **Low Pressure**: Shower Water Temp is **Mid**
- **Cold Water** AND **Mid Pressure**: Shower Water Temp is **Mid**
- **Cold Water** AND **High Pressure**: Shower Water Temp is **Mid**
- **Mid-Temperature Water** AND **Low Pressure**: Shower Water Temp is **Warm**
- **Mid-Temperature Water** AND **Mid Pressure**: Shower Water Temp is **Warm**
- **Mid-Temperature Water** AND **High Pressure**: Shower Water Temp is **Warm**
- **Warm Water** AND **Low Pressure**: Shower Water Temp is **Hot**
- **Warm Water** AND **Mid Pressure**: Shower Water Temp is **Hot**
- **Warm Water** AND **High Pressure**: Shower Water Temp is **Hot**

### 4. When the Heater is at High Temperature (35°C - 60°C):
- **Cold Water** AND **Low Pressure**: Shower Water Temp is **Warm**
- **Cold Water** AND **Mid Pressure**: Shower Water Temp is **Warm**
- **Cold Water** AND **High Pressure**: Shower Water Temp is **Warm**
- **Mid-Temperature Water** AND **Low Pressure**: Shower Water Temp is **Hot**
- **Mid-Temperature Water** AND **Mid Pressure**: Shower Water Temp is **Hot**
- **Mid-Temperature Water** AND **High Pressure**: Shower Water Temp is **Hot**
- **Warm Water** AND **Low Pressure**: Shower Water Temp is **Hot**
- **Warm Water** AND **Mid Pressure**: Shower Water Temp is **Hot**
- **Warm Water** AND **High Pressure**: Shower Water Temp is **Hot**

---

