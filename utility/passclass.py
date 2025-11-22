import pytest

@pytest.mark.usefixtures("setup")
class passclass :
    driver = None
    swag = None