import requests
import json
from settings import url_base


class Sklad15Inventorization:
    """Класс c методом отправки GET запроса к REST API "Склад 15 Базовый" для тестирования функции "Инвентаризация"."""

    def __init__(self):
        self.base_url = url_base

    def get_select_docs_info(self, query: str):
        """GET-mетод для предоставления сведений о документах инвентаризации приложения MobileSMARTS "Склад 15, Базовый.
         Аргументы query_key и query_value принимают значения, указанные в REST API документации Swagger для
         «Mobile SMARTS: Магазин 15»."""

        response = requests.get(self.base_url + query)

        status = response.status_code
        result = ""
        try:
            result = response.json()
        except json.decoder.JSONDecodeError:
            result = response.text

        return status, result

    def post_inventar_doc(self, id_doc: str, name_doc: str):
        """"""

        body = {
            "id": id_doc,
            "name": name_doc,
            "appointment": "string",
            "userId": "string",
            "userName": "string",
            "lastChangeDate": "2024-08-02T08:42:06.975Z",
            "createDate": "2024-08-02T08:42:06.975Z",
            "documentTypeName": "string",
            "declaredItems": [
                {
                    "uid": "string",
                    "lines": [
                        {}
                    ],
                    "createdBy": 0,
                    "productId": "string",
                    "declaredQuantity": 0,
                    "currentQuantity": 0,
                    "currentQuantityWithBinding": 0,
                    "firstCellId": "string",
                    "firstStorageBarcode": "string",
                    "packingId": "string",
                    "sscc": "string",
                    "registeredDate": "2024-08-02T08:42:06.975Z",
                    "registrationDate": "2024-08-02T08:42:06.975Z",
                    "index": 0,
                    "expiredDate": "2024-08-02T08:42:06.975Z",
                    "secondCellId": "string",
                    "secondStorageBarcode": "string",
                    "product": {
                        "id": "string",
                        "name": "string",
                        "packings": [
                            {
                                "name": "string",
                                "selfWeight": 0,
                                "selfVolume": 0,
                                "unitsQuantity": 0,
                                "barcode": "string",
                                "barcodes": [
                                    "string"
                                ],
                                "id": "string",
                                "marking": "string"
                            }
                        ],
                        "barcode": "string",
                        "basePackingId": "string",
                        "marking": "string",
                        "quantityPolicy": {
                            "multiline": True,
                            "id": "string",
                            "packingIds": [
                                "string"
                            ]
                        },
                        "versionNumber": 0,
                        "classificatorIds": [
                            "string"
                        ]
                    },
                    "packing": {
                        "name": "string",
                        "selfWeight": 0,
                        "selfVolume": 0,
                        "unitsQuantity": 0,
                        "barcode": "string",
                        "barcodes": [
                            "string"
                        ],
                        "id": "string",
                        "marking": "string"
                    },
                    "bindedLineUid": "string",
                    "bindedLine": {},
                    "productName": "string",
                    "productMarking": "string",
                    "productBarcode": "string",
                    "packingName": "string",
                    "packingUnitsQuantity": 0
                }
            ],
            "combinedItems": [
                {
                    "uid": "string",
                    "lines": [
                        {}
                    ],
                    "createdBy": 0,
                    "productId": "string",
                    "declaredQuantity": 0,
                    "currentQuantity": 0,
                    "currentQuantityWithBinding": 0,
                    "firstCellId": "string",
                    "firstStorageBarcode": "string",
                    "packingId": "string",
                    "sscc": "string",
                    "registeredDate": "2024-08-02T08:42:06.975Z",
                    "registrationDate": "2024-08-02T08:42:06.975Z",
                    "index": 0,
                    "expiredDate": "2024-08-02T08:42:06.975Z",
                    "secondCellId": "string",
                    "secondStorageBarcode": "string",
                    "product": {
                        "id": "string",
                        "name": "string",
                        "packings": [
                            {
                                "name": "string",
                                "selfWeight": 0,
                                "selfVolume": 0,
                                "unitsQuantity": 0,
                                "barcode": "string",
                                "barcodes": [
                                    "string"
                                ],
                                "id": "string",
                                "marking": "string"
                            }
                        ],
                        "barcode": "string",
                        "basePackingId": "string",
                        "marking": "string",
                        "quantityPolicy": {
                            "multiline": True,
                            "id": "string",
                            "packingIds": [
                                "string"
                            ]
                        },
                        "versionNumber": 0,
                        "classificatorIds": [
                            "string"
                        ]
                    },
                    "packing": {
                        "name": "string",
                        "selfWeight": 0,
                        "selfVolume": 0,
                        "unitsQuantity": 0,
                        "barcode": "string",
                        "barcodes": [
                            "string"
                        ],
                        "id": "string",
                        "marking": "string"
                    },
                    "bindedLineUid": "string",
                    "bindedLine": {},
                    "productName": "string",
                    "productMarking": "string",
                    "productBarcode": "string",
                    "packingName": "string",
                    "packingUnitsQuantity": 0
                }
            ],
            "modified": True,
            "inProcess": True,
            "finished": True,
            "currentItems": [
                {
                    "uid": "string",
                    "lines": [
                        {}
                    ],
                    "createdBy": 0,
                    "productId": "string",
                    "declaredQuantity": 0,
                    "currentQuantity": 0,
                    "currentQuantityWithBinding": 0,
                    "firstCellId": "string",
                    "firstStorageBarcode": "string",
                    "packingId": "string",
                    "sscc": "string",
                    "registeredDate": "2024-08-02T08:42:06.975Z",
                    "registrationDate": "2024-08-02T08:42:06.975Z",
                    "index": 0,
                    "expiredDate": "2024-08-02T08:42:06.975Z",
                    "secondCellId": "string",
                    "secondStorageBarcode": "string",
                    "product": {
                        "id": "string",
                        "name": "string",
                        "packings": [
                            {
                                "name": "string",
                                "selfWeight": 0,
                                "selfVolume": 0,
                                "unitsQuantity": 0,
                                "barcode": "string",
                                "barcodes": [
                                    "string"
                                ],
                                "id": "string",
                                "marking": "string"
                            }
                        ],
                        "barcode": "string",
                        "basePackingId": "string",
                        "marking": "string",
                        "quantityPolicy": {
                            "multiline": True,
                            "id": "string",
                            "packingIds": [
                                "string"
                            ]
                        },
                        "versionNumber": 0,
                        "classificatorIds": [
                            "string"
                        ]
                    },
                    "packing": {
                        "name": "string",
                        "selfWeight": 0,
                        "selfVolume": 0,
                        "unitsQuantity": 0,
                        "barcode": "string",
                        "barcodes": [
                            "string"
                        ],
                        "id": "string",
                        "marking": "string"
                    },
                    "bindedLineUid": "string",
                    "bindedLine": {},
                    "productName": "string",
                    "productMarking": "string",
                    "productBarcode": "string",
                    "packingName": "string",
                    "packingUnitsQuantity": 0
                }
            ],
            "warehouseId": "string",
            "barcode": "string",
            "priority": 0,
            "description": "string",
            "autoAppointed": True,
            "serverHosted": True,
            "deviceId": "string",
            "deviceName": "string",
            "deviceIP": "string",
            "licenseStatus": 0,
            "tables": [
                {
                    "version": "string",
                    "name": "string",
                    "rows": [
                        {
                            "uid": "string",
                            "index": 0
                        }
                    ]
                }
            ],
            "states": [
                {
                    "modified": True,
                    "modifiedDate": "2024-08-02T08:42:06.975Z",
                    "inProcess": True,
                    "inProcessDate": "2024-08-02T08:42:06.975Z",
                    "finished": True,
                    "finishedDate": "2024-08-02T08:42:06.975Z",
                    "processingTime": "string",
                    "userId": "string"
                }
            ],
            "notOpenedYet": True,
            "pokazyvatBP": "string",
            "imyaBP": "string",
            "vybrannyjBPnaTSD": "string",
            "kontrolKolva": True,
            "idSklada1S": "string",
            "skladVvedenNaTSD": True,
            "nastrojkaBiznesProcessa": "string",
            "status": "string",
            "imyaSklada": "string"
        }

        response = requests.post(self.base_url, data=body)

        status = response.status_code
        result = ""
        try:
            result = response.json()
        except json.decoder.JSONDecodeError:
            result = response.text

        return status, result
