from basecase.basecase import BaseCase


class TestAddDesktop(BaseCase):
    def test_add_desktop(self):
        res = self.adddesktop.add_desktop()
        print(res.json())
        assert res.status_code == 200