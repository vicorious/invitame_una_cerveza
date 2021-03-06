"""
Service http module
"""
import logging
from flask import Flask, jsonify, json, request
from flask_api import status
from flask_cors import CORS, cross_origin
from flask_swagger import swagger
from sqlalchemy.orm.exc import MultipleResultsFound
from proxy import ProxyConfiguration
from facade_user import UserFacade
from facade_bares import BarFacade
from facade_cerveza import BeerFacade
from facade_usuario_cerveza import UserBeerFacade
from facade_promotion import PromotionFacade
from facade_climate import Climate
from facade_parameters import FacadeParameters

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app)

OK = 'OK'
FAIL = 'FAIL'

logging.basicConfig(filename="test.log", level=logging.DEBUG)

@app.route('/user/login', methods=['POST'])
@cross_origin()
def login():
    """
    Login method
    ---
    tags:
      - users
    definitions:
      - schema:
          id: Group
          properties:
            name:
             type: string
             description: the group's name
    parameters:
      - in: body
        name: body
        schema:
          id: User
          required:
            - email
            - name
          properties:
            email:
              type: string
              description: email for user
            name:
              type: string
              description: name for user
            address:
              description: address for user
              schema:
                id: Address
                properties:
                  street:
                    type: string
                  state:
                    type: string
                  country:
                    type: string
                  postalcode:
                    type: string
            groups:
              type: array
              description: list of groups
              items:
                $ref: "#/definitions/Group"
    responses:
      201:
        description: User created
    """
    try:
        _json_login = request.get_json()
        UserFacade().login(_json_login)
        return jsonify(OK)
    except MultipleResultsFound as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/user/register/INSERT', methods=['POST'])
@cross_origin()
def register():
    """
    Register method
    """
    try:
        _json_registro = request.get_json()
        UserFacade().register(_json_registro)
        return jsonify(OK)
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/user/password/UPDATE', methods=['PUT'])
@cross_origin()
def forgot_password():
    """
    Forgot method
    """
    try:
        _json_olvido = request.get_json()
        UserFacade().forgot_password(_json_olvido)
        return jsonify(OK)
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/bars/<_bar_id>/GET', methods=['GET'])
@cross_origin()
def bar_for_id(_bar_id):
    """
    Bar for id method
    """
    try:
        _bar = BarFacade().bar_id(_bar_id)
        if _bar is None:
            return jsonify(_bar), status.HTTP_204_NO_CONTENT
        return jsonify(_bar)
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/bars', methods=['GET'])
@cross_origin()
def bars():
    """
    Get bars method
    """
    try:
        queryStringDict = request.args
        _bars = BarFacade().bars(queryStringDict)
        if len(_bars) > 0:
            return jsonify(_bars)    
        return jsonify(_bars), status.HTTP_204_NO_CONTENT
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/bars/INSERT', methods=['POST'])
@cross_origin()
def insert_bar():
    """
    Insert bar method
    """
    try:
        _json_bar = request.get_json()
        BarFacade().insert_bar(_json_bar)
        return jsonify(OK)
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/bars/UPDATE', methods=['PUT'])
@cross_origin()
def update_bar():
    """
    Update bar method
    """
    try:
        _json_bar = request.get_json()
        BarFacade().update_bar(_json_bar)
        return jsonify(OK)
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/beers/<_beer_id>/GET', methods=['GET'])
@cross_origin()
def beer_id(_beer_id):
    """
    Beer for id method
    """
    try:
        _beer = BeerFacade().beer_id(_beer_id)
        if _beer is None:
            return jsonify(_beer), status.HTTP_204_NO_CONTENT
        return jsonify(_beer)
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/beer/<_bar_id>', methods=['GET'])
@cross_origin()
def beer_by_bar(_bar_id):
    """
    Beer for id method
    """
    try:
        _beer = BeerFacade().beer_by_bar(_bar_id)
        if _beer is None:
            return jsonify(_beer), status.HTTP_204_NO_CONTENT
        return jsonify(_beer)
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT    


@app.route('/beers', methods=['GET'])
@cross_origin()
def beers():
    """
    get Beers method
    """
    try:
        queryStringDict = request.args
        _beers = BeerFacade().beers(queryStringDict)
        if len(_beers) > 0:
            return jsonify(_beers)
        return jsonify(_beers), status.HTTP_204_NO_CONTENT
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/beers/pairing/<beer_id>', methods=['GET'])
@cross_origin()
def beers_pairing(beer_id):
    """
    get Beers method
    """
    try:
        _beers = BeerFacade().beer_pairing(beer_id)
        if len(_beers) > 0:
            return jsonify(_beers)
        return jsonify(_beers), status.HTTP_204_NO_CONTENT
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/beer/INSERT', methods=['POST'])
@cross_origin()
def insert_beer():
    """
    Insert beer method
    """
    try:
        _json_beer = request.get_json()
        BeerFacade().insert_beer(_json_beer)
        return jsonify(OK)
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/beer/UPDATE', methods=['PUT'])
@cross_origin()
def update_beer():
    """
    Update beer method
    """
    try:
        _json_beer = request.get_json()
        BeerFacade().update_beer(_json_beer)
        return jsonify(OK)
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/userBeer/<_user_id>/GET', methods=['GET'])
@cross_origin()
def user_for_visit(_user_id):
    """
    User for visit method
    """
    try:
        user_beer = UserBeerFacade().user_for_visit(_user_id)
        if len(user_beer) > 0:
            return jsonify(user_beer)
        return jsonify(user_beer), status.HTTP_204_NO_CONTENT
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/userBeer/<_user_id>/<_beer_id>/GET', methods=['GET'])
@cross_origin()
def user_beer_for_visit(_user_id, _beer_id):
    """
    User beer method
    """
    try:
        _beers = UserBeerFacade().user_beer_for_visit(_user_id, _beer_id)
        if len(_beers) > 0:
            return jsonify(_beers)
        return jsonify(_beers), status.HTTP_204_NO_CONTENT
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/userBeer/<_user_id>/<_beer_id>/<_pay_type_id>/GET', methods=['GET'])
@cross_origin()
def user_beer_pay_type_for_visit(_user_id, _beer_id, _pay_type_id):
    """
    User beer pay type for visit method
    """
    try:
        _beers = UserBeerFacade().user_beer_pay_type_for_visit(_user_id, _beer_id, _pay_type_id)
        if len(_beers) > 0:
            return jsonify(_beers)
        return jsonify(_beers), status.HTTP_204_NO_CONTENT
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/userBeer/<_user_id>/<_pay_type_id>/GET', methods=['GET'])
@cross_origin()
def user_pay_type_for_visit(_user_id, _pay_type_id):
    """
    User pay type for visit method
    """
    try:
        _beers = UserBeerFacade().user_pay_type_for_visit(_user_id, _pay_type_id)
        if len(_beers) > 0:
            return jsonify(_beers)
        return jsonify(_beers), status.HTTP_204_NO_CONTENT
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT


@app.route('/userBeer/INSERT', methods=['POST'])
@cross_origin()
def insert_user_by_visit():
    """
    Insert user by visit method
    """
    try:
        _json = request.get_json()
        UserBeerFacade().insert_user_for_visit(_json)
        return jsonify(OK)
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/promotions', methods=['GET'])
@cross_origin()
def promotions():
    """
    Promotions method
    """
    try:
        _promotions = PromotionFacade().promotions()
        if len(_promotions) > 0:
            return jsonify(_promotions)
        return jsonify(_promotions), status.HTTP_204_NO_CONTENT
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/promotions_by_bar/<_bar_id>', methods=['GET'])
@cross_origin()
def promotions_by_bar(_bar_id):
    """
    Promotions method
    """
    try:
        _promotions = PromotionFacade().promotions_by_bar(_bar_id)
        if len(_promotions) > 0:
            return jsonify(_promotions)
        return jsonify(_promotions), status.HTTP_204_NO_CONTENT
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT    


@app.route('/promotions/INSERT', methods=['POST'])
@cross_origin()
def insert_promotion():
    """
    Insert promotion method
    """
    try:
        _json_promotion = request.get_json()
        PromotionFacade().insert_promotion(_json_promotion)
        return jsonify(OK)
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/promotions/UPDATE', methods=['PUT'])
@cross_origin()
def update_promotion():
    """
    Update promotion method
    """
    try:
        _json_promotion = request.get_json()
        PromotionFacade().update_promotion(_json_promotion)
        return jsonify(OK)
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/pay_type', methods=['GET'])
@cross_origin()
def pay_type():
    """
    Pay type's method
    """
    try:
        pay_types = FacadeParameters().pay_type()
        return jsonify(pay_types)
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/climate/weather/<city>', methods=['GET'])
@cross_origin()
def weather(city):
    """
    Weather method
    """
    try:
        climate_dto = Climate().get_current_weather(city)
        return jsonify(climate_dto)
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/postgre', methods=['GET'])
@cross_origin()
def postgre():
    """
    Postgre instalation method
    """
    try:
        proxy = ProxyConfiguration()
        proxy.install_postgre()
        return jsonify(OK)
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT

@app.route('/create_database_and_dml', methods=['GET'])
@cross_origin()
def create_database_and_dml():
    """
    Create database_and_dml method
    """
    try:
        proxy = ProxyConfiguration()
        if proxy.exist_data_base():
            logging.debug("Begin insert DML!")
            proxy.create_dml()
        else:
            logging.debug("Database no exists. we going to create it!")
            proxy.create_database()
            proxy.create_ddl()
            proxy.create_dml()
        return jsonify(OK)
    except Exception as _excep:
        logging.debug("Unexpected Error %s", _excep)
    return jsonify(FAIL), status.HTTP_409_CONFLICT
    
    
@app.route("/spec", methods=['GET'])
@cross_origin()
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "My API"
    return jsonify(swag)

if __name__ == '__main__':
    app.run()
