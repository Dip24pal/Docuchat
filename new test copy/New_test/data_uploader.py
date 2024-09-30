# data_uploader.py
import os

def save_pdf(uploaded_file, directory="/app/data"):
    """
    Save the uploaded PDF file to the specified directory.

    Args:
        uploaded_file: The file uploaded by the user (Streamlit's UploadedFile object).
        directory (str): The path to the directory where the file should be saved.

    Returns:
        str: The path where the file was saved, or None if an error occurred.
    """
    
    if not os.path.exists(directory):
        os.makedirs(directory)

    
    file_path = os.path.join(directory, uploaded_file.name)
    
    try:
        
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return file_path
    except Exception as e:
        print(f"Error saving file: {e}")
        return None