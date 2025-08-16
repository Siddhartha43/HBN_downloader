# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial release of EEG Downloader Tool
- Support for multiple input formats (Excel, CSV, TSV, plain text)
- Batch download functionality
- Smart file naming convention handling
- Comprehensive logging system
- Command-line interface with multiple options
- Error handling and failure reporting

### Fixed
- File naming rule handling for run-based tasks
- Path construction for NAS file structure
- Round number parsing and formatting

## [1.0.0] - 2025-08-16

### Added
- Core EEG file download functionality
- Support for HBN EEG dataset structure
- Automatic file naming convention detection
- Multi-format input parsing
- Progress tracking and statistics
- MIT License

### Features
- **File Naming Rules**: Automatic conversion of task names to file names
  - `contrastChangeDetection_1` → `contrastChangeDetection_run-1_eeg.set`
  - `surroundSupp_1` → `surroundSupp_run-1_eeg.set`
  - `ThePresent` → `ThePresent_eeg.set`
- **Input Formats**: Excel (.xlsx, .xls), CSV, TSV, plain text
- **Output Management**: Customizable output directories
- **Logging**: Detailed console and file logging
- **Error Handling**: Comprehensive error reporting

### Technical Details
- Python 3.7+ compatibility
- Dependencies: pandas, openpyxl, pathlib2
- NAS path configuration support
- Batch processing capabilities
- Memory-efficient file copying

---

## Version History

### v1.0.0 (Current)
- Initial stable release
- 100% success rate on test dataset (39/39 files)
- Comprehensive documentation
- GitHub repository setup
