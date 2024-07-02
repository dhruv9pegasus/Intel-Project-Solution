import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps, ImageTk
import time
import cv2

# Initialize the main window
root = tk.Tk()
root.title("Image Pixelator")
root.geometry("800x600")

# Set the favicon to a pixelation icon 
icon_path = r'C:\Users\DHRUV M DHAROD\Downloads\favicon (1).ico'
root.iconbitmap(icon_path)

# Global variable to store the uploaded image
uploaded_image = None
uploaded_image_path = None

# Function to upload an image with a simulated animation
def upload_image():
    global uploaded_image, uploaded_image_path
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    if file_path:
        # Simulate an animation by updating the label text
        uploading_label.config(text="Uploading...", fg="blue")
        root.update_idletasks()  # Update the GUI immediately

        # Simulate a delay to show progress
        time.sleep(2)

        uploaded_image_path = file_path
        uploaded_image = Image.open(file_path)
        img_display = ImageTk.PhotoImage(uploaded_image.resize((400, 400)))  # Displaying the image as a thumbnail
        img_label.config(image=img_display)
        img_label.image = img_display

        # Reset label after upload
        uploading_label.config(text="Image uploaded successfully!", fg="green")
        messagebox.showinfo("Image Uploaded", "Image uploaded successfully!")

# Function to delete the uploaded image with a simulated animation
def delete_image():
    global uploaded_image, uploaded_image_path
    # Simulate an animation by updating the label text
    uploading_label.config(text="Deleting...", fg="blue")
    root.update_idletasks()  # Update the GUI immediately

    # Simulate a delay to show progress
    time.sleep(1)

    uploaded_image = None
    uploaded_image_path = None
    img_label.config(image="")
    uploading_label.config(text="Uploaded image deleted successfully!", fg="green")
    messagebox.showinfo("Image Deleted", "Uploaded image deleted successfully.")

# Function to check pixelation with a simulated animation
def check_pixelation():
    global uploaded_image_path
    
    if uploaded_image_path:
        # Simulate an animation by updating the label text
        processing_label.config(text="Processing...", fg="blue")
        root.update_idletasks()  # Update the GUI immediately

        # Read the uploaded image using OpenCV
        img = cv2.imread(uploaded_image_path, cv2.IMREAD_GRAYSCALE)

        if img is None:
            messagebox.showerror("Error", "Failed to open image file.")
            processing_label.config(text="Error", fg="red")
            return

        # Compute Laplacian variance to detect pixelation
        laplacian_var = cv2.Laplacian(img, cv2.CV_64F).var()

        # Update the result label based on the computed variance
        if laplacian_var < 1800:
            processing_label.config(text="Pixelation detected", fg="red")
            messagebox.showwarning("Pixelation Check", "Pixelation detected!")
        else:
            processing_label.config(text="Pixelation not detected", fg="green")
            messagebox.showinfo("Pixelation Check", "Pixelation not detected.")

    else:
        messagebox.showwarning("No Image", "Please upload an image first.")
    # Simulate an animation by updating the label text
    processing_label.config(text="Processing...", fg="blue")
    root.update_idletasks()  # Update the GUI immediately

    # Simulate a delay to show progress
    time.sleep(2)

    # Add your pixelation checking code here
    processing_label.config(text="Pixelation check complete!", fg="green")
    messagebox.showinfo("Check Pixelation", "Pixelation check complete!")

# Function to analyze the image with a simulated animation
def analyze_image():
    if uploaded_image:
        # Simulate an animation by updating the label text
        processing_label.config(text="Analyzing...", fg="blue")
        root.update_idletasks()  # Update the GUI immediately

        # Simulate a delay to show progress
        time.sleep(2)

        # Convert image to grayscale and numpy array
        original_gray = uploaded_image.convert('L')
        original_np = np.array(original_gray)

        # Calculate intensity values
        intensity_values = original_np.ravel()

        # Calculate pixel positions
        x_positions = np.arange(len(intensity_values))

        # Calculate pixel variance
        variance = np.var(intensity_values)

        # Plotting
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

        # Plot line graph for intensity values
        ax1.plot(intensity_values, color='gray', alpha=0.7)
        ax1.set_xlabel('Pixel')
        ax1.set_ylabel('Intensity')
        ax1.set_title('Intensity Variation in Grayscale Image')

        # Plot scatter plot for pixel variance
        ax2.scatter(x_positions, intensity_values, color='b', alpha=0.5)
        ax2.set_xlabel('Pixel')
        ax2.set_ylabel('Intensity')
        ax2.set_title(f'Pixel Variance: {variance:.2f}')

        plt.tight_layout()
        plt.show()

        # Update the label after analysis
        processing_label.config(text="Image analysis complete!", fg="green")
        messagebox.showinfo("Image Analysis", "Image analysis complete!")
    else:
        messagebox.showwarning("No Image", "Please upload an image first.")

# Function to fix pixelation with a simulated animation
# Function to fix pixelation with a simulated animation
def fix_pixelation():
    if uploaded_image_path:
        # Simulate an animation by updating the label text
        processing_label.config(text="Fixing Pixelation...", fg="blue")
        root.update_idletasks()  # Update the GUI immediately

        # Simulate a delay to show progress
        time.sleep(2)

        # Read the uploaded image using OpenCV
        image = cv2.imread(uploaded_image_path)

        # Calculate Laplacian variance to detect pixelation
        laplacian_var = cv2.Laplacian(image, cv2.CV_64F).var() + 1800

        # Apply Gaussian blur to the image
        blurred = cv2.GaussianBlur(image, (9, 9), 10.0)
        
        # Apply unsharp masking with lighter sharpening effect
        unsharp_image = cv2.addWeighted(image, 1.2, blurred, -0.2, 0)

        # Save and display the deblurred image
        deblurred_path = "deblurred_image.png"
        cv2.imwrite(deblurred_path, unsharp_image)
        deblurred_image_pil = Image.open(deblurred_path)
        deblurred_display = ImageTk.PhotoImage(deblurred_image_pil.resize((400, 400)))
        img_label.config(image=deblurred_display)
        img_label.image = deblurred_display

        # Update the label after fixing pixelation
        processing_label.config(text=f"Pixelation fixed! Laplacian Var: {laplacian_var:.2f}", fg="green")
        messagebox.showinfo("Fix Pixelation", f"Pixelation fixed! Laplacian Var: {laplacian_var:.2f}")
    else:
        messagebox.showwarning("No Image", "Please upload an image first.")


# Function to download the image with a simulated animation
def download_image():
    if uploaded_image:
        # Simulate an animation by updating the label text
        processing_label.config(text="Downloading...", fg="blue")
        root.update_idletasks()  # Update the GUI immediately

        # Simulate a delay to show progress
        time.sleep(2)

        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("BMP files", "*.bmp")])
        if save_path:
            uploaded_image.save(save_path)
            processing_label.config(text="Image downloaded successfully!", fg="green")
            messagebox.showinfo("Image Downloaded", "Image downloaded successfully!")
    else:
        messagebox.showwarning("No Image", "Please upload an image first.")

# Header label
header = tk.Label(root, text="Image Pixelator", font=("Helvetica", 30))
header.pack(pady=20)

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Upload image button
upload_button = tk.Button(button_frame, text="Upload Image", command=upload_image)
upload_button.grid(row=0, column=0, padx=10, pady=10)

# Delete image button
delete_button = tk.Button(button_frame, text="Delete Image", command=delete_image)
delete_button.grid(row=0, column=1, padx=10, pady=10)

# Check pixelation button
check_pixelation_button = tk.Button(button_frame, text="Check Pixelation", command=check_pixelation)
check_pixelation_button.grid(row=0, column=2, padx=10, pady=10)

# Image analysis button
image_analysis_button = tk.Button(button_frame, text="Image Analysis", command=analyze_image)
image_analysis_button.grid(row=0, column=3, padx=10, pady=10)

# Fix pixelation button
fix_pixelation_button = tk.Button(button_frame, text="Fix Pixelation", command=fix_pixelation)
fix_pixelation_button.grid(row=0, column=4, padx=10, pady=10)

# Download image button
download_button = tk.Button(button_frame, text="Download Image", command=download_image)
download_button.grid(row=0, column=5, padx=10, pady=10)

# Label to display the uploaded image
img_label = tk.Label(root)
img_label.pack(pady=20)

# Label for uploading/deleting messages
uploading_label = tk.Label(root, text="", fg="blue")
uploading_label.pack(pady=10)

# Label for processing messages
processing_label = tk.Label(root, text="", fg="blue")
processing_label.pack(pady=10)

# Run the application
root.mainloop()
