# 서비스
from flask import Flask

app =   Flask(__name__)

@app.route('/')
def home() :
    return 'aws 홈페이지3'

if __name__ == "__main__" :
    app.run( debug= True )