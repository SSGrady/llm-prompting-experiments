# src/main.py
import os
from pathlib import Path
from choose_model_client import APIConfig, OpenAIClient
from dag_processor import process_dag_response
from validator import DAGValidationError
import time
import json

def run_lgts_pipeline(max_retries: int = 3):
    client = OpenAIClient(APIConfig())
    prompt = Path("minigrid_prompt.txt").read_text()
    attempt = 0
    while attempt < max_retries:
        try:
            raw = client.generate_response(
                system_prompt="You are a reasoning agent that generates paths from initial states to goal states in a grid-based environment. Each path is a sequence of symbolic states. Output JSON only.",
                user_prompt=prompt
            )
            paths = process_dag_response(raw)
            output = {"paths": paths}
            print(json.dumps(output, indent=2))
            return
        except DAGValidationError as ve:
            attempt += 1
            print(f"Validation failed on attempt {attempt}:")
            for error in ve.errors:
                print(f" - {error}")
            if attempt < max_retries:
                prompt = f"Let's retry generating the DAG with improved adherence to the constraints.\n{Path('minigrid_prompt.txt').read_text()}"
                time.sleep(1)
            else:
                print("Max retries reached. Exiting pipeline.")
                raise ve

if __name__ == "__main__":
    run_lgts_pipeline()