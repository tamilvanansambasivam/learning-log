Let's walk through **every micro-step** to build a basic **To-Do app** using just **HTML and JavaScript** (no frameworks). This app will let you:

- Add a task
- View tasks
- Mark tasks as done
- Delete tasks

We'll build this from scratch, and I’ll explain **why** we do every single step.

---

## 🧠 PHASE 1: PLAN THE FEATURES

Before writing any code, understand what we want to do.

### 🔍 Goal:

We want an app where users can:

1. Type in a task
2. Click "Add"
3. See the task in a list
4. Mark it as done (optional)
5. Delete it (optional)

---

## 🧱 PHASE 2: SETTING UP THE HTML STRUCTURE

HTML is for **structure** only — it’s what we see in the browser.

---

### ✅ STEP 1: Create a new HTML file

**Why?**
We need a file to hold our app’s structure.

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
  <head>
    <title>To-Do App</title>
  </head>
  <body></body>
</html>
```

---

### ✅ STEP 2: Add a heading and input field

**Why?**
We need a place for the user to type a new task and a button to submit it.

```html
<h1>My To-Do List</h1>

<input type="text" id="taskInput" placeholder="Enter a new task" />
<button id="addTaskBtn">Add</button>
```

---

### ✅ STEP 3: Add a list container

**Why?**
We need a place to display the tasks — an unordered list (`<ul>`) is perfect.

```html
<ul id="taskList"></ul>
```

---

At this point, your full HTML looks like:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>To-Do App</title>
  </head>
  <body>
    <h1>My To-Do List</h1>
    <input type="text" id="taskInput" placeholder="Enter a new task" />
    <button id="addTaskBtn">Add</button>
    <ul id="taskList"></ul>

    <script src="script.js"></script>
  </body>
</html>
```

---

## ⚙️ PHASE 3: ADDING FUNCTIONALITY WITH JAVASCRIPT

Now we add behavior. JavaScript will let us **respond to button clicks** and **manipulate the DOM**.

---

### ✅ STEP 4: Create a new JS file

**Why?**
To keep logic separate from structure.

Create a file called `script.js` in the same folder.

---

### ✅ STEP 5: Access DOM elements

**Why?**
We need to grab the input, button, and task list so we can work with them.

```js
// script.js
const taskInput = document.getElementById("taskInput");
const addTaskBtn = document.getElementById("addTaskBtn");
const taskList = document.getElementById("taskList");
```

---

### ✅ STEP 6: Add a click event listener

**Why?**
We want something to happen when the "Add" button is clicked.

```js
addTaskBtn.addEventListener("click", function () {
  const taskText = taskInput.value;
  // More code coming here!
});
```

---

### ✅ STEP 7: Check for empty input

**Why?**
We don’t want to add empty tasks.

```js
addTaskBtn.addEventListener("click", function () {
  const taskText = taskInput.value.trim();
  if (taskText === "") {
    alert("Please enter a task!");
    return;
  }
  // More code coming here!
});
```

---

### ✅ STEP 8: Create a new `<li>` element

**Why?**
To show the new task inside the `<ul>` list.

```js
const li = document.createElement("li");
li.textContent = taskText;
```

---

### ✅ STEP 9: Add a "Delete" button

**Why?**
So we can remove tasks later.

```js
const deleteBtn = document.createElement("button");
deleteBtn.textContent = "Delete";
```

---

### ✅ STEP 10: Attach delete function to the button

**Why?**
We want it to actually remove the task when clicked.

```js
deleteBtn.addEventListener("click", function () {
  taskList.removeChild(li);
});
```

---

### ✅ STEP 11: Optional: Add "Done" toggle

**Why?**
To mark tasks as completed (visually).

```js
li.addEventListener("click", function () {
  li.classList.toggle("done");
});
```

---

### ✅ STEP 12: Put the button inside the `<li>`, and add `<li>` to the list

**Why?**
To visually keep the button next to the task.

```js
li.appendChild(deleteBtn);
taskList.appendChild(li);
```

---

### ✅ STEP 13: Clear the input field

**Why?**
For better user experience — the field should be blank after adding a task.

```js
taskInput.value = "";
```

---

### ✅ STEP 14: Add CSS for `.done` (optional)

**Why?**
So done tasks look different (e.g., crossed out)

Add this to a `<style>` tag in your HTML:

```html
<style>
  .done {
    text-decoration: line-through;
    color: gray;
  }
</style>
```

---

## ✅ Final `script.js`

```js
const taskInput = document.getElementById("taskInput");
const addTaskBtn = document.getElementById("addTaskBtn");
const taskList = document.getElementById("taskList");

addTaskBtn.addEventListener("click", function () {
  const taskText = taskInput.value.trim();
  if (taskText === "") {
    alert("Please enter a task!");
    return;
  }

  const li = document.createElement("li");
  li.textContent = taskText;

  const deleteBtn = document.createElement("button");
  deleteBtn.textContent = "Delete";

  deleteBtn.addEventListener("click", function () {
    taskList.removeChild(li);
  });

  li.addEventListener("click", function () {
    li.classList.toggle("done");
  });

  li.appendChild(deleteBtn);
  taskList.appendChild(li);

  taskInput.value = "";
});
```

---

## ✅ Final Result

When you open `index.html` in a browser:

- You can type a task
- Click "Add"
- See the task appear with a delete button
- Click on the task to mark it done
- Click "Delete" to remove it

---

## ✅ NEXT POSSIBLE IMPROVEMENTS

- Save tasks in localStorage
- Add due dates
- Drag-and-drop ordering
- Edit task names

---
