import unittest
import datetime
import sys


import service

TASK_ID = 1
TASK_TEXT = "text text"
TASKS = {TASK_ID: TASK_TEXT}

class TestGetTask(unittest.TestCase):

    def setUp(self):
        print(1)

    def test_id_exists(self):
        service.TASKS = TASKS
        task_id = TASK_ID
        result_task = service.get_task(task_id)
        self.assertEqual(result_task, TASK_TEXT)
    
    def test_id_doesnt_exist(self):
        service.TASKS = TASKS
        task_id = 2
        result_task = service.get_task(task_id)
        self.assertFalse(result_task)

    def tearDown(self):
        print(2)

class GetAllTasks(unittest.TestCase):
    def test_get_all_tasks_empty(self):
        service.TASKS = {}
        all_tasks = service.get_all_tasks()
        self.assertEqual(all_tasks, {})
    
    def test_get_all_tasks(self):
        service.TASKS = TASKS
        all_tasks = service.get_all_tasks()
        self.assertEqual(all_tasks, TASKS)

class CreateTask(unittest.TestCase):
    def test_create_task_success(self):
        date = (
            datetime.datetime.now() + 
            datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
        text = TASK_TEXT
        task = service.create_task(date, text)
        self.assertTrue(task)
    
    def test_create_task_in_past(self):
        date = (
            datetime.datetime.now() - 
            datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
        text = TASK_TEXT
        task = service.create_task(date, text)
        self.assertIsNone(task)

class TestSkippedCase(unittest.TestCase):
    
    @unittest.skip("this test is skipped for a reason")
    def test_plain_skip(self):
        self.fail("some reason")

class TextxFailsCase(unittest.TestCase):
    
    @unittest.expectedFailure
    def test_expected_failure(self):
        self.fail("this test should fail")

class TestSkippedConditionalCase(unittest.TestCase):
    @unittest.skipIf(sys.version.startswith("2"),"supported only in newer Python versions")
    def test_test_scip_if(self):
        self.assertIsNone(None)
        

    @unittest.skipUnless(sys.platform.startswith("win"), "this test runs only on Win")
    def test_windows_support(self):
        self.assertIsNone(None)



if __name__ == '__main__':
    unittest.main()