from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import pyotp
import qrcode
import random
import string
from io import BytesIO

app = Flask(__name__)

# A dictionary to store the TOTP secret keys for different IP addresses
totp_secrets = {}

@app.route('/')
def index():
    # Get the client's IP address
    client_ip = request.remote_addr
    
    # If the client's IP is not in the dictionary, generate a new TOTP secret key for it
    if client_ip not in totp_secrets:
        totp_secrets[client_ip] = pyotp.random_base32()

    # Create a TOTP object using the secret key for the client's IP
    totp = pyotp.TOTP(totp_secrets[client_ip])

    # Generate a random file name for the QR code for the client's IP
    file_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + '.png'

    # Encode the TOTP URI into a QR code
    totp_uri = totp.provisioning_uri(name="Python QR code example", issuer_name="MyApp")
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(totp_uri)
    qr.make(fit=True)

    # Save the QR code as a PNG image with a random file name for the client's IP
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(os.path.join("img", file_name))

    return render_template('index.html', secret_key=totp_secrets[client_ip], qr_code_file=file_name)


@app.route('/verify', methods=['POST'])
def verify():
    # Get the client's IP address
    client_ip = request.remote_addr
    
    # Create a TOTP object using the secret key for the client's IP
    totp = pyotp.TOTP(totp_secrets[client_ip])

    entered_token = request.form['totpToken']
    current_token = totp.now()

    if entered_token == current_token:
        return jsonify({'result': 'Correct!'})
    else:
        return jsonify({'result': 'Incorrect!'})


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
