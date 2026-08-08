import time
import os
import shutil

def file_sorter():
    print("Welcome to the File Extension Sorter!")

    try:
        path = input("Please paste the path to your folder (eg. C:\\...): ")

        if not os.path.exists(path):
            raise FileNotFoundError(f"The path '{path}' does not exist!")
        if not os.path.isdir(path):
            raise NotADirectoryError(f"The path '{path}' is a file, not a folder.")

        contents = os.listdir(path) 
        print("Folder accessed successfully!")

    except FileNotFoundError as e:
        print(f"Path Error: {e}")
        return
    except NotADirectoryError as e:
        print(f"Type Error: {e}")
        return

    image_extensions = (".jpg", ".jpeg", ".png", ".gif", ".webp")
    document_extensions = (".pdf", ".txt", ".docx", ".doc")
    video_extensions = (".mp4", ".mov", ".avi", ".mkv")
    audio_extensions = (".mp3", ".wav", ".flac")
    code_extensions = (".py", ".js", ".html", ".css", ".c", ".cpp")
    archives_extensions = (".zip", ".rar", ".7z")

    for file in contents:
        lower_file = file.lower()

        if lower_file.endswith(image_extensions):
            print(f"Moving {file} to Images folder...")
            time.sleep(1.5)

            image_folder = os.path.join(path, "Images")
            os.makedirs(image_folder, exist_ok=True)
            shutil.move(os.path.join(path, file), image_folder)

        elif lower_file.endswith(document_extensions):
            print(f"Moving {file} to Documents folder...")
            time.sleep(1.5)

            document_folder = os.path.join(path, "Documents")
            os.makedirs(document_folder, exist_ok=True)
            shutil.move(os.path.join(path, file), document_folder)

        elif lower_file.endswith(video_extensions):
            print(f"Moving {file} to Videos folder...")
            time.sleep(1.5)
            
            video_folder = os.path.join(path, "Videos")
            os.makedirs(video_folder, exist_ok=True)
            shutil.move(os.path.join(path, file), video_folder)

        elif lower_file.endswith(audio_extensions):
            print(f"Moving {file} to Audios folder...")
            time.sleep(1.5)
            
            audio_folder = os.path.join(path, "Audios")
            os.makedirs(audio_folder, exist_ok=True)
            shutil.move(os.path.join(path, file), audio_folder)

        elif lower_file.endswith(code_extensions):
            print(f"Moving {file} to Codes folder...")
            time.sleep(1.5)
            
            code_folder = os.path.join(path, "Codes")
            os.makedirs(code_folder, exist_ok=True)
            shutil.move(os.path.join(path, file), code_folder)

        elif lower_file.endswith(archives_extensions):
            print(f"Moving {file} to Archives folder...")
            time.sleep(1.5)
            
            archives_folder = os.path.join(path, "Images")
            os.makedirs(archives_folder, exist_ok=True)
            shutil.move(os.path.join(path, file), archives_folder)

        else:
            print(f"Moving {file} to Unknown folder...")
            time.sleep(1.5)

            unknown_folder = os.path.join(path, "Unknown")
            os.makedirs(unknown_folder, exist_ok=True)
            shutil.move(os.path.join(path, file), unknown_folder)

    print("Files Have Been Sorted Successfully!")

file_sorter()