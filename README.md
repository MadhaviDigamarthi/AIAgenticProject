# Autonomous Task-Oriented AI Agent

## Problem Statement
Design an AI agent that can autonomously plan and execute a multi-step task using external tools.

### User Goal
Find the top 3 recent AI research papers on agriculture, summarize them, and store the output in a structured format.

## Solution Overview
This project demonstrates an autonomous AI agent that:
1. Understands the user goal
2. Plans the required steps
3. Executes the task
4. Stores the final output in JSON format

## Task Decomposition
1. Identify recent AI research papers related to agriculture  
2. Select the top 3 relevant papers  
3. Summarize each paper in simple language  
4. Store the results in a structured JSON file  

## Output
The final output is stored in:
- `output.json`

It contains:
- Paper title
- Year of publication
- Domain
- Summary


## Architecture
The system follows an agent-based approach:
- Input: User goal
- Planning: Task decomposition
- Execution: Data selection and summarization
- Output: Structured JSON storage

