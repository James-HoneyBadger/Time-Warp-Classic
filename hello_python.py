#!/usr/bin/env python3
"""
Python Example Program - Simple Calculator with Turtle Graphics
This program demonstrates Python syntax, functions, and turtle graphics integration
"""

import turtle
import math


def draw_circle(radius, color="blue"):
    """Draw a circle with given radius and color"""
    turtle.pencolor(color)
    turtle.circle(radius)
    return radius * 2 * math.pi  # Return circumference


def draw_square(side, color="red"):
    """Draw a square with given side length and color"""
    turtle.pencolor(color)
    for _ in range(4):
        turtle.forward(side)
        turtle.right(90)
    return side * 4  # Return perimeter


def calculate(operation, x, y):
    """Perform basic arithmetic operations"""
    if operation == "+":
        return x + y
    elif operation == "-":
        return x - y
    elif operation == "*":
        return x * y
    elif operation == "/":
        return x / y if y != 0 else "Error: Division by zero"
    else:
        return "Unknown operation"


def main():
    print("🐍 Python Calculator with Turtle Graphics Demo")
    print("=" * 50)

    # Get user input
    try:
        x = float(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /): ")
        y = float(input("Enter second number: "))

        result = calculate(operation, x, y)
        print(f"Result: {x} {operation} {y} = {result}")

    except ValueError:
        print("Error: Please enter valid numbers")
        return

    # Turtle graphics demonstration
    print("\n🎨 Now let's draw some shapes!")

    # Set up turtle
    turtle.speed(1)  # Slow speed for demonstration
    turtle.bgcolor("lightblue")

    # Draw shapes
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()

    # Draw circle
    circumference = draw_circle(50, "blue")
    print(f"Circle circumference: {circumference:.2f}")

    # Move to next position
    turtle.penup()
    turtle.goto(50, 0)
    turtle.pendown()

    # Draw square
    perimeter = draw_square(80, "red")
    print(f"Square perimeter: {perimeter}")

    # Draw some text
    turtle.penup()
    turtle.goto(-150, -150)
    turtle.pendown()
    turtle.write("Python + Turtle = Fun!", font=("Arial", 16, "bold"))

    print("\n✨ Python demo complete! Click on the turtle window to exit.")

    # Keep window open
    turtle.done()


if __name__ == "__main__":
    main()
