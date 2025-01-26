# LgTS Implementation

UCF Team L15's living LLM implementation for "Dynamic Task Sampling using LLM-generated sub-goals"

![Img of prettyied LLM-guided DAGA generated json](https://i.ibb.co/t3dNs3d/llm-dag-gen-pretified-json.png)

## Features
- LLM-guided DAG generation
- Teacher-Student ready adjacency lists
- Farama's MiniGrid-compliant prompt engineering

## 1. Clone with SSH
```
git clone git@github.com:SSGrady/llm-prompting-experiments.git
cd llm-prompting-experiments
```

## 2. Setup
```
pip install -r requirements.txt
echo "DEEPSEEK_API_KEY=your_key" > .env
```

## 3. Running
```
python3 src/main.py
```
