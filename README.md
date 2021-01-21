## Image Similarity

### This api compares two images, and response with their simailarity (JSON).


#### ■  To run this,

* Bash
```bash
$ export FLASK_APP=app
$ flask run
```
* CMD
```cmd
set FLASK_APP=app
flask run
```
* Powershell
```powershell
$env:FLASK_APP = "app"
flask run
```


#### ■  If you encounter any issue with importin PIL, please run ```pip install Pillow```

#### ■  If you want to test out the file upload using Postman,

  1. Please comment out ```save_from_urls()``` function (line 73),

  2. and uncomment ```save_from_file_upload()``` function (line 76)
 
#### ■  Two routes :
  - http://127.0.0.1:5000/  (for API key validation)
  - http://127.0.0.1:5000/compare  (for image similarity)
  
  
#### ■  Environment

- macOS Big Sur 11.0.1
- Python 3.7.0
- Flask 1.1.2
- Werkzeug 1.0.1
