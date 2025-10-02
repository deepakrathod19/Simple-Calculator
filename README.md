# Simple-Calculator
# Create the README.md content
readme_content = """# 🧮 Simple Calculator

![Flask](https://img.shields.io/badge/Flask-2.3.3-blue?style=flat-square&logo=flask)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=flat-square&logo=python)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

A modern, responsive web-based calculator built with Python Flask, HTML, CSS, and JavaScript. This calculator provides a clean interface for performing basic arithmetic operations with a beautiful gradient design and smooth animations.

## ✨ Features

- **🎨 Clean Modern Interface**: Beautiful gradient background with responsive design
- **🔢 Basic Arithmetic Operations**: Addition (+), Subtraction (-), Multiplication (×), Division (÷)
- **🔧 Advanced Functions**: Supports decimal calculations and parentheses
- **⚡ Real-time Calculations**: Instant results with JavaScript integration
- **🛡️ Error Handling**: Robust error handling for invalid expressions and division by zero
- **📱 Mobile Responsive**: Works seamlessly on desktop and mobile devices
- **⌨️ Keyboard Support**: Use your keyboard for faster input
- **✨ Visual Feedback**: Button press animations and hover effects

## 🚀 Demo

Access the calculator by running the application locally and navigating to `http://127.0.0.1:5000`

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.8 or higher installed on your system
- pip (Python package installer)

## 🔧 Installation & Setup

### Option 1: Quick Start (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/simple-calculator.git
   cd simple-calculator
   ```

2. **Run the setup script**
   ```bash
   python run.py
   ```
   
   The script will automatically:
   - Install required dependencies
   - Create necessary directories
   - Start the Flask server

3. **Open your browser** and navigate to `http://127.0.0.1:5000`

### Option 2: Manual Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/simple-calculator.git
   cd simple-calculator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create necessary directories and organize files**
   ```bash
   mkdir templates static
   mv index.html templates/
   mv style.css static/
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the calculator** at `http://127.0.0.1:5000`

## 📁 Project Structure

```
simple-calculator/
│
├── app.py              # Main Flask application
├── run.py              # Setup and run script
├── requirements.txt    # Python dependencies (Flask==2.3.3)
├── index.html          # Calculator interface template
├── style.css          # Styling and animations
├── templates/          # Flask templates directory (auto-created)
│   └── index.html     # Moved here during setup
├── static/            # Static files directory (auto-created)
│   └── style.css      # Moved here during setup
└── README.md          # This documentation
```

## 🎯 Usage

### Web Interface
1. Start the application using one of the installation methods above
2. Open your web browser and go to `http://127.0.0.1:5000`
3. Use the on-screen buttons or your keyboard to input calculations
4. Press `=` or `Enter` to calculate results
5. Use `C` to clear the display
6. Use `AC` to reset everything

### Keyboard Shortcuts
- **Numbers (0-9)**: Input numbers
- **Operators (+, -, *, /)**: Mathematical operations
- **Enter**: Calculate result
- **Escape/c**: Clear display
- **Backspace**: Delete last character
- **Decimal point (.)**: Add decimal point

### API Endpoint
The calculator also provides a REST API endpoint:

**Endpoint:** `POST /calculate`

**Request:**
```bash
curl -X POST http://127.0.0.1:5000/calculate \\
  -H "Content-Type: application/json" \\
  -d '{"expression": "2 + 3 * 4"}'
```

**Response:**
```json
{
  "result": "14"
}
```

## 🛠️ Technical Details

### Built With
- **Backend**: Python Flask 2.3.3
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS with CSS Grid and Flexbox
- **Responsive Design**: Mobile-first approach
- **HTTP Methods**: GET for interface, POST for calculations

### Key Components

#### Flask Backend (`app.py`)
- `Calculator` class with basic arithmetic methods
- Safe expression evaluation using regex validation
- RESTful API endpoint for calculations
- Error handling for invalid inputs and mathematical errors
- Routes for serving the main interface

#### Frontend Interface (`index.html`)
- Semantic HTML structure
- Grid-based button layout for calculator
- JavaScript event handlers for user interactions
- AJAX requests for server communication
- Responsive design elements

#### Responsive Styling (`style.css`)
- Modern gradient background (#667eea to #764ba2)
- Neumorphism-inspired button design
- Smooth animations and transitions
- Mobile-responsive breakpoints
- CSS Grid layout for calculator buttons

#### Setup Script (`run.py`)
- Automated installation of requirements
- Directory structure creation
- Application startup with user-friendly messages

## 🧪 Testing

To test the calculator manually:

1. **Basic Operations**: 
   - `2 + 3 = 5`
   - `10 - 5 = 5`
   - `4 * 6 = 24`
   - `15 / 3 = 5`

2. **Decimal Numbers**: 
   - `3.14 + 2.86 = 6`
   - `10.5 / 2.1 = 5`

3. **Complex Expressions**: 
   - `(2 + 3) * 4 - 1 = 19`
   - `2 * (3 + 4) = 14`

4. **Error Cases**: 
   - `5 / 0` → "Error: Cannot divide by zero"
   - Invalid expressions → "Error: Invalid expression"

5. **API Testing**:
   ```bash
   # Test basic calculation
   curl -X POST http://127.0.0.1:5000/calculate -H "Content-Type: application/json" -d '{"expression": "5+5"}'
   ```

## 🚨 Error Handling

The calculator includes comprehensive error handling:

- **Division by Zero**: Returns "Error: Cannot divide by zero"
- **Invalid Characters**: Validates input using regex patterns
- **Malformed Expressions**: Catches and handles syntax errors
- **Server Errors**: Proper HTTP status codes and error messages

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Commit your changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
5. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
6. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Use meaningful commit messages
- Add comments for complex logic
- Test your changes before submitting
- Update documentation if needed
- Ensure responsive design works on mobile devices

## 🐛 Known Issues & Limitations

- Expression evaluation uses Python's `eval()` function (safely implemented with regex validation)
- Complex mathematical functions (sin, cos, log, sqrt) are not implemented
- No calculation history feature
- Limited to standard arithmetic operations
- No memory functions (M+, M-, MR, MC)

## 🔮 Future Enhancements

- [ ] Scientific calculator mode with advanced functions
- [ ] Calculation history with save/load functionality
- [ ] Keyboard shortcuts help modal
- [ ] Dark/Light theme toggle
- [ ] Memory functions (M+, M-, MR, MC)
- [ ] Unit tests implementation with pytest
- [ ] Docker containerization
- [ ] Progressive Web App (PWA) features
- [ ] Export calculations to PDF/CSV
- [ ] Multiple calculator themes

## 📄 License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## 👨‍💻 Author

**[Your Name]** - BTech Student at VIT Pune
- 🎓 Computer Science Engineering Student
- 💻 Python & Web Development Enthusiast
- 📧 Email: [your.email@example.com]
- 🔗 LinkedIn: [linkedin.com/in/yourprofile]
- 🐱 GitHub: [@yourusername](https://github.com/yourusername)
- 🌐 Portfolio: [yourwebsite.com]

## 🙏 Acknowledgments

- Flask framework documentation and community
- Modern CSS design inspiration from Dribbble and CodePen
- Calculator UI/UX best practices
- Stack Overflow community for troubleshooting
- VIT Pune CSE department for technical guidance

## 💡 Support & Contact

If you found this project helpful, please give it a ⭐️ on GitHub!

**Need Help?**
- 📋 Open an [Issue](https://github.com/yourusername/simple-calculator/issues) for bugs
- 💬 Start a [Discussion](https://github.com/yourusername/simple-calculator/discussions) for questions
- 📧 Email me directly for collaboration opportunities

**Connect with me:**
- 💼 [LinkedIn](https://www.linkedin.com/in/deeprathod1/)


---

<div align="center">

**🧮 Happy Calculating! ✨**



