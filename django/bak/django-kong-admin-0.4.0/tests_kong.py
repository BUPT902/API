from kong.exceptions import ConflictError
from kong.simulator import KongAdminSimulator
from kong.client import KongAdminClient
from kong.compat import TestCase, skipIf, run_unittests, OrderedDict, urlencode, HTTPConnection
from kong.utils import uuid_or_string, add_url_params, sorted_ordered_dict
import os


def test_create():
    API_URL = os.environ.get('PYKONG_TEST_API_URL', 'http://localhost:8001')
    username = 'abcde'
    custom_id = 1233333333333
    client = KongAdminClient(API_URL)

    result = client.consumers.create(
        username=username, custom_id=custom_id)
    print result
    result2 = client.consumers.acl(result['id']).create(group='black_list')
    print result2
    result2 = client.consumers.acl(result['id']).create(group='black_list2')
    print result2

if __name__ == '__main__':
    test_create()