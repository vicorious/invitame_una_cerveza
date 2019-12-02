"""
Service http module
"""
import logging
from flask import Flask, jsonify, json, request
from flask_api import status
from proxy import ProxyConfiguration
from json_encoder import AlchemyEncoder
from facade_user import UserFacade
from facade_bares import BarFacade
from facade_cerveza import BeerFacade
from facade_usuario_cerveza import UserBeerFacade
from facade_promotion import PromotionFacade
from facade_climate import Climate

###### Flask Object ######################################
app = Flask(__name__)

###### Constant ##########
OK = 'OK'
FAIL = 'FAIL'
###### Log #################

logging.basicConfig(filename="test.log", level=logging.DEBUG)
#################### USER #############################
@app.route('/user/login', methods=['POST'])
def login():
    """
    Login method
    """
    try:
        _json_login = request.get_json()
        UserFacade().login(_json_login)
        return jsonify(OK)
    except Exception as exception:
        logging.debug("Unexpected Error %s", exception)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/user/register/INSERT', methods=['POST'])
def register():
    """
    Register method
    """
    try:
        _json_registro = request.get_json()
        UserFacade().register(_json_registro)
        return jsonify(OK)
    except Exception as exception:
        logging.debug("Unexpected Error %s", exception)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/user/password/UPDATE', methods=['PUT'])
def forgot_password():
    """
    Forgot method
    """
    try:
        _json_olvido = request.get_json()
        UserFacade().forgot_password(_json_olvido)
        return jsonify(OK)
    except Exception as exception:
        logging.debug("Unexpected Error %s", exception)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

################## BAR´S #################################

@app.route('/bar/<_bar_id>/GET', methods=['GET'])
def bar_for_id(_bar_id):
    """
    Bar for id method
    """
    try:
        bar = BarFacade().bar_id(_bar_id)
        if bar is None:
            return jsonify(bar), status.HTTP_204_NO_CONTENT
        
        return jsonify(json.dumps(bar, cls=AlchemyEncoder))
    except Exception as exception:
        logging.debug("Unexpected Error %s", exception)
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/bars', methods=['GET'])
def bars():
    """
    Get bars method
    """
    try:
        bars = BarFacade().bars()
        if len(bars) > 0:
            return jsonify(json.dumps(bars, cls=AlchemyEncoder))
        elif len(bars) == 0:
            return jsonify(bars), status.HTTP_204_NO_CONTENT
    except Exception as exception:
        logging.debug("Unexpected Error %s", exception)
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/bar/INSERT', methods=['POST'])
def insert_bar():
    """
    Insert bar method
    """
    try:
        _json_bar = request.get_json()
        BarFacade().insert_bar(_json_bar)
        return jsonify(OK)
    except Exception as exception:
        logging.debug("Unexpected Error %s", exception)
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/bar/UPDATE', methods=['PUT'])
def update_bar():
    """
    Update bar method
    """
    try:
        _json_bar = request.get_json()
        BarFacade().update_bar(_json_bar)
        return jsonify(OK)
    except Exception as exception:
        logging.debug("Unexpected Error %s", exception)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

##################### Cerveza #############################################

@app.route('/beer/<_beer_id>/GET', methods=['GET'])
def beer_id(_beer_id):
    """
    Beer for id method
    """
    try:
        beer = BeerFacade().beer_id(_beer_id)
        if beer is None:
            return jsonify(beer), status.HTTP_204_NO_CONTENT
        return jsonify(json.dumps(beer, cls=AlchemyEncoder))
    except Exception as exception:
        logging.debug("Unexpected Error %s", exception)
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/beers', methods=['GET'])
def beers():
    """
    get Beers method
    """
    try:
        beers = BeerFacade().beers()
        if len(beers) > 0:
            return jsonify(json.dumps(beers, cls=AlchemyEncoder))
        return jsonify(beers), status.HTTP_204_NO_CONTENT
    except Exception as exception:
        logging.debug("Unexpected Error %s", exception)
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/beer/INSERT', methods=['POST'])
def insert_beer():
    """
    Insert beer method
    """
    try:
        _json_beer = request.get_json()
        BeerFacade().insert_beer(_json_beer)
        return jsonify(OK)
    except Exception as exception:
        logging.debug("Unexpected Error %s", exception)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/beer/UPDATE', methods=['PUT'])
def update_beer():
    """
    Update beer method
    """
    try:
        _json_beer = request.get_json()
        BeerFacade().update_beer(_json_beer)
        return jsonify(OK)
    except Exception as exception:
        logging.debug("Unexpected Error %s", exception)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

#################### Usuario cerveza ###########################

@app.route('/userBeer/<_user_id>/GET', methods=['GET'])
def user_for_visit(_user_id):
    """
    User for visit method
    """
    try:
        user_beer = UserBeerFacade().user_for_visit(_user_id)
        if len(user_beer) > 0:
            return jsonify(json.dumps(user_beer, cls=AlchemyEncoder))
        return jsonify(user_beer), status.HTTP_204_NO_CONTENT
    except Exception as exception:
        logging.debug("Unexpected Error %s", exception)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/userBeer/<_user_id>/<_beer_id>/GET', methods=['GET'])
def user_beer_for_visit(_user_id, _beer_id):
    """
    User beer method
    """
    try:
        beers = UserBeerFacade().user_beer_for_visit(_user_id, _beer_id)
        if len(beers) > 0:
            return jsonify(json.dumps(beers, cls=AlchemyEncoder))
        return jsonify(beers), status.HTTP_204_NO_CONTENT
    except Exception as exception:
        logging.debug("Unexpected Error %s", exception)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/userBeer/<_user_id>/<_beer_id>/<_pay_type_id>/GET', methods=['GET'])
def user_beer_pay_type_for_visit(_user_id, _beer_id, _pay_type_id):
    """
    User beer pay type for visit method
    """
    try:
        beers = UserBeerFacade().user_beer_pay_type_for_visit(_user_id, _beer_id, _pay_type_id)
        if len(beers) > 0:
            return jsonify(json.dumps(beers, cls=AlchemyEncoder))
        return jsonify(beers), status.HTTP_204_NO_CONTENT
    except Exception as exception:
        logging.debug("Unexpected Error %s", exception)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/userBeer/<_user_id>/<_pay_type_id>/GET', methods=['GET'])
def user_pay_type_for_visit(_user_id, _pay_type_id):
    """
    User pay type for visit method
    """
    try:
        beers = UserBeerFacade().user_pay_type_for_visit(_user_id, _pay_type_id)
        if len(beers) > 0:
            return jsonify(json.dumps(beers, cls=AlchemyEncoder))        
        return jsonify(beers), status.HTTP_204_NO_CONTENT
    except Exception as exception:
        logging.debug("Unexpected Error %s", exception)
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/userBeer/INSERT', methods=['POST'])
def insert_user_by_visit():
    """
    Insert user by visit method
    """
    try:
        _json = request.get_json()
        UserBeerFacade().insert_usuario_cerveza(_json)
        return jsonify(OK)
    except Exception as exception:
        logging.debug("Unexpected Error %s", exception)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

############ Promotion ################################################

@app.route('/promotion', methods=['GET'])
def promotions():
    """
    Promotions method
    """
    try:
        promotions = PromotionFacade().promotions()
        if len(promotions) > 0:
            return jsonify(json.dumps(promotions, cls=AlchemyEncoder))        
        return jsonify(promotions), status.HTTP_204_NO_CONTENT
    except Exception as exception:
        logging.debug("Unexpected Error %s", exception)
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/promotion/INSERT', methods=['POST'])
def insert_promotion():
    """
    Insert promotion method
    """
    try:
        _json_promotion = request.get_json()
        PromotionFacade().insert_promotion(_json_promotion)
        return jsonify(OK)
    except Exception as exception:
        logging.debug("Unexpected Error %s", exception)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/promotion/UPDATE', methods=['PUT'])
def update_promotion():
    """
    Update promotion method
    """
    try:
        _json_promotion = request.get_json()
        PromotionFacade().update_promotion(_json_promotion)
        return jsonify(OK)
    except Exception as exception:
        logging.debug("Unexpected Error %s", exception)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

##################### Climate ##################################################

@app.route('/climate/weather', methods=['PUT'])
def weather():
    """
    Weather method
    """
    try:
        _json_promotion = request.get_json()
        Climate().get_current_weather(_json_promotion)
        return jsonify(OK)
    except Exception as exception:
        logging.debug("Unexpected Error %s", exception)
    return jsonify(FAIL), status.HTTP_409_CONFLICT


#@app.before_request

######################### Configuration #################################################

@app.route('/postgre', methods=['GET'])
def postgre():
    """
    Postgre instalation method
    """
    try:
        proxy = ProxyConfiguration()
        proxy.install_postgre()
        return jsonify(OK)
    except Exception as exception:
        logging.debug("Unexpected Error %s", exception)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/create_data_base', methods=['GET'])
def create_database():
    """
    Create database method
    """
    try:
        proxy = ProxyConfiguration()
        if not proxy.exist_data_base():
            logging.debug("DataBase no exists!")
            proxy.create_database()
            proxy.create_ddl()
        else:
            logging.debug("Database was already created!")
        return jsonify(OK)
    except:
        return jsonify(FAIL), status.HTTP_409_CONFLICT
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/create_database_dml', methods=['GET'])
def create_dml():
    """
    Create dml method
    """
    try:
        proxy = ProxyConfiguration()
        if proxy.exist_data_base():
            logging.debug("Begin insert DML!")
            proxy.create_dml()
        else:
            logging.debug("Database no exists. we going to create it!")
            proxy.exist_data_base()
            proxy.create_ddl()
            proxy.create_dml()
        return jsonify(OK)
    except:
        return jsonify(FAIL), status.HTTP_409_CONFLICT
    return jsonify(FAIL), status.HTTP_409_CONFLICT

####### Main ############
if __name__ == '__main__':
    app.run()
