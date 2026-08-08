import time
import os
import shutil

def file_sorter():
    path = input("Paste the path to your folder: ")
    os.chdir(path)

    list_directory = os.listdir(path)

    image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".webp"]
    document_extensions = [".pdf", ".txt", ".docx", ".doc"]
    video_extensions = [".mp4", ".mov", ".avi", ".mkv"]
    audio_extensions = [".mp3", ".wav", ".flac"]
    code_extensions = [".py", ".js", ".html", ".css", ".c", ".cpp"]
    archives_extensions = [".zip", ".rar", ".7z"]

    for file in list_directory:
        #extension = extension.lower()

        if not os.path.exists("Images"):
            os.mkdir("Images")
        else:
            for extension in image_extensions:
                shutil.move(file, "Images")
        if not os.path.exists("Documents"):
            os.mkdir("Documents")
        else:
            for extension in document_extensions:
                shutil.move(file, "Documents")
        if not os.path.exists("Videos"):
            os.mkdir("Videos")
        else:
            for extension in video_extensions:
                shutil.move(file, "Videos")
        if not os.path.exists("Audio"):
                    os.mkdir("Audio")
        else:
            for extension in audio_extensions:
                shutil.move(file, "Audio")
        if not os.path.exists("Code"):
            os.mkdir("Code")
        else:
            for extension in code_extensions:
                shutil.move(file, "Code")
        if not os.path.exists("Archives"):
            os.mkdir("Archives")
        else:
            for extension in archives_extensions:
                shutil.move(file, "Archives")
        if not os.path.exists("Unknown"):
            os.mkdir("Unknown")
        else:
            shutil.move(file, "Unknown")

file_sorter()