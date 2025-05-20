# models/UserKGModel.py
from extentions import db 


class UserKG(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    file_path = db.Column(db.String(255))
    entity_types = db.Column(db.String(255))
    relation_types = db.Column(db.String(255))
    status = db.Column(db.String(50))
    created_by = db.Column(db.String(50))  # username of uploader
