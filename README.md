# LgTS Implementation

UCF Team L15's living LLM implementation for "Dynamic Task Sampling using LLM-generated sub-goals"

![Img of LLM-guided DAG json](https://i.ibb.co/xSrmjZDY/mini-llm-guided-2d-dag.png)

## Features
- LLM-guided DAG generation
- Teacher-Student-ready 2D list
- MiniGrid-compliant prompt engineering

## 1. Clone with SSH
```
git clone git@github.com:SSGrady/llm-prompting-experiments.git
cd llm-prompting-experiments
```

## 2. Setup
```
pip install -r requirements.txt
```

## 3. Choose
```
echo "DEEPSEEK_API_KEY=your_key" > .env
```
OR
```
echo "OPENAI_API_KEY=your_key" > .env
```

## 4. Running
```
python3 src/main.py
```
