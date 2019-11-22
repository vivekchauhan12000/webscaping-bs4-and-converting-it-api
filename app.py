from bottle import route, run

@route('/home')
def hello():
    return "News api"

run(host='localhost', port=8080, debug=True)