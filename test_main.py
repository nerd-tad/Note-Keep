from flask import Flask, render_template
from admin_component.bp1 import bp_1
app = Flask(__name__)
app.register_blueprint(bp_1, url_prefix='/admin')  #only if we see /admin in url we gonna extend things in bp_1

@app.route('/')
def test():
	return '<h1>This is a Test</h1>'

if __name__ == '__main__':
	app.run(port=10001, debug=True)
