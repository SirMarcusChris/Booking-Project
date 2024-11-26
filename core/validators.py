import allure

def verify_booking_response(response, booking_data):
    """ Проверяет, что данные в ответе совпадают с данными отправленной брони.
    :param response: Ответ API в виде словаря
    :param booking_data: Отправленные данные бронирования """
    with allure.step("Verify booking response"):
        assert response['booking']['firstname'] == booking_data['firstname'], f"Expected firstname {booking_data['firstname']}, but got {response['booking']['firstname']}"
        assert response['booking']['lastname'] == booking_data['lastname'], f"Expected lastname {booking_data['lastname']}, but got {response['booking']['lastname']}"
        assert response['booking']['totalprice'] == booking_data['totalprice'], f"Expected totalprice {booking_data['totalprice']}, but got {response['booking']['totalprice']}"
        assert response['booking']['depositpaid'] == booking_data['depositpaid'], f"Expected depositpaid {booking_data['depositpaid']}, but got {response['booking']['depositpaid']}"
        assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin'], f"Expected checkin {booking_data['bookingdates']['checkin']}, but got {response['booking']['bookingdates']['checkin']}"
        assert response['booking']['bookingdates']['checkout'] == booking_data['bookingdates']['checkout'], f"Expected checkout {booking_data['bookingdates']['checkout']}, but got {response['booking']['bookingdates']['checkout']}"
        if 'additionalneeds' in booking_data:
            assert response['booking']['additionalneeds'] == booking_data['additionalneeds'], f"Expected additionalneeds {booking_data['additionalneeds']}, but got {response['booking']['additionalneeds']}"
