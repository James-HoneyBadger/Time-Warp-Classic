#!/usr/bin/env ruby
# Ruby Example Program - Object-Oriented Turtle Graphics
# This program demonstrates Ruby's object-oriented features and turtle graphics integration

# Define a Shape class
class Shape
  attr_accessor :name, :color

  def initialize(name, color = "blue")
    @name = name
    @color = color
  end

  def draw
    puts "Drawing a #{color} #{name}"
  end
end

# Define a TurtleGraphics class for managing turtle operations
class TurtleGraphics
  def initialize
    @x = 0
    @y = 0
    @heading = 0
    @pen_down = true
    @color = "black"
  end

  def forward(distance)
    turtle_forward(distance)
    puts "🐢 Moved forward #{distance} units"
  end

  def back(distance)
    turtle_back(distance)
    puts "🐢 Moved back #{distance} units"
  end

  def left(angle)
    turtle_left(angle)
    puts "🐢 Turned left #{angle} degrees"
  end

  def right(angle)
    turtle_right(angle)
    puts "🐢 Turned right #{angle} degrees"
  end

  def penup
    turtle_penup
    @pen_down = false
    puts "🐢 Pen up"
  end

  def pendown
    turtle_pendown
    @pen_down = true
    puts "🐢 Pen down"
  end

  def home
    turtle_home
    @x = 0
    @y = 0
    @heading = 0
    puts "🐢 Went home"
  end

  def color(new_color)
    turtle_color(new_color)
    @color = new_color
    puts "🐢 Color changed to #{new_color}"
  end

  def circle(radius)
    turtle_circle(radius)
    puts "🐢 Drew circle with radius #{radius}"
  end

  def goto(x, y)
    turtle_goto(x, y)
    @x = x
    @y = y
    puts "🐢 Moved to position (#{x}, #{y})"
  end
end

# Define specific shape classes
class Square < Shape
  def initialize(side_length, color = "red")
    super("square", color)
    @side_length = side_length
  end

  def draw(turtle)
    puts "Drawing a #{color} square with side #{side_length}"
    turtle.color(color)
    4.times do
      turtle.forward(@side_length)
      turtle.right(90)
    end
  end
end

class Triangle < Shape
  def initialize(side_length, color = "green")
    super("triangle", color)
    @side_length = side_length
  end

  def draw(turtle)
    puts "Drawing a #{color} triangle with side #{side_length}"
    turtle.color(color)
    3.times do
      turtle.forward(@side_length)
      turtle.right(120)
    end
  end
end

class Circle < Shape
  def initialize(radius, color = "blue")
    super("circle", color)
    @radius = radius
  end

  def draw(turtle)
    puts "Drawing a #{color} circle with radius #{radius}"
    turtle.color(color)
    turtle.circle(@radius)
  end
end

# Main program
puts "🟥 Ruby Example Program - Object-Oriented Turtle Graphics"
puts "=" * 60

# Create turtle instance
turtle = TurtleGraphics.new

# Create shapes
shapes = [
  Square.new(80, "red"),
  Triangle.new(100, "green"),
  Circle.new(50, "blue"),
  Square.new(60, "purple"),
  Triangle.new(80, "orange")
]

# Draw each shape
shapes.each_with_index do |shape, index|
  puts "\n🎨 Drawing shape #{index + 1}:"
  shape.draw(turtle)

  # Move to next position
  turtle.penup
  turtle.forward(120)
  turtle.pendown
end

# Draw a pattern
puts "\n🌟 Drawing a star pattern..."
turtle.home
turtle.color("gold")

5.times do
  turtle.forward(100)
  turtle.right(144)
end

# Draw some text
puts "\n📝 Adding some text..."
turtle.penup
turtle.goto(-150, 120)
turtle.pendown
turtle.color("black")

# Interactive section
puts "\n🎮 Interactive Section!"
puts "Enter a number between 1 and 10:"
number = gets.to_i

if number.between?(1, 10)
  puts "You entered: #{number}"
  puts "Drawing #{number} circles..."

  turtle.home
  turtle.penup
  turtle.goto(-200, -100)
  turtle.pendown

  colors = ["red", "blue", "green", "yellow", "purple", "orange"]
  number.times do |i|
    turtle.color(colors[i % colors.length])
    turtle.circle(20 + i * 5)
    turtle.penup
    turtle.forward(50)
    turtle.pendown
  end
else
  puts "Invalid number! Drawing a default pattern..."
  turtle.home
  turtle.color("pink")
  8.times do
    turtle.forward(60)
    turtle.right(45)
  end
end

puts "\n✨ Ruby turtle graphics demo complete!"
puts "Ruby's object-oriented features make it great for structured graphics programming!"