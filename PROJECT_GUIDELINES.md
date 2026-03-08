# Project: AI Autonomous Purchase Repository

## 1. Objective
Build a simple internal purchase system to manage products, prices, and orders. The system allows users to:
* Create, update, and delete products.
* Manage inventory levels and prices.
* Generate purchase orders.

## 2. Architecture & Tech Stack
* **Backend:** Python 3.12+ using **FastAPI**. Follows a RESTful API pattern.
* **Frontend:** **Angular** (latest version). Uses a component-based architecture.
* **Deployment:** Containerized with **Docker** and deployed on **Google Cloud Run**.
* **Database:** Currently in-memory (MVP), transitioning to PostgreSQL/Supabase.

## 3. Project Structure
* `/backend`: Contains the API logic. Main file: `main.py`.
* `/frontend`: Contains the Angular application.
* `/infra`: Terraform files for cloud resources.

## 4. Engineering Rules (Strict)
* **Language:** All code, comments, variables, and documentation MUST be in **English**.
* **Naming Convention:** * Python: `snake_case` for variables and functions.
    * Angular: `camelCase` for variables; `PascalCase` for classes.
* **Best Practices:** * Always include Type Hints in Python (`name: str`).
    * Use descriptive names for API endpoints (e.g., `/api/v1/products`).
    * Keep functions small and focused on a single responsibility.
* **Pre-change Protocol:** 1. Read `PROJECT_GUIDELINES.md` to confirm scope.
    2. Use `list_files` to locate relevant components.
    3. Read the target file to understand current implementation.
    4. Apply changes and verify syntax.
