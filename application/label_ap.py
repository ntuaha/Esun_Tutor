import pandas as pd
import json
from flask import Flask,g
from flask import request as req
from flask import jsonify
from flask import Response

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
db = pd.read_excel('../sample.xlsx')

# https://github.com/ntuaha/FMP/blob/master/src/main.py#L21
# 基本設定
@app.route('/')
def hello():
  return "HI"

# 取得目前所有使用者名單
@app.route('/user/<int:uid>',methods=['GET'])
def getUserProfile(uid):
  label = json.loads(db[db.Cust_No == uid].to_json(orient='records',force_ascii=False))
  res = jsonify(label)
  res.headers['Content-Type'] = 'application/json; charset=utf-8'
  return res
  
if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=6001)