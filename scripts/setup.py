#!/usr/bin/env python3
"""
Setup script for Course Information RAG System
Automates the initial setup process including environment validation,
dependency installation, and vector database initialization.
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Verify Python version compatibility."""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    print(f"✅ Python {sys.version.split()[0]} detected")

def check_environment_file():
    """Check if .env file exists and has required variables."""
    env_file = Path(".env")
    if not env_file.exists():
        print("❌ .env file not found. Please copy .env.example to .env and configure it.")
        return False
    
    with open(env_file) as f:
        content = f.read()
        if "NVIDIA_API_KEY=your_nvidia_api_key_here" in content:
            print("❌ Please configure your NVIDIA API key in .env file")
            return False
    
    print("✅ Environment configuration found")
    return True

def install_requirements():
    """Install required Python packages."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def check_datasets():
    """Verify dataset files exist."""
    datasets_path = Path("Datasets")
    required_files = ["coursera_courses.csv", "udemy_courses.csv", "udacity_courses.csv"]
    
    if not datasets_path.exists():
        print("❌ Datasets directory not found")
        return False
    
    missing_files = []
    for file in required_files:
        if not (datasets_path / file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing dataset files: {', '.join(missing_files)}")
        return False
    
    print("✅ All dataset files found")
    return True

def create_directories():
    """Create necessary directories."""
    directories = ["db", "logs", "outputs"]
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
    print("✅ Directory structure created")

def main():
    """Main setup function."""
    print("🚀 Setting up Course Information RAG System...\n")
    
    # Check prerequisites
    check_python_version()
    
    if not check_environment_file():
        print("\nSetup incomplete. Please configure .env file first.")
        sys.exit(1)
    
    if not check_datasets():
        print("\nSetup incomplete. Please add required dataset files.")
        sys.exit(1)
    
    # Install dependencies
    if not install_requirements():
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    print("\n🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Run: python 1_ingestion_pipeline.py")
    print("2. Run: python 4_history_aware_generation.py")
    print("\nFor testing: python 2_retrieval_pipeline.py")

if __name__ == "__main__":
    main()