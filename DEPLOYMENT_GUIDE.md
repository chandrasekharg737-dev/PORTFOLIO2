# 🚀 Ultimate Render Deployment Guide

If your previous deployment failed, follow this guide carefully. It contains fixes for common "Build Failed" or "Runtime Error" issues.

## 🛠️ Step 0: Fix the Files Locally
I have already updated these files for you:
1.  **`requirements.txt`**: Now uses `pypdf` (modern library) and includes `gunicorn`.
2.  **`app.py`**: Now uses Linux-compatible paths (`app.root_path`).

## 📤 Step 1: Push Changes to GitHub
Open your terminal in the `PORTFOLIO2` folder and run:
```bash
git add .
git commit -m "Fix deployment dependencies and paths"
git push origin main
```

---

## 🌐 Step 2: Configure Render Correctly
1. Go to your **Web Service** on Render.
2. Go to the **Settings** tab:
   - **Build Command**: `pip install -r requirements.txt` (Verify it's exactly this)
   - **Start Command**: `gunicorn app:app` (Verify it's exactly this)
3. Go to the **Environment** tab and ensure these are added:
   - `GROQ_API_KEY`: `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`
   - `PYTHON_VERSION`: `3.10.0` (Optional, but often helps)

---

## 🔍 Step 3: Troubleshooting (If it fails again)

### **Case 1: Build Failed**
- **Symptoms**: Logs say "Command failed" or "Could not find a version...".
- **Solution**: Check the **Deploy Logs** in Render. Look for the red text. It usually means a library in `requirements.txt` is missing or has a typo. I have updated yours to be very standard.

### **Case 2: Start Failed / Application Error**
- **Symptoms**: Logs say "gunicorn: command not found" or "ModuleNotFoundError: No module named 'app'".
- **Solution**: 
  1. Ensure `app.py` is in the **root** folder (not inside a subfolder).
  2. Ensure your Start Command is exactly `gunicorn app:app`.
  3. Ensure `gunicorn` is listed in your `requirements.txt`.

### **Case 3: Chatbot says "API Error"**
- **Symptoms**: Website loads, but chat doesn't work.
- **Solution**: Your `GROQ_API_KEY` is missing or incorrect in the **Environment** tab on Render.

---

## 💡 Pro Tip: Check the Logs
If it fails, click on the **Events** or **Logs** tab in Render. **Copy the last 20 lines of the error** and paste them here. I can tell you exactly what's wrong if I see the error!
