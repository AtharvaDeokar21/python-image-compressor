# Image Compression Script

This Python script utilizes the Tinify API to compress images in a specified folder, reducing their file size while maintaining quality.

## Features

- Compresses images using the Tinify API.
- Supports compressing individual images or all images in a folder.
- Generates optimized images in a specified destination folder.

## Setup

1. **Clone the repository**

2. **Tinify API Key:**
   - Obtain an API key from [Tinify](https://tinypng.com/developers) and replace the placeholder in the script with your key:

     ```python
     tinify.key = 'your_tinify_api_key'
     ```

3. **Installation:**
   - Install the Tinify Python package:

     ```bash
     pip install tinify
     ```

4. **Update the source and destination folders in the script**
    ```python
    source_folder = r'path/to/source/folder'
    destination_folder = r'path/to/destination/folder'
    ```

## Run the Script
Execute the script to compress images:
    ```bash
    python image_compressor.py
    ```

## Notes

• The program uses the os module for file and folder operations.
• Consider using the glob module for more advanced file matching patterns.

## Contributing
Feel free to contribute to this project by opening issues or creating pull requests.

