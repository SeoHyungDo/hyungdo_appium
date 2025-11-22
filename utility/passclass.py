import pytest

@pytest.mark.usefixtures("setup")
class passclass :
    driver = None
    swag = None
    wait = None
    swag_home = None