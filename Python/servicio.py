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

###### Constant ##########
OK   = 'OK'
FAIL = 'FAIL'

###### Log #################

logging.basicConfig(filename="test.log", level=logging.DEBUG)

#################### USER #############################
@app.route('/user/login', methods=['POST'])
def login():    
    try:
        _json_login = request.get_json()
        UserFacade().login(_json_login)
        return jsonify(OK)
    except Exception as e:
        logging.debug("Error: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/user/register/INSERT', methods=['POST'])
def register():
    try:
        _json_registro = request.get_json()
        UserFacade().register(_json_registro)
        return jsonify(OK)                    
    except Exception as e:
        logging.debug("Error: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/user/password/UPDATE', methods=['PUT'])
def forgotPassword():
    try:
        _json_olvido = request.get_json()
        UserFacade().forgotPassword(_json_olvido)
        return jsonify(OK)                    
    except Exception as e:
        logging.debug("Error: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

################## BAR´S #################################

@app.route('/bar/<bar_id>/GET', methods=['GET'])
def barForId(bar_id):
    try: 
        bar = BarFacade().bar_id(bar_id)
		bar is None ? return jsonify(bar), status.HTTP_204_NO_CONTENT : return jsonify(bar)
    except Exception as e:
        logging.debug("Error: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/bars', methods=['GET'])
def bars():
    try:
        bars = BarFacade().bars()
        len(bars) > 0 ? return jsonify(bars) : return jsonify(bars), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Error: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/bar/INSERT', methods=['POST'])
def insertBar():
    try:
        _json_bar = request.get_json()
        BarFacade().insertBar(_json_bar)
        return jsonify(OK)
    except Exception as e:
        logging.debug("Error: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/bar/UPDATE', methods=['PUT'])
def updateBar():
    try:
        _json_bar = request.get_json()
        BarFacade().updateBar(_json_bar)
        return jsonify(OK)
    except Exception as e:
        logging.debug("Error: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

##################### Cerveza #############################################

@app.route('/beer/<_beer_id>/GET', methods=['GET'])
def beerId(_beer_id):
    try:
        beer = BeerFacade().beerId(_beer_id)
        beer is None ? return jsonify(beer), status.HTTP_204_NO_CONTENT : return jsonify(beer)
    except Exception as e:
        logging.debug("Error: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/beers', methods=['GET'])
def beers():
    try:
        beers  = BeerFacade().beers()
        len(beers) > 0 ? return jsonify(beers) : return jsonify(beers), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Error: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/beer/INSERT', methods=['POST'])
def insertBeer():
    try:
        _json_beer = request.get_json()
        BeerFacade().insertBeer(_json_beer) ? return jsonify(OK) : return jsonify(FAIL), status.HTTP_409_CONFLICT
    except Exception as e:
        logging.debug("Error: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT
	
@app.route('/beer/UPDATE', methods=['PUT'])
def updateBeer():
    try:
        _json_beer = request.get_json()
        BeerFacade().updateBeer(_json_beer)
        return jsonify(OK)
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

#################### Usuario cerveza ###########################

@app.route('/userBeer/<_user_id>/GET', methods=['GET'])
def userForVisit(_user_id):
    try:
        user_beer = UserBeerFacade().userForVisit(_user_id)
        len(user_beer) > 0 ? return jsonify(user_beer) : return jsonify(user_beer), status.HTTP_204_NO_CONTENT            
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/userBeer/<_user_id>/GET/<_beer_id>/GET', methods=['GET'])
def userBeerForVisit(_user_id, _beer_id):
    try:
        cervezas  = UserBeerFacade().userBeerForVisit(_user_id, _beer_id)
        len(cervezas) > 0 ? return jsonify(cervezas) : return jsonify(cervezas), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT    

@app.route('/userBeer/<_user_id>/GET/<_beer_id>/GET/<_pay_type_id>/GET', methods=['GET'])
def userBeerPayTypeForVisit(_user_id, _beer_id, _pay_type_id):
    try:
        cervezas  = UserBeerFacade().userBeerPayTypeForVisit(_usuario_id, _cerveza_id, _tipo_pago_id)
        if len(cervezas) > 0 ? return jsonify(cervezas) : return jsonify(cervezas), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT   

@app.route('/userBeer/<_user_id>/GET/<_pay_type_id>/GET', methods=['GET'])
def userPayTypeForVisit(_user_id, _pay_type_id):
    try:
        cervezas  = UserBeerFacade().userPayTypeForVisit(_usuario_id, _tipo_pago_id)
        len(cervezas) > 0 ? return jsonify(cervezas) : return jsonify(cervezas), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT    


@app.route('/userBeer/INSERT', methods=['POST'])
def insertUserForVisit():
    try:
        _json_cerveza = request.get_json()
		UserBeerFacade().insert_usuario_cerveza(_json_cerveza)
        return jsonify(OK)
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


####### Main ############
if __name__ == '__main__':
    app.run()