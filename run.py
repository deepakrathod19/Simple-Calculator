#!/usr/bin/env python3
"""
Simple Calculator App Setup and Run Script
"""
import os
import sys
import subprocess

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements!")
        return False

def create_directories():
    """Create necessary directories"""
    print("📁 Creating directories...")
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    print("✅ Directories created!")

def run_app():
    """Run the Flask application"""
    print("🚀 Starting Calculator App...")
    print("📱 Open your browser to: http://127.0.0.1:5000")
    print("⏹️  Press Ctrl+C to stop the server")
    print("-" * 50)

    try:
        os.system('python app.py')
    except KeyboardInterrupt:
        print("\n👋 Calculator app stopped!")

if __name__ == '__main__':
    print("🧮 Simple Calculator App Setup")
    print("=" * 40)

    # Check if we're in the right directory
    if not os.path.exists('app.py'):
        print("❌ app.py not found! Make sure you're in the calculator app directory.")
        sys.exit(1)

    create_directories()

    # Install requirements if needed
    if not os.path.exists('venv') and not os.path.exists('.venv'):
        install_requirements()

    # Run the app
    run_app()
