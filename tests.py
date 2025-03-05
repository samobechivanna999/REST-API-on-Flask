import unittest
import requests

BASE_URL = "http://localhost:5000"

class TestTodoAPI(unittest.TestCase):
    def test_01_get_all_tasks(self):
        """Проверяет получение списка всех задач."""
        response = requests.get(f"{BASE_URL}/tasks")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_02_get_task_by_id(self):
        """Создает задачу и получает её по ID."""
        new_task = {"title": "Test Task", "description": "Testing get by ID"}
        create_response = requests.post(f"{BASE_URL}/tasks", json=new_task)
        self.assertEqual(create_response.status_code, 201)
        task_id = create_response.json()["id"]

        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], task_id)

    def test_03_create_task(self):
        """Создает новую задачу."""
        new_task = {"title": "New Task", "description": "This is a new task"}
        response = requests.post(f"{BASE_URL}/tasks", json=new_task)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["title"], "New Task")

    def test_04_update_task(self):
        """Создает задачу и затем обновляет её."""
        new_task = {"title": "Old Task", "description": "Old description"}
        create_response = requests.post(f"{BASE_URL}/tasks", json=new_task)
        self.assertEqual(create_response.status_code, 201)
        task_id = create_response.json()["id"]

        updated_task = {"title": "Updated Task", "description": "Updated description"}
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=updated_task)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["title"], "Updated Task")

    def test_05_delete_task(self):
        """Создает задачу, затем удаляет её и проверяет, что её больше нет."""
        new_task = {"title": "Task to Delete", "description": "To be deleted"}
        create_response = requests.post(f"{BASE_URL}/tasks", json=new_task)
        self.assertEqual(create_response.status_code, 201)
        task_id = create_response.json()["id"]

        delete_response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        self.assertEqual(delete_response.status_code, 200)
        self.assertEqual(delete_response.json()["result"], True)

        # Проверяем, что задача удалена
        get_response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        self.assertEqual(get_response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
