'''
This is the main file of the Intersection over Union (IoU) calculator program.
It provides a graphical user interface (GUI) for the user to enter bounding box coordinates and calculate IoU.
'''
import tkinter as tk
from tkinter import messagebox
import numpy as np
def calculate_iou():
    try:
        pred_bbox = np.array([float(pred_x1.get()), float(pred_y1.get()), float(pred_x2.get()), float(pred_y2.get())])
        gt_bbox = np.array([float(gt_x1.get()), float(gt_y1.get()), float(gt_x2.get()), float(gt_y2.get())])
        iou = compute_iou(pred_bbox, gt_bbox)
        messagebox.showinfo("IoU Calculation", f"The IoU value is: {iou:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values for bounding box coordinates.")
def compute_iou(pred_bbox, gt_bbox):
    '''
    Calculates the Intersection over Union (IoU) between two bounding boxes.
    '''
    x1 = max(pred_bbox[0], gt_bbox[0])
    y1 = max(pred_bbox[1], gt_bbox[1])
    x2 = min(pred_bbox[2], gt_bbox[2])
    y2 = min(pred_bbox[3], gt_bbox[3])
    intersection_area = max(0, x2 - x1 + 1) * max(0, y2 - y1 + 1)
    pred_bbox_area = (pred_bbox[2] - pred_bbox[0] + 1) * (pred_bbox[3] - pred_bbox[1] + 1)
    gt_bbox_area = (gt_bbox[2] - gt_bbox[0] + 1) * (gt_bbox[3] - gt_bbox[1] + 1)
    iou = intersection_area / float(pred_bbox_area + gt_bbox_area - intersection_area)
    return iou
# Create the GUI
root = tk.Tk()
root.title("IoU Calculator")
# Create labels and entry fields for predicted bounding box coordinates
pred_label = tk.Label(root, text="Predicted Bounding Box:")
pred_label.grid(row=0, column=0, padx=5, pady=5)
pred_x1_label = tk.Label(root, text="x1:")
pred_x1_label.grid(row=1, column=0, padx=5, pady=5)
pred_x1 = tk.Entry(root)
pred_x1.grid(row=1, column=1, padx=5, pady=5)
pred_y1_label = tk.Label(root, text="y1:")
pred_y1_label.grid(row=2, column=0, padx=5, pady=5)
pred_y1 = tk.Entry(root)
pred_y1.grid(row=2, column=1, padx=5, pady=5)
pred_x2_label = tk.Label(root, text="x2:")
pred_x2_label.grid(row=3, column=0, padx=5, pady=5)
pred_x2 = tk.Entry(root)
pred_x2.grid(row=3, column=1, padx=5, pady=5)
pred_y2_label = tk.Label(root, text="y2:")
pred_y2_label.grid(row=4, column=0, padx=5, pady=5)
pred_y2 = tk.Entry(root)
pred_y2.grid(row=4, column=1, padx=5, pady=5)
# Create labels and entry fields for ground truth bounding box coordinates
gt_label = tk.Label(root, text="Ground Truth Bounding Box:")
gt_label.grid(row=5, column=0, padx=5, pady=5)
gt_x1_label = tk.Label(root, text="x1:")
gt_x1_label.grid(row=6, column=0, padx=5, pady=5)
gt_x1 = tk.Entry(root)
gt_x1.grid(row=6, column=1, padx=5, pady=5)
gt_y1_label = tk.Label(root, text="y1:")
gt_y1_label.grid(row=7, column=0, padx=5, pady=5)
gt_y1 = tk.Entry(root)
gt_y1.grid(row=7, column=1, padx=5, pady=5)
gt_x2_label = tk.Label(root, text="x2:")
gt_x2_label.grid(row=8, column=0, padx=5, pady=5)
gt_x2 = tk.Entry(root)
gt_x2.grid(row=8, column=1, padx=5, pady=5)
gt_y2_label = tk.Label(root, text="y2:")
gt_y2_label.grid(row=9, column=0, padx=5, pady=5)
gt_y2 = tk.Entry(root)
gt_y2.grid(row=9, column=1, padx=5, pady=5)
# Create the calculate button
calculate_button = tk.Button(root, text="Calculate IoU", command=calculate_iou)
calculate_button.grid(row=10, column=0, columnspan=2, padx=5, pady=10)
# Run the GUI
root.mainloop()