from zenml_pipeline.pipeline import training_pipeline

if __name__ == '__main__':
    print("\n🚀 Running training pipeline...")
    training_pipeline()
    print("\n✅ Model training complete. You can now run the FastAPI server to serve predictions.")
