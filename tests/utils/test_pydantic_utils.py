from typing import Dict

import pytest

from evidently.base_metric import MetricResult


class MockMetricResultField(MetricResult):
    nested_field: str


class MockMetricResult(MetricResult):
    field1: MockMetricResultField
    field2: int


def test_field_path():
    assert MockMetricResult.fields.list_fields() == ["type", "field1", "field2"]
    assert MockMetricResult.fields.field1.list_fields() == ["type", "nested_field"]
    assert MockMetricResult.fields.list_nested_fields() == ["type", "field1.type", "field1.nested_field", "field2"]

    with pytest.raises(AttributeError):
        MockMetricResult.fields.field3.list_fields()


class MockMetricResultWithDict(MetricResult):
    d: Dict[str, MockMetricResultField]


def test_field_path_with_dict():
    assert MockMetricResultWithDict.fields.list_fields() == ["type", "d"]
    assert MockMetricResultWithDict.fields.list_nested_fields() == ["type", "d.*.type", "d.*.nested_field"]

    assert MockMetricResultWithDict.fields.d.lol.list_fields() == ["type", "nested_field"]

    assert str(MockMetricResultWithDict.fields.d.lol.nested_field) == "d.lol.nested_field"