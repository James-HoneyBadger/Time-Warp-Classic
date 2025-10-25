#!/usr/bin/env python3
"""
Ruby Language Executor for TimeWarp IDE
========================================

Executes Ruby code using the system's Ruby interpreter.
Supports basic Ruby syntax, object-oriented programming, and integration with TimeWarp's turtle graphics.
"""

import subprocess
import sys
import os
import tempfile
import re
from typing import Optional, Any, Dict, List


class RubyExecutor:
    """
    Ruby language executor for TimeWarp IDE.

    Executes Ruby code by interfacing with the system Ruby interpreter.
    Supports turtle graphics integration and variable sharing.
    """

    def __init__(self, interpreter):
        """Initialize Ruby executor with reference to main interpreter."""
        self.interpreter = interpreter
        self.ruby_available = self._check_ruby_availability()
        self.variables = {}  # Local variable storage for Ruby-Turtle integration

        if not self.ruby_available:
            self.interpreter.log_output(
                "⚠️  Ruby interpreter not found. Ruby support disabled."
            )
            self.interpreter.log_output(
                "   Install Ruby to enable Ruby programming: https://www.ruby-lang.org/"
            )

    def _check_ruby_availability(self) -> bool:
        """Check if Ruby interpreter is available on the system."""
        try:
            result = subprocess.run(
                ["ruby", "--version"], capture_output=True, text=True, timeout=5
            )
            return result.returncode == 0
        except (
            subprocess.TimeoutExpired,
            FileNotFoundError,
            subprocess.SubprocessError,
        ):
            return False

    def execute_command(self, command: str) -> str:
        """
        Execute a Ruby command or script.

        Args:
            command: Ruby code to execute

        Returns:
            Execution result status
        """
        if not self.ruby_available:
            self.interpreter.log_output("❌ Ruby is not available on this system")
            return "error"

        try:
            # Handle special turtle graphics commands
            if self._is_turtle_command(command):
                return self._execute_turtle_command(command)

            # Execute regular Ruby code
            result = self._execute_ruby_code(command)

            if result:
                self.interpreter.log_output(result)

            return "continue"

        except Exception as e:
            error_msg = f"❌ Ruby execution error: {str(e)}"
            self.interpreter.log_output(error_msg)
            return "error"

    def _is_turtle_command(self, command: str) -> bool:
        """Check if command is a turtle graphics operation."""
        turtle_commands = [
            "turtle.forward",
            "turtle.back",
            "turtle.left",
            "turtle.right",
            "turtle.penup",
            "turtle.pendown",
            "turtle.home",
            "turtle.clear",
            "turtle.color",
            "turtle.circle",
            "turtle.goto",
        ]
        command_lower = command.strip().lower()
        return any(cmd in command_lower for cmd in turtle_commands)

    def _execute_turtle_command(self, command: str) -> str:
        """Execute turtle graphics commands by translating to interpreter calls."""
        try:
            # Simple turtle command translation
            if "turtle.forward" in command.lower():
                distance = self._extract_number(command)
                if distance:
                    self.interpreter.turtle_forward(distance)
                    self.interpreter.log_output(
                        f"🐢 Turtle moved forward {distance} units"
                    )

            elif "turtle.back" in command.lower():
                distance = self._extract_number(command)
                if distance:
                    self.interpreter.turtle_forward(-distance)
                    self.interpreter.log_output(
                        f"🐢 Turtle moved back {distance} units"
                    )

            elif "turtle.left" in command.lower():
                angle = self._extract_number(command) or 90
                self.interpreter.turtle_turn(-angle)
                self.interpreter.log_output(f"🐢 Turtle turned left {angle} degrees")

            elif "turtle.right" in command.lower():
                angle = self._extract_number(command) or 90
                self.interpreter.turtle_turn(angle)
                self.interpreter.log_output(f"🐢 Turtle turned right {angle} degrees")

            elif "turtle.penup" in command.lower():
                # Simulate pen up by setting pen_down to False
                if hasattr(self.interpreter, "turtle_graphics"):
                    self.interpreter.turtle_graphics["pen_down"] = False
                    self.interpreter.log_output("🐢 Pen up")

            elif "turtle.pendown" in command.lower():
                # Simulate pen down by setting pen_down to True
                if hasattr(self.interpreter, "turtle_graphics"):
                    self.interpreter.turtle_graphics["pen_down"] = True
                    self.interpreter.log_output("🐢 Pen down")

            elif "turtle.home" in command.lower():
                self.interpreter.turtle_home()
                self.interpreter.log_output("🐢 Turtle went home")

            elif "turtle.clear" in command.lower():
                self.interpreter.clear_turtle_screen()
                self.interpreter.log_output("🐢 Screen cleared")

            elif "turtle.color" in command.lower():
                color = self._extract_string(command)
                if color and hasattr(self.interpreter, "turtle_graphics"):
                    self.interpreter.turtle_graphics["pen_color"] = color
                    self.interpreter.log_output(f"🐢 Color set to {color}")

            elif "turtle.circle" in command.lower():
                radius = self._extract_number(command) or 50
                self.interpreter.turtle_circle(radius)
                self.interpreter.log_output(f"🐢 Drew circle with radius {radius}")

            elif "turtle.goto" in command.lower():
                coords = self._extract_coordinates(command)
                if coords:
                    x, y = coords
                    self.interpreter.turtle_setxy(x, y)
                    self.interpreter.log_output(f"🐢 Moved to position ({x}, {y})")

            return "continue"

        except Exception as e:
            self.interpreter.log_output(f"❌ Turtle command error: {str(e)}")
            return "error"

    def _extract_number(self, command: str) -> Optional[float]:
        """Extract numeric value from command."""
        match = re.search(r"(\d+(?:\.\d+)?)", command)
        return float(match.group(1)) if match else None

    def _extract_string(self, command: str) -> Optional[str]:
        """Extract string value from command."""
        match = re.search(r'["\']([^"\']+)["\']', command)
        return match.group(1) if match else None

    def _extract_coordinates(self, command: str) -> Optional[tuple]:
        """Extract x,y coordinates from command."""
        match = re.search(
            r"goto\s*\(\s*([-\d.]+)\s*,\s*([-\d.]+)\s*\)", command, re.IGNORECASE
        )
        if match:
            return float(match.group(1)), float(match.group(2))
        return None

    def _execute_ruby_code(self, code: str) -> str:
        """
        Execute Ruby code using subprocess.

        Args:
            code: Ruby code to execute

        Returns:
            Execution output
        """
        try:
            # Create a temporary Ruby script
            with tempfile.NamedTemporaryFile(mode="w", suffix=".rb", delete=False) as f:
                # Add turtle integration helpers
                ruby_script = f"""
# TimeWarp Ruby Integration
def turtle_forward(distance)
  puts "TURTLE_FORWARD:#{distance}"
end

def turtle_back(distance)
  puts "TURTLE_BACK:#{distance}"
end

def turtle_left(angle)
  puts "TURTLE_LEFT:#{angle}"
end

def turtle_right(angle)
  puts "TURTLE_RIGHT:#{angle}"
end

def turtle_penup
  puts "TURTLE_PENUP"
end

def turtle_pendown
  puts "TURTLE_PENDOWN"
end

def turtle_home
  puts "TURTLE_HOME"
end

def turtle_clear
  puts "TURTLE_CLEAR"
end

def turtle_color(color)
  puts "TURTLE_COLOR:#{color}"
end

def turtle_circle(radius)
  puts "TURTLE_CIRCLE:#{radius}"
end

def turtle_goto(x, y)
  puts "TURTLE_GOTO:#{x},#{y}"
end

# User code
{code}
"""
                f.write(ruby_script)
                temp_file = f.name

            # Execute the Ruby script
            result = subprocess.run(
                ["ruby", temp_file], capture_output=True, text=True, timeout=10
            )

            # Clean up temp file
            os.unlink(temp_file)

            # Process output
            output = result.stdout.strip()
            if result.stderr:
                output += "\n" + result.stderr.strip()

            # Handle turtle commands from Ruby output
            if output:
                lines = output.split("\n")
                processed_output = []

                for line in lines:
                    if line.startswith("TURTLE_"):
                        self._handle_turtle_output(line)
                    else:
                        processed_output.append(line)

                return "\n".join(processed_output) if processed_output else ""

            return output

        except subprocess.TimeoutExpired:
            return "❌ Ruby execution timed out"
        except Exception as e:
            return f"❌ Ruby execution failed: {str(e)}"

    def _handle_turtle_output(self, line: str):
        """Handle turtle commands output from Ruby script."""
        try:
            if line.startswith("TURTLE_FORWARD:"):
                distance = float(line.split(":")[1])
                self.interpreter.turtle_forward(distance)
            elif line.startswith("TURTLE_BACK:"):
                distance = float(line.split(":")[1])
                self.interpreter.turtle_forward(-distance)
            elif line.startswith("TURTLE_LEFT:"):
                angle = float(line.split(":")[1])
                self.interpreter.turtle_turn(-angle)
            elif line.startswith("TURTLE_RIGHT:"):
                angle = float(line.split(":")[1])
                self.interpreter.turtle_turn(angle)
            elif line == "TURTLE_PENUP":
                if hasattr(self.interpreter, "turtle_graphics"):
                    self.interpreter.turtle_graphics["pen_down"] = False
            elif line == "TURTLE_PENDOWN":
                if hasattr(self.interpreter, "turtle_graphics"):
                    self.interpreter.turtle_graphics["pen_down"] = True
            elif line == "TURTLE_HOME":
                self.interpreter.turtle_home()
            elif line == "TURTLE_CLEAR":
                self.interpreter.clear_turtle_screen()
            elif line.startswith("TURTLE_COLOR:"):
                color = line.split(":")[1]
                if hasattr(self.interpreter, "turtle_graphics"):
                    self.interpreter.turtle_graphics["pen_color"] = color
            elif line.startswith("TURTLE_CIRCLE:"):
                radius = float(line.split(":")[1])
                self.interpreter.turtle_circle(radius)
            elif line.startswith("TURTLE_GOTO:"):
                coords = line.split(":")[1].split(",")
                x, y = float(coords[0]), float(coords[1])
                self.interpreter.turtle_setxy(x, y)
        except Exception as e:
            self.interpreter.log_output(f"❌ Turtle output error: {str(e)}")

    def get_ruby_version(self) -> Optional[str]:
        """Get Ruby version information."""
        if not self.ruby_available:
            return None

        try:
            result = subprocess.run(
                ["ruby", "--version"], capture_output=True, text=True, timeout=5
            )
            return result.stdout.strip() if result.returncode == 0 else None
        except:
            return None
