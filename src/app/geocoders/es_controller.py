import json
from src import log

logger = log.setup_custom_logger('ES_GEO_CONTROLLER')


def search_by_index_and_id(es, _index, _id):
    logger.info(f'Searching cache for address id <{_id}>')
    res = es.get(
        index=_index,
        id=_id
    )

    return res


def add_to_index(es, _index, _id, body):
    logger.info(f'Adding address with <{_id}> to index')

    res = es.index(
        index=_index,
        id=_id,
        body=json.dumps(body)
    )
    return res

