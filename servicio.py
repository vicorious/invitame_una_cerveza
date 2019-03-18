from flask               import Flask,jsonify,json, request
from flask_api           import status
from facade_user         import ClienteFacade
from facade_bares        import BaresFacade
from facade_cerveza      import CervezaFacade
import sys
import logging

###### Flask Object ######################################
app = Flask(__name__)

###### Constantes ##########
OK   = 'OK'
FAIL = 'FAIL'

###### Log #################

logging.basicConfig(filename="test.log", level=logging.DEBUG)

#################### Usuario #############################
@app.route('/login', methods=['POST'])
def login():    
    try:
        _json_login = request.get_json()        
        facade = ClienteFacade()
        logueo = facade.logueo(_json_login)
        if logueo > 0:
            return jsonify(OK)
        else:
            return jsonify(FAIL), status.HTTP_409_CONFLICT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/registrarse', methods=['POST'])
def registrarse():
    try:
        _json_registro = request.get_json()
        facade   = ClienteFacade()
        registro = facade.registrarme(_json_registro)
        if(registro):
            return jsonify(OK)
        else:
            return jsonify(FAIL), status.HTTP_409_CONFLICT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/olvido_contrasena', methods=['PUT'])
def olvido_contrasena():
    try:
        _json_olvido = request.get_json()
        facade = ClienteFacade()
        olvido = facade.olvido_contrasena(_json_olvido)
        if(olvido):
            return jsonify(OK)
        else:
            return jsonify(FAIL), status.HTTP_409_CONFLICT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

################## Bares #################################

@app.route('/bares/<bar_id>', methods=['GET'])
def bares_id(bar_id):
    try:        
        facade = BaresFacade()
        bar = facade.bares_id(bar_id)
        if bar is not None:
            return jsonify(bar)
        else:
            return jsonify(bar), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/bares', methods=['GET'])
def bares():
    try:
        facade = BaresFacade()
        bares  = facade.bares()
        if len(bares) > 0:
            return jsonify(bares)
        else:
            return jsonify(bares), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/bares', methods=['POST'])
def bares_insert():
    try:
        _json_bar = request.get_json()
        facade   = BaresFacade()
        registro = facade.insertar_bar(_json_bar)
        if(registro):
            return jsonify(OK)
        else:
            return jsonify(FAIL), status.HTTP_409_CONFLICT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

##################### Cerveza #############################################

@app.route('/cervezas/<_cerveza_id>', methods=['GET'])
def cerveza_id(_cerveza_id):
    try:        
        facade = CervezaFacade()
        cerveza = facade.cerveza_id(_cerveza_id)
        if cerveza  is not None:
            return jsonify(cerveza)
        else:
            return jsonify(cerveza), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/cervezas', methods=['GET'])
def cervezas():
    try:
        facade = CervezaFacade()
        cervezas  = facade.cervezas()
        if len(cervezas) > 0:
            return jsonify(cervezas)
        else:
            return jsonify(cervezas), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/bares', methods=['POST'])
def cerveza_insert():
    try:
        _json_cerveza = request.get_json()
        facade   = CervezaFacade()
        registro = facade.insert_cerveza(_json_cerveza)
        if(registro):
            return jsonify(OK)
        else:
            return jsonify(FAIL), status.HTTP_409_CONFLICT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

####### Main ############
if __name__ == '__main__':
    app.run()
