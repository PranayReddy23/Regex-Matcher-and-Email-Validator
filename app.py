from flask import Flask, request, render_template

app = Flask(__name__)
import re
################################################
@app.route('/', methods = ['GET', 'POST'])
def regex_match():
    match = None
    if request.method == 'POST':
        pattern = request.form.get('pattern')
        text = request.form.get('string')

        try:
            match = re.findall(pattern, text)
            if match:
                if isinstance(match[0], tuple):
                    match = [item for tup in match for item in tup]
                match = ', '.join(match)
            else:
                match = 'No Match Found'
        except re.error:
            match = 'Invalid Regex Pattern'
    
    return render_template('regex_home.html', match = match)


@app.route('/email_validator', methods=['GET', 'POST'])
def email_validator():
    match = None
    if request.method == 'POST':
        mail = request.form.get('email_address')

        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+\.[a-zA-Z]{2,}$'
        
        if re.fullmatch(pattern, mail):
            match = 'Valid Email'
        else:
            match = 'Invalid Email'

    return render_template('email_validator.html', match=match)



################################################

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0')