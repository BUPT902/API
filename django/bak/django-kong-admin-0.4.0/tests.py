from kong.exceptions import ConflictError
from kong.simulator import KongAdminSimulator
from kong.client import KongAdminClient
from kong.compat import TestCase, skipIf, run_unittests, OrderedDict, urlencode, HTTPConnection
from kong.utils import uuid_or_string, add_url_params, sorted_ordered_dict


def test_create(self):
    API_URL = os.environ.get('PYKONG_TEST_API_URL', 'http://localhost:8001')
    username = 'abcdefg'
    custom_id = 1233333333
    client = KongAdminClient(API_URL)

    result = self.client.consumers.create(
        username=username, custom_id=custom_id)

if __name__ == '__main__':
    test_create()