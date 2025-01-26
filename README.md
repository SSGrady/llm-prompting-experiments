# LgTS Implementation

UCF Team L15's LLM implementation for "Dynamic Task Sampling using LLM-generated sub-goals" (LgTS)

![Img of prettyied LLM-guided DAGA generated json](https://i.ibb.co/t3dNs3d/llm-dag-gen-pretified-json.png)

## Features
- LLM-guided DAG generation
- Teacher-Student ready adjacency lists
- Farama's MiniGrid-compliant prompt engineering

## Setup
```
pip install -r requirements.txt
echo "DEEPSEEK_API_KEY=your_key" > .env
```

## Running
```
cd llm-prompting-experiments
python3 src/main.py
```