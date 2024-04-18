document.addEventListener('DOMContentLoaded', function() {
    loadTodos();
});

function loadTodos() {
    fetch('https://jsonplaceholder.typicode.com/todos')
        .then(response => response.json())
        .then(data => {
            const todoList = document.getElementById('todoList');
            todoList.innerHTML = '';
            data.forEach(todo => {
                const li = document.createElement('li');
                li.textContent = todo.title;
                todoList.appendChild(li);
            });
        })
        .catch(error => console.error('Error fetching todos:', error));
}

function addTodo() {
    const todoInput = document.getElementById('todoInput');
    const newTodo = todoInput.value.trim();
    if (newTodo !== '') {
        fetch('https://jsonplaceholder.typicode.com/todos', {
            method: 'POST',
            body: JSON.stringify({
                title: newTodo,
                completed: false
            }),
            headers: {
                'Content-type': 'application/json; charset=UTF-8',
            },
        })
        .then(response => response.json())
        .then(() => {
            todoInput.value = '';
            loadTodos();
        })
        .catch(error => console.error('Error adding todo:', error));
    }
}
