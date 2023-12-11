import pytest
from app.delivery import calculate_delivery_cost
from app.delivery_enums import Dimensions, ServiceWorkload
from app.delivery_constants import MIN_DELIVERY_COST


# Given When Then
@pytest.mark.parametrize("service_workload,expected_cost",
                         [
                             pytest.param(ServiceWorkload.NORMAL, MIN_DELIVERY_COST),
                             pytest.param(ServiceWorkload.BIG, 480),
                             pytest.param(ServiceWorkload.HIGH, 560),
                             pytest.param(ServiceWorkload.VERY_HIGH, 640),
                         ])
def test_calculate_delivery_cost_with_different_service_workload_should_be_positive(service_workload, expected_cost):
    # Act
    current_cost = calculate_delivery_cost(15, Dimensions.BIG, False, service_workload)

    # Assert
    assert current_cost == expected_cost


# Given When Then
@pytest.mark.parametrize("service_workload",
                         [
                             pytest.param(1.5),
                             pytest.param("test_string")
                         ])
def test_calculate_delivery_cost_with_service_workload_should_throw_exception_value_error(service_workload):
    # Act, Assert
    with pytest.raises(TypeError):
        calculate_delivery_cost(15, Dimensions.BIG, False, service_workload)
