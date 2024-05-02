import os
import shutil

def organize_files(destination_folder):
    # Create folders if they don't exist
    for folder in destination_folder.values():
        os.makedirs(folder, exist_ok=True)

    # Get the current working directory
    source_folder = os.getcwd()

    # Get a list of all files in the source folder
    files = os.listdir(source_folder)

    for file in files:
        # Get the file extension
        _, file_extension = os.path.splitext(file)

        # Check the extension and move the file to the corresponding folder
        if file_extension.lower() in destination_folder:
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder[file_extension.lower()], file)

            # Handle file name conflicts
            if os.path.exists(destination_path):
                # If the file already exists in the destination, rename it
                base_name, extension = os.path.splitext(file)
                count = 1
                while os.path.exists(os.path.join(destination_folder[file_extension.lower()], f"{base_name}_{count}{extension}")):
                    count += 1
                destination_path = os.path.join(destination_folder[file_extension.lower()], f"{base_name}_{count}{extension}")

            shutil.move(source_path, destination_path)
            print(f"Moved {file} to {destination_path}")
            

if __name__ == "__main__":
    # Specify the destination folders for each file type
    destination_folder = {
        '.jpg': r'C:\Users\User\Pictures\Saved Pictures',
        '.jpeg': r'C:\Users\User\Pictures\Saved Pictures',
        '.png': r'C:\Users\User\Pictures\Saved Pictures',
        '.pdf': r'C:\Users\User\Documents\Documents',
        '.doc': r'C:\Users\User\Documents\Documents',
        '.docx': r'C:\Users\User\Documents\Documents',
        '.txt': r'C:\Users\User\Documents\Documents',
        '.psd': r'C:\Users\User\Documents\Photoshops',
        # Add more file types and corresponding folders as needed
    }

    # Call the function to organize files
    organize_files(destination_folder)