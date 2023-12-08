# Intersection over Union (IoU) Calculator

The Intersection over Union (IoU) Calculator is a Python program that calculates the IoU between two bounding boxes. IoU is a crucial metric in computer vision, particularly in object detection tasks. This program provides a graphical user interface (GUI) for the user to enter the coordinates of the predicted and ground truth bounding boxes and calculates the IoU value.

## Installation

To run the program, you need to have Python 3.x and the NumPy library installed. You can install NumPy using pip by running the following command in the terminal:

```
pip install numpy
```

Once you have Python and NumPy installed, you can download the program code from [GitHub](https://github.com/your-repo-url) and save it as `main.py`.

## Usage

To calculate the IoU, follow these steps:

1. Open a terminal and navigate to the directory where you saved `main.py`.

2. Run the program by executing the following command:

   ```
   python main.py
   ```

3. The program will open a graphical user interface (GUI) window.

4. Enter the coordinates of the predicted bounding box in the "Predicted Bounding Box" section. The coordinates should be entered as floating-point numbers.

5. Enter the coordinates of the ground truth bounding box in the "Ground Truth Bounding Box" section. Again, the coordinates should be entered as floating-point numbers.

6. Click the "Calculate IoU" button.

7. The program will calculate the IoU value and display it in a message box.

   - If the IoU value is 0, it means there is no overlap between the two bounding boxes.
   - If the IoU value is 1, it means there is a perfect overlap between the two bounding boxes.

8. You can repeat the process with different bounding box coordinates by entering new values and clicking the "Calculate IoU" button again.

## Error Handling

The program handles potential errors and exceptions to ensure stability and robustness. If you enter invalid input, such as non-numeric values for the bounding box coordinates, the program will display an error message in a message box.

## Conclusion

The Intersection over Union (IoU) Calculator is a Python program that provides a convenient way to calculate the IoU between two bounding boxes. It is a useful tool for evaluating the performance of object detection algorithms in computer vision tasks. By following the installation and usage instructions provided in this manual, you can easily recreate and use the program to calculate IoU values for your own bounding boxes.