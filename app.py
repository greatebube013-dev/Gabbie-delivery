from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)

# Home page - shows your website
@app.route("/")
def home():
    return render_template("index.html")

# This handles the form when someone clicks "Send Order"
@app.route("/send-message", methods=["POST"])
def send_message():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    
    # Get current time
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Save order to a text file
    with open("messages.txt", "a", encoding="utf-8") as f:
        f.write(f"--- NEW ORDER ---\n")
        f.write(f"Time: {now}\n")
        f.write(f"Name: {name}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Order: {message}\n")
        f.write(f"-----------------\n\n")
    
    # After saving, go back to homepage
    return "<h2>Order Received! 🚚</h2><p>Thank you " + name + ". We will contact you soon.</p><a href='/'>Back to Home</a>"

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)