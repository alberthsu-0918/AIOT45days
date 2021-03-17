  
# yolo  + Flask

import os
import sys
from flask import Flask, render_template
import time

sys.path.append('/home/pi/darknet/')
PEOPLE_FOLDER = os.path.join('static', 'people_photo')
#from new_darknet import performDetect
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

def default_yolo(): 
    path = os.getcwd()
    imgpath = '/home/pi/Documents/flask_webcam/orangeTest.jpg' #input pic
    #imgpath = '/home/pi/Downloads/test.jpg'
    output_path = '/home/pi/Documents/flask_webcam/static/prediction.jpg' #predict result
    configPath = "./cfg/yolov3_training.cfg"
    weightPath = "./cfg/yolov3_training_final.weights"
    metaPath= "./data/obj.data"
    
    os.chdir('/home/pi/darknet')
    from darknet1 import performDetect

    a = performDetect(imagePath=imgpath, configPath=configPath,
                      weightPath=weightPath, metaPath=metaPath)
    print(a[0])
    
    print(a[0][1])
    os.system('cp -f '+ imgpath + ' ' +output_path) #copy predict to static folder
    os.chdir(path)
    return a

def defult_display():
    ans = default_yolo()
    text0 = 'detect: '+ans[0][0]+'\tconfidence: '\
        +str(format(ans[0][1], '.5f'))
    text2 = '\ntime is: '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    reply = text0 + text2
    return reply


if __name__ == "__main__":
    
    reply = defult_display()
    
    @app.route("/")
    def abc():
        return reply

    @app.route('/index') #put predict pic on address
    def show_index():
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'shovon.jpg')
        return render_template("index.html", user_image = full_filename)

    app.run(host='192.168.199.75', port = 8080, debug = False, threaded = True)
