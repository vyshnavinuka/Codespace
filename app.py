from flask import Flask
import subprocess
import os
import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Full Name
    full_name = "Your Full Name"  # Replace with your actual full name
    
    # System Username
    username = os.getenv("USER", os.getenv("USERNAME", "Unknown"))
    
    # Server Time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')

    # Run 'top' command and capture output
    top_output = subprocess.getoutput("top -b -n 1")

    # Generate HTML response
    html_response = f"""
    <html>
    <head>
        <title>HTOP Output</title>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f5f5f5; padding: 20px; }}
            pre {{ background-color: #fff; padding: 15px; border: 1px solid #ddd; border-radius: 5px; overflow-x: auto; }}
            h1, h2 {{ color: #333; }}
        </style>
    </head>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> {full_name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <h2>Top Output</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    
    return html_response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
