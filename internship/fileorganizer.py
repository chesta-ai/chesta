import os
import shutil

# Function to create a directory if it doesn't exist
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Function to organize files
def organize_files(source_folder):
    # Create destination folders based on file types
    image_folder = os.path.join(source_folder, 'Images')
    document_folder = os.path.join(source_folder, 'Documents')
    audio_folder = os.path.join(source_folder, 'Audio')
    video_folder = os.path.join(source_folder, 'Videos')
    other_folder = os.path.join(source_folder, 'Others')

    # Create the directories if they don't exist
    create_directory(image_folder)
    create_directory(document_folder)
    create_directory(audio_folder)
    create_directory(video_folder)
    create_directory(other_folder)

    # Define file extensions for each category
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    document_extensions = ['.txt', '.pdf', '.docx', '.xlsx', '.pptx']
    audio_extensions = ['.mp3', '.wav', '.flac', '.aac']
    video_extensions = ['.mp4', '.mkv', '.avi', '.mov']
    
    # List all files in the source folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, extension = os.path.splitext(filename)

        # Organize based on extension
        if extension.lower() in image_extensions:
            destination = os.path.join(image_folder, filename)
        elif extension.lower() in document_extensions:
            destination = os.path.join(document_folder, filename)
        elif extension.lower() in audio_extensions:
            destination = os.path.join(audio_folder, filename)
        elif extension.lower() in video_extensions:
            destination = os.path.join(video_folder, filename)
        else:
            destination = os.path.join(other_folder, filename)

        # Move the file to the corresponding folder
        shutil.move(file_path, destination)
        print(f"Moved: {filename} to {destination}")

# Main execution
if __name__ == "__main__":
    source_folder = input("Enter the path to the folder you want to organize: ")
    
    if os.path.exists(source_folder):
        organize_files(source_folder)
        print("File organization complete!")
    else:
        print("The specified folder does not exist!")
