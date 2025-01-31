# lgts/dag_processor.py
import re
import json
import hashlib
from pathlib import Path
from lgts.validator import validate_dag

def strip_code_fences(text: str) -> str:
    # Remove trailing ``` common for our JSON LLM-guided DAG list
    pattern = r"^```(?:json)?\s*|\s*```$"
    return re.sub(pattern, "", text.strip())

def process_dag_response(response: str, output_dir: str = "lgts_output") -> list[list[str]]:
    # Catch empty responses from LLM
    if not response.strip():
        raise ValueError("Empty response received from the LLM.")

    cleaned_response = strip_code_fences(response)
    data = json.loads(cleaned_response)
    paths = data.get("paths", [])
    validate_dag(paths)
    Path(output_dir).mkdir(exist_ok=True)
    response_hash = hashlib.md5(response.encode()).hexdigest()[:8]
    with open(f"{output_dir}/paths_{response_hash}.json", "w") as f:
        json.dump({"paths": paths}, f, indent=2)
    return paths