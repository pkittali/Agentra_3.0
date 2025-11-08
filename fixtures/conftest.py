import pytest
from core.driver_factory import DriverFactory

def pytest_addoption(parser):
    parser.addoption('--platform', action='store', default='web', help='Platform: web|mobile|desktop')

@pytest.fixture(scope='session')
def platform(request):
    return request.config.getoption('--platform')

@pytest.fixture(scope='function')
def driver(platform):
    drv = DriverFactory.get_driver(platform)
    yield drv
    try:
        drv.quit()
    except Exception:
        pass
