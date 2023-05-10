# OTP-Hydra

OTP-Hydra is a Python web application that provides two-factor authentication using TOTP (Time-based One-Time Password) codes. It generates QR codes for TOTP secrets, validates user-entered TOTP codes, and returns a result indicating whether the code is correct or incorrect. It uses Flask for the web framework, pyotp for TOTP generation, qrcode for QR code generation, and jQuery for client-side validation.

## Installation

To run OTP-Hydra, you need to have Python 3.x and pip installed on your system.

1. Clone the repository: `git clone https://github.com/jonmalki/OTP-Hydra/`
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the application: `python main.py`
4. Open your web browser and go to http://localhost:8080

Note: OTP-Hydra stores the TOTP secret keys in a dictionary in memory. If you need to store the secret keys securely, consider using a database or another secure storage solution.

## Usage

When you run the application, it will generate a TOTP secret key and a QR code that you can scan with your authenticator app (such as Google Authenticator or Authy). OTP-Hydra generates a separate TOTP secret key and QR code for each client IP address, so each client has a unique TOTP secret key.

To use OTP-Hydra:

1. Open your authenticator app and add a new account using the TOTP secret key displayed in OTP-Hydra.
2. Enter the TOTP code displayed in your authenticator app into OTP-Hydra.
3. Click the "Check" button to verify the code.
4. OTP-Hydra will display a message indicating whether the code is correct or incorrect.

Note: If you access OTP-Hydra from a different device or IP address, you will see a different TOTP secret key and QR code. You will need to add a new account in your authenticator app and use the new TOTP secret key to generate codes for OTP-Hydra.

## Contributing

Contributions to OTP-Hydra are always welcome! If you find a bug or have a feature request, please create an issue or submit a pull request. When submitting a pull request, please follow these guidelines:

- Fork the repository and create a new branch for your changes.
- Ensure that your code follows the PEP 8 style guide and includes docstrings and comments as needed.
- Write clear commit messages that describe the changes you made.
- Run the tests and ensure that they pass before submitting your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
