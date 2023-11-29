
# Intersection over Union (IoU) Calculation Script

## Overview

This Python script calculates the Intersection over Union (IoU) between two bounding boxes. IoU is a crucial metric in computer vision, particularly in object detection tasks, as it quantifies the accuracy of a predicted bounding box against the ground truth.

## Purpose

The script's main purpose is to provide a simple yet effective way to compute the IoU for evaluating object detection models. This metric is vital for understanding how well a model is performing in terms of locating and identifying objects within an image.

## Prerequisites

- Python 3.x
- NumPy library, which can be installed via pip:

  ```bash
  pip install numpy
  ```

## How to Run the Script

1. Ensure Python 3.x and NumPy are installed on your system.
2. Download the script to your local machine.
3. Run the script using the following command:

   ```bash
   python Compute_IoU.py
   ```

## Script Details

### Functionality

- The script takes two bounding boxes as input: the predicted bounding box and the ground truth bounding box.
- It calculates the IoU by finding the area of overlap between these two bounding boxes and dividing it by the area of their union.
- The IoU is returned as a value between 0 (no overlap) and 1 (perfect overlap).

### Usage Examples

To calculate IoU, modify the `pred_bbox` and `gt_bbox` variables in the script with the coordinates of your predicted and ground truth bounding boxes, respectively. For example:

```python
pred_bbox = np.array([40, 40, 100, 100]) # Predicted bounding box
gt_bbox = np.array([70, 80, 110, 130])   # Ground truth bounding box
```

Then, run the script to see the IoU value.

## Author

[Mason](https://github.com/JohnMasoner)

