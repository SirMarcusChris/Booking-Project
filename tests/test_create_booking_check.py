import allure
import pytest
import requests

from conftest import generate_random_booking_data


@allure.feature('Test create booking')
@allure.story('Test create booking')
def test_create_booking(api_client, generate_random_booking_data):
    response = api_client.create_booking(generate_random_booking_data)

    with allure.step('Check create booking firstname'):
        assert response['booking']['firstname'] == generate_random_booking_data['firstname']
    with allure.step('Check create booking lastname'):
        assert response['booking']['lastname'] == generate_random_booking_data['lastname']
    with allure.step('Check create booking totalprice'):
        assert response['booking']['totalprice'] == generate_random_booking_data['totalprice']
    with allure.step('Check create booking depositpaid'):
        assert response['booking']['depositpaid'] == generate_random_booking_data['depositpaid']
    with allure.step('Check create booking bookingdates_checkin'):
        assert response['booking']['bookingdates']['checkin'] == generate_random_booking_data['bookingdates']['checkin']
    with allure.step('Check create booking bookingdates_checkout'):
        assert response['booking']['bookingdates']['checkout'] == generate_random_booking_data['bookingdates']['checkout']

@allure.feature('Test create booking')
@allure.story('Test server unavailability')
def test_ping_server_anavailability(api_client, mocker):
    mocker.patch.object(api_client.session, 'post', side_effect=Exception("Server unavailable"))
    with pytest.raises(Exception, match="Server unavailable"):
        api_client.create_booking(generate_random_booking_data)

@allure.feature('Test create booking')
@allure.story('Test wrong HTTP method')
def test_create_booking_wrong_method(api_client, mocker, generate_random_booking_data):
    mock_response = mocker.Mock()
    mock_response.status_code = 405
    mocker.patch.object(api_client.session, 'post', return_value=mock_response)
    with pytest.raises(AssertionError, match=f"Expected status 200 but got 405"):
        api_client.create_booking(generate_random_booking_data)
        
@allure.feature('Test create booking')
@allure.story('Test server error')
def test_create_booking_internal_server_error(api_client, mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 500
    mocker.patch.object(api_client.session,'post', return_value=mock_response)
    with pytest.raises(AssertionError, match="Expected status 200 but got 500"):
        api_client.create_booking(generate_random_booking_data)

@allure.feature('Test create booking')
@allure.story('Test wrong URL')
def test_create_booking_not_found(api_client, mocker, generate_random_booking_data):
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mocker.patch.object(api_client.session, 'post', return_value=mock_response)
    with pytest.raises(AssertionError, match=f"Expected status 200 but got 404"):
        api_client.create_booking(generate_random_booking_data)
        
@allure.feature('Test create booking')
@allure.story('Test connection with different success code')
def test_ping_success_different_code(api_client, mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 201
    mocker.patch.object(api_client.session,'post', return_value=mock_response)
    with pytest.raises(AssertionError, match="Expected status 200 but got 201"):
        api_client.create_booking(generate_random_booking_data)
        
@allure.feature('Test ping')
@allure.story('Test timeout')
def test_create_booking_timeout(api_client, mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mocker.patch.object(api_client.session, 'post', side_effect=requests.Timeout)
    with pytest.raises(requests.Timeout):
        api_client.create_booking(generate_random_booking_data)