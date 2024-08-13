from flask import Flask, request, render_template,send_from_directory
import os, json,webbrowser
import socket
import qrcode #FOR GENERATE QR CODE FOR URL/LOCAL IP BUT CURRENTLY NOT IN USE

port = 5000
folderPath = r'd:\DEVELOPERS !!!\PYTHON DEVLOPMENT\File Transfer\uploads'


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
        return 'No file uploaded.'


@app.route('/get_urls')
def send_url():
    files=os.listdir(folderPath)
    return files


@app.route('/download/<filename>',methods=['GET'])
def download(filename):
    #return render_template('index.html')
    # Use send_from_directory to serve the file
    return send_from_directory('uploads',filename, as_attachment=True)    
    
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
######
# To be used when have to generate qr code to share its url/local IP

# img = qrcode.make(f'http://{localIP}:{port}/')
# img.show(img)
#####

localIP = get_local_ip()  
          
if __name__ == '__main__':
    webbrowser.open(f'http://{localIP}:5000')
    app.run(debug=True,host="0.0.0.0" ,port=port)       