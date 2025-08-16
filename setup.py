#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="eeg-downloader",
    version="1.0.0",
    author="EEG Downloader Team",
    author_email="your.email@example.com",
    description="A Python tool for automatically downloading EEG files from NAS storage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/eeg-downloader",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "eeg-downloader=eeg_downloader:main",
        ],
    },
    keywords="eeg, neuroscience, data-download, nas, batch-processing",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/eeg-downloader/issues",
        "Source": "https://github.com/yourusername/eeg-downloader",
        "Documentation": "https://github.com/yourusername/eeg-downloader#readme",
    },
)
