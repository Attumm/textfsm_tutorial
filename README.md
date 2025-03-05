# TextFSM Tutorial

This repository provides a series of step-by-step examples illustrating how to parse text with the [TextFSM](https://github.com/google/textfsm) library. Each step focuses on a specific feature or technique, allowing you to gradually become familiar with TextFSM's template syntax and parsing capabilities.

## Overview

TextFSM is a Python library that facilitates parsing of semi-structured text data. It uses templates containing regular expressions to match and extract information. These templates can be especially helpful when parsing network device outputs, logs, or other text-based data formats that do not have consistent, tabular structures.

The tutorials in this repository showcase various ways to leverage TextFSM’s capabilities:
- **Step 0:** Introduction to TextFSM with a simple example of parsing first and last names.  
- **Step 1+:** Progressively more complex use cases, such as handling multiple records, using states to separate sections, filling down values, requiring values, and other common text-parsing tasks.

## Repository Structure

Below is a brief overview of the files and folders in the `basics/` directory:

- **`step_0_introduction.py`**  
  Demonstrates how to parse a simple string (`"John Doe"`) to extract the first and last names.
  
- **`step_1_multiple_records.py`**  
  Shows how to handle multiple lines of similar format.

- **`step_2_states_separator.py`**  
  Introduces state management in TextFSM templates to handle varied text sections.

- **`step_3_value_filldown.py`** and **`step_3_0_value_filldown.py`**  
  Illustrate how to fill down values when some fields are missing in subsequent lines.

- **`step_4_value_required.py`**  
  Demonstrates the concept of required values in your parsed data.

- **`step_5_remove_the_clutter.py`**  
  Shows strategies to clean up unwanted parts of the output and simplify templates.

- **`common.py`**  
  Contains shared helper functions, including `run_textfsm()`, used by all examples to run the parsing logic.

## Getting Started

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/Attumm/textfsm_tutorial
   cd textfsm_tutorial
   ```

2. **Create and Activate a Virtual Environment**  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate    # Linux/Mac
   # or
   .venv\Scripts\activate       # Windows
   
   pip install -r requirements.txt
   ```

3. **Install Dependencies**  
   Make sure [TextFSM](https://github.com/google/textfsm) is installed:
   ```bash
   pip install textfsm
   ```

4. **Run the Examples**  
   Navigate to the `basics/` folder and run any of the step scripts. For instance, to run the first example:
   ```bash
   cd basics
   python step_0_introduction.py
   ```

## Notes on Usage

- Each example is self-contained. Review the source code in each script for guidance on how TextFSM templates are defined and used.
- The `run_textfsm()` function in `common.py` encapsulates the typical loading and execution steps of TextFSM, so you do not have to write the boilerplate code repeatedly.
