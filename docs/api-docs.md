# 📡 OpenVAFix API Documentation

## 📌 Overview
The OpenVAFix API allows users to submit VA forms for OCR processing and AI validation.

### 🔹 API Endpoints

#### 1️⃣ Process a VA Form
**`POST /api/process`**
- **Request:** Upload a PDF or image of the VA form
- **Response:** JSON with extracted text and structured data

#### 2️⃣ Get OCR Status
**`GET /api/status/{id}`**
- **Request:** Form submission ID
- **Response:** Status of OCR processing (pending, completed, error)

---
📌 **Future Features**
- Form validation with AI
- Integration with VA databases
- User authentication for secure submissions

