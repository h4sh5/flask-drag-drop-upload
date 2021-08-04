#!/usr/bin/env python3
from flask import Flask, render_template, request,jsonify
from werkzeug.utils import secure_filename
import os
app = Flask(__name__,
            static_url_path='',
            static_folder='templates',
            template_folder='templates')
UPLOADPATH = 'uploads'

@app.route('/')
def index():
   return render_template('index.html')
    
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        import pprint
        pprint.pprint(request.files)

        # files = request.files
        # import code
        # code.interact(local=locals())

        for f in request.files.getlist('files[]'):
            if f.filename != "":
                print('secure filename: ', secure_filename(f.filename))
                f.save(os.path.join(UPLOADPATH, secure_filename(f.filename)))
    
        return jsonify({'message':'file uploaded successfully', 'success':1})
        
if __name__ == '__main__':
   app.run(debug = True)