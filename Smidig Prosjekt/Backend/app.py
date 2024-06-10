from flask import Flask, render_template, jsonify, request


#import mysql.connector
'''
# Database connection
mydb = mysql.connector.connect(
  host="localhost",
  user="smidig",
  password="password",
  database="smidigDB"
)

# Sjekker om databasen er connected til backenden. 
if mydb.is_connected():
    print("Connected to the database")
else:
    print("Failed to connect to the database")

print(mydb)
'''


# Flask (frontend connection)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#Alert med text fra backend
@app.route('/get-message')
def get_message():
    return jsonify(message="Hello World")

# Henter input fra frontend og sender til alert fra backend
@app.route('/get-input', methods=['POST'])
def get_input():
    data = request.get_json()
    userInput = data.get('userInput', '')
    valgSpm = data.get('valgSpm', '')
    valg1 = data.get('valg1', '')
    valg2 = data.get('valg2', '')
    valg3 = data.get('valg3', '')
    valg4 = data.get('valg4', '')
    kjSpm = data.get('kjSpm', False)

    return jsonify(message=f"You entered: {userInput}, {valgSpm}, {valg1}, {valg2}, {valg3}, {valg4}, {kjSpm}")
    
if __name__ == '__main__':
    app.run(debug=True)
