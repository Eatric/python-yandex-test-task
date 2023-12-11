import pytest
from app.delivery import calculate_delivery_cost
from app.delivery_enums import Dimensions, ServiceWorkload


# Given When Then
@pytest.mark.parametrize("fragile,expected_cost",
                         [
                             pytest.param(True, 1120),
                             pytest.param(False, 640),
                         ])
def test_calculate_delivery_cost_with_different_fragile_should_be_positive(fragile, expected_cost):
    # Act
    current_cost = calculate_delivery_cost(29, Dimensions.BIG, fragile, ServiceWorkload.VERY_HIGH)

    # Assert
    assert current_cost == expected_cost


# Given When Then
@pytest.mark.parametrize("fragile",
                         [
                             pytest.param(1),
                             pytest.param("true"),
                         ])
def test_calculate_delivery_cost_with_different_fragile_should_throw_exception_type_error(fragile):
    # Act, Assert
    with pytest.raises(TypeError):
        calculate_delivery_cost(10, Dimensions.BIG, fragile, ServiceWorkload.VERY_HIGH)


# Given When Then
@pytest.mark.parametrize("distance,fragile",
                         [
                             pytest.param(31, True),
                         ])
def test_calculate_delivery_cost_with_fragile_distance_more_30_should_throw_exception_value_error(distance, fragile):
    # Act, Assert
    with pytest.raises(ValueError):
        calculate_delivery_cost(distance, Dimensions.BIG, fragile, ServiceWorkload.VERY_HIGH)
