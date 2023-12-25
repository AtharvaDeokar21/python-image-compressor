import os
import tinify

tinify.key = 'Kf628xxxxxxxxxx' #Enter your own API_KEY

def compress_image(input_path, output_path):
    try:
        source = tinify.from_file(input_path)
        source.to_file(output_path)
        print(f'Image compressed: {input_path}')
    except tinify.Error as e:
        print(f'Error compressing {input_path}: {e.message}')

def compress_folder(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)     # Generating a new destination folder 

    for filename in os.listdir(source_folder):
        input_path = os.path.join(source_folder, filename)
        output_path = os.path.join(destination_folder, filename)

        compress_image(input_path, output_path)


source_folder = r'D:\Atharva\PYTHON\pypng\unoptimized_images' #Location of folder consisting of unoptimized images
destination_folder = r'D:\Atharva\PYTHON\pypng\optimized_images' #This is the destination path.

compress_folder(source_folder, destination_folder)

# The program is made using os module.
# We can also use glob module of python.