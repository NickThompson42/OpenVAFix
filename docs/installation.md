# 🚀 OpenVAFix Installation Guide

## 📌 Prerequisites
Ensure you have the following dependencies installed:

### **1️⃣ System Requirements**
- **OS:** Ubuntu 20.04+ / macOS / Windows (WSL recommended)
- **Python:** 3.8+
- **Docker & Docker Compose**
- **Node.js & npm** (for frontend development)
- **Tesseract OCR** (for text extraction)

### **2️⃣ Install Dependencies**
#### **🔹 Linux (Ubuntu/Debian)**
```sh
sudo apt update && sudo apt install -y \
    python3 python3-pip python3-venv \
    docker.io docker-compose \
    tesseract-ocr tesseract-ocr-eng \
    nodejs npm
```

#### **🔹 macOS**
```sh
brew install python node tesseract docker
```

#### **🔹 Windows (WSL Recommended)**
1. Install [WSL2](https://docs.microsoft.com/en-us/windows/wsl/install)
2. Install dependencies:
   ```sh
   sudo apt update && sudo apt install -y \
       python3 python3-pip python3-venv \
       docker.io docker-compose \
       tesseract-ocr tesseract-ocr-eng \
       nodejs npm
   ```

---

## 🏗️ Setting Up the Backend
```sh
# Clone the repository
git clone https://github.com/yourusername/OpenVAFix.git
cd OpenVAFix

# Create a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt
```

---

## 🖼️ Running OCR Processing Locally
```sh
python scripts/ocr_processor.py sample_form.png
```

---

## 🖥️ Running with Docker
```sh
docker build -t openvafix .
docker run -it --rm openvafix
```

---

## 🌍 Running the Web Frontend
```sh
cd frontend
npm install
npm run dev
```
- Open `http://localhost:3000` in your browser.

---

## 🚀 Deployment with Kubernetes
```sh
kubectl apply -f deployment/k8s/
```

---

## 🛠️ Troubleshooting
- **Tesseract Not Found?** Run:
  ```sh
  which tesseract
  ```
- **Docker Permission Issues?** Try:
  ```sh
  sudo usermod -aG docker $USER && newgrp docker
  ```
- **Errors?** Check logs:
  ```sh
  docker logs <container_id>
  ```

---

## 🎯 Next Steps
- Read [`docs/strategy.md`](strategy.md) for technical details.
- Pick an open issue from [`docs/contribution.md`](contribution.md).

✅ *Open-source automation to fix VA inefficiencies.* 🚀
