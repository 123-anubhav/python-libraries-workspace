# python-libraries-workspace
python demo examples with 
# fast api, # requests , # json, # streamlit ui, # rest apis with mysql db connect and crud
---
---

# To Set Environment and Run the Proejcts Steps

# to set virtual environment of proejct specific
# $ python -m venv .venv  

 # for activate virtual environment
# $ .venv\Scripts\Activate

# for de-Activate virtual environment
# $ deactivate 

 after that install plugin that proejcts requires mentions at file `requirements.txt`
# $ pip install -r `requirements.txt`

 uvicorn proejct file: variable name of where fastapi() define --reload
# example uvicorn main:app --reload

# Note : 
# inside fast api pydantic avaiable and bydefault python has sqlite, json

 requests is use to develop consumer application just like to call http requests.

 json with file and without file concept 

 json with file has uses method dump() to wrtie data inside file and load() to read data from file

 json without file has uses method dumps() to wrtie data and loads() to read data

# Note For JSON is :
  if data getting from `pydantic` then we need to use model_dump() to parse data into json then we can write inside file using dump(parse data)

# Fast API  uses `uvicorn` server to run rest api's and fast api has internally `pydantic` to data validate and requested.

# StreamLit use for quick demo purpose for cassroom or ai developer to develop ui just for basics not need much required knowledge of ui tech html,cs,,angular,reat etc.

# requirements.txt use for to define project requirements plugin 
# example like
```
fastapi
uvicorn
pydantic
```
