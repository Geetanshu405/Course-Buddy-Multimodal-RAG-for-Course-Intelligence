#!/usr/bin/env python3
"""
Validation script for Course Information RAG System
Performs comprehensive system checks to ensure everything is configured correctly.
"""

import os
import sys
from pathlib import Path
import pandas as pd

def validate_environment():
    """Validate environment configuration."""
    print("🔍 Validating environment configuration...")
    
    env_file = Path(".env")
    if not env_file.exists():
        print("❌ .env file missing")
        return False
    
    # Check for API key
    with open(env_file) as f:
        content = f.read()
        if "NVIDIA_API_KEY=" not in content:
            print("❌ NVIDIA_API_KEY not found in .env")
            return False
        if "your_nvidia_api_key_here" in content:
            print("❌ NVIDIA_API_KEY not configured (still has placeholder)")
            return False
    
    print("✅ Environment configuration valid")
    return True

def validate_datasets():
    """Validate dataset files and content."""
    print("\n🔍 Validating datasets...")
    
    datasets_path = Path("Datasets")
    if not datasets_path.exists():
        print("❌ Datasets directory not found")
        return False
    
    datasets = {
        "coursera_courses.csv": ["course_title", "course_url", "course_rating"],
        "udemy_courses.csv": ["course_title", "url", "num_reviews"],
        "udacity_courses.csv": ["Title", "URL", "Rating"]
    }
    
    for filename, required_columns in datasets.items():
        filepath = datasets_path / filename
        if not filepath.exists():
            print(f"❌ {filename} not found")
            return False
        
        try:
            df = pd.read_csv(filepath)
            missing_columns = [col for col in required_columns if col not in df.columns]
            if missing_columns:
                print(f"❌ {filename} missing columns: {missing_columns}")
                return False
            
            if len(df) == 0:
                print(f"❌ {filename} is empty")
                return False
            
            print(f"✅ {filename} valid ({len(df)} rows)")
        
        except Exception as e:
            print(f"❌ Error reading {filename}: {e}")
            return False
    
    return True

def validate_dependencies():
    """Validate required Python packages."""
    print("\n🔍 Validating dependencies...")
    
    required_packages = [
        "langchain",
        "langchain_chroma", 
        "langchain_nvidia_ai_endpoints",
        "langchain_community",
        "pandas",
        "python-dotenv",
        "chromadb"
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing packages: {', '.join(missing_packages)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("✅ All required packages installed")
    return True

def validate_api_connectivity():
    """Test NVIDIA API connectivity."""
    print("\n🔍 Testing NVIDIA API connectivity...")
    
    try:
        from dotenv import load_dotenv
        from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
        
        load_dotenv()
        
        if not os.getenv("NVIDIA_API_KEY"):
            print("❌ NVIDIA_API_KEY environment variable not set")
            return False
        
        # Test embedding model
        embedding_model = NVIDIAEmbeddings(model="nvidia/nv-embed-v1")
        test_embedding = embedding_model.embed_query("test query")
        
        if test_embedding and len(test_embedding) > 0:
            print("✅ NVIDIA API connectivity confirmed")
            return True
        else:
            print("❌ Invalid response from NVIDIA API")
            return False
    
    except Exception as e:
        print(f"❌ API connectivity test failed: {e}")
        return False

def validate_vector_database():
    """Check if vector database exists or can be created."""
    print("\n🔍 Validating vector database setup...")
    
    db_path = Path("db/chroma_db")
    if db_path.exists():
        print("✅ Vector database directory exists")
        
        # Check if it contains data
        if any(db_path.iterdir()):
            print("✅ Vector database contains data")
        else:
            print("⚠️  Vector database is empty - run 1_ingestion_pipeline.py")
    else:
        print("⚠️  Vector database not found - will be created during ingestion")
    
    return True

def main():
    """Main validation function."""
    print("🔍 Validating Course Information RAG System Setup\n")
    
    validation_steps = [
        ("Environment", validate_environment),
        ("Dependencies", validate_dependencies), 
        ("Datasets", validate_datasets),
        ("API Connectivity", validate_api_connectivity),
        ("Vector Database", validate_vector_database)
    ]
    
    passed = 0
    total = len(validation_steps)
    
    for step_name, validation_func in validation_steps:
        try:
            if validation_func():
                passed += 1
        except Exception as e:
            print(f"❌ {step_name} validation failed with error: {e}")
    
    print(f"\n📊 Validation Results: {passed}/{total} checks passed")
    
    if passed == total:
        print("🎉 System validation successful! Ready to run the RAG system.")
        print("\nNext steps:")
        print("1. python 1_ingestion_pipeline.py  # Build vector database")
        print("2. python 4_history_aware_generation.py  # Start chat interface")
    else:
        print("❌ System validation failed. Please fix the issues above.")
        sys.exit(1)

if __name__ == "__main__":
    main()