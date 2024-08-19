# 0x04. UTF-8 Validation

This project implements a method to determine if a given data set represents a valid UTF-8 encoding.

## Task 0: UTF-8 Validation

### Description

Implement a method `validUTF8(data)` that determines if a given data set represents a valid UTF-8 encoding.

- Prototype: `def validUTF8(data)`
- Return: `True` if data is a valid UTF-8 encoding, else return `False`
- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

### Files

- `0-validate_utf8.py`: Contains the implementation of the `validUTF8` function.
- `0-main.py`: Main file for testing the `validUTF8` function.

## Requirements

- Python 3.4.3
- Ubuntu 20.04 LTS
- PEP 8 style (version 1.7.x)

## Usage

```bash
./0-main.py
