import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)
def main():
    access_token="sl.BGzWNC_aHBcQ3Mld80WctkWq5cWqMTyVuQpT2D2O5K85UWTaiX8z5iPKpxpFA7VgyPrURCAQmgziS5PGxv-5HbetogEJffWE4KmtMdGZKRwYCKjBn2ALF5JCmM_KStIuSuRQtqE"
    transferData=TransferData(access_token)
    file_from=input("enter the file path to transfer")
    file_to=input("enter the full path to upload to dropbox")
    transferData.upload_file(file_from,file_to)
    print("file has been moved")
main()
for root,dirs,files in os.walk(file_from):
relative_path=os.path.relpath(local_path,file_from)
dropbox_path=os.path.join(file_to,relative_path)
with open(local_path,'rb') as f:
    dbx:files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))