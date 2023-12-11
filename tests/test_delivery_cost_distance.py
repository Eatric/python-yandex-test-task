import pytest
from app.delivery import calculate_delivery_cost
from app.delivery_enums import Dimensions, ServiceWorkload
from app.delivery_constants import MIN_DELIVERY_COST


# Given When Then
@pytest.mark.parametrize("distance,expected_cost",
                         [
                             pytest.param(1.9, MIN_DELIVERY_COST),
                             pytest.param(2.0, MIN_DELIVERY_COST),
                             pytest.param(2.1, 480),
                             pytest.param(9.9, 480),
                             pytest.param(10, 480),
                             pytest.param(10.1, 640),
                             pytest.param(29.9, 640),
                             pytest.param(30, 640),
                             pytest.param(30.1, 800),
                         ])
def test_calculate_delivery_cost_with_different_distance_should_be_positive(distance, expected_cost):
    # Act
    current_cost = calculate_delivery_cost(distance, Dimensions.BIG, False, ServiceWorkload.VERY_HIGH)

    # Assert
    assert current_cost == expected_cost


# Given When Then
@pytest.mark.parametrize("distance",
                         [
                             pytest.param(-10),
                             pytest.param(0)
                         ])
def test_calculate_delivery_cost_with_distance_lower_zero_should_throw_exception_value_error(distance):
    # Act, Assert
    with pytest.raises(ValueError, match="Argument distance cannot be lower or equal zero."):
        calculate_delivery_cost(distance, Dimensions.BIG, False, ServiceWorkload.VERY_HIGH)


# Given When Then
@pytest.mark.parametrize("distance",
                         [
                             pytest.param("test_string"),
                             pytest.param("123")
                         ])
def test_calculate_delivery_cost_with_distance_wrong_type_throw_exception_type_error(distance):
    # Act, Assert
    with pytest.raises(TypeError, match="Argument distance should be float/int type."):
        calculate_delivery_cost(distance, Dimensions.BIG, False, ServiceWorkload.VERY_HIGH)
