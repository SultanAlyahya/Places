import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app
from models import setup_db, Togo, Went
import os


class TriviaTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client
        self.database_name = "Places"
        self.database_path = """postgres://postgres:14231423az@localhost:
        5432/places"""
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
            viewer_token = os.environ.get('VIEWER_TOKEN')
            admin_token = os.environ.get('ADMIN_TOKEN')
            self.admin_header = {'Authorization': 'Bearer ' + str(admin_token)}
            self.viewer_header = {'Authorization': 'Bearer ' + str(viewer_token)}

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

    def test_get_went(self):
        res = self.client().get('/went', headers=self.viewer_header)
        data = json.loads(res.data)

        self.assertTrue(data['went'])

    def test_get_went_404(self):
        res = self.client().get('/went/1', headers=self.viewer_header)

        self.assertEqual(res.status_code, 404)

    def test_post_togo(self):
        res = self.client().post('/togo', json={
                                                "location": "testT",
                                                "date": "2020/7/6",
                                                "description": "testT"
                                              },
                                 headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'yes')
        self.assertEqual(res.status_code, 201)

    def test_post_togo_500(self):
        res = self.client().post('/togo', json={
                                                "location": 1,
                                                "description": True
                                                },
                                 headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'no')
        self.assertEqual(res.status_code, 500)

    def test_post_went(self):
        res = self.client().post('/went', json={
                                                "location": "testT",
                                                "description": "testT"
                                                },
                                 headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'yes')

    def test_post_went_500(self):
        res = self.client().post('/togo', json={
                                                "location": True,
                                                "description": True
                                                },
                                 headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'no')
        self.assertEqual(res.status_code, 500)

    def test_patch_togo(self):
        res = self.client().patch('/togo/5', json={
                                                    "location": "testS",
                                                    "date": "2020/7/6",
                                                    "description": "testS"
                                                    },
                                  headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'yes')

    def test_patch_togo_500(self):
        res = self.client().patch('/togo/99', json={
                                                    "location": "testS",
                                                    "date": "2020/7/6",
                                                    "description": "testS"
                                                    },
                                  headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'no')

    def test_delete_togo(self):
        res = self.client().delete('/togo/7',  headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'yes')

    def test_delete_togo_404(self):
        res = self.client().delete('/togo/99',  headers=self.admin_header)
        data = json.loads(res.data)

        self.assertEqual(data['done'], 'no')

    def test_get_togo_adminRole(self):
        res = self.client().get('/togo', headers=self.admin_header)

        self.assertEqual(res.status_code, 401)

    def test_get_went_adminRole(self):
        res = self.client().get('/went', headers=self.admin_header)

        self.assertEqual(res.status_code, 401)

    def test_post_went_viewerRole(self):
        res = self.client().post('/went', json={
                                                "location": "testT",
                                                "description": "testT"
                                                },
                                 headers=self.viewer_header)

        self.assertEqual(res.status_code, 401)

    def test_patch_togo_viewerRole(self):
        res = self.client().patch('/togo/5', json={
                                                    "location": "testS",
                                                    "date": "2020/7/6",
                                                    "description": "testS"
                                                    },
                                  headers=self.viewer_header)

        self.assertEqual(res.status_code, 401)


if __name__ == "__main__":
    unittest.main()
