from ..utils import func
from ..utils import common

class TestEditActivity:
    def test_view_activity(self):
        driver = common.get_driver()
        func.login(driver)
        assert 0