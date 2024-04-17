from flask import Blueprint,,request,jsonify
from flask_jwt_extended import  jwt_required, get_jwt_identity,create_access_token,create_refresh_token
from app.models import User

auth_bp = Blueprint('auth',__name__,url_prefix='/auth')
@auth_bp.post('/register')
def register():
    data = request.json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"message":'username or password is not found'}),402
    if User.query.filter_by(username=username).first():
        return jsonify({"message":"username alread exists"}), 400
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201
@auth_bp.post('/login')
def login():
    data = request.json()
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid username or password'}), 401
    #above user don't exist
    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200

@auth_bp.get('/protected')
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    return jsonify({'message': f'Protected endpoint accessed by user {current_user_id}'}), 200
