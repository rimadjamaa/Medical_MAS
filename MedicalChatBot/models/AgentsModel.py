from extentions import db
from datetime import datetime

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)  
    description = db.Column(db.Text) 
    main_code = db.Column(db.Text, nullable=False)  
    created_by = db.Column(db.String(100))  
    status = db.Column(db.String(20), default='inactive') 
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    