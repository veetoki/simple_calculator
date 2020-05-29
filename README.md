# Simple Calculator

Simple calculator is a simple dynamic calculator that developed for the interview requirement.

## Installation
 

```bash
git clone https://github.com/veetoki/test_interview.git
```

## Usage
Prepare and put the json file contain collected data in the same directory with calc.py.

Go to directory stored calc.py and run:
```bash
./calc.py
```

## Test Sample
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
"price * amount * discount" -> output 2500
"price * amount * discount + 1000" -> output 3500
"price * amount * unit" -> output 5000000
"discount * 1000 + amount * price" -> output 55000
```

## Limitation
This simple calculator does not support parentheses.

This simple calculator does not going to handle many user exceptions such as: wrong format operands, ... .

Task Complexity: 5pts

Workload Estimated: 4 hours

