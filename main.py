from fastapi import FastAPI, HTTPException, Header
import pandas as pd



#membuat object FastAPI -> instance FastAPI
app = FastAPI()

#endpoint mengambil data-> sebuah url
#get/data

password = "123"

#endpoint untuk menampilkan halaman awal / landing page
@app.get('/') #karena biasanya www.example.com/
def getHome():
    #apa yang akan dilakukan oleh server
    return{
        "message" : "selamat datang"
    }

@app.get('/data')
def getData(api_key: str = Header(None)):
    #mengambil data existing
    df = pd.read_csv('data.csv')

    #cek api_key
    if api_key != None or api_key != password:
        #raise error
        raise HTTPException(status_code=401, detail="api-key salah atau tidak ada!")

    #mengembalikan response (data+status code => 200)
    return df.to_dict(orient='records') # mengubah dari dataframe ke dictionary

@app.post('/data/{id}')
def getDataById(id: int):
    #mengambil data existing
    df = pd.read_csv('data.csv')

    filter = df[df['id'] == id]

    if len(filter) == 0:
        raise HTTPException(status_code=404, detail="data tidak ditemukan!")

    #mengembalikan dataframe yang baru 
    return filter.to_dict(orient='records') # mengubah dari dataframe ke dictionary