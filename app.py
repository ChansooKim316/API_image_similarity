from flask import Flask, request, jsonify
from PIL import Image
import requests, imagehash
'''
* If you encounter any issue with PIL, please run 'pip install Pillow'

* If you want to test out the file upload using Postman, 
  1. please comment out "save_from_urls()" function (line 73),
  2. and uncomment "save_from_file_upload" function (line 76)
  
* Two routes :
  1. http://127.0.0.1:5000/          (for key validation)
  2. http://127.0.0.1:5000/compare   (for image similarity)
'''

app = Flask(__name__)
api_key = "kmrhn74zgzcq4nqb"

# a function that saves images from url requests
# (both inputs should be urls)
def save_from_urls() :
    form_data = request.form.to_dict()
    keys = list(form_data)
    # first value -> url_1 , second value -> url_2
    url_1 = form_data[keys[0]]
    url_2 = form_data[keys[1]]
    try:
        if url_1 and url_2:
            print('url1 :', url_1)
            r = requests.get(url_1)
            with open('./image_1.png', 'wb') as f:
                f.write(r.content)
            print('url 1 done.')
            r = requests.get(url_2)
            with open('./image_2.png', 'wb') as f:
                f.write(r.content)
        else:
            return jsonify({"message": "please check your inputs"}), 422
    except Exception as e:
        return e

# a function that saves images from file upload.
# (both inputs should be files)
def save_from_file_upload():
    try :
        file_1 = request.files['img1']
        file_2 = request.files['img2']
        if file_1 and file_2 :
            file_1.save('image_1.png')
            file_2.save('image_2.png')
        else :
            return jsonify({"message": "please check your inputs"}), 422
    except Exception as e:
        return e

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        headers = request.headers
        first_header = list(headers.keys())[0]
        given_key = headers.get(first_header)
        if given_key == api_key:
            return jsonify({"message": "OK: Authorized"}), 200
        else :
            return jsonify({"message": "ERROR: Unauthorized"}), 401
    return "<h3>API key validating page</h3>"


@app.route('/compare', methods=['GET', 'POST'])
def compare():
    if request.method == 'POST':
        # save images from urls (both inputs should be urls)
        save_from_urls()

        # save images from file_upload (both inputs should be files)
        # save_from_file_upload()

        # read & compare
        try :
            img1 = Image.open('./image_1.png')
            img2 = Image.open('./image_2.png')
        except :
            return  '''
                    failed to read images \n (can't read data uri inputs)
                    '''
        hash = imagehash.average_hash(img1)
        otherhash = imagehash.average_hash(img2)
        similarity = 100 - (hash - otherhash)
        return jsonify({"similarity" : similarity}), 200

    return '<h3>Image comparing page</h3>'

if __name__ == '__main__':
    app.run(debug=True)


