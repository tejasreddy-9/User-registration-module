# User Registration Module - FastAPI Based System

## Overview

This User Registration Module is built using Python’s FastAPI framework and integrates MongoDB and MySQL as backends. It provides secure and structured endpoints for user registration, login, password management, and logout functionality. Key features include JWT authentication, detailed logging using Python’s `logging` module, and custom exception handling. Postman collections are used to test and demonstrate API usage.

---

## Tech Stack

- **Backend Framework**: FastAPI
- **Databases**: MongoDB or MySQL
- **Models**: Pydantic for Request and Response validation
- **Authentication**: JWT Token
- **Logging**: Python’s `logging` module with log file output
- **Security**: Password complexity enforcement, expiry, and reuse prevention
- **Tools**: Postman for API testing
- **Enhancements**: Decorators, Lambda functions where needed

---

## Functional Modules

### 1. Register

- Accepts:
  - **Username**: Email or Phone Number (Unique, Non-empty)
  - **First Name**, **Last Name**
  - **Date of Birth**, **Date of Joining**
  - **Address**, **Comments**, **Active Status**
- **Validation**:
  - No duplicate email or phone number
  - Strong password enforcement (8–20 chars, must include uppercase, lowercase, numbers, special chars)
- Password expiry every 30 days
- Log each registration attempt

### 2. Login

- Login using **Email/Phone** and **Password**
- If password expired: force user to change password and re-login
- JWT token generation
- Log successful and failed login attempts
- Response Time: `{Execution Time : 3 ms}`

### 3. Change Password

- Logged-in users only
- Old and new password required
- Password reuse not allowed
- Success/Failure logged with timestamp

### 4. Forget Password

- Max 3 requests allowed within password reset window
- Sends email with a secure reset link (valid for 24 hours only)
- Link invalid after expiry or successful password reset
- Reset attempt is logged

### 5. Logout

- Invalidates JWT token (Blacklisting / Token expiration)
- Ensures clean logout process

---

## Security Measures

- JWT Authentication to ensure session-based access
- Password policy:
  - Min 8 characters, Max 20
  - At least one uppercase, lowercase, number, and special character
  - Prevents reuse
  - Mandatory change after 30 days
- Custom exceptions for validation errors
- Logging of every action (register, login, logout, error)

---

## 🎯 Why Use This Approach?

Using FastAPI gives the benefit of high-speed asynchronous API development with automatic documentation (Swagger/OpenAPI). JWT ensures stateless, scalable authentication, while Pydantic enforces data validation. Combining MongoDB (for NoSQL flexibility) and MySQL (for structured relational data) makes the system adaptable. Logging and error handling enhance debugging and audit trails.

---

## When to Use

Use this system when building:

- A secure and scalable user management backend
- A RESTful API requiring email/phone login
- Systems where compliance, logging, and security are critical
- Applications needing a combination of SQL and NoSQL data stores

---

## Advantages

- High performance with FastAPI
- Clean and structured validation using Pydantic
- Custom error responses
- JWT ensures secure and scalable auth flow
- Activity logging improves maintainability and traceability
- Modular, extensible design using decorators and lambda expressions

---

## Common Interview Questions

1. What is FastAPI and how is it different from Flask?
2. How does JWT token-based authentication work?
3. Why use Pydantic in FastAPI? How is validation handled?
4. How do you ensure password complexity and expiration in APIs?
5. How would you send email securely from a FastAPI backend?
6. How do you log API requests/responses securely?
7. How do you prevent password reuse in authentication systems?
8. What are the advantages of using both MongoDB and MySQL in the same project?
9. How would you design a password reset system with token expiration?
10. How would you handle failed login attempts or brute-force attacks?

---

