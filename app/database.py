from random import randint

from todo import Todo


class Database:
    def __init__(self):
        self.todos = {}
        self._last_todo_key = 0
    
    def add_todos(self, data):
        for item in data:
            todo_ = Todo(data[item]['text'], data[item]['time'])
            self.todos[self._last_todo_key] = todo_
            self._last_todo_key += 1

    def add_todo(self, todo):
        self._last_todo_key += 1
        self.todos[self._last_todo_key] = todo
        return self._last_todo_key
    
    def random_todo(self):
        rand_int = randint(0, self._last_todo_key-1)
        todo_ = self.get_todo(rand_int)
        return todo_

    def delete_todo(self, todo_key):
        if todo_key in self.todos:
            del self.todos[todo_key]

    def get_todo(self, todo_key):
        todo = self.todos.get(todo_key)
        if todo is None:
            return None
        todo_ = Todo(todo.text, time=todo.time)
        return todo_

    def get_todos(self):
        todos = []
        for todo_key, todo in self.todos.items():
            todo_ = Todo(todo.text, time=todo.time)
            todos.append((todo_key, todo_))
        return todos