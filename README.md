# Awesome AI Paper Reproduction Radar

<div align="center">

**A searchable radar of high-interest AI papers and unofficial PyTorch reproduction repositories.**

Find hot AI papers, code status, and unofficial reproduction starters in one searchable radar.

![Repos](https://img.shields.io/badge/reproductions-61-blue) ![Collections](https://img.shields.io/badge/curated_tracks-7-purple) ![Updated](https://img.shields.io/badge/updated-2026-06-21-green) ![License](https://img.shields.io/badge/license-MIT-green)

[Browse table](#repository-radar) · [Curated tracks](#curated-tracks) · [Latest daily note](docs/daily/2026-06-21.md) · [Code-status policy](docs/status/code-availability-policy.md) · [Searchable HTML](docs/index.html) · [Data JSON](data/reproductions.json) · [Contribute](CONTRIBUTING.md)

</div>

> Maintained by [@StaryMoon](https://github.com/StaryMoon). If this radar helps you find, compare, or start reproducing an AI paper, please consider starring the repository and following my GitHub profile.

## What Makes This Different

Most paper lists are either raw link dumps or single-topic awesome lists. This radar is built around three more useful layers:

- **Searchable data layer**: every entry is stored in `data/reproductions.json` for scripting, filtering, and reuse.
- **Curated tracks**: papers are grouped by research intent, not only by repo name or conference.
- **Implementation-status view**: each entry points to paper, repo, tags, and current reproduction interface in one table.
- **Daily metadata refresh**: GitHub Actions can refresh stars, topics, and push timestamps without manual bookkeeping.

Every linked implementation is clearly marked as **unofficial** and keeps paper citations separate from local experiment logs.

## Latest Daily Radar Note

- [2026-06-21](docs/daily/2026-06-21.md) — a maintenance note on clearer official-code status wording and starter-first tracking.

## Starter-First Code-Status Watchlist

This section highlights papers where the radar currently indexes an unofficial starter and has not yet indexed an official-code link. This is a radar status, not a claim that no official implementation exists.

| Paper | Venue / topic | Official code status | Unofficial starter | Why people search it |
|---|---|---|---|---|
| [Skywork Open Reasoner 1 Technical Report](https://arxiv.org/abs/2505.22312) | Reasoning RL / arXiv 2025 | Official link not indexed in this radar yet | [Skywork-OR1](https://github.com/StaryMoon/Skywork-OR1-Unofficial) | Reasoning RL and test-time scaling papers are searched for starter code before official recipes settle. |
| [Phi-4 Technical Report](https://arxiv.org/abs/2412.08905) | Compact Reasoning LLM / arXiv 2024 | Official link not indexed in this radar yet | [Phi-4](https://github.com/StaryMoon/Phi-4-Unofficial) | Reasoning RL and test-time scaling papers are searched for starter code before official recipes settle. |
| [Wan: Open and Advanced Large-Scale Video Generative Models](https://arxiv.org/abs/2503.20314) | Video Generation / arXiv 2025 | Official link not indexed in this radar yet | [Wan2-1](https://github.com/StaryMoon/Wan2-1-Unofficial) | Video generation and world-model papers are hard to compare without a runnable interface map. |
| [Cosmos World Foundation Model Platform for Physical AI](https://arxiv.org/abs/2501.03575) | World Models / arXiv 2025 | Official link not indexed in this radar yet | [Cosmos-WFM](https://github.com/StaryMoon/Cosmos-WFM-Unofficial) | Video generation and world-model papers are hard to compare without a runnable interface map. |
| [RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation](https://arxiv.org/abs/2410.07864) | Robotics Diffusion / arXiv 2024 | Official link not indexed in this radar yet | [RDT-1B](https://github.com/StaryMoon/RDT-1B-Unofficial) | VLA and robot-policy readers need quick links from papers to action-interface starters. |
| [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246) | VLA Robotics / arXiv 2024 | Official link not indexed in this radar yet | [OpenVLA](https://github.com/StaryMoon/OpenVLA-Unofficial) | VLA and robot-policy readers need quick links from papers to action-interface starters. |
| [OSDFace: One-Step Diffusion Model for Face Restoration](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_OSDFace_One-Step_Diffusion_Model_for_Face_Restoration_CVPR_2025_paper.html) | CVPR 2025 | Official link not indexed in this radar yet | [OSDFace](https://github.com/StaryMoon/OSDFace-Unofficial) | Restoration papers attract readers looking for baselines, degradation settings, and PyTorch entrypoints. |
| [UniRestore: Unified Perceptual and Task-Oriented Image Restoration Model Using Diffusion Prior](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_UniRestore_Unified_Perceptual_and_Task-Oriented_Image_Restoration_Model_Using_Diffusion_CVPR_2025_paper.html) | CVPR 2025 | Official link not indexed in this radar yet | [UniRestore](https://github.com/StaryMoon/UniRestore-Unofficial) | Restoration papers attract readers looking for baselines, degradation settings, and PyTorch entrypoints. |
| [Janus-Pro: Unified Multimodal Understanding and Generation with Data and Model Scaling](https://arxiv.org/abs/2501.17811) | Multimodal Generation / arXiv 2025 | Official link not indexed in this radar yet | [Janus-Pro](https://github.com/StaryMoon/Janus-Pro-Unofficial) | Multimodal papers move quickly, so readers often search for unified starter repos. |
| [Janus: Decoupling Visual Encoding for Unified Multimodal Understanding and Generation](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_Janus_Decoupling_Visual_Encoding_for_Unified_Multimodal_Understanding_and_Generation_CVPR_2025_paper.html) | CVPR 2025 | Official link not indexed in this radar yet | [Janus-CVPR2025](https://github.com/StaryMoon/Janus-CVPR2025-Unofficial) | Multimodal papers move quickly, so readers often search for unified starter repos. |

## Radar Snapshot

| Area | Count | Representative repos |
|---|---:|---|
| Frontier LLMs | 7 | [DeepSeek-V3](https://github.com/StaryMoon/DeepSeek-V3-Unofficial), [Gemma-3](https://github.com/StaryMoon/Gemma-3-Unofficial), [InternVL3](https://github.com/StaryMoon/InternVL3-Unofficial), [Kimi-VL](https://github.com/StaryMoon/Kimi-VL-Unofficial), [LLaDA-V](https://github.com/StaryMoon/LLaDA-V-Unofficial) |
| Reasoning LLMs | 9 | [DAPO](https://github.com/StaryMoon/DAPO-Unofficial), [DeepSeek-R1](https://github.com/StaryMoon/DeepSeek-R1-Unofficial), [Kimi-k1-5](https://github.com/StaryMoon/Kimi-k1-5-Unofficial), [LIMO](https://github.com/StaryMoon/LIMO-Unofficial), [Open-Reasoner-Zero](https://github.com/StaryMoon/Open-Reasoner-Zero-Unofficial) |
| Vision-Language Models | 4 | [Demo2Tutorial](https://github.com/StaryMoon/Demo2Tutorial-Unofficial), [Janus-CVPR2025](https://github.com/StaryMoon/Janus-CVPR2025-Unofficial), [Janus-Pro](https://github.com/StaryMoon/Janus-Pro-Unofficial), [OmniGen2](https://github.com/StaryMoon/OmniGen2-Unofficial) |
| Video and World Models | 11 | [LongVT](https://github.com/StaryMoon/LongVT-Unofficial), [CogVideoX](https://github.com/StaryMoon/CogVideoX-Unofficial), [Cosmos-WFM](https://github.com/StaryMoon/Cosmos-WFM-Unofficial), [DeltaWorld](https://github.com/StaryMoon/DeltaWorld-Unofficial), [Diffusion-Renderer](https://github.com/StaryMoon/Diffusion-Renderer-Unofficial) |
| Generation and Diffusion | 5 | [Chat2SVG](https://github.com/StaryMoon/Chat2SVG-Unofficial), [DiffSensei](https://github.com/StaryMoon/DiffSensei-Unofficial), [ACE-Step](https://github.com/StaryMoon/ACE-Step-Unofficial), [SANA](https://github.com/StaryMoon/SANA-Unofficial), [Stable-Diffusion-3](https://github.com/StaryMoon/Stable-Diffusion-3-Unofficial) |
| 3D and Rendering | 8 | [DeSiRe-GS](https://github.com/StaryMoon/DeSiRe-GS-Unofficial), [Feat2GS](https://github.com/StaryMoon/Feat2GS-Unofficial), [FlashGS](https://github.com/StaryMoon/FlashGS-Unofficial), [Hunyuan3D-2](https://github.com/StaryMoon/Hunyuan3D-2-Unofficial), [Omni-Scene](https://github.com/StaryMoon/Omni-Scene-Unofficial) |
| Robotics and Embodied AI | 6 | [DexGrasp-Anything](https://github.com/StaryMoon/DexGrasp-Anything-Unofficial), [RDT-1B](https://github.com/StaryMoon/RDT-1B-Unofficial), [Tartan-IMU](https://github.com/StaryMoon/Tartan-IMU-Unofficial), [OpenVLA](https://github.com/StaryMoon/OpenVLA-Unofficial), [Pi0](https://github.com/StaryMoon/Pi0-Unofficial) |
| Image Restoration | 7 | [SnowMaster](https://github.com/StaryMoon/SnowMaster-Unofficial), [Dual-Prompt-DiT](https://github.com/StaryMoon/Dual-Prompt-DiT-Unofficial), [IPC-Dehaze](https://github.com/StaryMoon/IPC-Dehaze-Unofficial), [OSDFace](https://github.com/StaryMoon/OSDFace-Unofficial), [ResFlow](https://github.com/StaryMoon/ResFlow-Unofficial) |
| Segmentation and Motion | 2 | [Motions-as-Queries](https://github.com/StaryMoon/Motions-as-Queries-Unofficial), [S-Seg](https://github.com/StaryMoon/S-Seg-Unofficial) |
| Code Models | 1 | [Seed-Coder](https://github.com/StaryMoon/Seed-Coder-Unofficial) |
| Efficient Sequence Models | 1 | [Mamba2](https://github.com/StaryMoon/Mamba2-Unofficial) |

## Curated Tracks

These are the buy-in oriented collections: each one explains who should care, why the area is hot, and which repos form a readable route through the topic.

| Track | Good for | Why now | Representative repos |
|---|---|---|---|
| [Reasoning RL and Test-Time Scaling Pack](docs/collections/reasoning-rl-test-time-scaling.md) | LLM researchers, students building reasoning baselines, and engineers following GRPO-style systems. | Reasoning models are still the highest-search AI topic, and readers want one place that links papers, repos, and implementation interfaces. | `DeepSeek-R1`, `Kimi-k1-5`, `s1-Test-Time-Scaling`, `LIMO`, `DAPO`, +3 more |
| [Frontier LLM Engineering Pack](docs/collections/frontier-llm-engineering.md) | LLM infrastructure learners, model architecture readers, and people comparing technical reports. | Most technical report readers do not need a full training run first; they need a structured implementation map and citation trail. | `DeepSeek-V3`, `Qwen3`, `Gemma-3`, `Phi-4`, `MiniMax-01`, +1 more |
| [VLM, Multimodal, and Agent Interface Pack](docs/collections/vlm-agent-multimodal.md) | VLM students, multimodal agent builders, and researchers looking for cross-modal repo templates. | VLM work is fragmented across understanding, generation, action, and agent tasks; this track groups them by reusable interface shape. | `Qwen2-5-VL`, `InternVL3`, `Kimi-VL`, `Janus-Pro`, `Janus-CVPR2025`, +3 more |
| [Video Generation and World Model Pack](docs/collections/video-world-models.md) | Video generation builders, world model readers, and robotics people who need visual dynamics references. | Video/world-model papers are search-heavy but scattered; a curated track makes the field easier to scan. | `HunyuanVideo`, `CogVideoX`, `Wan2-1`, `Cosmos-WFM`, `DeltaWorld`, +5 more |
| [3D, Gaussian, and Rendering Pack](docs/collections/3d-rendering-generation.md) | 3D vision students, graphics readers, and embodied AI researchers who need a cross-paper map. | 3D repos are often hard to compare because each paper uses different asset, rendering, and representation assumptions. | `Hunyuan3D-2`, `TRELLIS`, `FlashGS`, `Feat2GS`, `DeSiRe-GS`, +4 more |
| [Image Restoration and Low-Level Vision Pack](docs/collections/image-restoration-cvpr.md) | Low-level vision researchers, restoration students, and people following CVPR restoration papers. | Restoration work is easier to buy into when papers are grouped by degradation, prior, and interface rather than by conference only. | `ResFlow`, `IPC-Dehaze`, `OSDFace`, `Dual-Prompt-DiT`, `UniRestore`, +2 more |
| [Robotics, VLA, and Embodied AI Pack](docs/collections/robotics-vla-embodied.md) | Robotics students, embodied AI builders, and people comparing action-conditioned model interfaces. | Robotics papers are getting pulled into foundation-model discussions; a focused track makes this transition more legible. | `OpenVLA`, `Pi0`, `RDT-1B`, `DexGrasp-Anything`, `RoboBrain`, +1 more |

## Repository Radar

The full machine-readable dataset lives in [`data/reproductions.json`](data/reproductions.json).

### Frontier LLMs

| Repo | Paper | Source | Implementation status | Tags |
|---|---|---|---|---|
| [DeepSeek-V3](https://github.com/StaryMoon/DeepSeek-V3-Unofficial) | DeepSeek-V3 Technical Report | [2412.19437](https://arxiv.org/abs/2412.19437) | README, config, PyTorch interface, smoke test, release | deepseek, deepseek-v3, llm, mla, moe |
| [Gemma-3](https://github.com/StaryMoon/Gemma-3-Unofficial) | Gemma 3 Technical Report | [2503.19786](https://arxiv.org/abs/2503.19786) | README, config, PyTorch interface, smoke test, release | gemma, gemma-3, llm, long-context, multimodal |
| [InternVL3](https://github.com/StaryMoon/InternVL3-Unofficial) | InternVL3: Exploring Advanced Training and Test-Time Recipes for Open-Source Multimodal Models | [2504.10479](https://arxiv.org/abs/2504.10479) | README, config, PyTorch interface, smoke test, release | internvl, mllm, multimodal-pretraining, pytorch, reproduction |
| [Kimi-VL](https://github.com/StaryMoon/Kimi-VL-Unofficial) | Kimi-VL Technical Report | [2504.07491](https://arxiv.org/abs/2504.07491) | README, config, PyTorch interface, smoke test, release | kimi-vl, long-context, moe, multimodal, pytorch |
| [LLaDA-V](https://github.com/StaryMoon/LLaDA-V-Unofficial) | LLaDA-V: Large Language Diffusion Models with Visual Instruction Tuning | [2505.16933](https://arxiv.org/abs/2505.16933) | README, config, PyTorch interface, smoke test, release | cvpr-2026, diffusion-language-model, diffusion-model, mllm, multimodal |
| [MiniMax-01](https://github.com/StaryMoon/MiniMax-01-Unofficial) | MiniMax-01: Scaling Foundation Models with Lightning Attention | [2501.08313](https://arxiv.org/abs/2501.08313) | README, config, PyTorch interface, smoke test, release | attention, lightning-attention, llm, long-context, minimax |
| [Qwen2-5-VL](https://github.com/StaryMoon/Qwen2-5-VL-Unofficial) | Qwen2.5-VL Technical Report | [2502.13923](https://arxiv.org/abs/2502.13923) | README, config, PyTorch interface, smoke test, release | document-understanding, mllm, pytorch, qwen, reproduction |

### Reasoning LLMs

| Repo | Paper | Source | Implementation status | Tags |
|---|---|---|---|---|
| [DAPO](https://github.com/StaryMoon/DAPO-Unofficial) | DAPO: An Open-Source LLM Reinforcement Learning System at Scale | [2503.14476](https://arxiv.org/abs/2503.14476) | README, config, PyTorch interface, smoke test, release | dapo, llm-reasoning, policy-optimization, pytorch, reinforcement-learning |
| [DeepSeek-R1](https://github.com/StaryMoon/DeepSeek-R1-Unofficial) | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning | [2501.12948](https://arxiv.org/abs/2501.12948) | README, config, PyTorch interface, smoke test, release | deepseek-r1, grpo, llm, pytorch, reasoning |
| [Kimi-k1-5](https://github.com/StaryMoon/Kimi-k1-5-Unofficial) | Kimi k1.5: Scaling Reinforcement Learning with LLMs | [2501.12599](https://arxiv.org/abs/2501.12599) | README, config, PyTorch interface, smoke test, release | kimi, llm, long-context, pytorch, reasoning |
| [LIMO](https://github.com/StaryMoon/LIMO-Unofficial) | LIMO: Less is More for Reasoning | [2502.03387](https://arxiv.org/abs/2502.03387) | README, config, PyTorch interface, smoke test, release | data-efficient-learning, math-reasoning, pytorch, reasoning, reproduction |
| [Open-Reasoner-Zero](https://github.com/StaryMoon/Open-Reasoner-Zero-Unofficial) | Open-Reasoner-Zero: An Open Source Approach to Scaling Up Reinforcement Learning on the Base Model | [2503.24290](https://arxiv.org/abs/2503.24290) | README, config, PyTorch interface, smoke test, release | llm-reasoning, open-reasoner-zero, ppo, pytorch, reinforcement-learning |
| [Phi-4](https://github.com/StaryMoon/Phi-4-Unofficial) | Phi-4 Technical Report | [2412.08905](https://arxiv.org/abs/2412.08905) | README, config, PyTorch interface, smoke test, release | compact-model, llm, phi-4, pytorch, reasoning |
| [Qwen3](https://github.com/StaryMoon/Qwen3-Unofficial) | Qwen3 Technical Report | [2505.09388](https://arxiv.org/abs/2505.09388) | README, config, PyTorch interface, smoke test, release | llm, moe, multilingual, pytorch, qwen3 |
| [s1-Test-Time-Scaling](https://github.com/StaryMoon/s1-Test-Time-Scaling-Unofficial) | s1: Simple test-time scaling | [2501.19393](https://arxiv.org/abs/2501.19393) | README, config, PyTorch interface, smoke test, release | budget-forcing, llm, pytorch, reasoning, reproduction |
| [Skywork-OR1](https://github.com/StaryMoon/Skywork-OR1-Unofficial) | Skywork Open Reasoner 1 Technical Report | [2505.22312](https://arxiv.org/abs/2505.22312) | README, config, PyTorch interface, smoke test, release | code, grpo, long-cot, math, pytorch |

### Vision-Language Models

| Repo | Paper | Source | Implementation status | Tags |
|---|---|---|---|---|
| [Demo2Tutorial](https://github.com/StaryMoon/Demo2Tutorial-Unofficial) | Demo2Tutorial: From Human Experience to Multimodal Software Tutorials | [2606.03951](https://arxiv.org/abs/2606.03951) | README, config, PyTorch interface, smoke test, release | cvpr-2026, gui-agent, multimodal, multimodal-tutorial, pytorch |
| [Janus-CVPR2025](https://github.com/StaryMoon/Janus-CVPR2025-Unofficial) | Janus: Decoupling Visual Encoding for Unified Multimodal Understanding and Generation | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_Janus_Decoupling_Visual_Encoding_for_Unified_Multimodal_Understanding_and_Generation_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | computer-vision, cvpr-2025, generation, image-generation, multimodal |
| [Janus-Pro](https://github.com/StaryMoon/Janus-Pro-Unofficial) | Janus-Pro: Unified Multimodal Understanding and Generation with Data and Model Scaling | [2501.17811](https://arxiv.org/abs/2501.17811) | README, config, PyTorch interface, smoke test, release | image-generation, janus-pro, multimodal-generation, pytorch, reproduction |
| [OmniGen2](https://github.com/StaryMoon/OmniGen2-Unofficial) | OmniGen2: Towards Instruction-Aligned Multimodal Generation | [2506.18871](https://arxiv.org/abs/2506.18871) | README, config, PyTorch interface, smoke test, release | cvpr-2026, diffusion, image-generation, instruction-following, multimodal-generation |

### Video and World Models

| Repo | Paper | Source | Implementation status | Tags |
|---|---|---|---|---|
| [LongVT](https://github.com/StaryMoon/LongVT-Unofficial) | LongVT: Incentivizing Thinking with Long Videos via Native Tool Calling | [2511.20785](https://arxiv.org/abs/2511.20785) | README, config, PyTorch interface, smoke test, release | cvpr-2026, long-video-understanding, mllm, pytorch, reproduction |
| [CogVideoX](https://github.com/StaryMoon/CogVideoX-Unofficial) | CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer | [2408.06072](https://arxiv.org/abs/2408.06072) | README, config, PyTorch interface, smoke test, release | cogvideox, diffusion-transformer, pytorch, reproduction, text-to-video |
| [Cosmos-WFM](https://github.com/StaryMoon/Cosmos-WFM-Unofficial) | Cosmos World Foundation Model Platform for Physical AI | [2501.03575](https://arxiv.org/abs/2501.03575) | README, config, PyTorch interface, smoke test, release | cosmos, physical-ai, pytorch, reproduction, robotics |
| [DeltaWorld](https://github.com/StaryMoon/DeltaWorld-Unofficial) | A Frame Is Worth One Token: Efficient Generative World Modeling with Delta Tokens | [2604.04913](https://arxiv.org/abs/2604.04913) | README, config, PyTorch interface, smoke test, release | cvpr-2026, cvpr-highlight, delta-tokens, pytorch, reproduction |
| [Diffusion-Renderer](https://github.com/StaryMoon/Diffusion-Renderer-Unofficial) | Diffusion Renderer: Neural Inverse and Forward Rendering with Video Diffusion Models | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Liang_Diffusion_Renderer_Neural_Inverse_and_Forward_Rendering_with_Video_Diffusion_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | computer-vision, cvpr-2025, inverse-rendering, neural-rendering, pytorch |
| [HunyuanVideo](https://github.com/StaryMoon/HunyuanVideo-Unofficial) | HunyuanVideo: A Systematic Framework For Large Video Generative Models | [2412.03603](https://arxiv.org/abs/2412.03603) | README, config, PyTorch interface, smoke test, release | diffusion-transformer, hunyuanvideo, pytorch, reproduction, text-to-video |
| [Presto-SCA](https://github.com/StaryMoon/Presto-SCA-Unofficial) | Long Video Diffusion Generation with Segmented Cross-Attention and Content-Rich Video Data Curation | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Yan_Long_Video_Diffusion_Generation_with_Segmented_Cross-Attention_and_Content-Rich_Video_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | computer-vision, cross-attention, cvpr-2025, diffusion, diffusion-model |
| [ReCapture](https://github.com/StaryMoon/ReCapture-Unofficial) | ReCapture: Generative Video Camera Controls for User-Provided Videos using Masked Video Fine-Tuning | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_ReCapture_Generative_Video_Camera_Controls_for_User-Provided_Videos_using_Masked_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | camera-control, computer-vision, cvpr-2025, masked-finetuning, pytorch |
| [SketchVideo](https://github.com/StaryMoon/SketchVideo-Unofficial) | SketchVideo: Sketch-based Video Generation and Editing | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_SketchVideo_Sketch-based_Video_Generation_and_Editing_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | computer-vision, cvpr-2025, pytorch, sketch, sketch-guided-generation |
| [VideoDirector](https://github.com/StaryMoon/VideoDirector-Unofficial) | VideoDirector: Precise Video Editing via Text-to-Video Models | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VideoDirector_Precise_Video_Editing_via_Text-to-Video_Models_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | computer-vision, cvpr-2025, diffusion, diffusion-model, pytorch |
| [Wan2-1](https://github.com/StaryMoon/Wan2-1-Unofficial) | Wan: Open and Advanced Large-Scale Video Generative Models | [2503.20314](https://arxiv.org/abs/2503.20314) | README, config, PyTorch interface, smoke test, release | diffusion, diffusion-transformer, pytorch, reproduction, text-to-video |

### Generation and Diffusion

| Repo | Paper | Source | Implementation status | Tags |
|---|---|---|---|---|
| [Chat2SVG](https://github.com/StaryMoon/Chat2SVG-Unofficial) | Chat2SVG: Vector Graphics Generation with Large Language Models and Image Diffusion Models | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_Chat2SVG_Vector_Graphics_Generation_with_Large_Language_Models_and_Image_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | computer-vision, cvpr-2025, diffusion, llm, multimodal-generation |
| [DiffSensei](https://github.com/StaryMoon/DiffSensei-Unofficial) | DiffSensei: Bridging Multi-Modal LLMs and Diffusion Models for Customized Manga Generation | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_DiffSensei_Bridging_Multi-Modal_LLMs_and_Diffusion_Models_for_Customized_Manga_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | computer-vision, cvpr-2025, diffusion, diffusion-model, manga-generation |
| [ACE-Step](https://github.com/StaryMoon/ACE-Step-Unofficial) | ACE-Step: A Step Towards Music Generation Foundation Model | [2506.00045](https://arxiv.org/abs/2506.00045) | README, config, PyTorch interface, smoke test, release | ace-step, audio, diffusion, foundation-model, music-generation |
| [SANA](https://github.com/StaryMoon/SANA-Unofficial) | SANA: Efficient High-Resolution Image Synthesis with Linear Diffusion Transformers | [2410.10629](https://arxiv.org/abs/2410.10629) | README, config, PyTorch interface, smoke test, release | diffusion-transformer, efficient-ai, linear-attention, pytorch, reproduction |
| [Stable-Diffusion-3](https://github.com/StaryMoon/Stable-Diffusion-3-Unofficial) | Scaling Rectified Flow Transformers for High-Resolution Image Synthesis | [2403.03206](https://arxiv.org/abs/2403.03206) | README, config, PyTorch interface, smoke test, release | diffusion-transformer, pytorch, rectified-flow, reproduction, stable-diffusion-3 |

### 3D and Rendering

| Repo | Paper | Source | Implementation status | Tags |
|---|---|---|---|---|
| [DeSiRe-GS](https://github.com/StaryMoon/DeSiRe-GS-Unofficial) | DeSiRe-GS: 4D Street Gaussians for Static-Dynamic Decomposition and Surface Reconstruction for Urban Driving Scenes | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Peng_DeSiRe-GS_4D_Street_Gaussians_for_Static-Dynamic_Decomposition_and_Surface_Reconstruction_for_Urban_Driving_Scenes_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | 4d-gaussian-splatting, autonomous-driving, computer-vision, cvpr-2025, pytorch |
| [Feat2GS](https://github.com/StaryMoon/Feat2GS-Unofficial) | Feat2GS: Probing Visual Foundation Models with Gaussian Splatting | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Feat2GS_Probing_Visual_Foundation_Models_with_Gaussian_Splatting_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | 3d-gaussian-splatting, 3d-reconstruction, computer-vision, cvpr-2025, foundation-models |
| [FlashGS](https://github.com/StaryMoon/FlashGS-Unofficial) | FlashGS: Efficient 3D Gaussian Splatting for Large-scale and High-resolution Rendering | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Feng_FlashGS_Efficient_3D_Gaussian_Splatting_for_Large-scale_and_High-resolution_Rendering_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | 3d-gaussian-splatting, 3d-reconstruction, computer-vision, cvpr-2025, gaussian-splatting |
| [Hunyuan3D-2](https://github.com/StaryMoon/Hunyuan3D-2-Unofficial) | Hunyuan3D 2.0: Scaling Diffusion Models for High Resolution Textured 3D Assets Generation | [2501.12202](https://arxiv.org/abs/2501.12202) | README, config, PyTorch interface, smoke test, release | 3d-generation, diffusion-transformer, hunyuan3d, pytorch, reproduction |
| [Omni-Scene](https://github.com/StaryMoon/Omni-Scene-Unofficial) | Omni-Scene: Omni-Gaussian Representation for Ego-Centric Sparse-View Scene Reconstruction | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Wei_Omni-Scene_Omni-Gaussian_Representation_for_Ego-Centric_Sparse-View_Scene_Reconstruction_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | 3d-gaussian-splatting, computer-vision, cvpr-2025, egocentric, egocentric-vision |
| [SAGE-3D](https://github.com/StaryMoon/SAGE-3D-Unofficial) | SAGE: Scalable Agentic 3D Scene Generation for Embodied AI | [2602.10116](https://arxiv.org/abs/2602.10116) | README, config, PyTorch interface, smoke test, release | 3d-scene-generation, agentic-ai, cvpr-2026, embodied-ai, pytorch |
| [ThreeDTopia-XL](https://github.com/StaryMoon/ThreeDTopia-XL-Unofficial) | 3DTopia-XL: Scaling High-quality 3D Asset Generation via Primitive Diffusion | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_3DTopia-XL_Scaling_High-quality_3D_Asset_Generation_via_Primitive_Diffusion_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | 3d-assets, 3d-generation, computer-vision, cvpr-2025, primitive-diffusion |
| [TRELLIS](https://github.com/StaryMoon/TRELLIS-Unofficial) | Structured 3D Latents for Scalable and Versatile 3D Generation | [2412.01506](https://arxiv.org/abs/2412.01506) | README, config, PyTorch interface, smoke test, release | 3d-generation, pytorch, rectified-flow, reproduction, slat |

### Robotics and Embodied AI

| Repo | Paper | Source | Implementation status | Tags |
|---|---|---|---|---|
| [DexGrasp-Anything](https://github.com/StaryMoon/DexGrasp-Anything-Unofficial) | DexGrasp Anything: Towards Universal Robotic Dexterous Grasping with Physics Awareness | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Zhong_DexGrasp_Anything_Towards_Universal_Robotic_Dexterous_Grasping_with_Physics_Awareness_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | computer-vision, cvpr-2025, dexterous-grasping, dexterous-manipulation, physics-aware |
| [RDT-1B](https://github.com/StaryMoon/RDT-1B-Unofficial) | RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation | [2410.07864](https://arxiv.org/abs/2410.07864) | README, config, PyTorch interface, smoke test, release | bimanual-manipulation, diffusion-transformer, pytorch, rdt, reproduction |
| [Tartan-IMU](https://github.com/StaryMoon/Tartan-IMU-Unofficial) | Tartan IMU: A Light Foundation Model for Inertial Positioning in Robotics | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_Tartan_IMU_A_Light_Foundation_Model_for_Inertial_Positioning_in_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | computer-vision, cvpr-2025, foundation-model, imu, inertial-positioning |
| [OpenVLA](https://github.com/StaryMoon/OpenVLA-Unofficial) | OpenVLA: An Open-Source Vision-Language-Action Model | [2406.09246](https://arxiv.org/abs/2406.09246) | README, config, PyTorch interface, smoke test, release | openvla, pytorch, reproduction, robot-manipulation, robotics |
| [Pi0](https://github.com/StaryMoon/Pi0-Unofficial) | $π_0$: A Vision-Language-Action Flow Model for General Robot Control | [2410.24164](https://arxiv.org/abs/2410.24164) | README, config, PyTorch interface, smoke test, release | flow-matching, pi0, pytorch, reproduction, robot-policy |
| [RoboBrain](https://github.com/StaryMoon/RoboBrain-Unofficial) | RoboBrain: A Unified Brain Model for Robotic Manipulation from Abstract to Concrete | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Ji_RoboBrain_A_Unified_Brain_Model_for_Robotic_Manipulation_from_Abstract_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | computer-vision, cvpr-2025, embodied-ai, manipulation, pytorch |

### Image Restoration

| Repo | Paper | Source | Implementation status | Tags |
|---|---|---|---|---|
| [SnowMaster](https://github.com/StaryMoon/SnowMaster-Unofficial) | SnowMaster: Comprehensive Real-world Image Desnowing via MLLM with Multi-Model Feedback Optimization | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Lai_SnowMaster_Comprehensive_Real-world_Image_Desnowing_via_MLLM_with_Multi-Model_Feedback_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | computer-vision, cvpr-2025, image-desnowing, image-restoration, mllm |
| [Dual-Prompt-DiT](https://github.com/StaryMoon/Dual-Prompt-DiT-Unofficial) | Dual Prompting Image Restoration with Diffusion Transformers | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Kong_Dual_Prompting_Image_Restoration_with_Diffusion_Transformers_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | computer-vision, cvpr-2025, diffusion-transformer, image-restoration, prompt-learning |
| [IPC-Dehaze](https://github.com/StaryMoon/IPC-Dehaze-Unofficial) | Iterative Predictor-Critic Code Decoding for Real-World Image Dehazing | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Fu_Iterative_Predictor-Critic_Code_Decoding_for_Real-World_Image_Dehazing_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | codebook, computer-vision, cvpr-2025, image-dehazing, image-restoration |
| [OSDFace](https://github.com/StaryMoon/OSDFace-Unofficial) | OSDFace: One-Step Diffusion Model for Face Restoration | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_OSDFace_One-Step_Diffusion_Model_for_Face_Restoration_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | computer-vision, cvpr-2025, diffusion, diffusion-model, face-restoration |
| [ResFlow](https://github.com/StaryMoon/ResFlow-Unofficial) | Reversing Flow for Image Restoration | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Qin_Reversing_Flow_for_Image_Restoration_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | computer-vision, cvpr-2025, deraining, flow-matching, image-restoration |
| [UniRestore](https://github.com/StaryMoon/UniRestore-Unofficial) | UniRestore: Unified Perceptual and Task-Oriented Image Restoration Model Using Diffusion Prior | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_UniRestore_Unified_Perceptual_and_Task-Oriented_Image_Restoration_Model_Using_Diffusion_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | computer-vision, cvpr-2025, diffusion-prior, image-restoration, low-level-vision |
| [URWKV](https://github.com/StaryMoon/URWKV-Unofficial) | URWKV: Unified RWKV Model with Multi-state Perspective for Low-light Image Restoration | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_URWKV_Unified_RWKV_Model_with_Multi-state_Perspective_for_Low-light_Image_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | computer-vision, cvpr-2025, image-restoration, low-light-enhancement, pytorch |

### Segmentation and Motion

| Repo | Paper | Source | Implementation status | Tags |
|---|---|---|---|---|
| [Motions-as-Queries](https://github.com/StaryMoon/Motions-as-Queries-Unofficial) | Motions as Queries: One-Stage Multi-Person Holistic Human Motion Capture | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Motions_as_Queries_One-Stage_Multi-Person_Holistic_Human_Motion_Capture_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | computer-vision, cvpr-2025, human-motion-capture, motion-queries, motion-reconstruction |
| [S-Seg](https://github.com/StaryMoon/S-Seg-Unofficial) | Exploring Simple Open-Vocabulary Semantic Segmentation | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Lai_Exploring_Simple_Open-Vocabulary_Semantic_Segmentation_CVPR_2025_paper.html) | README, config, PyTorch interface, smoke test, release | computer-vision, cvpr-2025, maskformer, open-vocabulary-segmentation, pytorch |

### Code Models

| Repo | Paper | Source | Implementation status | Tags |
|---|---|---|---|---|
| [Seed-Coder](https://github.com/StaryMoon/Seed-Coder-Unofficial) | Seed-Coder: Let the Code Model Curate Data for Itself | [2506.03524](https://arxiv.org/abs/2506.03524) | README, config, PyTorch interface, smoke test, release | code-generation, code-llm, data-curation, llm, pytorch |

### Efficient Sequence Models

| Repo | Paper | Source | Implementation status | Tags |
|---|---|---|---|---|
| [Mamba2](https://github.com/StaryMoon/Mamba2-Unofficial) | Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality | [2405.21060](https://arxiv.org/abs/2405.21060) | README, config, PyTorch interface, smoke test, release | efficient-attention, mamba2, pytorch, reproduction, sequence-modeling |

## Search Locally

```bash
python scripts/build.py
python scripts/refresh_github_metadata.py
```

The static page at [`docs/index.html`](docs/index.html) provides a client-side searchable table for all entries.

## Add a Paper

Open a pull request that edits `data/reproductions.json` and then runs `python scripts/build.py`. Good entries should include:

- paper title and paper URL;
- repository URL;
- category and tags;
- current implementation status;
- clear unofficial attribution if the repository is not from the paper authors.

## Disclaimer

This project is an independent index of unofficial paper reproduction repositories. Paper names, datasets, model names, official code, and trademarks belong to their respective owners. Always cite the original papers and check the licenses of official assets before reuse.
