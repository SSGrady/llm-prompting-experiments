# LgTS Implementation

UCF Team L15's living LLM implementation for "Dynamic Task Sampling using LLM-generated sub-goals"

![Img of LLM-guided DAG json](https://i.ibb.co/xSrmjZDY/mini-llm-guided-2d-dag.png)

## Overview
This project produces **2D DAG lists** describing paths from a start state to a goal state in a grid-based environment, guided by an LLM. 

It can switch between **Deepseek** or **OpenAI** calls, generating valid state sequences according to environment constraints.


## Features
- **LLM-guided DAG generation**: Auto-generates paths with constraints
- **Teacher-Student-ready**: Outputs a 2D list of states for gridworld tasks
- **MiniGrid-compliant prompts**: Uses standard objects and predicates (Keys, Doors, Lava, etc)
- **Seamless Packaging**: Installs via `pyproject.toml` for easy distribution

## 1. Clone with SSH
```
git clone git@github.com:SSGrady/llm-prompting-experiments.git
cd llm-prompting-experiments
```

## 2. Installation
Install the package **locally** from the root directory. Run this command to handle dependency and build management:
```
pip install --upgrade .
```

## 3. Environment Variables
You can use either **DeepSeek** or **OpenAI** API keys. Place them in your environment:
```
export "DEEPSEEK_API_KEY=your_key"
# OR
export "OPENAI_API_KEY=your_key"
```

## 4. Usage
Once installed, you can run this on your CLI:
```
lgts-run
```

This executes the main pipeline:
1. Reads environment variables (e.g., OPENAI_API_KEY)
2. Loads `minigrid_prompt.txt`
3. Calls the LLM to generate DAG states
4. Validates and prints the remaining JSON paths
5. Saves them to `lgts_output/` in JSON format

## 5. Developer Mode
If you plan to make frequent changes to the repo, install in editable mode:
```
pip install --upgrade -e .
```

Any Python files changed are reflected immediately without reinstallation.