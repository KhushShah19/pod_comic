

from flask import Flask , redirect, request
# import requests
import time 

app = Flask(__name__) 
  
@app.route("/", methods=['GET']) 
def basic_data(): 
    return redirect("/basic_prompt")

@app.route("/basic_prompt", methods=['GET']) 
def basic_prompt():
    dict_data = {
    "positive": "a beautiful flower", 
    "negative": "blur", 
    "seed": 1234   
    } 
    prompts = {"positive prompt": dict_data['positive'], "negative prompt": dict_data['negative'], "given seed": dict_data['seed']}
    return prompts

@app.route("/basic_prompt_post", methods=['POST']) 
def basic_prompt_post():
    dict_data = request.json
    print(dict_data)
    prompts = {"positive prompt": dict_data['positive'], "negative prompt": dict_data['negative'], "given seed": dict_data['seed']}
    return prompts

def input_values():
    dict_data = {
    "positive": "a beautiful flower", 
    "negative": "blur", 
    "seed": 1234   
    } 
    basic_prompt(dict_data)

if __name__ == "__main__": 
    # app.run(debug=True) 
    # app.run(debug=False)
    # app.run(host='192.168.0.105', port=3000, debug=False) 
    # app.run(host='192.188.0.105')
    app.run(port=3503, debug=False) 
    # time.sleep(10)
    # input_values()






