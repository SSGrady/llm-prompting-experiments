# src/dag_processor.py
import json
import hashlib
from pathlib import Path

def process_dag_response(response: str, output_dir: str = "lgts_output") -> list[list[int]]:
    """Converts LLM response to adjacency list per paper requirements"""
    # Processing
    sequences = [eval(s) for s in response.strip().split('\n') if s.startswith('[')]
    
    # Create node mapping
    state_map = {}
    adj = []
    for seq in sequences:
        for i in range(len(seq)-1):
            src = seq[i]
            dst = seq[i+1]
            
            # Create unique node IDs
            if src not in state_map:
                state_map[src] = len(state_map)
                adj.append([])
            if dst not in state_map:
                state_map[dst] = len(state_map)
                adj.append([])
            
            # Add edge if not exists
            if state_map[dst] not in adj[state_map[src]]:
                adj[state_map[src]].append(state_map[dst])

    # Save outputs with hash-based naming
    Path(output_dir).mkdir(exist_ok=True)
    response_hash = hashlib.md5(response.encode()).hexdigest()[:8]
    
    with open(f"{output_dir}/dag_{response_hash}.json", "w") as f:
        json.dump({
            "nodes": list(state_map.keys()),
            "edges": adj
        }, f)
    
    return adj