import tkinter as tk
from PIL import Image, ImageTk
import os

def resize_image(image, size):
    return image.resize(size, Image.LANCZOS)

def create_scale(root, from_, to_, orient, relx, rely, command):
    scale = tk.Scale(root, from_=from_, to_=to_, orient=orient, width=13, length=150, cursor="hand2", command=command)
    scale.place(relx=relx, rely=rely)
    return scale

def label_factory(root, text_, relx, rely):
    label = tk.Label(root, text=text_, font=("Arial", 14), justify="center", bg='#ffde59')
    label.place(relx=relx, rely=rely)
    return label

# Fuzzy membership functions
def fuzzify_water_pressure(pressure):
    if pressure <= 41:
        return ('Low', 1)
    elif 41 < pressure <= 62:
        return ('Mid', (62 - pressure) / 21)
    else:
        return ('High', (pressure - 62) / 23)

def fuzzify_heater_temp(heater_temp):
    if heater_temp < 15:
        return ('Off', 1)
    elif 15 <= heater_temp < 30:
        return ('Low', (30 - heater_temp) / 15)
    elif 30 <= heater_temp < 45:
        return ('Mid', (45 - heater_temp) / 15)
    else:
        return ('High', (heater_temp - 45) / 15)

def fuzzify_initial_temp(temp):
    if temp <= 15:
        return ('Cold', 1)
    elif 15 < temp <= 35:
        return ('Mid-Temperature', (35 - temp) / 14)
    elif 35 < temp < 50:
        return ('Warm', (temp - 35) / 15)
    else:
        return ('Hot', 1)

# Apply fuzzy logic rules
def apply_fuzzy_rules(initial_temp, water_press, heater_temp):
    if heater_temp[0] == 'Off':
        # Use the initial temperature scale to determine the description
        if initial_temp[0] == 'Cold':
            return 'Cold', 'Below 15°C'
        elif initial_temp[0] == 'Mid-Temperature':
            return 'Mid-Temperature', '15°C - 35°C'
        elif initial_temp[0] == 'Warm':
            return 'Warm', '35°C - 49°C'
        else:
            return 'Hot', '50°C and Above'
        
    elif heater_temp[0] == 'Low':
        if water_press[0] == 'Low':
            if initial_temp[0] == 'Cold':
                return 'Chilly', '15°C - 25°C'
            elif initial_temp[0] == 'Mid-Temperature':
                return 'Warm', '30°C - 40°C'
            elif initial_temp[0] == 'Warm':
                return 'Warm', '35°C - 49°C'
            elif initial_temp[0] == 'Hot':
                return 'Hot', '50°C and Above'
        elif water_press[0] == 'Mid':
            if initial_temp[0] == 'Cold':
                return 'Cool', '20°C - 30°C'
            elif initial_temp[0] == 'Mid-Temperature':
                return 'Mid', '25°C - 35°C'
            elif initial_temp[0] == 'Warm':
                return 'Warm', '35°C - 49°C'
            elif initial_temp[0] == 'Hot':
                return 'Hot', '50°C and Above'
        else:  # High pressure
            if initial_temp[0] == 'Cold':
                return 'Cool', '20°C - 30°C'
            elif initial_temp[0] == 'Mid-Temperature':
                return 'Chilly', '15°C - 25°C'
            elif initial_temp[0] == 'Warm':
                return 'Mid', '25°C - 35°C'
            elif initial_temp[0] == 'Hot':
                return 'Warm', '35°C - 49°C                             '

    elif heater_temp[0] == 'Mid':
        if water_press[0] == 'Low':
            if initial_temp[0] == 'Cold':
                return 'Warm', '30°C - 40°C'
            elif initial_temp[0] == 'Mid-Temperature':
                return 'Warm', '35°C - 49°C'
            elif initial_temp[0] == 'Warm':
                return 'Hot', '50°C and Above'
            elif initial_temp[0] == 'Hot':
                return 'Hot', '50°C and Above'
        elif water_press[0] == 'Mid':
            if initial_temp[0] == 'Cold':
                return 'Mid', '25°C - 35°C'
            elif initial_temp[0] == 'Mid-Temperature':
                return 'Warm', '35°C - 49°C'
            elif initial_temp[0] == 'Warm':
                return 'Hot', '50°C and Above'
            elif initial_temp[0] == 'Hot':
                return 'Hot', '50°C and Above'
        else:  # High pressure
            if initial_temp[0] == 'Cold':
                return 'Chilly', '15°C - 25°C'
            elif initial_temp[0] == 'Mid-Temperature':
                return 'Mid', '25°C - 35°C'
            elif initial_temp[0] == 'Warm':
                return 'Warm', '35°C - 49°C'
            elif initial_temp[0] == 'Hot':
                return 'Hot', '50°C and Above'

    elif heater_temp[0] == 'High':
        if water_press[0] == 'Low':
            if initial_temp[0] == 'Cold':
                return 'Warm', '35°C - 49°C'
            elif initial_temp[0] == 'Mid-Temperature':
                return 'Hot', '50°C and Above'
            elif initial_temp[0] == 'Warm':
                return 'Hot', '50°C and Above'
            elif initial_temp[0] == 'Hot':
                return 'Hot', '50°C and Above'
        elif water_press[0] == 'Mid':
            if initial_temp[0] == 'Cold':
                return 'Mid', '25°C - 35°C'
            elif initial_temp[0] == 'Mid-Temperature':
                return 'Warm', '35°C - 49°C'
            elif initial_temp[0] == 'Warm':
                return 'Hot', '50°C and Above'
            elif initial_temp[0] == 'Hot':
                return 'Hot', '50°C and Above'
        else:  # High pressure
            if initial_temp[0] == 'Cold':
                return 'Chilly', '15°C - 25°C'
            elif initial_temp[0] == 'Mid-Temperature':
                return 'Mid', '25°C - 35°C'
            elif initial_temp[0] == 'Warm':
                return 'Hot', '50°C and Above'
            elif initial_temp[0] == 'Hot':
                return 'Hot', '50°C and Above'

def calculate_shower_temp(event=None):
    initial_temp_value = initialTemp.get()
    water_press_value = waterPress.get()
    heater_temp_value = heaterTemp.get()

    initial_temp_fuzzy = fuzzify_initial_temp(initial_temp_value)
    water_press_fuzzy = fuzzify_water_pressure(water_press_value)
    heater_temp_fuzzy = fuzzify_heater_temp(heater_temp_value)

    # Apply fuzzy logic rules
    shower_temp, temp_range = apply_fuzzy_rules(initial_temp_fuzzy, water_press_fuzzy, heater_temp_fuzzy)

    # Update the label with the calculated temperature
    result_label.config(text=f"Shower Water Temperature: {shower_temp} ({temp_range})")
    
    print(initial_temp_fuzzy)
    print(water_press_value)
    print(heater_temp_value)

def main():
    root = tk.Tk()
    root.title("Full Screen Tkinter App")
    root.attributes('-fullscreen', True)

    def update_bg_image(event=None):
        width = root.winfo_width()
        height = root.winfo_height()
        original_image = Image.open("simulator-images/bg.png")
        resized_image = resize_image(original_image, (width, height))
        bg_image = ImageTk.PhotoImage(resized_image)
        bg_label.config(image=bg_image)
        bg_label.image = bg_image

    bg_label = tk.Label(root)
    bg_label.place(relwidth=1, relheight=1)
    root.bind('<Configure>', update_bg_image)
    update_bg_image()

    label_factory(root, 'Initial Water Temp Cool (°C)', relx=0.745, rely=0.0575)
    global initialTemp
    initialTemp = create_scale(root, from_=2, to_=50, orient='horizontal', relx=0.775, rely=0.1, command=calculate_shower_temp)

    label_factory(root, 'Water Pressure (psi)', relx=0.7675, rely=0.1575)
    global waterPress
    waterPress = create_scale(root, from_=20, to_=85, orient='horizontal', relx=0.775, rely=0.2, command=calculate_shower_temp)

    label_factory(root, 'Shower Heater Heat (°C)' , relx=0.755, rely=0.2575)
    global heaterTemp
    heaterTemp = create_scale(root, from_=0, to_=60, orient='horizontal', relx=0.775, rely=0.3, command=calculate_shower_temp)

    global result_label
    result_label = label_factory(root, 'Shower Water Temperature: ', relx=0.68, rely=0.945)

    os.system('cls')

    root.mainloop()

if __name__ == "__main__":
    main()
