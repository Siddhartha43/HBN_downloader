#!/bin/bash

# EEG Downloader Tool - Git Repository Initialization Script
# This script helps you initialize a Git repository and prepare for GitHub

echo "🚀 Initializing Git repository for EEG Downloader Tool..."

# Initialize Git repository
git init

# Add all files (except those in .gitignore)
git add .

# Create initial commit
git commit -m "Initial commit: EEG Downloader Tool v1.0.0

- Core EEG file download functionality
- Support for multiple input formats (Excel, CSV, TSV, plain text)
- Smart file naming convention handling
- Batch download capabilities
- Comprehensive logging and error handling
- MIT License and documentation"

echo "✅ Git repository initialized successfully!"
echo ""
echo "📋 Next steps:"
echo "1. Create a new repository on GitHub"
echo "2. Add the remote origin:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/eeg-downloader.git"
echo "3. Push to GitHub:"
echo "   git push -u origin main"
echo ""
echo "🔧 Before pushing, please update:"
echo "- README.md: Replace 'yourusername' with your actual GitHub username"
echo "- setup.py: Update author email and project URLs"
echo "- LICENSE: Update copyright holder if needed"
echo ""
echo "📁 Files included in this repository:"
echo "- Core Python scripts (eeg_downloader.py, simple_download.py)"
echo "- Documentation (README.md, 使用說明.md, CHANGELOG.md)"
echo "- Configuration files (.gitignore, requirements.txt, setup.py)"
echo "- GitHub templates (.github/ISSUE_TEMPLATE/)"
echo "- License and contribution guidelines"
echo ""
echo "❌ Files excluded (via .gitignore):"
echo "- Downloaded EEG files (my_eeg_files/)"
echo "- Log files (*.log)"
echo "- Python cache files (__pycache__/)"
echo "- IDE and system files"
