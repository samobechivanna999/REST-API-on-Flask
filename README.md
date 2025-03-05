# Создание REST API на Flask для управления списком задач (To-Do List)

# Цель

Разработать REST API на Flask, которое поддерживает CRUD операции (Create, Read, Update, Delete) для управления списком задач. API должно быть протестировано с использованием модуля unittest.

# Задача

1) Поддержка следующих ручек:  
```
GET /tasks — возвращает список всех задач.  
GET /tasks/<int:task_id> — возвращает задачу по её ID.  
POST /tasks — создаёт новую задачу (тело запроса должно содержать title и description).  
PUT /tasks/<int:task_id> — обновляет задачу по её ID.  
DELETE /tasks/<int:task_id> — удаляет задачу по её ID.  
```
2) Создание unit тестов

