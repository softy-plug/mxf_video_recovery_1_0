import os

os.system("pip install ffmpeg-python")

import subprocess

# import os
import ffmpeg

# Create the output directory if it doesn't exist
output_dir = os.path.join(os.getcwd(), 'out')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get all MXF files in the current directory
mxf_files = [f for f in os.listdir() if os.path.isfile(f) and f.lower().endswith('.mxf')]

for mxf_file in mxf_files:
    input_file = os.path.join(os.getcwd(), mxf_file)
    
    # Determine the output file format based on the original file
    if mxf_file.lower().endswith('.mxf'):
        output_file = os.path.join(output_dir, os.path.splitext(mxf_file)[0] + '.mp4')
    else:
        output_file = os.path.join(output_dir, os.path.splitext(mxf_file)[0] + '.mxf')

    # Convert the video file using ffmpeg
    stream = ffmpeg.input(input_file)
    stream = ffmpeg.output(stream, output_file)
    ffmpeg.run(stream)

print("Conversion complete. Converted files saved in 'out' directory.")

# softy_plug