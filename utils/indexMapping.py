indexMapping = {
    "properties": {
        "id": {
            "type": "long"
        },
        "address": {
            "type": "text"
        },
        "bedrooms": {
            "type": "text"
        },
        "bathrooms": {
            "type": "text"
        },
        "size": {
            "type": "text"
        },
        "pets": {
            "type": "text"
        },
        "type": {
            "type": "text"
        },
        "neighbourhood": {
            "type": "text"
        },
        "description": {
            "type": "text"
        },
        "sponsored": {
            "type": "boolean"
        },
        "image": {
            "type": "text"
        },
        "price": {
            "type": "float"
        },
        "naturalDescription": {
            "type": "text"
        },
        "naturalDescriptionVector": {
            "type": "dense_vector",
            "dims": 1536,
            "index": True,
            "similarity": "l2_norm"
        }

    }
}
