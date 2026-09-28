# Contributing to Course Information RAG System

Thank you for your interest in contributing to this RAG-based course recommendation system! This document provides guidelines for contributing to the project.

## Development Setup

1. Fork the repository
2. Clone your fork locally
3. Create a virtual environment: `python -m venv venv`
4. Activate the environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
5. Install dependencies: `pip install -r requirements.txt`
6. Copy `.env.example` to `.env` and add your NVIDIA API key

## Project Structure

- `1_ingestion_pipeline.py` - Data processing and vector database creation
- `2_retrieval_pipeline.py` - Retrieval testing and validation
- `3_answer_generation.py` - Basic RAG implementation
- `4_history_aware_generation.py` - Advanced conversational RAG system
- `Datasets/` - Course data from multiple platforms
- `db/` - ChromaDB vector database storage

## How to Contribute

### Reporting Issues
- Check existing issues before creating a new one
- Use clear, descriptive titles
- Include system information and error messages
- Provide steps to reproduce the issue

### Suggesting Enhancements
- Open an issue with the "enhancement" label
- Describe the feature and its benefits
- Consider backward compatibility

### Code Contributions
1. Create a feature branch: `git checkout -b feature-name`
2. Make your changes
3. Add tests if applicable
4. Update documentation
5. Ensure code follows the existing style
6. Submit a pull request

## Coding Standards

- Follow PEP 8 for Python code style
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep functions focused and modular
- Handle errors gracefully

## Testing

- Test your changes with various query types
- Verify vector database operations work correctly
- Check conversational flow and memory retention
- Validate metadata preservation and URL accuracy

## Documentation

- Update README.md if adding new features
- Add inline comments for complex logic
- Document any new configuration options
- Include examples for new functionality

## Pull Request Process

1. Update documentation as needed
2. Ensure all tests pass
3. Add a clear description of changes
4. Reference related issues
5. Wait for code review and feedback

## Questions or Need Help?

Feel free to open an issue for questions about:
- Architecture decisions
- Implementation details
- Feature requests
- Bug reports

Thank you for contributing to making course discovery more intelligent and accessible!