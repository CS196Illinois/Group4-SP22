import pandas as pd
import numpy as np
import random
from flask import Flask, request
df = pd.read_csv("threewords.csv")
max_index = df.shape[0] - 1
print("loaded dataframe")

app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello world!"
@app.route('/movies', methods=['GET'])
def result():
    if request.method == 'GET':
        #pull random row and return
        index = int(request.args.get('index'))
        if index is None:
            index = random.randint(0, max_index)
        ret = {"Title": df["Movie_Title"][index], "Year": int(df["Year"][index]), "ThreeWords":  df["ThreeWords"][index]}
        print(ret)
        return ret

if __name__ == '__main__':
    app.run(port=3000)