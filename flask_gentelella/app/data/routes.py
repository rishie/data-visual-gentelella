from app.data import blueprint
from flask import render_template
from flask_login import login_required
from .data_manipulation import *


@blueprint.route('/<template>')
# @login_required
def route_template(template):    
    data_json1 = get_data('../csv/Drivers_in_Fatal_Crashes.csv')
    # print(data_json1)

    data_json2 = get_data(
        '../csv/Persons_Injured_and_Injury Rates_by_Population.csv')
    # print(data_json2)

    data_json3 = get_data(
        '../csv/Drivers_per_state_2016.csv')
    # print(data_json3)
    
    return render_template(template + '.html', data_json1=data_json1, data_json2=data_json2, data_json3=data_json3)

