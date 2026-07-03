#!/home/prince/File-Sharing/venv/bin/python3

from flask import Flask, request, render_template,send_from_directory
import os
import socket

port = 5000
folderPath = '/tmp/uploads'
if not os.path.exists(folderPath):
    os.makedirs(folderPath)
#INITIALIZING THE UPLOAD FOLDER
with open(f"{folderPath}/INITIALISATION" , "wb") as f:
    f.write(b'x00')


app = Flask(__name__)
file_path=folderPath
# Set the folder where you want to store the uploaded files
app.config['UPLOAD_FOLDER'] = folderPath
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['file']
    if f:

        f.save(f"{folderPath}/{f.filename}")
        return 'File uploaded successfully.'
    else:
        return 'File not uploaded.'



@app.route('/get_urls')
def send_url():
    files=os.listdir(folderPath)
    return files


@app.route('/download/<filename>',methods=['GET'])
def download(filename):
    #return render_template('index.html')
    # Use send_from_directory to serve the file
    return send_from_directory(folderPath,filename, as_attachment=True)
    
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('192.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
localIP = get_local_ip()  
          
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0" ,port=port)       
