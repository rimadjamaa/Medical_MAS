from flask import Flask, render_template,request , jsonify
from services.chat_service import test_agent_response, test_graph


app = Flask(__name__)
app.secret_key = "74938f8ec2054cd9e2b9df012af5455a"


@app.route('/')
def chatbot():
    return render_template('chatbot.html')

@app.route("/chat", methods=["POST"])
def chat_api():
    try:
        data = request.get_json()
        print("Received JSON:", data)  # Log the incoming data

        user_message = data.get("message")
        print("User message:", user_message)

        # Just to test basic flow first:
        response = test_graph(user_message)

        #use jsonify to convert data sended into vectors.. (which be accpeted by http)
        return jsonify({"response": response})

    except Exception as e:
        print("❌ ERROR in /chat route:", e)
        return jsonify({"response": "Internal server error"}), 500
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    