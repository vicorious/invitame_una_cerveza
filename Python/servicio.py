from flask                  import Flask,jsonify,json, request
from flask_api              import status
from facade_user            import UserFacade
from facade_bares           import BarFacade
from facade_cerveza         import BeerFacade
from facade_usuario_cerveza import UserBeerFacade
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
        facade = UserFacade()
        logueo = facade.logueo(_json_login)
        if logueo > 0:
            return jsonify(OK)
        else:
            return jsonify(FAIL), status.HTTP_409_CONFLICT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/registrarse/INSERT', methods=['POST'])
def registrarse():
    try:
        _json_registro = request.get_json()
        facade   = UserFacade()
        registro = facade.registrarme(_json_registro)
        if(registro):
            return jsonify(OK)
        else:
            return jsonify(FAIL), status.HTTP_409_CONFLICT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/olvido_contrasena/UPDATE', methods=['PUT'])
def olvido_contrasena():
    try:
        _json_olvido = request.get_json()
        facade = UserFacade()
        olvido = facade.olvido_contrasena(_json_olvido)
        if(olvido):
            return jsonify(OK)
        else:
            return jsonify(FAIL), status.HTTP_409_CONFLICT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

################## Bares #################################

@app.route('/bares/<bar_id>/GET', methods=['GET'])
def bares_id(bar_id):
    try:        
        facade = BarFacade()
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
        facade = BarFacade()
        bares  = facade.bares()
        if len(bares) > 0:
            return jsonify(bares)
        else:
            return jsonify(bares), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/bares/INSERT', methods=['POST'])
def bares_insert():
    try:
        _json_bar = request.get_json()
        facade   = BarFacade()
        registro = facade.insertar_bar(_json_bar)
        if(registro):
            return jsonify(OK)
        else:
            return jsonify(FAIL), status.HTTP_409_CONFLICT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/bares/UPDATE', methods=['PUT'])
def bares_update():
    try:
        _json_bar = request.get_json()
        facade   = BarFacade()
        registro = facade.insertar_bar(_json_bar)
        if(registro):
            return jsonify(OK)
        else:
            return jsonify(FAIL), status.HTTP_409_CONFLICT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

##################### Cerveza #############################################

@app.route('/cervezas/<_cerveza_id>/GET', methods=['GET'])
def cerveza_id(_cerveza_id):
    try:        
        facade = BeerFacade()
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
        facade = BeerFacade()
        cervezas  = facade.cervezas()
        if len(cervezas) > 0:
            return jsonify(cervezas)
        else:
            return jsonify(cervezas), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/cerveza/INSERT', methods=['POST'])
def cerveza_insert():
    try:
        _json_cerveza = request.get_json()
        facade   = BeerFacade()
        registro = facade.insert_cerveza(_json_cerveza)
        if(registro):
            return jsonify(OK)
        else:
            return jsonify(FAIL), status.HTTP_409_CONFLICT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

#################### Usuario cerveza ###########################

@app.route('/usuario_visitas/<_usuario_id>/GET', methods=['GET'])
def usuario_visitas(_usuario_id):
    try:
        facade = UserBeerFacade()
        cervezas  = facade.usuario_visitas(_usuario_id)
        if len(cervezas) > 0:
            return jsonify(cervezas)
        else:
            return jsonify(cervezas), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/usuario_visitas/<_usuario_id>/GET/<_cerveza_id>/GET', methods=['GET'])
def usuario_visitas_cerveza(_usuario_id, _cerveza_id):
    try:
        facade = UserBeerFacade()
        cervezas  = facade.usuario_cerveza_visita(_usuario_id, _cerveza_id)
        if len(cervezas) > 0:
            return jsonify(cervezas)
        else:
            return jsonify(cervezas), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT    

@app.route('/usuario_visitas/<_usuario_id>/GET/<_cerveza_id>/GET/<_tipo_pago_id>/GET', methods=['GET'])
def usuario_visitas_cerveza_tipo(_usuario_id, _cerveza_id, _tipo_pago_id):
    try:
        facade = UserBeerFacade()
        cervezas  = facade.usuario_cerveza_tipo_pago_visita(_usuario_id, _cerveza_id, _tipo_pago_id)
        if len(cervezas) > 0:
            return jsonify(cervezas)
        else:
            return jsonify(cervezas), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT   

@app.route('/usuario_visitas/<_usuario_id>/GET/<_tipo_pago_id>/GET', methods=['GET'])
def usuario_tipo_pago(_usuario_id, _tipo_pago_id):
    try:
        facade = UserBeerFacade()
        cervezas  = facade.usuario_tipo_pago(_usuario_id, _tipo_pago_id)
        if len(cervezas) > 0:
            return jsonify(cervezas)
        else:
            return jsonify(cervezas), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT    


@app.route('/usuario_visitas/INSERT', methods=['POST'])
def cerveza_usuario_insert():
    try:
        _json_cerveza = request.get_json()
        facade   = UserBeerFacade()
        registro = facade.insert_usuario_cerveza(_json_cerveza)
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