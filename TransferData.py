import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.Axq0qk46P3VNd16w2TGMCkER4E_byV0fDdWVYPlvu5thd1jMewI_PBd1GcxkrWUO5bq0ZiNp6N2KkCw4YrZbw8HfcE39UnfcK98o3hGfo-uC6BKzrWi85M9F64R_6VpVrlPyVvgC'
    transferData = TransferData(access_token)

    file_from = input("Enter The File Path To Transfer: ")
    file_to = input("Enter The Full Path To Upload The DropBox: ")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File Has Been Moved")

if __name__ == '__main__':
    main()