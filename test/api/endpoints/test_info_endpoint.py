from  ThamesThrive .config import  ThamesThrive 
from  ThamesThrive .domain.version import Version
from test.utils import Endpoint

endpoint = Endpoint()


def test_should_return_version():
    response = endpoint.get('/info/version')
    assert response.status_code == 200
    result = response.json()
    assert result ==  ThamesThrive .version.version


def test_should_return_detailed_version():
    response = endpoint.get('/info/version/details')
    assert response.status_code == 200
    result = response.json()
    version = Version(**result)
    assert version.version ==  ThamesThrive .version.version
