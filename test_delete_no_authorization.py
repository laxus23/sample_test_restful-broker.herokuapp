import requests


class TestUsers:
    def __init__(self):
        self.new_booking = {
                "firstname": "John",
                "lastname": "Appleseed",
                "totalprice": 15151,
                "depositpaid": True,
                "bookingdates": {
                    "checkin": "2019-10-25",
                    "checkout": "2019-10-26"
                }
            }
        self.auth_token = {
                "username": "admin",
                "password": "password123"
            }

    def test_post_auth_token(self):
        """
        Test to see if a token is generated.
        :return:
        """
        response = requests.post("https://restful-booker.herokuapp.com/auth", Test.auth_token)
        token = response.json()["token"]
        assert response.status_code == 200
        assert len(token) > 0

    def test_delete_no_authorization(self):
        """
        Test to see if booking can be deleted without authorization.
        :return:
        """

        # Step 1 - creating a booking
        response = requests.post("https://restful-booker.herokuapp.com/booking", json=Test.new_booking)
        bookingid = response.json()["bookingid"]
        assert response.status_code == 200
        assert response.json()['booking'] == Test.new_booking

        # Step 2 - trying to delete a booking
        response = requests.delete(f"https://restful-booker.herokuapp.com/booking/{bookingid}")
        assert response.status_code == 403

        # Step 3 - checking  if booking still exist and it's the same
        response = requests.get(f"https://restful-booker.herokuapp.com/booking/{bookingid}")
        assert response.status_code == 200
        assert response.json() == Test.new_booking


Test = TestUsers()

Test.test_post_auth_token()

Test.test_delete_no_authorization()
