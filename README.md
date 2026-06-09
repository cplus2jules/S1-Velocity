# Smart Adaptive Backend for OpenAudio S1-Mini (S1 Velocity)

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-green.svg)](https://www.python.org/)
[![Framework: Fish-Speech](https://img.shields.io/badge/Framework-Fish--Speech-orange.svg)](https://github.com/fishaudio/fish-speech)
[![MIT Licensed](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


A production-ready inference framework that enables efficient Text-to-Speech (TTS) and zero-shot voice cloning on consumer hardware. Designed to solve common out-of-memory errors and performance paradoxes on devices spanning from 4GB NVIDIA GPUs to Apple M-Series chips and Intel CPUs.

## Languages Supported
The core framework supports following languages via the OpenAudio S1-Mini engine:
`English`, `Chinese`, `Japanese`, `Korean`, `French`, `German`, `Spanish`, `Arabic`.

---

## The Problem 
Modern Large Language Models (LLMs) and neural TTS like OpenAudio S1-Mini typically require expensive server-grade hardware, making them inaccessible for many. When run on consumer devices, users often face:
1. **Memory Swaps and Crashes**: Especially prevalent for GPUs with under 6GB of VRAM.
2. **Platform Inefficiency**: The "MPS Paradox", where using Apple's Metal Performance Shaders blindly can lead to out-of-memory errors and system freezing.
3. **Configuration Paradoxes**: Common optimizations (like INT8 quantization) can actually slow things down considerably (up to 95x) on platforms like Apple MPS if applied improperly.

## The Solution
The **Smart Adaptive Backend** is an intelligent framework built to overcome these limitations. It consists of three main subsystems:
- **Subsystem A (Hardware Detection and Profiling)**: Divides the host execution environment into performance classes (High-End CUDA, Apple Silicon, CPU only) and profiles VRAM and Unified Memory configurations.
- **Subsystem B (Configuration Engine)**: A dynamic memory budget manager that restricts specific environments, selectively picking optimal formats (FP16 or INT8) and preventing swapping defaults on Apple devices. 
- **Subsystem C (TTS Execution and Monitoring)**: Continuously observes metrics. It dynamically manages thermal restrictions on fanless devices (like the MacBook Air) avoiding thermal throttling for sustained tasks.

## Key Features

* **Zero-Shot Voice Cloning**: High-quality cloning using just 10-30 seconds of reference audio. 
* **Dynamic Budgeting**: Safely restricts VRAM usage avoiding OS-level OOM crashes.
* **Smart Quantization Routing**: Implements dynamic precision mapping (e.g., keeping FP16 on Apple MPS, using INT8 predominantly on Intel CPUs, and matching CUDA capabilities directly).
* **Thermal-Aware Task Scheduling**: Safeguards against thermal degradation over continuous runs on fanless implementations.
* **Diverse User Interface Options**: Choose from Gradio or Streamlit UIs. RestAPI provided.

## Quick Start Installation 

### 1. Prerequisite: Check System & Install UV
This project uses the modern package manager [uv](https://github.com/astral-sh/uv) to ensure reproducible and blazing-fast installations.

#### macOS/Linux
```bash
curl -lsSf https://astral.sh/uv/install.sh | sh
```
#### Windows
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Set Up Environment

```bash
# Clone the repository
git clone <your-repo-url>
cd <repo-name>

# Create the optimized virtual environment
uv venv .venv

# Activate it (macOS/Linux)
source .venv/bin/activate
# Or (Windows)
.venv\Scripts\activate

# Install dependencies using pnpm and uv
uv pip install -r requirements.txt
```

> **Note on PyTorch versions:**  
> The system typically assumes dependencies as laid out in `requirements.txt`. For strict CUDA configurations with NVIDIA Hardware, install Torch via:
> * CUDA 12.1: `uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121`

### 3. Setup OpenAudio S1-Mini Weights 

Ensure you have your models populated under `checkpoints/openaudio-s1-mini` by using Hugging Face CLI:

```bash
pip install huggingface-hub
huggingface-cli download fishaudio/openaudio-s1-mini --local-dir checkpoints/openaudio-s1-mini
```

### 4. Configure Application (.env)

Duplicate `.env_example` into `.env` (or setup manually).
```bash
# General config:
DEVICE=auto             # Automatically assigns based on adaptive detection
MIXED_PRECISION=auto    # Switches intelligently (FP16 / INT8 etc base on HW Class)
```

### 5. Running the Application

You can launch the framework through scripts or Python directly.

**Start the Framework & UIs**
```bash
# Backend 
python backend/app.py

# Pick your favorite UI Client in a new terminal:
python ui/gradio_app.py
# OR
streamlit run ui/streamlit_app.py
```

## 📊 Evaluation and Testing 
During empirical testing, the dynamic configuration yielded extensive RTF improvements and crash prevention over conventional unmanaged PyTorch configurations on:
- NVIDIA RTX Series
- Core i5 series (Integrated Graphics)
- Apple M1 Air (8GB RAM configuration) -- Reduced peak memory by 71% without RTF impact using optimization strategies natively. 

## Authorship & Contributions

This framework was developed as part of a Bachelor of Science in Computer Science thesis at **Caraga State University – Main Campus** by:

- **Julian L. Salas** (Lead Developer & System Architect)
- **Alethea Joy D. Montoyo** (Researcher & Technical Analyst)

### Technical Contributions
While the underlying TTS engine utilizes the OpenAudio S1-Mini (Fish Speech) architecture, the authors developed the following proprietary components from scratch to enable cross-platform efficiency:

1.  **Smart Adaptive Backend (SAB)**: The core middleware that negotiates between high-level inference requests and hardware constraints.
2.  **Hardware Profiling Subsystem**: Logic for real-time detection of CUDA capabilities, Apple Silicon memory pressure, and CPU thread optimization.
3.  **Dynamic Configuration Engine**: The decision logic that intelligently selects precision (FP16 vs. INT8) based on platform-specific "Paradox" findings (e.g., opting for CPU/FP16 on Apple M1 to save 71% memory).
4.  **Thermal-Aware Execution Logic**: A monitoring layer designed to safeguard fanless consumer hardware from performance degradation during long-form synthesis.
5.  **Multi-Frontend Integration**: Custom-built Gradio and Streamlit interfaces optimized for monitoring backend performance metrics.

## License & Acknowledgements
- **Core Engine**: [Fish Speech](https://github.com/fishaudio/fish-speech) (Released under Apache 2.0).
- **Model Weights**: [OpenAudio S1-Mini](https://huggingface.co/fishaudio/openaudio-s1-mini) (Released under CC-BY-NC-SA-4.0).
- **Thesis Advising**: Regien B. Nakazato, MSc.
- **Academic Support**: College of Computing and Information Sciences (CCIS), Caraga State University.
