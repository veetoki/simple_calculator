# Simple Calculator

Simple calculator is a simple dynamic calculator that developed for the interview requirement.

Simple calculator can operate simple expression with operator: +, -, *, /.

## Installation
 

```bash
git clone https://github.com/veetoki/simple_calculator.git
```

## Usage
Prepare and put the json file contain collected data in the same directory with calc.py.

Go to directory stored calc.py and run:
```bash
./calc.py
```

## Example
File data.json
```
{
"price": 100,
"amount": 50,
"discount": 0.5,
"unit": 1000,
"added_tax": 50000
}
```

Formula
```
Without parentheses:
calc("price * amount * discount", data) -> output 2500
calc("price * amount * discount + 1000", data) -> output 3500
calc("price * amount * unit", data) -> output 5000000
calc("discount * 1000 + amount * price", data) -> output 5500

With parentheses:
calc("(price * amount + added_tax) * (1 - discount)", data) -> output 27500
calc("(price * amount + added_tax) * (1 - discount) / unit", data) -> output 27.5
```

## Limitation
This simple calculator just support simple parentheses case, it does not support the case with more than 1 nested parentheses nested inside a parentheses.

Example:
```((a - b) / (d - c))```

This simple calculator does not going to handle many user exceptions such as: wrong format operands, ... .

Task Complexity:

Build postfix expression: 2pts

Implement evaluation postfix expression: 2pts

Improve evaluation postfix expression to support parentheses: 3pts

Total task complexity: 7pts

Workload Estimated: 6 hours

