from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


gauth = GoogleAuth()  
gauth.CommandLineAuth()         
drive = GoogleDrive(gauth)  

upload_file = 'disco.png'
gfile = drive.CreateFile({'parents': [{'id': '1pzschX3uMbxU0lB5WZ6IlEEeAUE8MZ-t'}]})
	# Read file and set it as the content of this instance.
gfile.SetContentFile(upload_file)
gfile.Upload() # Upload the file.