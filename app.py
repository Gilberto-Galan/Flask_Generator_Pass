from flask import Flask, render_template, request
import os
import random
import string

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'))

# Funcion para generar una contraseña
def generate_password(length=12, use_digits=True, use_special_chars=True):
    # Definir los caracteres que se utilizaran en la contraseña
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation
        
    # Genera la contraseña aleatoria
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Ruta principal
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para generar contraseña
@app.route('/generate', methods=['POST'])
def generate():
    # Obtener los datos del formulario
    length = int(request.form.get('length', 12))
    use_digits = 'digits' in request.form
    use_special_chars = 'special_chars' in request.form
    
    # Genera la contraseña
    password = generate_password(length, use_digits, use_special_chars)
    
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)