from flask import Flask, jsonify, request, abort
from models import setup_db, Togo, Went
from auth import requires_auth

app = Flask(__name__)
setup_db(app)


@app.route('/', methods=['GET'])
def test():
    return "works"


@app.route('/togo', methods=['GET'])
@requires_auth('get:location')
def all(jwt):
    togos = Togo.query.all()
    formatted_togo = [togo.format() for togo in togos]
    print(formatted_togo)
    return jsonify({'togos': formatted_togo})


@app.route('/togo', methods=['POST'])
@requires_auth('post:location')
def add_togo(jwt):
    try:
        Togo(location=request.get_json()['location'],
             date=request.get_json()['date'],
             description=request.get_json()['description']).insert()
        return jsonify({'done': 'yes'}), 201
    except Exception:
        return jsonify({'done': 'no'}), 500


@app.route('/togo/<id>', methods=['PATCH'])
@requires_auth('patch:location')
def edit_togp(jwt, id):
    try:
        togo = Togo.query.get(id)
        if not togo:
            return abort(404)
        if 'location' in request.get_json():
            togo.location = request.get_json()['location']

        if 'date' in request.get_json():
            togo.date = request.get_json()['date']

        if 'description' in request.get_json():
            togo.description = request.get_json()['description']

        togo.update()
        print(togo)
        return jsonify({'done': 'yes'}), 200
    except Exception:
        return jsonify({'done': 'no'}), 500


@app.route('/togo/<id>', methods=['DELETE'])
@requires_auth('delete:location')
def delete_togo(jwt, id):
    try:
        togo = togo = Togo.query.get(id)
        if not togo:
            return jsonify({'done': 'no'}), 404
        togo.delete()
        return jsonify({'done': 'yes'}), 200
    except Exception:
        return jsonify({'done': 'no'}), 500


@app.route('/went', methods=['GET'])
@requires_auth('get:went')
def went(jwt):
    wents = Went.query.all()
    formatted_went = [went.format() for went in wents]
    print(formatted_went)
    return jsonify({'went': formatted_went})


@app.route('/went', methods=['POST'])
@requires_auth('post:went')
def add_went(jwt):
    try:
        Went(location=request.get_json()['location'],
             description=request.get_json()['description']).insert()
        return jsonify({'done': 'yes'}), 201
    except Exception:
        return jsonify({'done': 'no'}), 500

    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({'error': 'api not found'}), 404

    @app.errorhandler(422)
    def server_error(error):
        return jsonify({'error': 'you reach Unprocessable api'}), 422

    @app.errorhandler(401)
    def not_found_error(error):
        return jsonify({'error': 'unauthorized access'}), 401

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({'error': 'server error'}), 500
