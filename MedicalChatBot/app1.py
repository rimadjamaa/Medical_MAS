from flask import Flask, render_template, redirect, url_for ,request , jsonify
from extentions import db
from services.chat_service import get_chat_response
from controlers.Registration import register
from controlers.Add_Agent import AddAgent
from controlers.Login import login_bp
from controlers.User_KG import UploadKG
from flask_login import LoginManager, login_required, logout_user, current_user
from models.UserModel import User 
from flask_bcrypt import Bcrypt
from flask import session


app = Flask(__name__)
app.secret_key = "74938f8ec2054cd9e2b9df012af5455a"

# Database config
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:mimirima123@localhost/MedicalChatbot"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login.login_rout'
bcrypt = Bcrypt()


app.register_blueprint(login_bp, url_prefix='/auth')
app.register_blueprint(register, url_prefix='/auth')
app.register_blueprint(AddAgent, url_prefix='/admin')
app.register_blueprint(UploadKG, url_prefix='/admin')


@login_manager.user_loader
def load_user(user_id):
    try:
        print("🔄 Loading user ID:", user_id)
        import sys; sys.stdout.flush()

        # Optional: verify db.session is ready
        if not hasattr(db, 'session'):
            print("⚠️ DB session is not ready")
            return None

        user = db.session.get(User, int(user_id))
        print("✅ User loaded:", user)
        return user
    except Exception as e:
        print("❌ Error in load_user:", e)
        import sys; sys.stdout.flush()
        return None


@app.route('/')
@login_required
def chatbot():
    return render_template('chatbot.html')


@app.route("/chat", methods=["POST"])
@login_required
def chat_api():
    try:
        data = request.get_json()
        print("Received JSON:", data)  # Log the incoming data

        user_message = data.get("message")
        print("User message:", user_message)

        # Just to test basic flow first:
        response = get_chat_response(user_message)

        #use jsonify to convert data sended into vectors.. (which be accpeted by http)
        return jsonify({"response": response})

    except Exception as e:
        print("❌ ERROR in /chat route:", e)
        return jsonify({"response": "Internal server error"}), 500
    
@app.route('/add_agent')
@login_required
def admin_add_agent():
    return render_template('admin_add_agent.html')

@app.route('/update_KG')
@login_required
def update_kg():
    return render_template('admin_update_KG.html')

@app.route('/logout')
def logout():
    logout_user()
    session.clear() 
    return redirect(url_for('login.login_rout'))

@app.route('/admin')
@login_required
def admin_dashboard():
    return render_template('admin_dashboard.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    

    

