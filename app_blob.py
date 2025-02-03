import os   
from azure.storage.blob import BlobServiceClient, ContentSettings
from flask import Flask, request 
import magic 

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING') 
container_name = "content" 

blob_service_client = BlobServiceClient.from_connection_string(conn_str=connect_str)
f = magic.Magic(mime=True, uncompress=True)
# content_settings = ContentSettings(content_type="image/jpeg")
# content_settings = ContentSettings(content_type="text/html")
# content_type="image/jpeg"

try:
    container_client = blob_service_client.get_container_client(container=container_name)
    container_client.get_container_properties() 

except Exception as e:
    container_client = blob_service_client.create_container(container_name) 

app = Flask(__name__)  
@app.route("/")  
def view_photos():  
    return '''  
        <h1>Upload new File</h1>  
        <form method="post" action="/upload-photos"   
            enctype="multipart/form-data">  
            <input type="file" name="photos" multiple >  
            <input type="submit">  
        </form>   
        '''  


@app.route("/upload-photos", methods=["POST"])
def upload_photos():
    filenames = ""

    for file in request.files.getlist("photos"):
        if file.filename.split(".")[1]=="jpeg":
            try:
                mime_type = f.from_file(file.filename)
                content_settings = ContentSettings(content_type=mime_type)
                container_client.upload_blob(file.filename, file, content_settings=content_settings)

                #container_client.upload_blob(file.filename, file) 
                filenames += file.filename + "<br /> "
            except Exception as e:
                print(e)
                print("Ignoring duplicate filenames") 
        
    return "<p>Uploaded: <br />{}</p>".format(filenames)        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
