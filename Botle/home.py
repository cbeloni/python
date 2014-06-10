import bottle

try:  # do not edit! added by PythonBreakpoints
    from ipdb import set_trace as _breakpoint
except ImportError:
    from pdb import set_trace as _breakpoint


@bottle.route('/')
def home_page():
	return "Hello World\n"

@bottle.route('/testpage')
def test_page():
	return  "<li>This is a teste page</li>"
bottle.debug(True)
bottle.run(host='localhost', port=8080)	
