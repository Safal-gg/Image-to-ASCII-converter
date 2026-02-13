# 🖼️ Image to ASCII Converter (Python)

Convert any image into ASCII art using Python.  
This project transforms images (like the Mona Lisa) into text-based representations using brightness mapping and character gradients.

---

## ✨ Features

- 📷 Load any image from file path
- 🔄 Automatic resizing with aspect ratio correction
- 🌑 Grayscale conversion for brightness analysis
- 🔤 ASCII character mapping based on pixel brightness
- 🖥️ Terminal-friendly output
- 🎨 Supports custom ASCII gradients

---

## 🧠 How It Works

1. **Load Image** using Pillow
2. **Resize** while maintaining aspect ratio
3. **Convert to Grayscale** (0–255 brightness scale)
4. **Map Brightness → ASCII Characters**
5. **Render ASCII Art** in terminal

---

## 📦 Requirements

- Python 3.x
- Pillow library

Install Pillow:

```bash
pip install pillow
