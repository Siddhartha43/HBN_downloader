# EEG File Downloader Tool

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/yourusername/eeg-downloader/graphs/commit-activity)

A Python tool for automatically downloading EEG files from NAS storage based on subject IDs, round numbers, and task names.

## 🚀 Features

- **Multi-format Input Support**: Excel (.xlsx, .xls), CSV, TSV, and plain text files
- **Batch Download**: Download multiple EEG files simultaneously
- **Smart File Naming**: Automatically handles complex file naming conventions including run numbers
- **Comprehensive Logging**: Detailed logs for successful downloads and failures
- **Flexible Configuration**: Customizable NAS paths and output directories
- **Error Handling**: Robust error handling with detailed failure reports

## 📋 Requirements

- Python 3.7 or higher
- Access to NAS storage with EEG files
- Required Python packages (see `requirements.txt`)

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/eeg-downloader.git
   cd eeg-downloader
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Usage

### Quick Start

For immediate use with the provided sample data:

```bash
python simple_download.py
```

This will download all 39 sample files to the `my_eeg_files` directory.

### Basic Usage

#### From Text File:
```bash
python eeg_downloader.py --input data.txt --output ./downloads
```

#### From Excel File:
```bash
python eeg_downloader.py --input data.xlsx --output ./downloads
```

#### Direct Text Input:
```bash
python eeg_downloader.py --text "sub-NDARAU044FP6	R10	ThePresent" --output ./test
```

### Advanced Usage

#### Custom NAS Path:
```bash
python eeg_downloader.py --nas-path /your/nas/path --input data.txt --output ./downloads
```

#### Batch Processing:
```bash
python eeg_downloader.py --input batch1.txt --output ./batch1
python eeg_downloader.py --input batch2.txt --output ./batch2
```

## 📊 Data Format

Input data should be in three-column format, tab-separated:

```
SubjectID	Round	TaskName
sub-NDARAU044FP6	R10	ThePresent
sub-NDARCA851LUG	R10	DiaryOfAWimpyKid
sub-NDARVB588TM7	R10	contrastChangeDetection_1
sub-NDARUZ062BWR	R10	surroundSupp_1
```

### File Naming Rules

The tool automatically handles complex file naming conventions:

| Input Task Name | Actual File Name |
|----------------|------------------|
| `ThePresent` | `ThePresent_eeg.set` |
| `contrastChangeDetection_1` | `contrastChangeDetection_run-1_eeg.set` |
| `surroundSupp_1` | `surroundSupp_run-1_eeg.set` |
| `contrastChangeDetection_2` | `contrastChangeDetection_run-2_eeg.set` |

## 📁 File Structure

The tool expects the following NAS structure:

```
/mnt/left/home/2025/eegimage/HBN-EEG/
├── HBN_EEG_R10/
│   └── sub-NDARAU044FP6/
│       └── eeg/
│           └── sub-NDARAU044FP6_task-ThePresent_eeg.set
└── HBN_EEG_R11/
    └── ...
```

## 📈 Performance

Tested with 39 sample files:
- **Success Rate**: 100% (39/39 files)
- **Average Download Time**: ~2-3 seconds per file
- **Total Size**: ~2.5 GB

## 🔧 Configuration

### Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--input, -i` | Input file path | None |
| `--text, -t` | Direct text input | None |
| `--output, -o` | Output directory | `./downloaded_eeg` |
| `--nas-path` | NAS base path | `/mnt/left/home/2025/eegimage/HBN-EEG` |

### Environment Variables

You can set the default NAS path using environment variables:

```bash
export EEG_NAS_PATH="/your/nas/path"
```

## 📝 Logging

The tool provides comprehensive logging:

- **Console Output**: Real-time progress updates
- **Log File**: `eeg_download.log` with detailed information
- **Statistics**: Success/failure counts and file lists

Example log output:
```
2025-08-16 16:09:32,933 - INFO - 下載完成! 成功: 39, 失敗: 0
```

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 🐛 Troubleshooting

### Common Issues

**Q: Files not found on NAS?**
A: Check the NAS path and file structure. Ensure the subject folders exist.

**Q: Permission denied?**
A: Verify you have read access to the NAS directory.

**Q: Wrong file names?**
A: The tool automatically handles file naming conventions. Check the mapping table above.

**Q: Memory issues with large files?**
A: The tool uses efficient file copying. For very large datasets, consider processing in smaller batches.

### Getting Help

If you encounter issues:

1. Check the log file (`eeg_download.log`)
2. Verify your input data format
3. Ensure NAS connectivity
4. Open an issue on GitHub with:
   - Error message
   - Input data sample
   - System information

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- HBN EEG Dataset for providing the sample data structure
- Python community for excellent libraries
- Contributors and users of this tool

---

⭐ If this tool helps you, please give it a star on GitHub!
