import tkinter as tk
from PIL import Image, ImageTk
import os
import random

def resize_image(image, size):
    return image.resize(size, Image.LANCZOS)

def create_scale(canvas, from_, to_, orient, relx, rely, command):
    scale = tk.Scale(canvas, from_=from_, to_=to_, orient=orient, width=13, length=150, cursor="hand2", command=command)
    scale.place(relx=relx, rely=rely, anchor=tk.CENTER)
    return scale

def label_factory(canvas, text_, relx, rely):
    label = tk.Label(canvas, text=text_, font=("Arial", 14), justify="center", bg='#ffde59')
    label.place(relx=relx, rely=rely, anchor=tk.CENTER)
    return label

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

def apply_fuzzy_rules(initial_temp, water_press, heater_temp):
    if heater_temp[0] == 'Off':
        if initial_temp_value <= 15:
            return 'Cold', 'Below 15°C'
        elif 15 < initial_temp_value <= 25:
            return 'Chilly', '16°C - 25°C'
        elif 25 < initial_temp_value <= 35:
            return 'Mid', '26°C - 35°C'
        elif 35 < initial_temp_value <= 49:
            return 'Warm', '36°C - 49°C'
        else:
            return 'Hot', '50°C and Above'
    elif heater_temp[0] == 'Low':
        if water_press[0] == 'Low':
            if initial_temp[0] == 'Cold':
                return 'Chilly', '16°C - 25°C'
            elif initial_temp[0] == 'Mid-Temperature':
                return 'Warm', '36°C - 49°C'
            elif initial_temp[0] == 'Warm':
                return 'Warm', '36°C - 49°C'
            elif initial_temp[0] == 'Hot':
                return 'Hot', '50°C and Above'
        elif water_press[0] == 'Mid':
            if initial_temp[0] == 'Cold':
                return 'Cold', 'Below 15°C'
            elif initial_temp[0] == 'Mid-Temperature':
                return 'Mid', '26°C - 35°C'
            elif initial_temp[0] == 'Warm':
                return 'Warm', '36°C - 49°C'
            elif initial_temp[0] == 'Hot':
                return 'Hot', '50°C and Above'
        else:
            if initial_temp[0] == 'Cold':
                return 'Cold', 'Below 15°C'
            elif initial_temp[0] == 'Mid-Temperature':
                return 'Chilly', '16°C - 25°C'
            elif initial_temp[0] == 'Warm':
                return 'Mid', '26°C - 35°C'
            elif initial_temp[0] == 'Hot':
                return 'Warm', '36°C - 49°C'
    elif heater_temp[0] == 'Mid':
        if water_press[0] == 'Low':
            if initial_temp[0] == 'Cold':
                return 'Warm', '36°C - 49°C'
            elif initial_temp[0] == 'Mid-Temperature':
                return 'Warm', '36°C - 49°C'
            elif initial_temp[0] == 'Warm':
                return 'Hot', '50°C and Above'
            elif initial_temp[0] == 'Hot':
                return 'Hot', '50°C and Above'
        elif water_press[0] == 'Mid':
            if initial_temp[0] == 'Cold':
                return 'Mid', '26°C - 35°C'
            elif initial_temp[0] == 'Mid-Temperature':
                return 'Warm', '36°C - 49°C'
            elif initial_temp[0] == 'Warm':
                return 'Hot', '50°C and Above'
            elif initial_temp[0] == 'Hot':
                return 'Hot', '50°C and Above'
        else:
            if initial_temp[0] == 'Cold':
                return 'Chilly', '16°C - 25°C'
            elif initial_temp[0] == 'Mid-Temperature':
                return 'Mid', '26°C - 35°C'
            elif initial_temp[0] == 'Warm':
                return 'Warm', '36°C - 49°C'
            elif initial_temp[0] == 'Hot':
                return 'Hot', '50°C and Above'
            
            
    elif heater_temp[0] == 'High':
        if water_press[0] == 'Low':
            if initial_temp[0] == 'Cold':
                return 'Warm', '36°C - 49°C'
            elif initial_temp[0] == 'Mid-Temperature':
                return 'Hot', '50°C and Above'
            elif initial_temp[0] == 'Warm':
                return 'Hot', '50°C and Above'
            elif initial_temp[0] == 'Hot':
                return 'Hot', '50°C and Above'
        elif water_press[0] == 'Mid':
            if initial_temp[0] == 'Cold':
                return 'Mid', '26°C - 35°C'
            elif initial_temp[0] == 'Mid-Temperature':
                return 'Warm', '36°C - 49°C'
            elif initial_temp[0] == 'Warm':
                return 'Hot', '50°C and Above'
            elif initial_temp[0] == 'Hot':
                return 'Hot', '50°C and Above'
        else:
            if initial_temp[0] == 'Cold':
                return 'Chilly', '16°C - 25°C'
            elif initial_temp[0] == 'Mid-Temperature':
                return 'Mid', '26°C - 35°C'
            elif initial_temp[0] == 'Warm':
                return 'Hot', '50°C and Above'
            elif initial_temp[0] == 'Hot':
                return 'Hot', '50°C and Above'

def calculate_shower_temp(event=None):
    global initial_temp_value
    initial_temp_value = initialTemp.get()
    water_press_value = waterPress.get()
    heater_temp_value = heaterTemp.get()

    initial_temp_fuzzy = fuzzify_initial_temp(initial_temp_value)
    water_press_fuzzy = fuzzify_water_pressure(water_press_value)
    heater_temp_fuzzy = fuzzify_heater_temp(heater_temp_value)

    shower_temp, temp_range = apply_fuzzy_rules(initial_temp_fuzzy, water_press_fuzzy, heater_temp_fuzzy)

    result_label.config(text=f"Shower Water Temperature: {shower_temp} ({temp_range})")
    
    print(initial_temp_fuzzy)
    print(water_press_value)
    print(heater_temp_value)

    shower_temp, temp_range = apply_fuzzy_rules(initial_temp_fuzzy, water_press_fuzzy, heater_temp_fuzzy)

    result_label.config(text=f"Shower Water Temperature: {shower_temp} ({temp_range})")
    
    update_animation_image()
    update_picture()

def update_animation_image():
    pressure = waterPress.get()
    if pressure <= 41:
        image_file = 'low-pres.png'
    elif 41 < pressure <= 62:
        image_file = 'mid-pres.png'
    else:
        image_file = 'high-pres.png'
    
    image_path = os.path.join('simulator-images', image_file)
    image = Image.open(image_path)
    image = resize_image(image, (image_width, image_height))
    global tk_image
    tk_image = ImageTk.PhotoImage(image)

def move_images():
    global image_ids
    images_to_remove = []
    for img_id, speed in image_ids:
        canvas.move(img_id, 0, speed)
        x, y = canvas.coords(img_id)
        if y > canvas.winfo_height():
            images_to_remove.append(img_id)
    for img_id in images_to_remove:
        canvas.delete(img_id)
        image_ids = [item for item in image_ids if item[0] != img_id]
    root.after(50, move_images)

def add_new_image():
    global image_ids
    pressure = waterPress.get()
    speed = calculate_speed(pressure)
    
    relative_positions = [
        (0.315, 0.28),(0.320, 0.28),(0.325, 0.28),
        (0.330, 0.28),(0.350, 0.28),(0.355, 0.28),
        (0.360, 0.28),(0.365, 0.28),(0.370, 0.28),
    ]
    
    relx, rely = random.choice(relative_positions)
    
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    image_x = relx * canvas_width
    image_y = rely * canvas_height
    
    image_id = canvas.create_image(image_x, image_y, anchor=tk.NW, image=tk_image)
    image_ids.append((image_id, speed))
    root.after(150, add_new_image)

def calculate_speed(pressure):
    if pressure <= 41:
        return 50
    elif 41 < pressure <= 62:
        return 70
    else:
        return 90

def update_picture():
    global tk_picture
    
    shower_temp = result_label.cget("text").split(': ')[1].split(' ')[0]
    if shower_temp == 'Cold':
        image_file = 'very-cold.png'
    elif shower_temp == 'Chilly':
        image_file = 'slightly-cold.png'
    elif shower_temp == 'Mid-Temperature':
        image_file = 'mid.png'
    elif shower_temp == 'Mid':
        image_file = 'mid.png'
    elif shower_temp == 'Warm':
        image_file = 'slightly-hot.png'
    elif shower_temp == 'Cool':
        image_file = 'cool.png'
    else:
        image_file = 'very-hot.png'
    
    image_path = os.path.join('simulator-images', image_file)
    image = Image.open(image_path)
    image = resize_image(image, (image_width * 6, image_height * 6))

    tk_picture = ImageTk.PhotoImage(image)
    
    canvas.delete("current_image")

    relx, rely = 0.4, 0.7
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    image_x = relx * canvas_width
    image_y = rely * canvas_height
    
    canvas.create_image(image_x, image_y, image=tk_picture, tags="current_image")

def main():
    global root, canvas, initialTemp, waterPress, heaterTemp, result_label, image_ids, tk_image, image_width, image_height

    root = tk.Tk()
    root.title("Full Screen Tkinter App")
    root.attributes('-fullscreen', True)

    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack(fill=tk.BOTH, expand=True)

    bg_image_path = 'simulator-images/bg.png'
    bg_image = Image.open(bg_image_path)
    bg_image = resize_image(bg_image, (root.winfo_screenwidth(), root.winfo_screenheight()))
    bg_photo = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

    label_factory(canvas, 'Initial Water Temp Cool (°C)', relx=0.825, rely=0.045)
    initialTemp = create_scale(canvas, from_=2, to_=50, orient='horizontal', relx=0.825, rely=0.1, command=calculate_shower_temp)

    label_factory(canvas, 'Water Pressure (psi)', relx=0.825, rely=0.195)
    waterPress = create_scale(canvas, from_=20, to_=85, orient='horizontal', relx=0.825, rely=0.25, command=calculate_shower_temp)

    label_factory(canvas, 'Shower Heater Heat (°C)' , relx=0.825, rely=0.345)
    heaterTemp = create_scale(canvas, from_=0, to_=60, orient='horizontal', relx=0.825, rely=0.40, command=calculate_shower_temp)

    result_label = label_factory(canvas, 'Shower Water Temperature: ', relx=0.825, rely=0.945)

    image_width = root.winfo_screenwidth() // 8
    image_height = root.winfo_screenheight() // 6
    update_animation_image()
    image_ids = []

    move_images()
    add_new_image()

    root.after(100, calculate_shower_temp)

    root.mainloop()

if __name__ == "__main__":
    main()
