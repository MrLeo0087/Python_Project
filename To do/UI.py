import streamlit as st
import os

TASK_FILE = "Task.txt"
COMPLETE_FILE = "Complete.txt"

# --- Helper functions ---
def read_tasks(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        return [line.strip().split(". ", 1)[-1] for line in f if line.strip()]

def write_tasks(tasks, filename):
    with open(filename, "w") as f:
        for i, task in enumerate(tasks, 1):
            f.write(f"{i}. {task}\n")

def append_task(task, filename):
    tasks = read_tasks(filename)
    tasks.append(task)
    write_tasks(tasks, filename)

# --- Streamlit App ---
st.title("📝 Task Manager")

menu = ["Add Task", "Remove Task", "Modify Task", "Complete Task", "View Tasks"]
choice = st.sidebar.radio("Navigation", menu)

if choice == "Add Task":
    st.subheader("➕ Add New Task")
    new_task = st.text_input("Enter Task:")
    if st.button("Add"):
        if new_task.strip():
            append_task(new_task, TASK_FILE)
            st.success(f"Task '{new_task}' added successfully!")
        else:
            st.warning("Task cannot be empty!")

elif choice == "Remove Task":
    st.subheader("❌ Remove Task")
    tasks = read_tasks(TASK_FILE)
    if tasks:
        task_to_remove = st.selectbox("Select task to remove:", tasks)
        if st.button("Remove"):
            tasks = [t for t in tasks if t != task_to_remove]
            write_tasks(tasks, TASK_FILE)
            st.success(f"Task '{task_to_remove}' removed!")
    else:
        st.info("No tasks available.")

elif choice == "Modify Task":
    st.subheader("✏️ Modify Task")
    tasks = read_tasks(TASK_FILE)
    if tasks:
        old_task = st.selectbox("Select task to modify:", tasks)
        new_task = st.text_input("Enter new task:")
        if st.button("Modify"):
            updated = [new_task if t == old_task else t for t in tasks]
            write_tasks(updated, TASK_FILE)
            st.success(f"Task '{old_task}' updated to '{new_task}'")
    else:
        st.info("No tasks available.")

elif choice == "Complete Task":
    st.subheader("✅ Complete Task")
    tasks = read_tasks(TASK_FILE)
    if tasks:
        task_to_complete = st.selectbox("Select task to complete:", tasks)
        if st.button("Mark Complete"):
            append_task(task_to_complete, COMPLETE_FILE)
            tasks = [t for t in tasks if t != task_to_complete]
            write_tasks(tasks, TASK_FILE)
            st.success(f"Task '{task_to_complete}' marked as complete!")
    else:
        st.info("No tasks available.")

elif choice == "View Tasks":
    st.subheader("📌 View Tasks")
    tasks = read_tasks(TASK_FILE)
    completed = read_tasks(COMPLETE_FILE)

    st.write("### 📋 Remaining Tasks")
    if tasks:
        for t in tasks:
            st.write(f"- {t}")
    else:
        st.info("No remaining tasks.")

    st.write("### ✅ Completed Tasks")
    if completed:
        for c in completed:
            st.write(f"- {c}")
    else:
        st.info("No completed tasks.")
