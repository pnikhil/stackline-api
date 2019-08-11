from flask import jsonify, request, json
from flask import Blueprint, Flask, Response
from config import Config
from api_error import BadRequest
import csv

from error_handler import *
from service import product_service

product_ctrl = Blueprint('Product Controller', __name__, url_prefix='/api/products')


@product_ctrl.route('/autocomplete', methods=['POST'])
def auto_complete():
    content = request.json
    if (check_autocomplete_request(content)):
        auto_complete_result_list = product_service.auto_complete_svc(content["type"], content["prefix"])

    return Response(json.dumps(auto_complete_result_list),  mimetype='application/json')


@product_ctrl.route('/search', methods=['POST'])
def search():
    content = request.json
    if(check_search_request(content)):
    #auto_complete_result_list = auto_complete_svc(content["type"], content["prefix"])
        search_result: list = product_service.search_product_svc(content["conditions"], content["pagination"])
        result_size = len(search_result)
        start = int(content["pagination"]["size"]) * (int(content["pagination"]["from"]) - 1)
        if start > result_size - 1:
            raise BadRequest('Page size value is empty or too big', 40001, {'ext': 1})

        paginated_result = product_service.paginate(search_result, content["pagination"]["size"], start, result_size)
    return Response(json.dumps(paginated_result),  mimetype='application/json')


@product_ctrl.route('/keywords', methods=['POST'])
def keywords():
    content = request.json
    if(check_keyword_request(content)):
        keyword_result = product_service.count_keywords(content["keywords"])
    return Response(json.dumps(keyword_result), mimetype='application/json')

@product_ctrl.errorhandler(BadRequest)
def handle_bad_request(error):
    """Catch BadRequest exception globally, serialize into JSON, and respond with 400."""
    payload = dict(error.payload or ())
    payload['status'] = error.status
    payload['message'] = error.message
    return jsonify(payload), 400
