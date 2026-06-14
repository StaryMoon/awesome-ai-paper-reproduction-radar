# Reasoning RL and Test-Time Scaling Pack

For readers tracking how long-chain reasoning moved from prompting tricks to RL systems, budget forcing, and verification-heavy training loops.

**Good for:** LLM researchers, students building reasoning baselines, and engineers following GRPO-style systems.

**Why now:** Reasoning models are still the highest-search AI topic, and readers want one place that links papers, repos, and implementation interfaces.

## Route

| Repo | Paper | Source | Tags |
|---|---|---|---|
| [DeepSeek-R1](https://github.com/StaryMoon/DeepSeek-R1-Unofficial) | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning | [2501.12948](https://arxiv.org/abs/2501.12948) | deepseek-r1, grpo, llm, pytorch, reasoning |
| [Kimi-k1-5](https://github.com/StaryMoon/Kimi-k1-5-Unofficial) | Kimi k1.5: Scaling Reinforcement Learning with LLMs | [2501.12599](https://arxiv.org/abs/2501.12599) | kimi, llm, long-context, pytorch, reasoning |
| [s1-Test-Time-Scaling](https://github.com/StaryMoon/s1-Test-Time-Scaling-Unofficial) | s1: Simple test-time scaling | [2501.19393](https://arxiv.org/abs/2501.19393) | budget-forcing, llm, pytorch, reasoning, reproduction |
| [LIMO](https://github.com/StaryMoon/LIMO-Unofficial) | LIMO: Less is More for Reasoning | [2502.03387](https://arxiv.org/abs/2502.03387) | data-efficient-learning, math-reasoning, pytorch, reasoning, reproduction |
| [DAPO](https://github.com/StaryMoon/DAPO-Unofficial) | DAPO: An Open-Source LLM Reinforcement Learning System at Scale | [2503.14476](https://arxiv.org/abs/2503.14476) | dapo, llm-reasoning, policy-optimization, pytorch, reinforcement-learning |
| [Open-Reasoner-Zero](https://github.com/StaryMoon/Open-Reasoner-Zero-Unofficial) | Open-Reasoner-Zero: An Open Source Approach to Scaling Up Reinforcement Learning on the Base Model | [2503.24290](https://arxiv.org/abs/2503.24290) | llm-reasoning, open-reasoner-zero, ppo, pytorch, reinforcement-learning |
| [Skywork-OR1](https://github.com/StaryMoon/Skywork-OR1-Unofficial) | Skywork Open Reasoner 1 Technical Report | [2505.22312](https://arxiv.org/abs/2505.22312) | code, grpo, long-cot, math, pytorch |
| [Qwen3](https://github.com/StaryMoon/Qwen3-Unofficial) | Qwen3 Technical Report | [2505.09388](https://arxiv.org/abs/2505.09388) | llm, moe, multilingual, pytorch, qwen3 |

## Suggested Reading Flow

1. Start from the first two repositories to understand the main architectural vocabulary.
2. Read the middle entries as design variants and ablations.
3. Use the later entries to compare adjacent tasks, data assumptions, or evaluation setups.

[Back to radar](../../README.md)
