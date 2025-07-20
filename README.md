# 🎵 Spotify Music Downloader

A beautiful, feature-rich Python application to download music from Spotify with an intuitive terminal interface.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Platform](https://img.shields.io/badge/platform-windows-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

- 🔍 **Search and Download**: Search for music by song name, artist, or keywords
- 📥 **Direct URL Download**: Paste Spotify URLs directly
- 📦 **Batch Download**: Download multiple songs at once
- 🎨 **Beautiful UI**: Clean terminal interface with progress bars
- 📊 **Statistics**: Track your download history
- 🚀 **Standalone Executable**: No Python installation required for end users

## 🖼️ Screenshots

```
═══════════════════════════════════════════════════════════
                🎵 SPOTIFY MUSIC DOWNLOADER 🎵
               Download your favorite music from Spotify
═══════════════════════════════════════════════════════════

┌─────────────────────────────────────────────┐
│                  MAIN MENU                  │
├─────────────────────────────────────────────┤
│  1. 🔍 Search and Download Music           │
│  2. 📥 Download from Spotify URL           │
│  3. 📦 Batch Download URLs                 │
│  4. 📊 View Statistics                     │
│  5. ❌ Exit                               │
└─────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Option 1: Use the Executable (Recommended)
1. Download `SpotifyDownloader.exe` from the [Releases](../../releases) section
2. Double-click to run (No Python installation required!)
3. Follow the on-screen prompts

### Option 2: Run from Source
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/spotify-downloader.git
cd spotify-downloader

# Install dependencies
pip install -r requirements.txt

# Run the application
python music_v2.py
```

## 📋 Requirements

### For Executable Users:
- ✅ Windows OS
- ✅ [spotDL](https://github.com/spotDL/spotify-downloader) installed (`pip install spotdl`)
- ✅ Internet connection

### For Developers:
- Python 3.7+
- spotDL
- Dependencies listed in `requirements.txt`

## 🛠️ Installation

### Install spotDL (Required)
```bash
pip install spotdl
```

### Verify Installation
```bash
spotdl --version
```

## 🎯 Usage Examples

### Search and Download
1. Run the application
2. Choose option `1` (Search and Download)
3. Enter song name: `"Shape of You Ed Sheeran"`
4. Select from search results
5. Choose output directory

### Direct URL Download
1. Copy a Spotify URL: `https://open.spotify.com/track/...`
2. Choose option `2` (Direct URL Download)
3. Paste the URL
4. Watch the magic happen!

### Batch Download
1. Choose option `3` (Batch Download)
2. Enter multiple Spotify URLs
3. Press Enter on empty line to start
4. All songs download automatically

## 📁 Project Structure

```
spotify-downloader/
├── music_v2.py              # Main application
├── music.py                 # Original version
├── music_enhanced.py        # Enhanced version (deprecated)
├── SpotifyDownloader.exe    # Standalone executable
├── spotify_icon.png         # Application icon
├── README.md               # This file
├── README_EXECUTABLE.md    # Executable-specific documentation
├── requirements.txt        # Python dependencies
└── dist/                   # Built executables
    └── SpotifyDownloader.exe
```

## 🔧 Building from Source

### Create Executable
```bash
# Install PyInstaller
pip install pyinstaller pillow

# Build executable with icon
pyinstaller --onefile --console --name "SpotifyDownloader" --icon="spotify_icon.png" music_v2.py
```

## 🐛 Troubleshooting

### Common Issues

**"spotdl is not recognized"**
```bash
pip install spotdl
# or
pip install --upgrade spotdl
```

**Downloads fail**
- Check internet connection
- Verify Spotify URL is valid
- Ensure spotDL is up to date

**Antivirus blocks executable**
- Add to antivirus whitelist
- This is a common false positive for PyInstaller executables

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational purposes only. Please respect artists and copyright laws. Only download music you have the right to download.

## 🙏 Acknowledgments

- [spotDL](https://github.com/spotDL/spotify-downloader) - The amazing library that powers this application
- [PyInstaller](https://www.pyinstaller.org/) - For creating standalone executables
- [Icons8](https://icons8.com/) - For the beautiful Spotify icon

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](../../issues) section
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about your environment and the error

---

⭐ **Star this repository if you found it helpful!** ⭐
