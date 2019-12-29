from pymongo import MongoClient

__author__ = "S. Mehdi Abdollahi"

if __name__ == "__main__":

    scf_db = MongoClient("mongodb://172.30.96.195:27017,172.30.96.196:27017,"
                         "172.30.96.222:27017/?replicaSet=SCFrs&readPreference=secondaryPreferred", connect=False)[
        'scf']

    res = scf_db['network_element'].find({"ip_address": {"$nin": [
        "172.31.18.4",
        "172.31.18.5",
        "172.31.18.6",
        "172.31.18.7",
        "172.31.18.8",
        "172.31.18.9",
        "172.31.18.11",
        "172.31.18.12",
        "172.31.18.13",
        "172.31.18.14",
        "172.31.18.15",
        "172.31.18.16",
        "172.31.18.17",
        "172.31.18.18",
        "172.31.18.19",
        "172.31.18.20",
        "172.31.18.21",
        "172.31.18.22",
        "172.31.18.23",
        "172.31.18.24",
        "172.31.18.25",
        "172.31.18.26",
        "172.31.18.28",
        "172.31.114.4",
        "172.31.114.5",
        "172.31.114.6",
        "172.31.114.7",
        "172.31.114.8",
        "172.31.114.9",
        "172.31.114.11",
        "172.31.114.12",
        "172.31.114.13",
        "172.31.114.15",
        "172.31.114.16",
        "172.31.114.19",
        "172.31.114.23",
        "172.31.114.24",
        "172.31.114.25",
        "172.31.114.27",
        "172.31.114.28",
        "172.31.114.29",
        "172.31.114.30",
        "172.31.114.31",
        "172.31.114.32",
        "172.31.114.33",
        "172.31.114.34",
        "172.31.114.35",
        "172.31.114.36",
        "172.31.114.37",
        "172.31.114.39",
        "172.31.131.132",
        "172.31.131.134",
        "172.31.131.135",
        "172.31.131.136",
        "172.31.131.138",
        "172.31.131.139",
        "172.31.131.140",
        "172.31.131.141",
        "172.31.64.4",
        "172.31.64.5",
        "172.31.64.6",
        "172.31.64.7",
        "172.31.64.8",
        "172.31.64.9",
        "172.31.64.10",
        "172.31.64.11",
        "172.31.64.12",
        "172.31.64.13",
        "172.31.64.14",
        "172.31.64.15",
        "172.31.64.16",
        "172.31.64.17",
        "172.31.64.18",
        "172.31.64.19",
        "172.31.64.20",
        "172.31.64.21",
        "172.31.64.22",
        "172.31.64.23",
        "172.31.48.50",
        "172.31.48.51",
        "172.31.48.4",
        "172.31.48.5",
        "172.31.48.6",
        "172.31.48.47",
        "172.31.48.48",
        "172.31.48.49",
        "172.31.48.31",
        "172.31.48.32",
        "172.31.48.33",
        "172.31.48.27",
        "172.31.48.8",
        "172.31.48.23",
        "172.31.48.22",
        "172.31.48.7",
        "172.31.48.12",
        "172.31.48.13",
        "172.31.48.24",
        "172.31.84.133",
        "172.31.84.134",
        "172.31.84.142",
        "172.31.84.147",
        "172.31.84.148",
        "172.31.84.149",
        "172.31.84.150",
        "172.31.84.151",
        "172.31.84.152",
        "172.31.84.153",
        "172.31.84.154",
        "172.31.84.155",
        "172.31.84.156",
        "172.31.84.135",
        "172.31.84.144",
        "172.31.84.138",
        "172.31.84.139",
        "172.31.84.137",
        "172.31.84.145",
        "172.31.84.143",
        "172.31.84.136",
        "172.31.34.4",
        "172.31.34.5",
        "172.31.34.6",
        "172.31.34.29",
        "172.31.34.30",
        "172.31.34.31",
        "172.31.34.42",
        "172.31.34.35",
        "172.31.34.36",
        "172.31.34.37",
        "172.31.34.8",
        "172.31.34.51",
        "172.31.34.9",
        "172.31.34.49",
        "172.31.34.47",
        "172.31.34.7",
        "172.31.34.48",
        "172.31.34.50",
        "172.31.34.53"
    ]}}, {"_id": 1})

    # print(res)
    arr = []
    for i in res:
        arr.append(str(i['_id']))

    res2 = scf_db["network_element_port"].count({'dlm_function_enabled': True, 'network_element_id': {'$nin': arr}})
    print(res2)