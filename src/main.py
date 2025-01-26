# main.py
import os
from pathlib import Path
from deepseek_client import APIConfig, DeepseekClient
from dag_processor import process_dag_response


def run_lgts_pipeline():
    """Main pipeline"""
    # Initialize components
    client = DeepseekClient(APIConfig(temperature=0.1))
    prompt = Path("minigrid_prompt.txt").read_text()
    
    # Generate DAG response
    raw = client.generate_response(
        system_prompt="Generate MiniGrid paths as per LgTS paper requirements",
        user_prompt=prompt
    )
    
    # Process and save
    adj = process_dag_response(raw)
    
    # Paper-style output
    print("Adjacency List:")
    for node, edges in enumerate(adj):
        print(f"q{node} -> {[f'q{e}' for e in edges]}")

if __name__ == "__main__":
    run_lgts_pipeline()