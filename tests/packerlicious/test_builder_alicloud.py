import pytest

import packerlicious.builder as builder


class TestAliCloudBuilder(object):

    def test_required_fields_missing(self):
        b = builder.AliCloud()

        with pytest.raises(ValueError) as excinfo:
            b.to_dict()
        assert 'required' in str(excinfo.value)
