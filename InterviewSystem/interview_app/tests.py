import json

from django.contrib.auth.hashers import make_password
from rest_framework.settings import api_settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from InterviewSystem.interview_app.models import CustomUser, SentEmail, Interview, Feedback


class AccountTests(APITestCase):
    def test_get_token_accurate_credentials(self):
        hruser = CustomUser.objects.create(
            email="hr@hr.com",
            first_name="Hr",
            last_name="Person",
            password=make_password('hrperson.123')
        )
        HEADERS = {
            "accept": "application/json",
            'Content-Type': 'application/json',
        }
        url = reverse('access')
        the_data = {"email": "hr@hr.com", "password": "hrperson.123"}
        response = self.client.post(url, the_data, headers=HEADERS, format='json')
        # print(response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_token_inaccurate_credentials(self):
        hruser = CustomUser.objects.create(
            email="hr@hr.com",
            first_name="Hr",
            last_name="Person",
            password=make_password('hrperson.123')
        )
        HEADERS = {
            "accept": "application/json",
            'Content-Type': 'application/json',
        }
        url = reverse('access')
        the_data = {"email": "hr@hr.com", "password": "h11rperson.123"}
        response = self.client.post(url, the_data, headers=HEADERS, format='json')
        # print(response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_candidate(self):
        hruser = CustomUser.objects.create(
            email="hr@hr.com",
            first_name="Hr",
            last_name="Person",
            password=make_password('hrperson.123')
        )
        HEADERS_FIRST = {
            "accept": "application/json",
            'Content-Type': 'application/json',
        }
        url = reverse('access')
        user_data = {"email": "hr@hr.com", "password": "hrperson.123"}
        response_access = self.client.post(url, user_data, headers=HEADERS_FIRST, format='json')
        tokken = json.loads(response_access.content.decode())["access"]

        client_data = {"name": "Petar", "email": "petar@123.com", "phone_number": "+35988888888"}

        HEADERS_TOKEN = {
            "accept": "application/json",
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {tokken}'
        }

        response = self.client.post('/api/candidates/', headers=HEADERS_TOKEN, data=client_data, format='json')
        self.assertEqual('{"id":1,"name":"Petar","email":"petar@123.com","phone_number":"+35988888888"}', response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_candidate_and_interview(self):
        hruser = CustomUser.objects.create(
            email="hr@hr.com",
            first_name="Hr",
            last_name="Person",
            password=make_password('hrperson.123')
        )
        HEADERS_FIRST = {
            "accept": "application/json",
            'Content-Type': 'application/json',
        }
        url = reverse('access')
        user_data = {"email": "hr@hr.com", "password": "hrperson.123"}
        response_access = self.client.post(url, user_data, headers=HEADERS_FIRST, format='json')
        tokken = json.loads(response_access.content.decode())["access"]

        candidate_data = {"name": "Petar", "email": "petar@123.com", "phone_number": "+35988888888"}

        HEADERS_TOKEN = {
            "accept": "application/json",
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {tokken}'
        }

        response_candidate = self.client.post('/api/candidates/', headers=HEADERS_TOKEN, data=candidate_data, format='json')
        candidate_id = json.loads(response_candidate.content.decode())['id']
        interview_data = {
          "interview_date": "2023-10-20T17:11:39.048Z",
          "interviewer": "Dimitar",
          "status": "Planned",
          "candidate": candidate_id
        }

        response = self.client.post('/api/interviews/',headers=HEADERS_TOKEN, data=interview_data, format='json')

        self.assertEqual(Interview.objects.count() ,1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_candidate_interview_and_feedback(self):
        hruser = CustomUser.objects.create(
            email="hr@hr.com",
            first_name="Hr",
            last_name="Person",
            password=make_password('hrperson.123')
        )
        HEADERS_FIRST = {
            "accept": "application/json",
            'Content-Type': 'application/json',
        }
        url = reverse('access')
        user_data = {"email": "hr@hr.com", "password": "hrperson.123"}
        response_access = self.client.post(url, user_data, headers=HEADERS_FIRST, format='json')
        tokken = json.loads(response_access.content.decode())["access"]

        candidate_data = {"name": "Petar", "email": "petar@123.com", "phone_number": "+35988888888"}

        HEADERS_TOKEN = {
            "accept": "application/json",
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {tokken}'
        }

        response_candidate = self.client.post('/api/candidates/', headers=HEADERS_TOKEN, data=candidate_data, format='json')
        candidate_id = json.loads(response_candidate.content.decode())['id']
        interview_data = {
          "interview_date": "2023-10-20T17:11:39.048Z",
          "interviewer": "Dimitar",
          "status": "Planned",
          "candidate": candidate_id
        }

        interview_response = self.client.post('/api/interviews/',headers=HEADERS_TOKEN, data=interview_data, format='json')
        interview_id = json.loads(interview_response.content.decode())['id']
        interviewer = json.loads(interview_response.content.decode())['interviewer']

        feedback_data = {
              "interviewer": interviewer,
              "feedback_text": "Very good first impression",
              "interview": interview_id
            }
        response = self.client.post('/api/feedback/', headers=HEADERS_TOKEN, data=feedback_data, format='json')

        self.assertEqual(Feedback.objects.count() ,1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_schedule(self):
        hruser = CustomUser.objects.create(
            email="hr@hr.com",
            first_name="Hr",
            last_name="Person",
            password=make_password('hrperson.123')
        )
        HEADERS_FIRST = {
            "accept": "application/json",
            'Content-Type': 'application/json',
        }
        url = reverse('access')
        user_data = {"email": "hr@hr.com", "password": "hrperson.123"}
        response_access = self.client.post(url, user_data, headers=HEADERS_FIRST, format='json')
        tokken = json.loads(response_access.content.decode())["access"]

        candidate_data = {"name": "Petar", "email": "petar@123.com", "phone_number": "+35988888888"}

        HEADERS_TOKEN = {
            "accept": "application/json",
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {tokken}'
        }

        response_candidate = self.client.post('/api/candidates/', headers=HEADERS_TOKEN, data=candidate_data, format='json')
        candidate_id = json.loads(response_candidate.content.decode())['id']
        interview_data = {
          "interview_date": "2023-10-20T17:11:39.048Z",
          "interviewer": "Dimitar",
          "status": "Scheduled",
          "candidate": candidate_id
        }

        response_interview = self.client.post('/api/interviews/',headers=HEADERS_TOKEN, data=interview_data, format='json')

        response = self.client.get('/api/schedule/', headers=HEADERS_TOKEN, format='json')
        items = len(json.loads(response.content.decode()))
        self.assertEqual( items,1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


