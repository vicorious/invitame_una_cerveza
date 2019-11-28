from flask                  import Flask,jsonify,json, request
from flask_api              import status
from facade_user            import UserFacade
from facade_bares           import BarFacade
from facade_cerveza         import BeerFacade
from facade_usuario_cerveza import UserBeerFacade
from facade_promotion       import PromotionFacade
from proxy                  import ProxyConfiguration
import sys
import logging
from json_encoder import AlchemyEncoder

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
        logging.debug("Unexpected Error {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/user/register/INSERT', methods=['POST'])
def register():
    try:
        _json_registro = request.get_json()
        UserFacade().register(_json_registro)
        return jsonify(OK)                    
    except Exception as e:
        logging.debug("Unexpected Error {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/user/password/UPDATE', methods=['PUT'])
def forgotPassword():
    try:
        _json_olvido = request.get_json()
        UserFacade().forgotPassword(_json_olvido)
        return jsonify(OK)                    
    except Exception as e:
        logging.debug("Unexpected Error {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

################## BAR´S #################################

@app.route('/bar/<_bar_id>/GET', methods=['GET'])
def barForId(_bar_id):
    try: 
        bar = BarFacade().bar_id(_bar_id)
        if bar is None:
            return jsonify(bar), status.HTTP_204_NO_CONTENT  
        else:
            return jsonify(json.dumps(bar, cls=AlchemyEncoder))        
    except Exception as e:
        logging.debug("Unexpected Error {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/bars', methods=['GET'])
def bars():
    try:
        bars = BarFacade().bars()
        if len(bars) > 0: 
            return jsonify(json.dumps(bars, cls=AlchemyEncoder))
        elif len(bars) == 0: 
            return jsonify(bars), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Unexpected Error {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/bar/INSERT', methods=['POST'])
def insertBar():
    try:
        _json_bar = request.get_json()
        BarFacade().insertBar(_json_bar)
        return jsonify(OK)
    except Exception as e:
        logging.debug("Unexpected Error {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/bar/UPDATE', methods=['PUT'])
def updateBar():
    try:
        _json_bar = request.get_json()
        BarFacade().updateBar(_json_bar)
        return jsonify(OK)
    except Exception as e:
        logging.debug("Unexpected Error {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

##################### Cerveza #############################################

@app.route('/beer/<_beer_id>/GET', methods=['GET'])
def beerId(_beer_id):
    try:
        beer = BeerFacade().beerId(_beer_id)
        if beer is None:
            return jsonify(beer), status.HTTP_204_NO_CONTENT  
        else: 
            return jsonify(json.dumps(beer, cls=AlchemyEncoder))
    except Exception as e:
        logging.debug("Unexpected Error {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/beers', methods=['GET'])
def beers():
    try:
        beers  = BeerFacade().beers()
        if len(beers) > 0:
            return jsonify(json.dumps(beers, cls=AlchemyEncoder))
        elif len(beers) == 0: 
            return jsonify(beers), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Unexpected Error {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/beer/INSERT', methods=['POST'])
def insertBeer():
    try:
        _json_beer = request.get_json()
        BeerFacade().insertBeer(_json_beer)
        return jsonify(OK)
    except Exception as e:
        logging.debug("Unexpected Error {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT
    
@app.route('/beer/UPDATE', methods=['PUT'])
def updateBeer():
    try:
        _json_beer = request.get_json()
        BeerFacade().updateBeer(_json_beer)
        return jsonify(OK)
    except Exception as e:
        logging.debug("Unexpected Error {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

#################### Usuario cerveza ###########################

@app.route('/userBeer/<_user_id>/GET', methods=['GET'])
def userForVisit(_user_id):
    try:
        user_beer = UserBeerFacade().userForVisit(_user_id)
        if len(user_beer) > 0:
            return jsonify(json.dumps(user_beer, cls=AlchemyEncoder))
        elif len(user_beer) == 0: 
            return jsonify(user_beer), status.HTTP_204_NO_CONTENT            
    except Exception as e:
        logging.debug("Unexpected Error {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/userBeer/<_user_id>/<_beer_id>/GET', methods=['GET'])
def userBeerForVisit(_user_id, _beer_id):
    try:
        beers  = UserBeerFacade().userBeerForVisit(_user_id, _beer_id)
        if len(beers) > 0:
            return jsonify(json.dumps(beers, cls=AlchemyEncoder)) 
        elif len(beers) == 0: 
            return jsonify(beers), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Unexpected Error {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT    

@app.route('/userBeer/<_user_id>/<_beer_id>/<_pay_type_id>/GET', methods=['GET'])
def userBeerPayTypeForVisit(_user_id, _beer_id, _pay_type_id):
    try:
        beers  = UserBeerFacade().userBeerPayTypeForVisit(_user_id, _beer_id, _pay_type_id)
        if len(beers) > 0:
            return jsonify(json.dumps(beers, cls=AlchemyEncoder)) 
        elif len(beers) == 0:
            return jsonify(beers), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Unexpected Error {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT   

@app.route('/userBeer/<_user_id>/<_pay_type_id>/GET', methods=['GET'])
def userPayTypeForVisit(_user_id, _pay_type_id):
    try:
        beers  = UserBeerFacade().userPayTypeForVisit(_user_id, _pay_type_id)
        if len(beers) > 0:
            return jsonify(json.dumps(beers, cls=AlchemyEncoder)) 
        elif len(beers) == 0:
            return jsonify(beers), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Unexpected Error {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT    


@app.route('/userBeer/INSERT', methods=['POST'])
def insertUserForVisit():
    try:
        _json = request.get_json()
        UserBeerFacade().insert_usuario_cerveza(_json)
        return jsonify(OK)
    except Exception as e:
        logging.debug("Unexpected Error {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT
	
############ Promotion ################################################

@app.route('/promotion', methods=['GET'])
def promotions():
    try:
        promotions  = PromotionFacade().promotions()
        if len(promotions) > 0:
            return jsonify(json.dumps(promotions, cls=AlchemyEncoder)) 
        elif len(promotions) == 0: 
            return jsonify(promotions), status.HTTP_204_NO_CONTENT
    except Exception as e:
        logging.debug("Unexpected Error {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/promotion/INSERT', methods=['POST'])
def insertPromotion():
    try:
        _json_promotion = request.get_json()
        PromotionFacade().insertPromotion(_json_promotion)
        return jsonify(OK)
    except Exception as e:
        logging.debug("Unexpected Error {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT
    
@app.route('/promotion/UPDATE', methods=['PUT'])
def updatePromotion():
    try:
        _json_promotion = request.get_json()
        PromotionFacade().updatePromotion(_json_promotion)
        return jsonify(OK)
    except Exception as e:
        logging.debug("Unexpected Error {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT
    
@app.route('/climate/weather', methods=['PUT'])
def weather():
    try:
        _json_promotion = request.get_json()
        PromotionFacade().updatePromotion(_json_promotion)
        return jsonify(OK)
    except Exception as e:
        logging.debug("Unexpected Error {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT


#@app.before_request

######################### Configuration #################################################

@app.route('/configuration', methods=['GET'])
def configuration():
    try:
        proxy = ProxyConfiguration()
        proxy.installPostgre()
        return jsonify(OK)
    except Exception as e:
        logging.debug("Unexpected Error {}".format(e))
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/create_data_base', methods=['GET'])
def createDataBase():
    try:
        proxy = ProxyConfiguration()
        if not proxy.existDataBase():
            logging.debug("DataBase no exists!")
            proxy.createDatabase()
            proxy.createDDL()
        else:
            logging.debug("Database was already created!")
        return jsonify(OK)
    except:
        return jsonify(FAIL), status.HTTP_409_CONFLICT
    return jsonify(FAIL), status.HTTP_409_CONFLICT
    
@app.route('/create_database_dml', methods=['GET'])
def createDML():
    try:
        proxy = ProxyConfiguration()
        if proxy.existDataBase():
            logging.debug("Begin insert DML!")
            proxy.createDML()
        else:
            logging.debug("Database no exists. we going to create it!")
            proxy.createDatabase()
            proxy.createDDL()
            proxy.createDML()
        return jsonify(OK)
    except:        
        return jsonify(FAIL), status.HTTP_409_CONFLICT
    return jsonify(FAIL), status.HTTP_409_CONFLICT        
####### Main ############
if __name__ == '__main__':
    app.run()