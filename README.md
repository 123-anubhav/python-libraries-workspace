# Python Libraries Workspace & Demo Examples

This workspace features python demo examples utilizing **FastAPI**, **Requests**, **JSON**, **Streamlit UI**, and **REST APIs with MySQL database connectivity and CRUD operations**.

---

## Environment Setup and Project Execution Steps

Follow these steps to configure your project-specific virtual environment and run the applications.

### 1. Managing the Virtual Environment

* **Create the virtual environment:**
  ```bash
  python -m venv .venv
  ```
* **Activate the virtual environment:**
  ```bash
  .venv\Scripts\Activate
  ```
* **Deactivate the virtual environment:**
  ```bash
  deactivate
  ```

### 2. Installing Project Dependencies

After activation, install the required plugins mentioned in your `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 3. Running the FastAPI Application

Use the `uvicorn` server followed by the filename and the variable name where `FastAPI()` is defined:
```bash
uvicorn project_file:variable_name --reload
```
* **Example:**
  ```bash
  uvicorn main:app --reload
  ```

---

## Technical Notes & Reference Guide

### 💡 Core Notes
* Inside **FastAPI**, **Pydantic** is readily available out-of-the-box.
* Python includes **SQLite** by default within its standard library.
* The **Requests** library is used to develop consumer applications by initiating HTTP requests.

### 📦 Working with JSON (File vs. Non-File Concepts)

* **With Files:**
  * Use `dump()` to write data inside a file.
  * Use `load()` to read data from a file.
* **Without Files:**
  * Use `dumps()` to parse/write data into a string.
  * Use `loads()` to read/load data from a string.

> ⚠️ **Important JSON Note:** If you are retrieving data from a **Pydantic** model, you must use `model_dump()` to parse the data into a dictionary format first. After that, you can write it inside a file using `dump(parsed_data, file)`.

### ⚡ FastAPI & Uvicorn
* **FastAPI** relies on the **Uvicorn** ASGI server to run REST APIs.
* **FastAPI** internally incorporates **Pydantic** to manage request data validation and schema handling.

### 🎈 Streamlit UI
* **Streamlit** is used for quick prototyping, classroom demos, or by AI developers to build user interfaces rapidly.
* It removes the necessity of having advanced front-end knowledge in technologies like **HTML**, **CSS**, **Angular**, or **React**.

### 📄 Requirements File (`requirements.txt`)
* Used to define your specific project plugin dependencies.
* **Example:**
  ```text
  fastapi
  uvicorn
  pydantic
  ```
