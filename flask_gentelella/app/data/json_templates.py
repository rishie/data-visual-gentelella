# from ast import literal_eval

# # write to json
# def get_chartjs_json(path):

#     # import csv
#     data_csv = pd.read_csv(path)

#     # convert our data of interest into json
#     data_json = data_csv[['State', 'Total_Killed']].to_json()

#     return format_chartjs_json(data_json, 'State', 'Total_Killed', 'bar')

# def get_echart_json(path):

#     # import csv
#     data_csv = pd.read_csv(path)

#     # convert our data of interest into json
#     data_json = data_csv[['State', 'Total_Killed']].to_json()

#     return format_echart_json(data_json, 'State', 'Total_Killed', 'bar', 'Fatalities', 'Traffice Fatalities by Gender')

# # TODO: add title option
# # required arguments: json, x axis name, y axis name, chart type
# def format_chartjs_json(json, x, y, chart_type, label="", backgroundColor=[], borderColor=[]):
#     dict_json = literal_eval(json)
#     data_obj = {
#         "type": chart_type,
#         "data": {
#             "labels": list(dict_json[x].values()),
#             "datasets": [
#                 {
#                     "label": label,
#                     "data": list(dict_json[y].values()),
#                     "fill": False,
#                     "backgroundColor": backgroundColor,
#                     "borderColor": borderColor,
#                     "lineTension": 0.1
#                 }
#             ]},
#         "options": {}
#     }

#     return data_obj

# # required arguments: json, x axis name, y axis name, chart type, title
# def format_echart_json(json, x, y, chart_type, title="", labels=[], backgroundColor=[], borderColor=[]):
#     dict_json = literal_eval(json)
#     data_obj = {
#         "title": {
#             "text": title
#         },
#         "tooltip": {},
#         "legend": {
#             "data": labels
#         },
#         "xAxis": {
#             "data": list(dict_json[x].values())
#         },
#         "yAxis": {}, # TODO
#         "series": [{
#             "name": "", # TODO
#             "type": chart_type,
#             "data": list(dict_json[y].values())
#         }]
#     }

#     return data_obj
