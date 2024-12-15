import json

from IPython.lib.deepreload import reload
from flask import Flask, request
app = Flask(__name__)
@app.route('/prime_number')
def prime_number():
    args=request.args
    numbers=[]
    integer=int(args.get('integer'))
    for number in range(1, integer + 1):
        number /=1
        if integer % number == 0:
            numbers.append(number)
    if integer == 1:
        response={"Number" : integer, "isPrime": False}
    elif len(numbers)==2:
        response={"Number": integer, "isPrime": True}
    else:
        response={"Number": integer, "isPrime": False}
    return json.dumps(response)
if __name__ == '__main__':
    app.run(use_reloader=True, debug=True, host='127.0.0.1', port=5000)


