# Day 3 Projects

Two Python projects built as part of the 100 Days of Python Bootcamp: Pizza Price Calculator and Treasure Island game.

## Projects

### 1. Pizza Python Price Calculator

A command-line pizza ordering system that calculates the total price based on pizza size and additional toppings.

#### Description

This program helps calculate the price of a pizza order by considering:
- Pizza size (Small, Medium, or Large)
- Additional pepperoni topping
- Extra cheese option

#### Features

- Different pricing for Small ($15), Medium ($20), and Large ($25) pizzas
- Additional charges for pepperoni ($2 for Small, $3 for Medium/Large)
- Extra cheese option (+$1)
- Case-insensitive input handling

#### How to Use

1. Run the script: `python P003_PizzaPythonPrice.py`
2. Choose your pizza size: Type `S`, `M`, or `L`
3. Add pepperoni: Type `Y` or `N`
4. Add extra cheese: Type `Y` or `N`
5. See your final bill!

#### Example Output

```
Welcome to the Pizza Python Price Calculator!
what size pizza do you want? S, M, L: L
Do you want to add peperoni? Y or N: Y
Do you want to add cheese? Y or N: Y
Your final bill is $29
```

### 2. Treasure Island

An interactive text-based adventure game where you navigate through choices to find the treasure.

#### Description

This is a choice-based adventure game where you make decisions at various crossroads. Each decision leads to different outcomes, with only one path leading to the treasure. The game features ASCII art and multiple decision points.

#### Features

- Multiple decision points with different outcomes
- ASCII art graphics
- Interactive gameplay
- Multiple game endings (win or game over scenarios)

#### How to Play

1. Run the script: `python P004_Treasure_Island.py`
2. Make your first choice: Go "Left" or "Right"
3. At the lake: Choose to "Swim" or "Wait"
4. At the doors: Choose a door color (Red, Blue, or Yellow)
5. Find the treasure to win!

#### Requirements

- Python 3.x
- No external dependencies (uses only built-in functions)

