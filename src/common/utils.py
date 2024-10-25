import zipfile
import os

def extract_zip(zip_path, extract_to='.'):
    """
    Extracts a zip file to the specified directory.
    
    :param zip_path: Path to the zip file
    :param extract_to: Directory to extract the contents to (default is current directory)
    """
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Successfully extracted {zip_path} to {extract_to}")
    except zipfile.BadZipFile:
        print(f"Error: {zip_path} is not a valid zip file.")
    except FileNotFoundError:
        print(f"Error: The file {zip_path} was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to extract to {extract_to}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Example usage:
# extract_zip('example.zip', 'output_folder')

