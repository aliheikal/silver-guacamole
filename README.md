
# 🧠 Silver Guacamole: End-to-End Minimal MLOps with GitHub Actions

This repository demonstrates a complete **MLOps workflow** using real tools in a simple, local-first project:

- ✅ Train an ML model using ZenML pipelines
- 📊 Track experiments with MLflow
- 🐳 Package model as a Dockerized FastAPI API
- 🔁 Run CI/CD with GitHub Actions
- 💬 Comment model results on PRs using CML
- 🧪 Simulate inference monitoring via logs

---

## 🔧 Tools Used

| Tool        | Purpose                                      |
|-------------|----------------------------------------------|
| ZenML       | Manages ML pipelines                         |
| MLflow      | Logs metrics, parameters, and models         |
| FastAPI     | Serves the model via REST API                |
| Docker      | Packages inference into a portable image     |
| GitHub Actions | Automates training, packaging, and testing |
| CML         | Posts results/logs as PR comments            |

---

## 📁 Project Structure

```
.
├── run_pipeline.py               # Runs ZenML training pipeline
├── train.py                      # Simple sklearn trainer (manual)
├── generate_report.py           # Extracts metrics/logs for markdown report
├── Dockerfile                   # FastAPI container
├── inference_api/
│   ├── app.py                   # API with logging
│   └── model.pkl                # Saved model (output)
├── zenml_pipeline/
│   ├── pipeline.py              # Pipeline definition
│   └── steps/train_step.py      # Training step (logs to MLflow)
└── .github/workflows/
    └── train-package-deploy.yml # Full CI/CD automation
```

---

## 🚀 Local Setup

```bash
pip install -r requirements.txt
zenml init

# Register local stack components
zenml orchestrator register local_orchestrator --flavor=local || true
zenml experiment-tracker register mlflow_tracker --flavor=mlflow || true
zenml artifact-store register local_store --flavor=local --path=$(pwd)/artifacts || true

# Combine into a local stack
zenml stack register local_stack -o local_orchestrator -a local_store -e mlflow_tracker || true
zenml stack set local_stack
```

---

## ▶️ Run Training Locally

```bash
python run_pipeline.py
```

This will:
- Train a Logistic Regression model on the Iris dataset
- Log metrics (`accuracy`, `solver`, `penalty`) to MLflow
- Save the model as `inference_api/model.pkl`

---

## 🔬 Run Inference API Locally

```bash
docker build -t local-model-api .
docker run -p 8080:8080 local-model-api
```

Visit: [http://localhost:8080/docs](http://localhost:8080/docs) to test predictions.

Each request logs a line like:

```
2025-08-04T15:00:00Z | INPUT: [...] | PREDICTION: ... | MEAN: ... | STD: ...
```

These are saved to: `inference_api/inference.log`

---

## 🤖 GitHub Actions CI/CD Pipeline

On **every PR** or **push to `main`**, the CI will:

1. Set up ZenML stack locally
2. Train model and log results
3. Build Docker image
4. Save image to `model-api-image.tar`
5. Simulate API inference to generate logs
6. Generate `results.md` with:
   - Accuracy
   - Hyperparameters
   - Log snippet
7. 📢 **Post comment** to the PR using **CML**

Artifacts uploaded:
- `model.pkl`
- `inference.log`
- `model-api-image.tar`

---

## 🗨️ Example PR Comment (Auto-Generated)

```
✅ Model Training Complete
📈 Accuracy: 0.93
⚙️ Hyperparameters: solver=lbfgs, penalty=l2
📦 Docker image built and exported as artifact

---

### 🧪 Inference Logs:
2025-08-04T15:00:00Z | INPUT: [...] | PREDICTION: ... | MEAN: ... | STD: ...

---

📦 Artifacts:
- model.pkl
- inference.log
- model-api-image.tar
```

---

## 📌 Summary

This is a **local-first**, fully automated MLOps setup:

- Train → Track → Package → Simulate → Comment → Repeat
- Reproducible and CI-friendly
- No cloud services required

Perfect for:
- Practicing CI/CD for ML
- Learning ZenML + GitHub Actions
- Experimenting with fast-feedback ML workflows

---

## ✅ You're All Set!

You can now fork this repo, run the pipeline, make your own PRs, and watch your MLOps system work automatically 🎯
