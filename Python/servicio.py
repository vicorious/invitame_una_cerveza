from flask                  import Flask,jsonify,json, request
from flask_api              import status
from facade_user            import UserFacade
from facade_bares           import BarFacade
from facade_cerveza         import BeerFacade
from facade_usuario_cerveza import UserBeerFacade
from proxy                  import ProxyConfiguration
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

@app.route('/bar/<_bar_id>/GET', methods=['GET'])
def barForId(_bar_id):
    try: 
        bar = BarFacade().bar_id(_bar_id)
        return jsonify(bar), status.HTTP_204_NO_CONTENT if bar is None else jsonify(bar)        
    except Exception as e:
        logging.debug("Error: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/bars', methods=['GET'])
def bars():
    try:
        bars = BarFacade().bars()
        return jsonify(bars) if len(bars) > 0 else jsonify(bars), status.HTTP_204_NO_CONTENT
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
        return jsonify(beer), status.HTTP_204_NO_CONTENT if beer is None else jsonify(beer)
    except Exception as e:
        logging.debug("Error: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/beers', methods=['GET'])
def beers():
    try:
        beers  = BeerFacade().beers()
        return jsonify(beers) if len(beers) > 0 else jsonify(beers), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Error: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/beer/INSERT', methods=['POST'])
def insertBeer():
    try:
        _json_beer = request.get_json()
        BeerFacade().insertBeer(_json_beer)
        return jsonify(OK)
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
        return jsonify(user_beer) if len(user_beer) > 0 else jsonify(user_beer), status.HTTP_204_NO_CONTENT            
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/userBeer/<_user_id>/<_beer_id>/GET', methods=['GET'])
def userBeerForVisit(_user_id, _beer_id):
    try:
        beers  = UserBeerFacade().userBeerForVisit(_user_id, _beer_id)
        return jsonify(beers) if len(beers) > 0 else jsonify(beers), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT    

@app.route('/userBeer/<_user_id>/<_beer_id>/<_pay_type_id>/GET', methods=['GET'])
def userBeerPayTypeForVisit(_user_id, _beer_id, _pay_type_id):
    try:
        beers  = UserBeerFacade().userBeerPayTypeForVisit(_user_id, _beer_id, _pay_type_id)
        return jsonify(beers) if len(beers) > 0 else jsonify(beers), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT   

@app.route('/userBeer/<_user_id>/<_pay_type_id>/GET', methods=['GET'])
def userPayTypeForVisit(_user_id, _pay_type_id):
    try:
        beers  = UserBeerFacade().userPayTypeForVisit(_user_id, _pay_type_id)
        return jsonify(beers) if len(beers) > 0 else jsonify(beers), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT    


@app.route('/userBeer/INSERT', methods=['POST'])
def insertUserForVisit():
    try:
        _json = request.get_json()
        UserBeerFacade().insert_usuario_cerveza(_json)
        return jsonify(OK)
    except Exception as e:
        logging.debug("Error no controlado: {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.before_request
def proxy():
    proxy = ProxyConfiguration()
    if not proxy.existDataBase():
        logging.debug("DataBase no exists!")
        proxy.createDatabase()
        proxy.createDDL()
    else:
        logging.debug("Database was already created!")

####### Main ############
if __name__ == '__main__':
    app.run()