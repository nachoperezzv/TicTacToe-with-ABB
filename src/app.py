from flask import (
    Flask, 
    jsonify,
    request,
    render_template
)

app = Flask("servicios")
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'wav'}

@app.route('/')
def main():
    return render_template('index.html')
    

if __name__ == '__main__':
    app.debug = True
    app.run(
        host="0.0.0.0",
        port=5000
    )


