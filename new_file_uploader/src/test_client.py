import os
import main_uploader

if __name__ == '__main__':
    client = main_uploader.Client('localhost:8888')

    file_name = "upload_this_file.txt"
    client.upload(file_name)