import tkinter as tk
import pickle
import numpy as np

# Load model and class names from pickle file
with open("MODEL 1.pkl", "rb") as file:
    model, class_names = pickle.load(file)

# Prediction function
def predict_flower():
    try:
        # Convert entries to float array
        features = [float(entry.get()) for entry in entries]
        features = np.array([features])

        # Make prediction
        prediction = model.predict(features)[0]
        result = class_names[prediction]

        # Show result in GUI (not popup)
        result_label.config(text=f"Predicted Iris species: {result.capitalize()}", fg="green")

    except ValueError:
        result_label.config(text="Please enter valid numbers for all fields.", fg="red")

# GUI setup
root = tk.Tk()
root.title("Iris Flower Predictor")

feature_names = ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)"]
entries = []

# Create input fields
for name in feature_names:
    frame = tk.Frame(root)
    frame.pack(pady=2)
    
    label = tk.Label(frame, text=name, width=20, anchor="w")
    label.pack(side=tk.LEFT)
    
    entry = tk.Entry(frame, width=20)
    entry.pack(side=tk.RIGHT)
    
    entries.append(entry)

# Predict button
predict_button = tk.Button(root, text="Predict", command=predict_flower)
predict_button.pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
