from fastapi import Security, FastAPI, HTTPException, Form
from fastapi.security.api_key import APIKeyQuery, APIKeyHeader
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.status import HTTP_403_FORBIDDEN
from PIL import Image
import urllib.request, imagehash, ssl


"""  
------- Please install before test out. -------

pip install fastapi
pip install python-multipart     (to receive 'form-data')
pip install Pillow               (instead of PIL)
pip install 'uvicorn[standard]'  (For Mac)
pip install uvicorn[standard]    (For Windows)

------- To initiate, please run  ---------
    
       uvicorn main:app --reload 

------- On Postman, inputs should be : -------

< API key : Authorization -> API Key >
______________________________________________________
    Route      |      Key       |        Value        |
------------------------------------------------------|    
  :8000/key    |     api_key    |   kmrhn74zgzcq4nqb  |
______________________________________________________|

< Images : Body -> form-data >
___________________________________________________
      Route       |    Key     |        Value      |
---------------------------------------------------|        
  :8000/compare   |    url1    |     https:// ...  |
  :8000/compare   |    url2    |     https:// ...  |
___________________________________________________|  
"""

app = FastAPI()

# to avoid urlopen SSL error
ssl._create_default_https_context = ssl._create_unverified_context

# Receive API keys from Query Params or API Key Header
API_KEY = "kmrhn74zgzcq4nqb"
API_KEY_NAME = "api_key"
api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


@app.get("/")
def read_root():
    return "The server is running"


@app.post("/key/")
async def get_api_key(
    api_key_query: str = Security(api_key_query),
    api_key_header: str = Security(api_key_header),
):
    if api_key_query == API_KEY:
        return "You are logged-in"
    elif api_key_header == API_KEY:
        return "You are logged-in"
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate the API key"
        )


@app.post("/compare/")
def compare(url1: str = Form(...), url2: str = Form(...)):
    # download images
    try :
        urllib.request.urlretrieve(url1, "image1.png")
        urllib.request.urlretrieve(url2, "image2.png")
    except Exception as err:
        return "Something went wrong... Please try other images. \n" , err

    # read images
    try:
        img1 = Image.open('image1.png')
        img2 = Image.open('image2.png')
    except Exception as err:
        return "Something went wrong... Please try other images. \n" , err

    # calculate similarity
    hash = imagehash.average_hash(img1)
    otherhash = imagehash.average_hash(img2)
    similarity = 100 - (hash - otherhash)

    # JSON encoding
    json_similarity = jsonable_encoder({"Similarity": similarity})

    return JSONResponse(content=json_similarity)