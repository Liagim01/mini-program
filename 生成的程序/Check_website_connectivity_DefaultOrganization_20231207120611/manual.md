# Website Status Checker User Manual

## Introduction

The Website Status Checker is a Python-based program that allows you to check the operational status of a list of websites. It takes a list of websites stored in a text file and determines whether each website is working or not. The results are then saved to a CSV file.

This user manual will guide you through the installation process, explain how to use the program, and provide examples to help you get started.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
   - [Step 1: Create the Configuration Files](#step-1-create-the-configuration-files)
   - [Step 2: Create the Python Script](#step-2-create-the-python-script)
   - [Step 3: Run the Program](#step-3-run-the-program)
3. [Examples](#examples)
4. [Troubleshooting](#troubleshooting)
5. [FAQs](#faqs)
6. [Support](#support)

## Installation <a name="installation"></a>

Before you can use the Website Status Checker, you need to ensure that you have Python 3.x installed on your system and the `requests` library installed. Follow the steps below to install the necessary dependencies:

1. Open a command window (cmd or terminal).
2. Run the following command to install the `requests` library:

   ```
   pip install requests
   ```

   This will install the `requests` module in your Python configuration.

3. Download the Website Status Checker program files from the provided source.

## Usage <a name="usage"></a>

To use the Website Status Checker program, follow the steps below:

### Step 1: Create the Configuration Files <a name="step-1-create-the-configuration-files"></a>

1. Create a text file in your working directory and name it `websites.txt`. This file will be used to store your list of websites.
2. Populate this text file with the URLs of the websites you want to check.

### Step 2: Create the Python Script <a name="step-2-create-the-python-script"></a>

1. Create a new file in your working directory and name it `check_website_status.py`. This file will contain the Python code for the website status checker program.
2. Copy the provided code from `check_website_status.py` and paste it into the file you just created.

### Step 3: Run the Program <a name="step-3-run-the-program"></a>

1. Ensure Python 3.x and the `requests` library are installed.
2. Open a command window (cmd or terminal) and navigate to your working directory.
3. Run the script using the following command:

   ```
   python check_website_status.py
   ```

4. After the program finishes executing, it will create a `website_status.csv` file which contains the operational statuses of the websites you listed in `websites.txt`.

## Examples <a name="examples"></a>

Here are a few examples to help you understand how to use the Website Status Checker program:

**Example 1: Checking the Status of Websites**

Suppose you have a `websites.txt` file with the following URLs:

```
https://www.example1.com
https://www.example2.com
https://www.example3.com
```

1. Create a new file named `check_website_status.py` in your working directory.
2. Copy the provided code from `check_website_status.py` and paste it into the `check_website_status.py` file.
3. Open a command window (cmd or terminal) and navigate to your working directory.
4. Run the script using the following command:

   ```
   python check_website_status.py
   ```

5. After the program finishes executing, it will create a `website_status.csv` file in your working directory. Open this file to view the operational statuses of the websites.

## Troubleshooting <a name="troubleshooting"></a>

If you encounter any issues while using the Website Status Checker program, try the following troubleshooting steps:

1. Make sure you have Python 3.x installed on your system. You can check your Python version by running the following command:

   ```
   python --version
   ```

2. Ensure that the `requests` library is installed. You can install it by running the following command:

   ```
   pip install requests
   ```

3. Double-check that the `websites.txt` file is located in your working directory and contains the correct URLs.

4. Verify that the `check_website_status.py` file is located in your working directory and contains the correct code.

5. If you're still experiencing issues, please refer to the FAQs section or contact our support team for assistance.

## FAQs <a name="faqs"></a>

**Q: Can I check the status of multiple websites at once?**

A: Yes, you can check the status of multiple websites by adding their URLs to the `websites.txt` file. Each URL should be on a separate line.

**Q: How often should I run the Website Status Checker program?**

A: The frequency of running the program depends on your needs. You can run it as frequently as you want to check the operational status of the websites. However, keep in mind that running it too frequently may put unnecessary load on the websites.

**Q: Can I customize the output format of the `website_status.csv` file?**

A: Currently, the program outputs the website status in a CSV format with two columns: "Website" and "Status". If you need a different output format, you can modify the code in the `save_results` method of the `WebsiteStatusChecker` class.

## Support <a name="support"></a>

If you need any assistance or have any questions regarding the Website Status Checker program, please reach out to our support team. You can contact us through [email address] or [phone number]. We are available [support hours] to provide you with the necessary support and guidance.

Thank you for choosing the Website Status Checker program! We hope it helps you efficiently monitor the operational status of your websites.

```