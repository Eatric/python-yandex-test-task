import pytest
from app.delivery import calculate_delivery_cost
from app.delivery_enums import Dimensions, ServiceWorkload
from app.delivery_constants import MIN_DELIVERY_COST


# Given When Then
@pytest.mark.parametrize("dimension,expected_cost",
                         [
                             pytest.param(Dimensions.BIG, 480),
                             pytest.param(Dimensions.SMALL, MIN_DELIVERY_COST),
                         ])
def test_calculate_delivery_cost_with_different_dimensions_should_be_positive(dimension, expected_cost):
    # Act
    current_cost = calculate_delivery_cost(10, dimension, False, ServiceWorkload.VERY_HIGH)

    # Assert
    assert current_cost == expected_cost


# Given When Then
@pytest.mark.parametrize("dimension",
                         [
                             pytest.param(200),
                             pytest.param("testdimension"),
                         ])
def test_calculate_delivery_cost_with_different_dimensions_should_throw_exception_type_error(dimension):
    # Act, Assert
    with pytest.raises(TypeError):
        calculate_delivery_cost(10, dimension, False, ServiceWorkload.VERY_HIGH)
