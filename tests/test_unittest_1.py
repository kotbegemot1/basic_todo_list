import unittest

import service

TASK_ID = 1
TASK_TEXT = 'text text'
TASKS = {TASK_ID: TASK_TEXT}

class TestGetTask(unittest.TestCase):
	"""docstring for TestGetTask"""
	def test_id_exist(self):
		service.TASKS = TASKS
		task_id = TASK_ID
		result_task = service.get_task(task_id)
		self.assertEqual(result_task, TASK_TEXT)

	def test_id_doesnt_exist(self):
		service.TASKS = TASKS
		task_id = 2
		result_task = service.get_task(task_id)
		self.assertFalse(result_task)

if __name__ == '__main__':
	unittest.main()