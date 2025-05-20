import uuid
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
from models.UserKGModel import UserKG
from extentions import db

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploaded_kgs')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

UploadKG = Blueprint('UploadKG', __name__)

@UploadKG.route('/upload-kg', methods=['GET', 'POST'])
@login_required
def upload_kg():
    if request.method == 'POST':
        description = request.form['kg_description']
        entity_types = request.form['entity_types']
        relation_types = request.form['relation_types']
        status = request.form['status']
        file = request.files['kg_file']

        if not file or not file.filename.endswith('.csv'):
            flash("Invalid file. Please upload a CSV file.", "danger")
            return redirect(request.url)
        

        filename = secure_filename(file.filename)
        unique_name = f"{uuid.uuid4().hex}_{filename}"
        file_path = os.path.join(UPLOAD_FOLDER, unique_name)
        file.save(file_path)

        # Save metadata to DB
        user_kg = UserKG(
            description=description,
            entity_types=entity_types,
            relation_types=relation_types,
            status=status,
            file_path=file_path,
            created_by=current_user.username
        )
        db.session.add(user_kg)
        db.session.commit()

        flash("Your knowledge graph has been uploaded successfully!", "success")
        return redirect(url_for('UploadKG.upload_kg'))

    return render_template('admin_update_KG.html')
