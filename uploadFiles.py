import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs,files in os.walk(file_from):

            for filename in files:

                local_path = os.path.join(root, filename)

                relative_path = os.path.realpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, "rb") as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode("overwrite"))

def main():
    access_token ="jS9gvv7qSrIAAAAAAAAAAc9CloE-lFpsGbiXy2MYBSzFpsL-ucEAXuXI0wbrv4Cn"
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder to be uploaded : "))
    file_to = input("Enter the full path to upload in dropbox : ")

    transferData.upload_files(file_from, file_to)
    print("The file had been moved.")

main()