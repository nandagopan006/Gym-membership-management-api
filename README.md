<h1 align="center">
  🏋️‍♂️ Gym Membership Management System
</h1>


## 🎯 About the Project

Managing gym memberships, tracking payments, and enforcing role-based access can be highly disorganized when done manually. This API was built to provide a structured, automated, and secure foundation for any gym's backend infrastructure.

The project uses a scalable **App-Based Architecture**:
- **`accounts`**: Responsible for authentication logic (Signup, Login, Token generation/refresh).
- **`users`**: Manages the custom `User` model, role definitions (`OWNER`, `MEMBER`), and user profiles.
- **`payments`**: Handles business logic related to transactions (PENDING, PAID, FAILED).

---

## ✨ Features

- **Authentication:** Secure Login & Registration via JSON Web Tokens (JWT).
- **Role-Based Access Control:** Distinct roles (`OWNER`, `MEMBER`) to protect sensitive administrative endpoints.
- **Payment Management:** Track payments, link them to users, and monitor payment statuses.
- **Interactive Documentation:** Auto-generated Swagger UI and OpenAPI schemas.
- **Robust Security:** Password Hashing (PBKDF2), stateless JWT protection, and strict DRF serializer validation.

---

## 💻 Tech Stack

| Category | Technology |
| :--- | :--- |
| **Language** | Python 3.10+ |
| **Framework** | Django 4.2+ |
| **API Toolkit** | Django REST Framework (DRF) |
| **Database** | SQLite |
| **Authentication** | djangorestframework-simplejwt |
| **Documentation** | drf-spectacular (Swagger) |

---
