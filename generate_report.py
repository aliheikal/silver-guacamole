import mlflow
from mlflow.tracking import MlflowClient

client = MlflowClient()
run = client.search_runs(experiment_ids=["0"], order_by=["start_time DESC"], max_results=1)[0]
accuracy = run.data.metrics.get("accuracy", "N/A")
solver = run.data.params.get("solver", "N/A")
penalty = run.data.params.get("penalty", "N/A")

with open("inference_api/inference.log", "r") as f:
    logs = "".join(f.readlines()[-3:])

with open("results.md", "w") as out:
    out.write(f'''
✅ **Model Training Complete**  
📈 Accuracy: `{accuracy}`  
⚙️ Hyperparameters: `solver={solver}`, `penalty={penalty}`  
📦 Docker image built and exported as artifact  

---

### 🧪 Inference Logs:
```
{logs.strip()}
```

---

📦 **Artifacts**:
- `model.pkl`
- `inference.log`
- `model-api-image.tar`
''')
