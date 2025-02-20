# GIF Combine

A Python utility to combine two GIF images side by side while maintaining the frame rate of the first GIF. This tool is perfect for creating comparison GIFs or combining multiple animated sequences.

## Features

- Combines two GIF images side by side
- Maintains the frame rate of the first GIF
- Supports different sized GIFs with automatic vertical centering
- Preserves transparency in GIF files
- Handles GIFs with different frame counts by looping shorter animations
- Output GIFs are set to loop forever
- Easy to use command line interface
- Comprehensive test suite included

## Requirements

- Python 3.8+
- Dependencies (automatically installed):
  - Pillow (PIL) >= 10.0.0 - Image processing
  - imageio >= 2.33.1 - GIF reading/writing
  - numpy >= 1.26.4 - Array operations
  - pytest >= 8.0.0 - Testing framework (development only)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/gifcombine.git
cd gifcombine
```

2. Create and activate a virtual environment:
```bash
# macOS/Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage
```bash
python gifcombine.py input1.gif input2.gif output.gif
```

### Example
```bash
python gifcombine.py animation1.gif animation2.gif combined.gif
```

### Notes
- The frame rate of the first GIF will be used for the combined output
- If GIFs have different heights, they will be centered vertically
- If GIFs have different frame counts, the shorter one will loop
- The output GIF will maintain transparency if present in the input files
- All output GIFs are configured to loop infinitely

## Development

### Running Tests
```bash
pytest test_gifcombine.py -v
```

### Project Structure
```
gifcombine/
├── README.md
├── requirements.txt
├── gifcombine.py      # Main script
├── test_gifcombine.py # Test suite
└── .gitignore
```

### Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Install development dependencies (`pip install -r requirements.txt`)
4. Make your changes
5. Run the tests (`pytest test_gifcombine.py -v`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## Troubleshooting

### Common Issues
1. **"ModuleNotFoundError"**: Make sure you've activated the virtual environment and installed dependencies
2. **"FileNotFoundError"**: Verify the input GIF files exist and paths are correct
3. **Memory Issues**: When combining very large GIFs, ensure sufficient system memory is available

### Error Messages
- If you see "Usage: python gifcombine.py input1.gif input2.gif output.gif", you need to provide all three required arguments
- If you get a PIL-related error, ensure your input files are valid GIF images

## License

MIT License - See [LICENSE](LICENSE) for details

## Authors

- Initial work - [Your Name]

## Acknowledgments

- Built with [Pillow](https://python-pillow.org/) and [imageio](https://imageio.readthedocs.io/)
- Inspired by the need for easy GIF comparison tools

## Version History

- 1.0.1 (2024-02-20)
  - Added infinite looping for output GIFs
- 1.0.0 (2024-02-20)
  - Initial release
  - Basic side-by-side GIF combining functionality
  - Test suite implementation 