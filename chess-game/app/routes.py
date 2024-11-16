# app/routes.py
from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "Healthy"}), 200
