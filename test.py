import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app
from models import setup_db, Togo, Went


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.database_name = "Places"
        self.database_path = "postgres://postgres:14231423az@localhost:5432/places"
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
            self.admin_header = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlNWZ2c5MEhMTTRRQ0xhanpNQ0dpdSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtc3VsdGFuLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjA1ZDMxZjJlYjMwMzAwMTljODQ3NWEiLCJhdWQiOiJwbGFjZSIsImlhdCI6MTU5NDI0NTcyMywiZXhwIjoxNTk0MjUyOTIzLCJhenAiOiJiRnozMFQ3WEUxaW1WZE12TlpicU9NRUx5OWRyY2RpTCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmxvY2F0aW9uIiwicGF0Y2g6bG9jYXRpb24iLCJwYXRjaDpwbGFjZSIsInBvc3Q6bG9jYXRpb24iLCJwb3N0OndlbnQiXX0.wVagDfc3maqX3pKCVHp6JliyDVlxgP1743FoeBW_OZ_6Hy0tNCgdOww-ixqaFJ8AeaVqoxes634KhU1vD28UwMx2_k-BmrIvpVxF-SqVdrNDJP81OWtTmWJvl5BrJAnyE517ZMtJ_Hl_YA_aektvZ7dftO9j5551XqNEK2iJkgEHPqxAxueoLz7WyPEVgA0Ytyz2BSOg3JRDsoZmWFCo8jMAhc0dXNwfBVczl5kPOKm1UhqgL3q25ReqrbWCIUvHSTps0cVCRiIsG0XWByXuRcjviryaRJvj4zstXl67xrcVNe7zKUvrYcicW-PIiaVpsn9y_7HKBp1c-gI_7W7VjQ'}
            self.viewer_header = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlNWZ2c5MEhMTTRRQ0xhanpNQ0dpdSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtc3VsdGFuLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjA1ZGM5NGExNWI3YjAwMTM2MWYzM2QiLCJhdWQiOiJwbGFjZSIsImlhdCI6MTU5NDI0NDA0NSwiZXhwIjoxNTk0MjUxMjQ1LCJhenAiOiJiRnozMFQ3WEUxaW1WZE12TlpicU9NRUx5OWRyY2RpTCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmxvY2F0aW9uIiwiZ2V0OndlbnQiXX0.ex9CvThjX7jw0-zfRsMnct06z8LdQGIkM8Bb011Ggln6JEX-1nnaptsl3DmSp7rBv1SeAlelUFwfa0gIghgPCPzamBWU6NPVWvS921WPrRBeQfEBXBTB-lulKxozKT18Dhn3s-mdhymTBEG6uQRDqebyhiNTEHouimLPCzMO_W6eKxLoYQ-BLJ67SiS4Tq-ThAAwJD6US1n6KhS2umt1yD6OFXapidIym0tCOVq_IOw3dDaAoo1OjcPUxOPf7rjZt9s5Xh9PzDPTAL84qX7vqFwkAKyFjMaK3gfl5fH7_ysTjNTeEoUQb4umtDMRgp7U5IHwvdqEIAeYDZbm-bIqUw'}
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_togo(self):
        res = self.client().get('/togo', headers=self.viewer_header)
        data = json.loads(res.data)

        self.assertTrue(data['togos'])

    def test_get_togo_405(self):
        res = self.client().get('/togo/1', headers=self.viewer_header)

        self.assertEqual(res.status_code, 405)
#================================================
    def test_get_went(self):
        res = self.client().get('/went', headers=self.viewer_header)
        data = json.loads(res.data)

        self.assertTrue(data['went'])

    def test_get_went_404(self):
        res = self.client().get('/went/1', headers=self.viewer_header)

        self.assertEqual(res.status_code, 404)
#================================================
    def test_post_togo(self):
        res = self.client().post('/togo', json={"location": "testT", "date": "2020/7/6", "description": "testT"}, headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'yes')
        self.assertEqual(res.status_code, 201)

    def test_post_togo_500(self):
        res = self.client().post('/togo', json={"location":1, "description": True}, headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'no')
        self.assertEqual(res.status_code, 500)
#================================================
    def test_post_went(self):
        res = self.client().post('/went', json={"location": "testT", "description": "testT"}, headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'yes')

    def test_post_went_500(self):
        res = self.client().post('/togo', json={"location":True, "description": True}, headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'no')
        self.assertEqual(res.status_code, 500)
#================================================
    def test_patch_togo(self):
        res = self.client().patch('/togo/5', json={"location": "testS", "date": "2020/7/6", "description": "testS"}, headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'yes')

    def test_patch_togo_500(self):
        res = self.client().patch('/togo/99', json={"location": "testS", "date": "2020/7/6", "description": "testS"}, headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'no')
#=================================================
    def test_delete_togo(self):
        res = self.client().delete('/togo/7',  headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'yes')

    def test_delete_togo_404(self):
        res = self.client().delete('/togo/99',  headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'no')
#=======================================================
    def test_get_togo_adminRole(self):
        res = self.client().get('/togo', headers=self.admin_header)
       
        self.assertEqual(res.status_code, 401)
    
    def test_get_went_adminRole(self):
        res = self.client().get('/went', headers=self.admin_header)
        
        self.assertEqual(res.status_code, 401)
#=======================================================   
    def test_post_went_viewerRole(self):
        res = self.client().post('/went', json={"location": "testT", "description": "testT"}, headers=self.viewer_header)

        self.assertEqual(res.status_code, 401)

    def test_patch_togo_viewerRole(self):
        res = self.client().patch('/togo/5', json={"location": "testS", "date": "2020/7/6", "description": "testS"}, headers=self.viewer_header)

        self.assertEqual(res.status_code, 401)
    # def test_get_questions(self):
    #     res = self.client().get('/questions?page=1')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertTrue(data['questions'])
    #     self.assertTrue(data['categories'])
    #     self.assertEqual(len(data['questions']), 10)
    #     self.assertLessEqual(data['totalQuestions'], 30)
    #     self.assertGreater(data['totalQuestions'], 20)

    # def test_404_get_questions(self):
    #     res = self.client().get('/questions?page=55')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['totalQuestions'], 0)

    # def test_delete_question(self):
    #     res = self.client().delete('/questions/55')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['question'], 'deleted')
    
    # def test_500_delete_question(self):
    #     res = self.client().delete('/questions/1000')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 500)
    #     self.assertEqual(data['question'], 'not deleted')

    # def test_create_question(self):
    #     res = self.client().post('/questions', json={'question':'test', 'answer':'test', 'difficulty':3, 'category':1}) 
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 201)
    #     self.assertEqual(data['done'], 'yes')

    # def test_500_create_question(self):
    #     res = self.client().post('/questions', json={'question':'test', 'answer':'test', 'difficulty':6, 'category':1}) 
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 500)
    #     self.assertTrue(data['done'])

    # def test_search(self):
    #     res = self.client().post('/searchForQuestions', json={'searchTerm':'title'}) 
    #     data = json.loads(res.data)
    #     print(data['questions'][0])
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(len(data['questions']), 1)
       
    # def test_404_search(self):
    #     res = self.client().post('/searchForQuestions', json={'searchTerm':'qwertyu'}) 
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['totalQuestions'], 0)

    # def test_questionsCategory(self):
    #     res = self.client().get('/categories/1/questions') 
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertTrue(data['questions'])
    #     self.assertGreater(data['totalQuestions'], 0)

    # def test_500_questionsCategory(self):
    #     res = self.client().get('/categories/5/questions') 
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 500)
    #     self.assertEqual(data['error'], 'server problem')
    
    # def test_categoryQuestions(self):
    #     res = self.client().post('/quizzes', json={'previous_questions': [], 'quiz_category':{'id':1}}) 
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertTrue(data['question'])
    #     self.assertEqual(data['question']['answer'], 'adsfg')
    #     self.assertNotEqual(data['question']['answer'], 'aaaa')

    # def test_500_categoryQuestions(self):
    #     res = self.client().post('/quizzes', json={'previous_questions': [], 'quiz_category':{'id':3}}) 
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['error'], 'there is no questions')


    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()