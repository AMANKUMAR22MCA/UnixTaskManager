const form = document.getElementById("auth-form");
const formTitle = document.getElementById("form-title");
const emailInput = document.getElementById("email");
const toggleLink = document.getElementById("toggle-link");
const toggleText = document.getElementById("toggle-text");
const userInfo = document.getElementById("user-info");

let isLogin = true;
const apiBase = "http://localhost:8000/api/auth";

// Toggle between Login and Register
toggleLink.onclick = () => {
  isLogin = !isLogin;
  formTitle.textContent = isLogin ? "Login" : "Register";
  emailInput.style.display = isLogin ? "none" : "block";
  toggleText.innerHTML = isLogin
    ? `Don't have an account? <span id="toggle-link">Register here</span>`
    : `Already have an account? <span id="toggle-link">Login here</span>`;
  document.getElementById("toggle-link").onclick = toggleLink.onclick;
};

// Submit handler
form.onsubmit = async (e) => {
  e.preventDefault();

  const payload = {
    username: document.getElementById("username").value,
    password: document.getElementById("password").value,
  };

  if (!isLogin) payload.email = document.getElementById("email").value;

  const endpoint = isLogin ? "/login/" : "/register/";

  try {
    const res = await fetch(`${apiBase}${endpoint}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const data = await res.json();
    if (res.ok && isLogin) {
      // Save the access token in localStorage or sessionStorage
      localStorage.setItem("access_token", data.access);
      getUser();
    } else {
      alert(data.message || JSON.stringify(data));
    }
  } catch (err) {
    alert("Error connecting to API");
  }
};

// Check if the user is already logged in on page load
document.addEventListener("DOMContentLoaded", async () => {
    const token = localStorage.getItem("access_token");
  
    if (token) {
      // If the token exists, fetch user data and show the authenticated UI
      getUser(); // This will fetch user info and display the logged-in state
    } else {
      // If there's no token, show the login form
      form.style.display = "block";
      toggleText.style.display = "block";
    }
  });

// Fetch user info after login
async function getUser() {
  const token = localStorage.getItem("access_token");

  if (!token) {
    alert("You are not logged in.");
    return;
  }

  const res = await fetch(`${apiBase}/me/`, {
    method: "GET",
    headers: {
      "Authorization": `Bearer ${token}`, // Send token in Authorization header
    },
  });

  const data = await res.json();

  if (res.ok) {
    form.style.display = "none";
    toggleText.style.display = "none";
    formTitle.textContent = "Welcome!";
    userInfo.style.display = "block";
    userInfo.innerHTML = `
      <p><strong>ID:</strong> ${data.id}</p>
      <p><strong>Username:</strong> ${data.username}</p>
      <p><strong>Email:</strong> ${data.email}</p>
    `;
    document.getElementById("task-manager").style.display = "block";
    loadTasks(); // ⬅️ Load tasks on login
    document.getElementById("logout-btn").style.display = "inline-block";  // Make the logout button visible

    // setInterval(loadTasks, 5000); // 🔁 refresh every 5 sec
  } else {
    alert("Login failed.");
  }
}

// Show task UI after login
async function loadTasks() {
  const filter = document.getElementById("task-filter").value;
  const url = new URL(`${apiBase.replace("/auth", "")}/tasks/`);
  if (filter) url.searchParams.append("state", filter);

  const token = localStorage.getItem("access_token");

  const res = await fetch(url.toString(), {
    method: "GET",
    headers: {
      "Authorization": `Bearer ${token}`, // Send token in Authorization header
    },
  });

  const tasks = await res.json();

  const list = document.getElementById("task-list");
  list.innerHTML = "";

  tasks.forEach(task => {
    const li = document.createElement("li");
    li.className = `task-${task.state}`;
    li.innerHTML = `
      <div>
        <strong>${task.name}</strong> – <em>${task.state}</em>
      </div>
      <button onclick="deleteTask(${task.id})">❌</button>
    `;
    list.appendChild(li);
  });
}

// Create a new task
async function createTask() {
  const name = document.getElementById("new-task-name").value.trim();
  if (!name) return alert("Enter task name.");

  const token = localStorage.getItem("access_token");

  const res = await fetch(`${apiBase.replace("/auth", "")}/tasks/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`, // Send token in Authorization header
    },
    body: JSON.stringify({ name }),
  });

  if (res.ok) {
    document.getElementById("new-task-name").value = "";
    loadTasks();
  } else {
    const data = await res.json();
    alert("Failed to create task: " + JSON.stringify(data));
  }
}

// Delete task
async function deleteTask(id) {
  if (!confirm("Delete this task?")) return;

  const token = localStorage.getItem("access_token");

  const res = await fetch(`${apiBase.replace("/auth", "")}/tasks/${id}/`, {
    method: "DELETE",
    headers: {
      "Authorization": `Bearer ${token}`, // Send token in Authorization header
    },
  });

  if (res.ok) loadTasks();
  else alert("Failed to delete task.");
}


// Add event listener for the logout button
document.getElementById("logout-btn").onclick = () => {
    // Remove the access token from localStorage
    localStorage.removeItem("access_token");
  
    // Redirect to the login page
    window.location.href = "http://127.0.0.1:5500/index.html";  // Adjust the URL to your login page
  };
  