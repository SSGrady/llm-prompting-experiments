# LgTS Implementation

Official implementation UCF's L15 for "Dynamic Task Sampling using LLM-generated sub-goals" (LgTS)

## Features
- LLM-guided DAG generation (Fig 1b)
- Teacher-Student ready adjacency lists (Table 1)
- MiniGrid-compliant prompt engineering

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