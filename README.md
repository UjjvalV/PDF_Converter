# DOCX to PDF Converter

A secure and user-friendly Streamlit application that converts `.docx` files  PDF documents. This tool provides a seamless interface for document conversion while offering metadata visualization.


## 📋 Prerequisites

- Python 3.11 or higher
- Required Python packages:
  ```bash
  streamlit
  spire.doc
  ```

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/UjjvalV/PDF_Converter.git
cd PDFConverter
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Launch the application:
```bash
streamlit run main.py
```

## 📁 Project Structure

```
PDFConverter/
│
├── app/
│   ├── converter.py    # Core conversion logic
│   ├── utilities.py    # File operations & metadata handling
│   └── __init__.py     # Package initialization
│
├── main.py            # Streamlit application entry point
├── README.md          # Project documentation
└── requirements.txt   # Dependencies list
```

## 💻 Usage

1. **Upload Your Document**
   - Select any `.docx` file from your system
   - Review the file metadata displayed automatically


2. **Convert and Download**
   - Click the conversion button
   - Download your PDF file
  

## 🌟 Future Enhancements

- Password Protection
- Bulk file conversion capabilities
- Enhanced metadata extraction and display
- Built-in PDF preview functionality
- Cloud storage integration (Google Drive, Dropbox)
- Support for additional document formats



## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👤 Author

**Ujjval Vashisht**
- Email: uvashisht2002@gmail.com


## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](../../issues).



