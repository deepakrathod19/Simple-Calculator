from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

class Calculator:
    """Simple Calculator class with basic operations"""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b

    def evaluate_expression(self, expression):
        """Safely evaluate mathematical expressions"""
        try:
            # Remove spaces and validate expression
            expression = expression.replace(' ', '')

            # Check if expression contains only allowed characters
            if not re.match(r'^[0-9+\-*/.()]+$', expression):
                return "Error: Invalid characters"

            # Evaluate the expression safely
            result = eval(expression)
            return result

        except ZeroDivisionError:
            return "Error: Cannot divide by zero"
        except Exception:
            return "Error: Invalid expression"

# Create calculator instance
calc = Calculator()

@app.route('/')
def index():
    """Render the main calculator page"""
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """Handle calculation requests"""
    try:
        data = request.get_json()
        expression = data.get('expression', '')

        if not expression:
            return jsonify({'result': 'Error: Empty expression'})

        result = calc.evaluate_expression(expression)
        return jsonify({'result': str(result)})

    except Exception as e:
        return jsonify({'result': 'Error: Something went wrong'})

if __name__ == '__main__':
    # Create directories if they don't exist
    import os
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)

    app.run(debug=True, host='127.0.0.1', port=5000)
