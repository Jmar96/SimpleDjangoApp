myData = {
    "1": {
        "name": "JProjekt",
        "role": "Dev"
    },
    "2": {
        "name": "Sorrymasen",
        "role": "Dev"
    },
}


def get_all():
    return myData


def get_one(item_id):
    return myData.get(item_id)


def create(data):
    # generate the next numeric-looking id, e.g. "1" -> "2" -> "3"
    existing_ids = [int(k) for k in myData.keys() if k.isdigit()]
    new_id = str(max(existing_ids, default=0) + 1)
    myData[new_id] = data
    return new_id, data


def update(item_id, data):
    if item_id not in myData:
        return None
    myData[item_id].update(data)
    return myData[item_id]


def delete(item_id):
    if item_id in myData:
        del myData[item_id]
        return True
    return False
