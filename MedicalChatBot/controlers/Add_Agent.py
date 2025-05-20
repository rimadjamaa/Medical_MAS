from flask import render_template, request, redirect, url_for, flash
from models.AgentsModel import Agent  
from extentions import db
import os
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

AGENTS_BASE_PATH = os.path.join(os.getcwd(), '../agents') 
GRAPH_FILE_PATH = os.path.join(os.getcwd(), '../graph.py') 

AddAgent = Blueprint('AddAgent', __name__)
@AddAgent.route('/add-agent', methods=['GET', 'POST'])
@login_required
def add_agent():
    if request.method == 'POST':
        name = request.form['agent_name']
        description = request.form['agent_discribe']
        main_code = request.form['main_py']
        status = request.form['status']
        created_by = current_user.username  

        # Check if agent with same name already exists
        if Agent.query.filter_by(name=name).first():
            flash('An agent with that name already exists.', 'danger')
            return render_template('admin_add_agent.html')

        # Create new agent instance
        new_agent = Agent(
            name=name,
            description=description,
            main_code=main_code,
            status=status,
            created_by=created_by
        )

        # Save to DB
        db.session.add(new_agent)
        db.session.commit()
        # Create directory for the new agent
        agent_folder = os.path.join(AGENTS_BASE_PATH, name.lower())
        os.makedirs(agent_folder, exist_ok=True)

        # Create main.py file with the submitted code
        main_py_path = os.path.join(agent_folder, 'main.py')
        with open(main_py_path, 'w', encoding='utf-8') as f:
            f.write(main_code)
        
        # Update graph.py dynamically
        update_graph_with_new_agent(name)

        flash('Agent added successfully!', 'success')
        return redirect(url_for('admin_add_agent'))  

    return render_template('admin_add_agent.html')


def update_graph_with_new_agent(agent_name):
    graph_file = GRAPH_FILE_PATH
    import_line = f"from agents.{agent_name.lower()}.main import {agent_name.lower()}\n"
    node_line = f'builder.add_node("{agent_name}", {agent_name.lower()})\n'
    conditional_entry_line = f'        "{agent_name}": "{agent_name}",\n'

    with open(graph_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Flags to know where to insert
    import_index = -1
    node_index = -1
    conditional_start = -1
    conditional_end = -1

    for idx, line in enumerate(lines):
        # Find the last import from agents...
        if line.startswith("from agents.") and "import" in line:
            import_index = idx
        # Find where to insert the new node
        if "Ajout des noeuds (agents)" in line:
            node_index = idx + 1  # insert right after the comment
        if 'builder.add_conditional_edges(' in line:
            conditional_start = idx
        if conditional_start != -1 and '}' in line and conditional_end == -1:
            conditional_end = idx

    # Check for duplicates before inserting
    if import_line not in lines:
        lines.insert(import_index + 1, import_line)

    if node_line not in lines:
        lines.insert(node_index + 1, node_line)

    # Add to conditional edges dictionary
    already_present = any(f'"{agent_name}": "{agent_name}"' in line for line in lines[conditional_start:conditional_end])
    if not already_present and conditional_start != -1 and conditional_end != -1:
        lines.insert(conditional_end, conditional_entry_line)

    # Save back to graph.py
    with open(graph_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)
