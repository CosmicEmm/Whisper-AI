import whisper
from sys import argv
import os
import logging

# Configure logging to display messages with timestamps and log levels (required otherwise logs won't display)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Check if the filename argument is provided
if len(argv) < 2:
    logging.error("No filename provided. Please provide the filename you want to transcribe.")
    exit(1)

# Retrieve the filename from the command-line arguments
filename = argv[1]

# Construct the full path to the input file
input_file_path = os.path.join(r'F:\Audit and Assurance', f'{filename}.ts')

# Define the output directory where the transcript will be saved
output_dir = r'G:\My Drive\Repos\Whisper\Transcripts'

# Construct the full path to the output file
output_file_path = os.path.join(output_dir, f'{filename}.txt')

# Load the Whisper model with a custom download directory
logging.info('Loading Whisper AI - medium...')
model = whisper.load_model("medium", download_root=r'F:\AI\models\Whisper')
logging.info("Model loaded!")

# Perform the transcription
logging.info('Transcription in process... Have some patience!')
result = model.transcribe(input_file_path)
logging.info('Transcription process completed!')

# Write the transcribed text to the output file
logging.info(f'Writing text file and saving it to {output_dir}...')

# Open the output file in write mode with UTF-8 encoding
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(result['text'])  # Write the transcribed text to the file

logging.info("Operation completely successfully!")