# 🧪 Incubyte TDD Kata – String Calculator

This is a solution to the String Calculator TDD Kata as part of the Incubyte hiring process. It demonstrates Test-Driven Development (TDD) using Python and `pytest`.

---

## 📌 Problem Requirements

Implement a method:
```python
def add(numbers: str) -> int
The method should:

Return 0 for an empty string.

Return the number itself if only one number is provided.

Return the sum of comma-separated numbers.

Allow \n (newline) as a separator.

Support custom delimiters using the format: //<delimiter>\n<numbers>, e.g., //;\n1;2.

Throw an exception if any negative numbers are present, listing all of them.

📁 File Structure
bash
Copy code
.
├── string_calculator.py   # Contains both the implementation and test cases
├── README.md              # This file
🧪 How to Run
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv env
env\Scripts\activate       # Windows
# OR
source env/bin/activate    # macOS/Linux
Install pytest:

bash
Copy code
pip install pytest
Run tests:

bash
Copy code
pytest string_calculator.py -v
✅ Features Covered
Feature	Input	Output
Empty string	""	0
One number	"1"	1
Two numbers	"1,2"	3
Multiple numbers	"1,2,3,4"	10
Newline separators	"1\n2,3"	6
Custom delimiter	"//;\n1;2"	3
Negative numbers	"1,-2,-3"	Exception with message

🔁 TDD Steps Followed
Write a failing test.

Implement the minimum code to pass the test.

Refactor to improve code without breaking tests.

Repeat for each requirement.

All tests and implementation are included in a single file for simplicity.

👨‍💻 Author
Deepesh Salve
GitHub: https://github.com/Mr-D-007/Task-Add