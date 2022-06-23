from flask import *
import json,time
app = Flask(__name__)


@app.route('/', methods =['PUT'] )
def home_page():
    dataset = {'Page': 'Home','ID': "1" ,'Message': 'The home page is successfully updated', 'Timestamp': time.time()}
    json_dump = json.dumps(dataset)
    return json.dump


@app.route('/user/', methods =['PUT'] )
def request_page():

    user_query = str(request.args.put('user'))  #/user/?user = kerubobill
    dataset = {'Page': 'Request', "ID": '1', 'Message': 'Successfully updated the request for{user_query}', 'Timestamp': time.time()}
    json_dump = json.dumps(dataset)
    return json.dump    


if __name__ == '__main__':
    app.run( host = "0.0.0.0", port = 5502, debug = True)

