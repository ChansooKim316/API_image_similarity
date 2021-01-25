## Image Similarity

### This API compares two images, and returns simailarity as a JSON response.


#### ▶  Please install before test out

```bash
pip install fastapi
pip install python-multipart     (to receive 'form-data')
pip install Pillow               (instead of PIL)
pip install 'uvicorn[standard]'  (For Mac)
pip install uvicorn[standard]    (For Windows)
```



#### ▶ To initiate, please run

```bash
uvicorn main:app --reload
```

#### ▶  On Postman, inputs should be :

##### < API key : Authorization -> API Key >
```bash
______________________________________________________
    Route      |      Key       |        Value        |
------------------------------------------------------|    
  :8000/key    |     api_key    |   kmrhn74zgzcq4nqb  |
______________________________________________________|
```
##### < Images : Body -> form-data >
```bash
___________________________________________________
      Route       |    Key     |        Value      |
---------------------------------------------------|        
  :8000/compare   |    url1    |     https:// ...  |
  :8000/compare   |    url2    |     https:// ...  |
___________________________________________________|  
```


#### ▶  Three routes :

  - http://127.0.0.1:8000/         -> landing page
  - http://127.0.0.1:8000/key      -> API Key validation
  - http://127.0.0.1:8000/compare  -> Image comparison
  
  
#### ▶  Environment

- macOS Big Sur 11.0.1
- Python 3.7.0
- FastAPI 0.63.0
- Pillow 8.1.0
- ImageHash 4.2.0
