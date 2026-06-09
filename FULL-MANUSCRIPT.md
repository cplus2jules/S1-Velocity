



Adaptive Hardware Optimization Framework for OpenAudio S1-Mini: Enabling
Efficient Text-to-Speech Inference Across Consumer Computer Hardware






A Thesis by






## Julian L. Salas
## Alethea Joy D. Montoyo






Submitted to the Department of Computer Science
College of Computing and Information Sciences (CCIS)
## Caraga State University – Main Campus






## In Partial Fulfillment
of the Requirements for the Degree
Bachelor of Science in Computer Science (BSCS)






## November 2025



ii

## APPROVAL SHEET


This thesis entitled Adaptive Hardware Optimization Framework for OpenAudio
S1-Mini:  Enabling  Efficient  Text-to-Speech  Inference  Across  Consumer  Computer
Hardware, prepared and submitted by Mr. Julian  L.  Salas and Ms. Alethea  Joy  D.
Montoyo in partial fulfillment of the requirements for the degree Bachelor of Science
in Computer Science is hereby accepted.



REGIEN B. NAKAZATO MSc.
## Thesis Adviser




## JAMES EARL CUBILLAS
## Chair, Oral Examination Panel




## JOHN MARK CORREA RUDOLPH JOSHUA CANDARE
## Panel Member Panel Member



Accepted and approved for the conferral of the degree Bachelor of Science in
Bachelor of Science in Computer Science in the 2
nd
semester of SY 2025-2026.


## JAYMER M. JAYOMA, ITD
Dean, CCIS






iii

## DEDICATION



To God Almighty, for His boundless grace and wisdom that guided us through this
journey. To our families, whose unwavering love, sacrifices, and belief in us made this
work possible.
To our community at Caraga State University, for fostering an environment where
curiosity and innovation thrive.
























iv

## ACKNOWLEDGMENT



We would like to express our deepest gratitude to all those who contributed to the
successful completion of this thesis.
First and foremost, we extend our sincere appreciation to our thesis adviser, Ms.
Regien B. Nakazato, MSc., for her unwavering support, guidance, and encouragement
throughout this research journey. Her invaluable insights and dedication have been
instrumental in shaping this work.
We  are  profoundly  grateful  to  Dr.  Bartosz  Majcher,  PhD,  for  his  exceptional
assistance with formatting, meticulous proofreading, and countless pieces of advice
that helped us curate and refine our paper. His expertise and generosity with his time
significantly elevated the quality of this research.
Special thanks to Mr. John Carlo Tecson and Mr. Jeff Rio Mausisa for graciously
lending  their  computers  and  laptops  for  our  hardware  testing  phase.  Their
contribution was essential in enabling us to conduct comprehensive experiments
across diverse hardware configurations, making this study possible
We would also like to acknowledge the CCIS-ICTCH at Caraga State University for
providing the resources that fostered our research.
Finally, we express our heartfelt gratitude to our families and friends for their
constant encouragement, patience, and understanding throughout this challenging
but rewarding academic endeavor

v

## TABLE OF CONTENTS

APPROVAL SHEET ............................................................................................................. ii
DEDICATION ..................................................................................................................... iii
ACKNOWLEDGMENT ....................................................................................................... iv
LIST OF FIGURES ................................................................ Error! Bookmark not defined.
LIST OF TABLES ................................................................................................................. x
LIST OF EQUATIONS ........................................................................................................ xi
ABSTRACT ........................................................................................................................ xii
CHAPTER 1 INTRODUCTION ............................................................................................... 1
1.1 Background of the Study ................................................................................................... 1
1.2    Statement of the Problem ................................................................................................ 2
1.3    Objectives of the Study ..................................................................................................... 3
1.4    Significance of the Study .................................................................................................. 4
1.5    Scope and Limitation of the Study ................................................................................... 5
CHAPTER 2.  REVIEW OF RELATED LITERATURE ............................................................ 6
2.1    Theoretical Framework ..................................................................................................... 6
2.2 OVERVIEW OF VOICE SYNTHESIS TECHNOLOGIES ............................................................ 7
2.2.1    Evolution from Traditional to Neural Approaches .............................................. 7
2.2.2    Neural text-to-speech architectures .................................................................... 8

vi

2.2.2    Neural Vocoders .................................................................................................. 10
2.3    Zero-shot Voice Cloning and Speaker Adaption ............................................................. 11
2.3.1    Speaker Embedding Architectures ..................................................................... 11
2.3.2   Contemporary Zero-Shot Systems ...................................................................... 12
2.4   Prosody Modeling and Emotional Speech Synthesis ...................................................... 12
2.5   Contextual Understanding In Speech Generation .......................................................... 13
2.6 Hardware-Aware Optimization for Resource-Constrained Deployment ......................... 15
2.6.1   Computational Challenges of Neural TTS Deployment ...................................... 15
2.6.2   Thermal Constraints In Fanless Devices .............................................................. 16
2.6.3   Model Quantization Strategies ........................................................................... 17
2.6.4 Cross-Platform Deployment with ONNX Runtime ............................................... 19
2.7 Identified Gaps and Problem Positioning .......................................................................... 19
2.8 Problem Positioning ........................................................................................................... 21
CHAPTER 3 METHODOLOGY .......................................................................................... 22
3.1    Introduction ..................................................................................................................... 22
3.2    Research Design .............................................................................................................. 22
3.2.1    Philosophical Stance ........................................................................................... 22
3.2.2    Hypothesis .......................................................................................................... 23
3.2.3    Experimental Strategy ....................................................................................... 23
3.2.4    Variables ............................................................................................................. 24

vii

3.3    Experimental Setup ........................................................................................................ 25
3.3.1    Hardware Configuration Matrix ......................................................................... 25
3.3.2  Software Stack and Dependencies ..................................................................... 26
3.4    System Architecture and Implementation Logic .......................................................... 28
3.4.1    Subsystem A: Hardware Detection and Profiling .............................................. 29
3.4.2    Subsystem B: Configuration Engine .................................................................. 34
3.4.3    Subsystem C: TTS Execution and Monitoring ................................................... 39
3.5    Data Collection ................................................................................................................ 43
3.5.1 Benchmark ............................................................................................................. 43
3.5.1 Benchmark ............................................................................................................. 44
3.6 Performance Metrics and Evaluation Criteria .................................................................. 45
3.6.1 Real-Time Factor (RTF) ......................................................................................... 45
3.6.2 Memory Stability Coefficient (MSC) .................................................................... 45
3.6.3 Throughput ........................................................................................................... 46
3.6.4 Success Rate ......................................................................................................... 46
3.6.5 Output Quality Metrics ......................................................................................... 46
3.7 Data Analysis Methods ...................................................................................................... 47
3.8 Validity and Limitations ..................................................................................................... 47
CHAPTER 4 RESULTS AND DISCUSSION ........................................................................ 49
4.1    Introduction ..................................................................................................................... 49

viii

4.2    Aggregate System Stability ............................................................................................ 49
4.2.1     Rate Validation ................................................................................................... 49
4.3    Computational Efficiency Analysis .................................................................................. 51
4.3.1     Real-Time Factor (RTF) Hierarchy ...................................................................... 51
4.3.2     The “MPS” Paradox .......................................................................................... 52
4.4    Resource Utilization and Management ......................................................................... 53
4.5    Scalability and Optimization Efficacy ............................................................................. 57
CHAPTER 5   SUMMARY .................................................................................................. 62
5.1 Summary of Contributions .............................................................................................. 62
5.2    Findings ........................................................................................................................... 62
5.3 Limitations ......................................................................................................................... 63
REFERENCES .................................................................................................................... 64
APPENDICES .................................................................................................................... 69
Appendix A: Smart adaptive backend implementation details ............................................ 69
A.1 HARDWARE PROFILING (SUBSYSTEM A) ............................................................... 69
A.2 CONFIGURATION ENGINE (SUBSYSTEM B) ........................................................... 74
A.3 TTS EXECUTION AND MONITORING (SUBSYSTEM C) ........................................... 79
Appendix B: Turnitin AI and Similarity Report ....................................................................... 82
Appendix C: Certificate of Substantial Use ............................................................................ 83
BIONOTE .......................................................................................................................... 84

ix

## LIST OF FIGURES
Figure 3.1 Hardware Detection and Profiling Architecture ........................................... 30
Figure 3.2 Hardware Detection and Profiling Subsystem ............................................. 32
Figure 3.3 Intelligent Configuration Selection Pipeline ................................................. 34
Figure 3.4 Subsystem B: Configuration Engine .............................................................. 37
Figure 3.5 TTS Execution and Monitoring Pipeline ........................................................ 39
Figure 3.6 Subsystem C: TTS Extraction and Real-time Monitoring (A) and (B) ........... 41
Figure 4.1 Comparative analysis of Real-Time Factor (RTF) across hardware ............... 51
Figure 4.2 Absolute memory consumption and Safety Thresholds ............................. 53
Figure 4.3 Temporal Analysis of Memory Allocation Across Processors ...................... 54
Figure 4.4 Kernel density estimation of CPU utilization ................................................ 56
Figure 4.5 Efficacy of INT8 Quantization on RTF and Throughput ............................... 57
Figure 4.6 Latency Decomposition by Pipeline Stage ................................................... 58
Figure 4.7 Projected Synthesis Time as a Function of Input Text Length. ................... 59
Figure 4.8 Normalized Performance Heatmap of Tested Configurations .................... 60


x

## LIST OF TABLES


Table 3.1 Utilized hardware environments ..................................................................... 26
Table 3.2 Platform Parameters ....................................................................................... 38
Table 4.1 System Stability Summary ............................................................................... 50
Table 4.2 Consolidated Efficiency and Stability Metrics Across Hardware .................. 50


xi


## LIST OF EQUATIONS
Equation 3.1 Real-Time Factor (RTF) Calculation ........................................................... 45
Equation 3.2 Memory Stability Coefficient (MSC) ......................................................... 45
Equation 3.3 Autoregressive Semantic Token Throughput .......................................... 46
Equation 3.4 Comparative Delta (%∆) for RTF Performance Improvement ............... 47






xii

## ABSTRACT

Newer Large Language Models (LLMs) and text-to-speech (TTS) systems using
neural networks (like OpenAudio S1-Mini) do a remarkably human-like job on the Seed-
TTS Eval tests (OpenAudio, tackling them with a word error rate of 0.011 and a
character error rate of 0.005). But using them usually means needing powerful,
expensive server computers. Running a 400 million parameter model on a normal
computer, phone or laptop is hard because of crashes, running out of memory, and
things being too slow.
This research presents Smart Adaptive Backend, a way of improving things so that
anyone can use the best TTS. It deals with three main issues: first, programs crashing
because of memory problems with graphics cards with under 6GB of VRAM; second,
ways things are done differently for each type of computer, specifically how Apple’s
Metal Performance Shaders (MPS) don't pay attention to how much memory is
available; and third, a strange situation with set up, where usual ways to make things
quicker (like INT8 quantization) actually slow things down on certain systems.

We've come up with a system for improving performance at several levels. It uses
quick checks of the computer to firmly limit how much memory is used, quantization
that changes depending on the computer (INT8 for CPUs and Ampere-class CUDA
GPUs, FP16 for other CUDA and MPS), and carefully assigning tasks to different parts
of the processor. When we tested it, it worked on devices previously considered too
weak, like the graphics in an i5 processor and 8GB MacBook Airs, it stopped crashes
and got as much work done as possible.
The most surprising finding is the MPS Paradox: on a MacBook Air M1, switching
off Apple’s MPS processor brought peak memory use down from 7.06GB to 4.12GB (a
71% fall) and only made the real time factor (RTF) 1.7% slower. This finding from
comparing C1 and C5 is why the system will normally run on the CPU for this S1-Mini job
on Apple Silicon.

Keywords: Zero-shot   TTS,   Voice   Cloning,   Hardware   Optimization,   Heterogeneous
Computing, Platform Aware, ONNX runtime, Model Quantization, Resource-
## Constrained Inference



## CHAPTER 1 INTRODUCTION


1.1 Background of the Study

Speech  synthesis  technology  has  seen  significant  progress  since  the
introduction of Transformer models. One of the most important improvements is
voice cloning using a few seconds of audio samples and reproducing speaker’s voice.
However, despite the recent advances in the area, there is still a wide gap between the
capabilities of today’s models and availability to average end-users. State-of-the-art
text-to-speech synthesizers are either hidden behind closed APIs or locked behind a
subscription wall. Some TTS models require high-end hardware such as NVIDIA A100
or H100 GPUs to be utilized effectively. Consequently, individual users or researchers
cannot access advanced TTS models since such models consume significant computing
power  and  memory.  Contemporary  models  of  TTS  systems  have  high  memory
bandwidth  requirements  for  decoding  and  require  VRAM  capacity  to  compute
attentions.
Inference on consumer devices that do not possess discrete GPUs or mid-tier
hardware leads to a multitude of problems such as out-of-memory, throttling due to
overheating on fanless devices, and very high latencies (Real-Time Factors > 70x).
As  demonstrated  by  empirical  evidence  obtained  in  device-side  machine
learning practice, runtime performance depends not only on model architecture but
also stability and effective use of resources across multiple devices. For instance, as



## 2
shown by the Talaria toolkit created by Apple, developers should take into account
model size, latency, and power efficiency in order to provide optimal performance in
deployment. Unfortunately, the most common approach of one-size-fits-all model in
numerous open-source projects fails to account for the diversity of consumer devices,
which results in sub-optimal performance in cases like Apple Silicon or even older Intel
CPUs.
The purpose of the thesis is to develop a Smart Adaptive Backend aimed to be
used alongside complex neural network architectures for text-to-speech and other
tasks.

1.2    Statement of the Problem

The OpenAudio S1-Mini is a prototype of an advanced TTS technology in a compact
device; however, the basic version lacks understanding of hardware limitations to
ensure consumer-grade usability. Functionally, most inference pipelines implement a
“fail first” philosophy by trying to reserve resources that are inaccessible in the low-
end configurations:
- Classic  auto-detectors  ignore  VRAM  overheads.  In  practice,  even  GPUs
equipped with less than 6 GB of VRAM (like the NVIDIA RTX 3050 4GB and RTX
4050 6GB) try to claim up to 6 GB of space while performing inference. The
effect  results  in  increased  swapping operations,  which  either  increase
inference time or crash the OS.



## 3
- There is no comprehensive support for non-CUDA platforms. On Apple M1
processors, common PyTorch implementations lack restrictions on Unified
Memory usage, leading to RAM consumption rates of over 98%, which may
result in freezing the OS.
- Optimization methods cannot be easily generalized across different platforms.
Advanced optimization methods for NVIDIA cards, such as INT8 quantization,
when implemented carelessly due to the absence of a particular kernel, may
lead to a tremendous slowdown (up to 95 times) when used on Apple MPS or
## CPU.

1.3    Objectives of the Study

The primary goal is to create and verify the Smart Adaptive Backend system for
inference on the Fish-Speech/OpenAudio S1-Mini model, which should provide stable
performance on under-resourced hardware
## Specific Objectives:
- To create an engine to profile hardware by dividing the possible host
environment into performance classes (High-end CUDA, Apple Silicon, CPU
only) before launching the model.
- To build a dynamic system of memory budget management, which sets
VRAM/RAM limits depending on the class of the host hardware, preventing
OOM (out of memory) on systems with 8GB or 4GB of RAM.



## 4
- To design optimization techniques suitable for different platforms, such as
INT8 quantization for Intel CPU and FP16 optimization for Apple MPS, in
order to achieve optimized execution of each particular instance.
- Implement  the  thermal-aware  scheduling  system  for  fanless  devices
(especially  the  MacBook  Air  M1)  predicting  performance  deterioration
when running inference for an extended period of time.
- Verify the proposed solution using benchmarks on success rates, memory
use, and Real-Time Factor (RTF) on a wide range of consumer hardware,
from Intel i5 to NVIDIA V100 clouds.

1.4    Significance of the Study
This research brings both theoretical knowledge and methods that could make
neural TTS resource efficient. These approaches would be useful for a wide variety of
computer  configurations.  Open  source  communities  can  benefit  from  having  a
platform to run large Transformer architectures using less expensive hardware than
cloud GPUs. The use of APIs and their fees become a problem only after integrating
such applications in products for which you would have to run an extra server. In this
case, voice cloning services become more affordable for developers and startups.
From a user’s point of view, it would improve privacy and allow the use of AI offline.





## 5
1.5    Scope and Limitation of the Study

This  research  pertains  to  inference  optimization  for  the  Fish  Speech  model
(OpenAudio S1-Mini). The Smart Adaptive Backend is optimized for consumer-grade
devices running Windows, Linux (WSL2), and macOS operating systems. Device types
covered by the optimization include CPUs (Intel Core processors (11th gen and above)),
graphics processing units (AMD Ryzen series and NVIDIA RTX + V100 series) and Apple
Silicon (M-series).
## Limitations:
- Optimization of model training for fine-tuning has not been considered due to
its extremely expensive nature on lower-end devices.
- At present, there are issues with the backend “safe” settings that force mid-
range GPUs to run in CPU-only mode in order to avoid system crashes; thus, the
device is not fully utilized.
- Some optimization techniques such as quantization of layers may be specific to
the  Transformer-based  structure  of  the  S1-Mini  model  and  difficult  to
implement in diffusion-based text-to-speech models.
- Listening  tests  for  perceptual  speech  quality  have  not  been  included.  As
quantization and back-end changes might affect the naturalness of generated
speech, MOS ratings and/or Word Error Rates measured through ASR should
be conducted for the output samples before submitting them.



## CHAPTER 2.  REVIEW OF RELATED LITERATURE


## 2.1    Theoretical Framework

The current paper relies on three theories: neural network optimization, hardware-
software co-design, and adaptive systems theory. The neural network optimization
framework provides the theoretical basis for model compression techniques such as
quantization, pruning, and knowledge distillation (Hinton et al., 2015; Han et al., 2015;
Gholami et al., 2021). These approaches minimize computational power and memory
usage without affecting the quality of the model. The fundamental assumption of
these techniques is that most neural networks are over-parameterized and can be
safely  compressed  (Frankle  &  Carbin,  2019;  Han  et  al.,  2015).  It  is  essential  for
facilitating deployment on low-end devices.
The hardware-software co-design paradigm focuses on automatic detection of
hardware properties and configuration of optimization algorithms (Yang et al., 2020;
Zhao, 2022; Ham et al., 2021). This field recognizes that inference settings should adjust
to specific computing environments (Memeti & Pllana, 2021; Fayyazi et al., 2025).
Instead  of  striving  for  a  universal  software  solution,  the  authors  advocate  for
middleware capable of adapting to a wide range of computing hardware including but
not limited to CUDA cores and the Apple Neural Engine (Yang et al., 2020; Zhao, 2022).
Finally, adaptive systems theory explains how dynamic resource allocation and
adaptation of performance happen in practice. It involves handling thermal limits and



## 7
memory  pressure,  especially  in  consumer-grade  fanless  devices,  where  external
conditions  and  continuous  loading  force  systems  to  act  and  adapt  to  new
circumstances. Adaptive systems theory is applied in terms of monitoring resources
and reconfiguring them according to the available hardware capabilities and runtime
information. This approach fills a notable gap left by the deployment frameworks.
The  current  work  takes  an  empirical  engineering  approach  based  on  the
aforementioned theories. The focus is not on innovative architectures for models.
Instead, the paper proposes a method for intelligent deployment of existing models
for  achieving  state-of-the-art  text-to-speech  synthesis  (TTS)  using  the  right
middleware tools. This reflects current trends in democratizing AI technology. The
gaps that exist between lab experiments and deployment can be attributed to poor
optimization rather than limitations inherent to deep learning itself.

## 2.2 OVERVIEW OF VOICE SYNTHESIS TECHNOLOGIES
2.2.1    Evolution from Traditional to Neural Approaches

Voice synthesis technology has developed through three different stages. The
first stage involved format synthesis, whereby voices were generated from acoustic
parameters based on acoustic models. The produced voices were clear but robotic and
unrealistic (Tan et al., 2021; Klatt, 1987). The second approach involved concatenative
synthesis where the phonetic sounds used to generate voices were constructed from
large databases of natural phonetics (diphones or triphones). Though the prosodic



## 8
aspects were enhanced, there was still a problem with segment transition, as well as
requiring storage space for databases (Tan et al., 2021; Hunt & Black, 1996).
The advent of Statistical Parametric Speech Synthesis (SPSS) marked a change
in voice synthesis approach to be more data-based. SPSS modeled acoustic parameters
by the use of Hidden Markov Models (HMMs) and Gaussian Mixture Models (GMMs)
to generate voices, which had the advantage of allowing for voice modification using
small databases (Black, 2006; Zen et al., 2013). However, SPSS over-smoothed the
acoustic parameter trajectory leading to “muffled” voices (Zen et al., 2013)

2.2.2    Neural text-to-speech architectures

Neural TTS signifies a paradigm change where deep learning architectures
achieve an entirely new level of naturalness (Tan et al., 2021; Ning et al., 2019). Modern
systems rely on Transformer architectures to model speech based on long-range
dependency techniques in speech (Łajszczak et al., 2024; Guo et al., 2024). The BASE
TTS framework stands as one example of such a paradigm driven by scale where a
Transformer of 1 billion parameters is trained on 100,000 hours of speech to yield
emergent properties (Łajszczak et al., 2024).
The  architecture  can  be  divided  between  autoregressive  and  non-
autoregressive systems, which have different pros and cons based on different use
cases. Autoregressive systems like VALL-E (Wang et al., 2023) and SPEAR-TTS model
acoustic tokens by conditioning on the output from previous frames. While such
systems provide great results in terms of speech quality, there are challenges of



## 9
latency and hallucination, such as word repetition and word omission. In order to
eliminate monotonic alignments, which cause those issues, decoder-only Generative
Transducers are used in VALL-T systems (Du et al., 2024).
As a solution to those problems, non-autoregressive TTS systems are used to
eliminate sequential dependencies for inference speedup. For example, MaskGCT is
using masked generative codecs to predict semantic tokens based on SSL models
without  the  use  of  any  text-speech  alignments  (Wang  et  al.,  2024).  Moreover,
Supertonic TTS uses flow-matching approaches to generate mel-spectrograms based
on text encoding to get much faster convergence than autoregressive systems (Tan et
al., 2025). In general, neural TTS evaluation can be done based on the real-time factor
## (RTF).
This metric reveals substantial variation across deployment targets: lightweight
models like EfficientSpeech achieve RTF exceeding 100x on embedded hardware such
as Raspberry Pi (Atienza, 2023), while large-scale industrial deployments target RTF
values below 1.0 to enable real-time interactivity. Achieving sub-1.0 RTF with billion
parameter models often requires novel architectural innovations, such as replacing
Transformer  components  with  ConvNeXt  encoders  to  bypass  computational
bottlenecks (Okamoto et al., 2024).
The computational demands of these architectures with models ranging from
400 million to 4 billion parameters creates a significant deployment challenge on
consumer hardware. Such models need a lot of memory bandwidth for autoregressive
decoding and a lot of VRAM for attention mechanisms. This balance between the



## 10
complexity of the model and its resource requirements is one of the obstacles to
delivering modern speech synthesis capabilities

## 2.2.2    Neural Vocoders

The neural vocoder can be considered an important component responsible for
mapping  intermediate  acoustic  representations  (like  mel-spectrogram  or  latent
tokens) into a waveform output format. Currently, modern vocoder models include
several types such as autoregressive vocoders (e.g., WaveNet, WaveRNN), generating
samples  progressively  (van  den  Oord  et  al.,  2016);  flow-based  vocoders  (e.g.,
WaveGlow), making use of invertible transformations (Prenger et al., 2019); and GAN-
based vocoders (HiFi-GAN, Vocos), which allow for high-fidelity parallel generation
(Kong et al., 2020; Suizdak, 2023).
Among recent developments, there is an interesting trend toward using the
codec-based approach based on encoding speech as discrete semantic tokens. For
example, FireRedTTS is a good illustration of this concept and can perform in-context
learning similar to that done by Large Language Models (LLMS) due to the speech-to-
token conversion (Guo et al., 2024a). However, the reconstruction quality of the
vocoder is critical to the naturalness of end-to-end synthesis. In sophisticated cases,
Residual Vector Quantization (RVQ), which reduces the reconstruction error, can be
used  (Défossez  et  al.,  2022).  Modern  tendencies  involve  creating  end-to-end
frameworks where the acoustic model and vocoder components work cooperatively
(Tan et al., 2021; Bataev et al., 2025).



## 11
2.3    Zero-shot Voice Cloning and Speaker Adaption

Voice cloning zero-shot is defined by the ability of the TTS system to create the
voice of the unknown speaker through voice synthesis without fine-tuning the system.
Zero-shot voice cloning is what makes modern TTS systems different from previous
multi-speaker techniques due to the latter requiring vast amounts of data to be
trained. According to research, it takes only 6-10 seconds of reference audio to reach
high-quality voice cloning using modern models, and gains in quality are minimal after
20 seconds (Zhu, 2023; Qin et al., 2024; Cooper et al., 2020).

## 2.3.1    Speaker Embedding Architectures

Early zero-shot approaches make use of global speaker embeddings that are
produced via fixed-dimension embeddings from training speaker verification models
with  the  Generalized  End-to-End  loss  (GE2E)  (Wan  et  al.,  2018).  Although  global
embeddings are highly computationally efficient, embeddings that have dimensions
between 128 and 512 are not capable of capturing localized speech properties such as
prosody and pronunciation (Jia et al., 2018; Cooper et al., 2020). Such limitations are
especially noticeable in cross-lingual speech synthesis due to the high degree of
variability in articulation behavior of phonemes across speakers.
The shortcomings in early approaches have been tackled by utilizing content-aware
fine-grained  embeddings  that  incorporate  attention  mechanisms  from  references
(Chen et al., 2022). Such an improvement allows the model to learn how each speaker



## 12
pronounces particular phonemes and guarantees that pronunciation properties will be
accurately preserved during synthesis alongside speaker identity.

2.3.2   Contemporary Zero-Shot Systems

Latest innovations in this field have clearly distinguished between speaker identity
embedding and speaking style modeling, which in turn allows individual control of
voice features. ControlSpeech adopts a two-codec system that makes it possible to
clone the voice of a target speaker while manipulating prosody arbitrarily based on
text prompts without requiring separate training for different emotions and styles
(Guo et al., 2024b). Such decoupling is a huge step forward in terms of controllability.
In  another  research  direction,  DS-TTS  introduces  a  Dual-Style  Encoding  Network
(DUSEN) with complementary style encoders that communicate with each other using
the  Style  Gating-Film  framework  (Wang  et  al.,  2025b).  It  solves  the  problem  of
synthesis inconsistency due to differences in sentence length by applying global and
local encoders.

2.4   Prosody Modeling and Emotional Speech Synthesis

The characteristics of prosody include pitch, rhythm, stress, and intonation, among
others. Generating prosody using neural speech synthesis is not an easy task; after
many years of research and developments in this field, creating diverse prosody
patterns through computation and algorithm still proves challenging. The critical



## 13
problem  in  synthesizing  prosody  can  be  referred  to  as  the  semantic-acoustic
information bottleneck because the phonemic system eliminates all semantic context
information needed to create natural prosody. Hence, the result produced has flat,
boring prosody which may appear robotic and lack emotional appeal. This is especially
true during cases involving long-range dependency where the model has to maintain
the  contextual  knowledge  from  word  to  word  within  a  sentence  to  apply  the
appropriate intonation and stress.
There have been various recent advancements to deal with this problem using
different  architecture  approaches.  Modern  models  improve  the  controllability  of
prosody  through  reference  encoder  architectures  which  allow  prosodic
representations to be obtained from an exemplar utterance utilizing strategies like
Global Style Tokens (Wang et al., 2018) or VAE based prosody encoder which enables
continuous  prosodic  distributions  to  be  generated.  In  another  approach  called
decoupled codec which allows both zero-shot speaker cloning and prosody adaptation
to be done using textual prompt (Guo et al., 2024b); in addition, there are dual-style
encoding networks with complementary style encoders which overcome the problem
of synthesis consistency at different sentence lengths (Wang et al., 2024b).

## 2.5   Contextual Understanding In Speech Generation

The notion of contextual awareness in TTS involves the ability of a system to
combine linguistic, semantic, and pragmatic data to create contextual-appropriate
speech with proper stress, intonation, and prosody (Guo et al., 2024; Jiang et al., 2023).



## 14
It  is  what  makes  advanced  TTS  capable  of  generating  naturalistic  speech  in
conversational contexts as opposed to basic TTS systems that are syntactically correct
but semantically inconsistent.
Modern  language  models  employed  for  TTS  systems  automatically  acquire
knowledge of the hierarchical nature of human language based on pre-training on
massive text corpuses (Guo et al., 2023c; Jiang et al., 2023). Multi-Scale Acoustic
Prompts  utilize  this potential  of  language  models  by  giving  them  hierarchical
contextual knowledge at various scales from world level to the sentence level to
control TTS output based on context.
Hierarchical context modeling is required for addressing the problem of long-form
synthesis. The proposed solution to this challenge involves using a hierarchical codec
language model (HALL-E), which operates in two stages – prosody planning and
refinement of detailed acoustic information (Le et al., 2024). Such an approach helps
avoid problems related to prosodic drift and accumulation of errors associated with
autoregressive models.
In recent works on speech synthesis, the focus has been on modeling the realistic
elements of hesitation, pause, and self-correction common to natural speech (Zhou et
al., 2024). Such research is premised on the understanding that fluent speech synthesis
is often perceived as artificial when used in conversations where it is common to have
hesitations, rephrasing, and corrections.




## 15
2.6 Hardware-Aware Optimization for Resource-Constrained Deployment
2.6.1   Computational Challenges of Neural TTS Deployment

The application of large-scale TTS models with 400 million parameters and higher
on consumer devices involves intrinsic technical difficulties associated with memory
bandwidth  and  VRAM  consumption.  According  to  literature  sources,  the  user-
friendliness of a model's operation is determined not only by the inference speed itself
but also by stability, resource efficiency, and heat generation characteristics—factors
often neglected in performance-centric benchmarking studies (Hohman et al., 2024;
## Tan & Cao, 2024).
Despite the considerable computational power provided by professional GPUs,
such as the NVIDIA V100 and H100 (with up to 80 GB VRAM), consumer devices can be
equipped with various types of GPUs, including discrete GPUs with 8-24 GB VRAM,
shared memory configurations, and systems running in CPU-only mode (Hohman et al.,
2024; Tan & Cao, 2024). Such heterogeneity necessitates the employment of dynamic
optimization methods capable of selecting appropriate approaches depending on the
characteristics of the hardware at hand, in contrast to static solutions targeting a
particular type of device (Yang et al., 2020; Ham et al., 2021).
Device-specific issues exacerbate the problem through the "configuration paradox"—
the situation where commonly utilized optimization algorithms lead to performance
deterioration  on  some  devices.  For  example,  the  Metal  Performance  Shaders
architecture implemented by Apple Silicon provides high-level abstraction layers for
coding for the M series processors (Hubner et al., 2025). However, Metal Performance



## 16
Shaders does not offer sufficient INT8 quantization capabilities. Thus, an optimization
approach efficient on NVIDIA CUDA-based systems can result in fallback to CPU
operations on Apple devices, causing a significant reduction in performance compared
to non-optimized code.
Unlike  other  approaches,  the  CUDA  technology  offered  by  NVIDIA  ensures  a
sophisticated  approach  to  virtual  memory  management  through  the
cuMemAddressReserve  and  cuMemMap,  functions.  Unified  Memory  makes  the
process of writing code easy as the data is transferred from the CPU to the GPU
automatically. Prefetching and the use of hints will lead to improved performance.
Consumer GPUs that do not have at least 6 GB of VRAM require efficient memory
budget management to prevent detrimental memory swapping.

## 2.6.2   Thermal Constraints In Fanless Devices

Management  of  the  device's  thermal  state  represents  one  of  the  crucial
constraints for fanless consumer devices such as Apple's MacBook Air. In a prolonged
computational effort, the system starts thermal throttling in just a few minutes,
reducing  CPU  frequencies  from  their  maximum  possible  value.  Accounts  from
community discussions and technical evaluations show temperatures rising up to 80-
90°C during intensive work, while there is even mention of thermal throttling kicking
in after two or three minutes.
From the perspective of TTS inference computations, thermal throttling manifests
itself in a gradual increase in the processing time during lengthy synthesis. The initial



## 17
request may take less than real-time, but, as time goes on, the computation becomes
less efficient as thermal safety measures come into play and lead to the RTF growing
above acceptable levels. While individual performances might be comparable to fan-
assisted systems, the long-term effects of thermal throttling become evident when
sustained workload is applied.
The absence of a fan means that the primary focus of the fanless design is noise
reduction and small size, trading off efficiency under high loads. Most research on
thermal aware scheduling has considered only stationary cases of embedded/mobile
inference with a fixed heat profile (Tan & Cao, 2024). It makes the current situation
different as there is no established thermal behavior during adaptive TTS computation.

## 2.6.3   Model Quantization Strategies

Quantization  represents  the  major  factor  behind  model  compression  and
accelerating  inference  on  hardware  with  restricted  capacities.  Quantization
transforms FP32 representations to low-precision ones: FP32 to FP16 leads to two
times smaller model size, and FP32 to INT8 makes the size around four times smaller
(Wu et al., 2024; Gholami et al., 2022). State-of-the-art GPUs support execution units
aimed at low-precision calculations, which makes INT8 operations perform two to four
times better in comparison with FP32 calculations on equal hardware.
The process of quantization can be split into post-training quantization (PTQ) and
quantization-aware training (QAT) (Gholami et al., 2022; Jacob et al., 2018). PTQ allows
applying the procedure to already trained models without modifying the training



## 18
pipeline. It uses the set of calibration data (up to 1,000 examples) and finds scaling
factors minimizing quantization errors. The described approach is useful in case of
prohibitively  expensive  retraining.  On  the  other  hand,  QAT  involves  adding  fake
quantization nodes to the training process and exposing the model to quantization
impact, leading to higher accuracy compared to PTQ, especially for aggressive INT8
quantization (Jacob et al., 2018).
To  solve  the  "outlier  problem,"  modern  algorithms  use  mixed  precision
quantization. Small parts of weights and activations are crucial in terms of model
performance, and their high contribution justifies preserving them at higher precision
levels. As a result, quantization involves FP16 outliers and INT8 quantization of all other
values, leading to an improved model and reduced memory consumption (Micikevicius
et al., 2018; Dettemers et al., 2022). Additionally, layer-wise analysis reveals critical
layers that should be preserved at FP16.
The hardware issues related to particular hardware architectures have a strong
impact on selecting the quantization method. FP8 quantization shows almost no
losses in terms of accuracy on different platforms, thus making it the best approach to
apply at large batch sizes (at least 16). However, when working with small batches,
weight-only quantization techniques like INT4 Activation-aware Weight Quantization
(AWQ) are better to use due to memory bandwidth restrictions and lack of quantized
activations (Lin et al., 2024). Regardless, the hardware-specific restrictions mean that
using INT8 quantization indiscriminately may be counterproductive.



## 19
2.6.4 Cross-Platform Deployment with ONNX Runtime

The ONNX Runtime is an industry-standard inference runtime engine that provides
fast model inference through various computing devices such as CPUs, GPUs, and
dedicated accelerators. This runtime framework utilizes graph-level optimizations like
operator fusion,  constant  folding,  and  kernel  selection  before  partitioning  the
computation  across  available  hardware.  Without  any  hardware-accelerated
computing, ONNX Runtime has been shown to achieve performance improvements of
around 1.5x to 2x when compared to original training frameworks.
Other frameworks are useful for cross-platform optimization of deep learning
models. For example, the Intel Extension for PyTorch allows mixed precision training
with  bfloat16  and  yields  considerable  speedups  while  performing  training  and
inference operations using discrete Intel GPUs. The framework allows users to use XPU
devices  through  simple  API  adjustments  and  hides  the  details  of  hardware
optimizations. Research studies have shown that an end-to-end optimized approach
involving  changes  to  architecture,  quantization,  compiling  optimizations,  and
scheduling can lead to up to 6x improvement in performance on consumer hardware
platforms (Wu et al., 2024; Gholami et al., 2022).

2.7 Identified Gaps and Problem Positioning
Despite  significant  breakthroughs  in  the  field  of  neural  TTS  architecture  and
individual optimization, there are still significant shortcomings with respect to actual
implementation on affordable consumer hardware:



## 20
## Gap 1: Universal Adaptive Optimization Frameworks
The majority of the current methods of optimization typically require manual setup
based on an understanding of the hardware. While individual optimization methods
have proven to be efficient in experiments, none of them provide a method for
combining the different types of optimization with platform specificity. There is a
configuration dilemma in the current research: typical optimization techniques may
lead to performance degradation on some platforms (e.g., INT8 quantization on Apple
## MPS).
Gap 2: Thermal-Aware Inference Control
Most studies concerning neural networks' deployment assume a thermal stable
environment, which aligns well with server settings that employ cooling mechanisms
(Tan & Cao, 2024). However, fanless consumer gadgets face substantial thermal
throttling,  resulting  in  subpar  performance  levels,  as  evidenced  by  technical
assessments geared toward consumers. Current studies on heat generation consider
dynamic  usage  patterns  but  lack  research  that  involves  heat  prediction  control
mechanisms aimed at maintaining desirable throughput amid thermal variations.
Gap 3: Management of Memory Pressure Handling for Integrated Graphics
Studies on optimizations are limited to testing their effectiveness with discrete
GPUs having dedicated VRAM or systems solely relying on CPUs without considering
integrated  graphic  cards  that  use  system  memory  along  with  other  applications
running concurrently with the operating system (Hubner et al., 2025). The usage of
such memory makes the process vulnerable to changing memory pressures depending



## 21
upon  the  workload;  hence, it  requires  memory  budgeting  to  be  managed  in  an
adaptive way rather than allocating static VRAM.

## 2.8 Problem Positioning

The above-mentioned problems are being addressed in this research by developing
a comprehensive system of adaptive optimization. This system is based on three main
modules,  including:  (1)  Dynamic  Hardware  Profiling,  wherein  host  machines  are
profiled  into specific  performance  classes  prior  to  running  models  in  order  to
proactively choose an appropriate configuration while avoiding any issues associated
with the use of a particular platform; (2) Adaptive Optimization Selection, wherein
platform-specific approaches (INT8 quantization on Intel CPUs, FP16 optimization on
Apple MPS, and mixed precision on NVIDIA GPUs) are implemented according to the
capabilities of hardware as opposed to one-size-fits-all optimization choices; and (3)
Thermal and Memory Pressure Management, wherein potential performance drops
caused by a lack of cooling systems on consumer-grade hardware are anticipated and
memory  requirements  of  integrated  GPUs  are  adapted  accordingly  in  order  to
guarantee adequate throughput.








## CHAPTER 3 METHODOLOGY


## 3.1    Introduction

In this chapter, the methodology of designing, implementing, and validating
the  Smart  Adaptive  Backend  will  be  presented.  A  quasi-experimental  research
approach will be taken based on a quantitative analysis framework where the main
focus  lies  on  benchmarking.  The  objective  of  this  chapter  is  to  examine  the
effectiveness of platform-based optimizations in contrast to traditional “out-of-the-
box” inference.
As previously described, a series of benchmarks will be run on different platforms in
order to find out how effective the backends are when trying to overcome the
particular bottlenecks found in each platform: memory bandwidth limitations, heat-
related  performance  degradation,  and  suboptimal  instruction  sets  used.  In  this
chapter, the research philosophy, hardware diversity of the testbed, systems design
and architecture, and data gathering procedures are going to be explained.
## 3.2    Research Design

## 3.2.1    Philosophical Stance

Viability is the focus of this research. It assumes that the significance of the
proposed model is based on its ability to prevent systems from crashing due to out-of-
memory issues within consumer devices.



## 23
## 3.2.2    Hypothesis
Based on the “configuration paradox” identified in Chapter 2, following technical
hypotheses are tested:
- H1 VRAM Requirement Threshold:
Due to the fact that unoptimized transformer inference requires around 5.97
GB VRAM, requiring CPU offloading or using a quantization fallback mechanism
on GPU with VRAM capacity below 6.0 GB should result in lower probabilities
of encountering any overflow problems.
## • H2 Precision Efficiency:
Platform-based  precision  selection  (i.e.,  INT8  for  x86;  FP16  for  MPS)  is
projected to produce higher RTF performance in comparison to the uniform
INT8 method in order to solve the configuration paradox on Apple Silicon
architecture.
## • H3 Thermal Scheduling:
On  fanless  machines,  such  as  MacBook  Air  M1,  the  use  of  burst  thread
scheduling together with thermal management should lead to lower variations
in RTF during a five-minute workload period.
## 3.2.3    Experimental Strategy

Due to the constant nature of the physical properties of computer hardware, a
randomized control trial becomes impossible. Thus, this research utilizes an approach
called a quasi-experiment whereby a Comparative Hierarchical Validation Protocol is



## 24
employed.  The  validation  protocol  ensures  that  correctness  testing  precedes
optimization testing for restricted hardware.
The test hierarchy consisted of the following:
## Stage 1: Functional Validation:
The backend was first executed on NVIDIA V100 in order to validate its basic
functionality in terms of logical consistency and correctness within an unrestricted
setting.
## Stage 2: Functional Validation:
After validating the backend, the experiment continued with moving the system to
the Apple M1 for testing the conversion process from CUDA inference (NVIDIA GPU)
to Metal Performance Shaders (ARM64).
## Stage 3: Constraints Stress Testing:
Lastly, the system was tested under the Intel i5 and AMD Ryzen architectures as a
means of exploring how the system performs when constrained by limited resources.

## 3.2.4    Variables

## • Independent Variable:
Inference  Backend  Configuration  (Baseline  OpenAudio  S1-Mini  vs  Treatment -
## Smart Adaptive Backend).



## 25
## • Dependent Variables:
RTF;  Memory  Peak  Usage  (MB);  System  Stability  (Pass/Fail);  CPU/GPU
## Utilization(%).
## • Control Variables:
Length of input text (77 characters); Duration of reference audio (20.1 seconds);
## Model Seed; Environmental Temperature.
Note:  Environmental  temperature  was  only  monitored  under  macOS  due  to  the
availability of monitoring tools.

## 3.3    Experimental Setup

## 3.3.1    Hardware Configuration Matrix

Purposive sampling was used to choose five different hardware configurations that
can capture specific resource bottlenecks.
## Table 3.1 Utilized Hardware Environments
Config ID Device
## Model
## Processor
## Specs
GPU/Accelerator Memory
## Architecture
## Bottleneck
## Target
C1 MacBook
## Air M1
## (MPS)
## Apple M1 (8
## Core:
## 4P/4E)
## 8-core
Integrated GPU
## (MPS)

8GB Unified
## (LPDDR4X)
## 4.8GB GPU
allocation

## Thermal &
## Unified
## Memory

C2 MSI Thin 15
## (AMD CPU)
AMD Ryzen
## Mobile
## Family 25
## Model 68
## RTX 4050
## Laptop
## (5.996GB
## VRAM)
## 7.2GB DDR5
System RAM
## ~6GB VRAM
## (discrete)
## VRAM
## Boundary
## Condition



## 26
## (6P/12L
threads)

## Memory
## Overflow
## Prevention

## C3 Acer Nitro
5 (Intel
## CPU)
Intel Core i5
## Family 6
## Model 154
## (12P/16L
threads)

## Intel Iris Xe
(Integrated, no
discrete GPU)
## 15.7GB DDR5
(Shared
## Memory)
## Compute &
No GPU
CPU-Only
## Inference
## C4 Cloud
## Instance
(Virtualized
## GPU)
## Intel Xeon
## Family 15
## Model 107
## (8P/8L
cores)

## NVIDIA GRID
## V100D-16A
## 16GB VRAM
## 64GB
System RAM
## 16GB VRAM
## (discrete)
## Unconstrained
## Baseline
(High-
performance
reference)

## C5
MacBook
## Air M1
## (CPU;
controlled
variant of
## C1)
## Apple M1
## (8-core:
## 4P/4E)
## GPU
disabled via
config
## Apple Silicon
## GPU
(Force disabled)
8GB Unified
(CPU-only
allocation)
## Backend
isolation:
same M1
hardware as
## C1, MPS
disabled

3.3.2  Software Stack and Dependencies
The experiment setup was standardized for replicability:
## Core Runtime Environment:
- Python version: 3.12.0
- PyTorch version: 2.1.0+ with platform specific builds
o CUDA version: 11.8 build for Windows NVIDIA GPU systems
- OpenAudio  S1-Mini: Pre-trained  model  (Dual-AR  Transformer,  400M
parameters).




## 27
## Optimization Libraries:
- ONNX Runtime Version: 1.16.0+ for cross platform inference acceleration
- Hardware: AMD Ryzen processor (CPU fallback mode)
o Remark: AVX-512 VNNI optimizations were not available in any of the
consumer hardware devices; ONNX Runtime was running in software
mode.
- Torch  Compile: Optional  library  available  only  for  Linux  CUDA  hardware
systems (disabled for Windows and macOS platforms because of the lack of
Triton Compiler support).
Telemetry and Monitoring:
- Psutil (v5.9.0+): A cross-platform system resource monitoring for RAM usage,
CPU utilization, and thread tracking.
o Nvidia-ml-py3  (NVML  Python  Wrapper): Intended  for  CUDA  VRAM
monitoring on NVIDIA GPUs.
o Implementation  Note: Library  was  not  installed  in  the  deployment
environment; GPU utilization metrics defaulted to 0% in logs.
- GPU memory usage was tracked via PyTorch’s torch.cuda.memory_allocated()
API as fallback.
- Platform-specific thermal monitoring:
o macOS: powermetrics command-line  utility  for  CPU  temperature
sensing (fanless MacBook Air M1)



## 28
o Windows: Attempted  integration  with  LibreHardwareMonitor/Core
Temp  via  WMI  interface  (not   installed   on   test   systems;   thermal
monitoring disabled).
o Linux: sysfs thermal zone reading
(/sys/class/thermal/thermal_zone*/temp) – not utilized in this study.
## Model Components:
- VQ-GAN  Decoder: Firefly  GAN  vocoder  for  semantic  token-to-waveform
synthesis.
- Text2Semantic Model: 28-layer Dual-AR Transformer (1024 hidden dimensions,
16 attention heads, 155,776 vocabulary size).
## Configuration Notes:
- Gradient Checkpointing – An added function on the Fish-Speech repository
which  was  force-disabled  during  inference  to  prevent  memory  overhead
(enabled only during training).
- Mixed Precision – FP16 on GPU systems, FP32 on CPU systems.
INT8 Quantization – Applied selectively to CPU and CUDA configurations; explicitly
disabled on Apple MPS due to performance regression.
3.4    System Architecture and Implementation Logic
Operation  of  the  Smart  Adaptive  Backend  is  made  possible  through  the
cooperation of three subsystems that, when used together, turn low-level hardware
data into optimized and secure inference executions. The first subsystem transforms



## 29
low-level data into a capability profile. The second acts as an engine verifier that
determines which execution option is to be selected from the profile. The third
subsystem carries out the selection.
3.4.1    Subsystem A: Hardware Detection and Profiling
This module executes at initialization (t = 0). It queries the kernel and hardware
registries to construct a capability object.
Figure 3.1 Hardware Detection and Profiling Architecture.

This subsystem executes once at startup and is responsible for building the
HardwareProfile shown in Figure 3.1.  The profiler first queries CPU topology using
psutil.cpucount with logical=False and logical=True, then it applies a platform-
specific solution to infer performance cores on hybrid architectures such as Apple M1,
where standard Python APIs do not expose the P-core/E-core labels.
On Apple Silicon, where torch.backend.mps.is_available() returns true,
the profiler computes unified memory size from psutil.virtual_memory,



## 30
reserves 40% for macOS and other processes and stores gpu_allocation = 0.6
along with total memory_gb in the profile to guide chunk-length decisions.
## Profiling Logic:
The CPU Topology differentiates between physical and logical cores using
psutil.cpu_count(logical=False). On hybrid architectures (Intel 12
th
## Gen,
Apple Silicon), it identifies P-Cores for thread affinity binding.
Implementation Note: The Apple M1 reports 8 physical cores and 8 logical cores,
without explicit P-core/E-core differentiation via standard Python APIs. The backend
assumes the first 4 cores are performance cores based on what was documented in
the Apple M1 architecture specifications, though this cannot be programmatically
verified through psutil alone.
- On  x86  platforms  (Linux/Windows),  the Instruction  Set  Detection profiler
attempts to detect AVX-512 VNNI support through:
Linux à Parsing /proc/cpuinfo for the avx512_vnni flag
Windows à Querying via the cpuinfo library or inspecting CPU feature
flags.
If AVX-512 VNNI is absent, INT8 quantization is flagged as “High Latency Risk”
since hardware-accelerated INT8 operations are unavailable, requiring
software emulation via ONNX Runtime.



## 31
Implementation Note: None of the consumer hardware we tested has an
activated AVX-512 VNN. This was simply put as an additional speed for future
use.
- The Thermal  Sensor  Availability profiler examine platform-specific thermal
monitoring interfaces to determine if real-time thermal throttling detection is
feasible:
- Windows à Queries WMI namespace
root\LibreHardwareMonitor for active sensor providers.
- macOS à Verifies command-line access to the powermetrics utility
- Linux à Scans /sys/class/thermal/thermal_zone* for
kernel-exposed thermal sensors.





## 32

Figure 3.2. Hardware Detection and Profiling Subsystem







## 33
The  hardware  profiling  subsystem  executes  the  following  library  calls  with
platform-specific handling. On all platforms, psutil.cpu_count(logical=False)
returns physical core count (e.g., 12 on Intel i5-1240P, 6 on Ryzen 5 7535HS, 8 on M1),
while psutil.cpu_count(logical=True) returns logical cores including from
efficiency cores via Python APIs; it sets pcores = 4 based on M1 specification (4P+4E),
accepting that psutil reports all 8 cores without labels.
GPU memory detection uses torch.cuda.get_device_properties(0).
total_memory on CUDA devices, returning bytes that are divided by 1e9 to yield
vram_gb (5.996 GB) on RTX 4060, 16 GB on V100).
The VRAM threshold was not chosen by random. Since preliminary testing with a
77-character  input  on  RTX  4050  Laptop  GPU  triggered  OOM  at  ~5.97Gb  peak
allocation, where the backend reports “GPU detected but insufficient VRAM (6.00GB <
6.00GB required)” and forces CPU mode to prevent system-level memory overflow. On
apple silicon, torch.backend.mps.is_available() confirms MPS support, and
psutil.virtual_memory() returns unified memory in bytes. The profiler multiplies
by 0.6 to reserve 40% for macOS and other applications, yielding gpu_allocation
used in later memory budget calculations.



## 3.4.2    Subsystem B: Configuration Engine
This  subsystem  implements  a  deterministic  decision  tree  to  map  hardware
capabilities to inference parameters:
## Figure 3.3 Intelligent Configuration Selection Pipeline.

Subsystem  B  implements  a  deterministic  decision  tree  to  map  hardware
capabilities to inference parameters:
The Configuration Engine gets the HardwareProfile from Subsystem A and
produces  an  Optimal  Config  object  that  specifies  device  selection,  precision,
quantization  strategy,  memory  budget,  and  thermal  management  settings,
implementing the optimization hypotheses of H1-H3 through a four-stage pipeline
shown in Figure 3.2.
On Step 1, it applies a strict VRAM threshold logic. If the HardwareProfile
indicates device_type=”cuda” and gpu_memory_gb >= 6.0, the engine selects
GPU execution, otherwise, it enforces CPU mode even if a GPU is available. This



## 35
decision prevents the OOM behavior observed on RTX 4050 Laptop GPU (5.996GB
VRAM), during preliminary testing with 77-characters inputs.
Step 2 applies the platform-aware precision and quantization rules to avoid the
configuration paradox where indiscriminate INT8 use causes severe performance
regressions. On CUDA devices with Ampere architecture or newer (compute capability
≥ 8.0), the engine selects FP16 precision and enables INT8 quantization for compatible
layers, leveraging dedicated INT8 tensor cores. Apple MPS devices, precision is locked
to FP16 and quantization is disabled to prevent CPU fallback, enabling INT8 on MPS
caused RTF to explode from ~33x to 95x due to unsupported Metal kernels falling back
to CPU execution. For CPU only configurations the engine enables ONNX Runtime INT8
quantization with expected small speedup, recognizing that speedups without vector
instructions  come primarily  from  reduced  memory  bandwidth  rather  than
computational acceleration.
The step 3 computes safe memory budgets and selects chunk length to prevent
allocation spikes that exceed available memory.
For CUDA devices, the engine calculates available_memory_gb = vram_gb x
0.85 to  reserve  15%  for  driver  overhead  and  fragmentation,  then  selects
chunk_length = 1024 when available_memory_gb ≥ 8.0 and chunk_length
= 512 otherwise, mirroring NVIDIA deployment guidelines that recommend against
planning allocations at 100% of theoretical VRAM. For unified memory systems like the



## 36
MPS, the budget is available_memory_gb = memory_gb – 3.0, subtracting a
fixed for macOS overhead, with the same chunk-length selection logic.
On the final step, the thermal-aware scheduling enables (if available) specially on
fanless devices. Unsustain high load triggers throttling. If the HardwareProfile
indicates thermal_capable = True and the CPU model contains “m1 air” for this
example, the engine sets burst_scheduling = True and pins inference thread to
cores, which correspond to the inferred performance cores on Apple M1’s 4P+4E
topology,  leaving  efficiency  cores  idle  to  handle  background  tasks  and  maintain
thermal headroom.
Other platforms, including actively cooled systems like M1 Pro/Max and standard
desktop CPUs, burst_scheduling = False and thread affinity is unrestricted,
allowing the OS to distribute freely.



## 37

## Figure 3.4 Subsystem B: Configuration Engine
VRAM Threshold Enforcement at (Line 4 – 9, Algorithm 3.2), the 5.97GB threshold
prevents catastrophic OOM crashes observed during preliminary testing on NVIDIA
RTX 4050 with a 6GB VRAM. As for the MPS Quantization Constraint at (Line 24 -25,



## 38
Algorithm 3.2), the INT8 quantization on Apple’s Metal Performance Shaders
backend triggers CPU fallback for unoptimized kernels, causes RTF to degrade to
95.64x with INT8 on MPS.
AVX-512 VNNI Detection (Line 34 – 42, Algorithm 3.2), hardware-accelerated INT8
on x86 CPUs requires Vector Neural Network Instructions (VNNI). Without this, it falls
back to software emulation.
## Table 3.2 Platform Parameters
Platform Precision Quantization ONNX Chunk Thread
## Affinity
## CUDA (≥8	퐺퐵)
## FP16
## INT8
## (AMPERE +)

## NO 1024 ALL CORES

## CUDA (<6퐺퐵)
## CPU
## FALLBACK
## FP32
## YES 512 ALL CORES
## M1 AIR MPS
## FP16
## NONE NO 1024 ALL CORES
CPU (No AVX-512)
## FP32
## INT8 YES 512 ALL CORES

A summary of the platform-aware optimization strategies automatically selected
by the Configuration Engine (Algorithm 3.2) for each hardware category tested in this
study. The configuration parameters addressed the three bottlenecks starting from
VRAM threshold enforcement, Precision strategy selection, and the Memory Budget
## Allocation.
As for the VRAM threshold, where the GPUs with <6GBs of VRAM are forced into
CPU fallback to prevent OOM crashes. With the precision strategy applying FP16 for
CUDA and MPS platforms while reserving INT8 quantization exclusively for CPU



## 39
architectures. Memory budget allocation with conservative chunk sized of 512 tokens
for constrained devices with ONNX Runtime acceleration for CPU-only inference.
3.4.3    Subsystem C: TTS Execution and Monitoring
A thread runs concurrently with the inference loop with a sampling rate of
## 퐹
## !
## =1.0퐻푧.

Figure 3.5 TTS Execution and Monitoring Pipeline.
Subsystem C’s implementation of the execution harness, applies the OptimalConfig
from Subsystem B to the OpenAudio S1-Mini/Fish-speech model while continuously
monitoring system state at 1hz.
The subsystem handles three concurrent workflows as shown in Figure 3.3: The
main inference thread executing TTS generation, a monitoring thread sampling
system resources, and a post-synthesis finalization step that computes aggregate
metrics.
Execution begins when a synthesis request arrives at the /tts FastAPI
endpoint in backend/app.py. The backend calls
monitor.start_synthesis(request_id), estimated_token, config) to



## 40
initialize a SynthesisMetrics object with a timestamp anchor (start_time =
time.time()) d ThreadSafeQueue for metric samples. The monitoring thread is
then launched as an asynchronous “coroutine” via asyncio.create-
task(monitor.monitor_loop()), which executes the metric collection loop in
parallel with the main inference.
The Inference itself runs in a thread pool executor
(loop.run_in_executor()) to prevent blocking the async event loop, calling
run_tts_sync() with the user’s text, reference audio, temperature, top_p, and
seed parameters.
Inside this function, the model is invoked with the chunk length, quantization and
thread affinity setting from the OptimalConfig, and the model processes the text
through its pipeline: the LLM generates semantic tokens, the VQ-GAN decoder
converts token to audio features, and the final waveform is synthesized and written
to a WAV file.
When the inference thread completes, monitor.end_synthesis() computes
derived metrics from the accumulated time-series snapshots, implementing the
calculations formalized in Section 3.6, Real-Time Factor (RTF) is calculated as 푅푇퐹=
## !
generation
## !
## )*+,-
, where 푇
## "#$%&
is the length of the generated WAV file parsed from its header.



## 41
Memory Stability Coefficient (MSC) is computed as	푀푆퐶=
## '
mem
## (
mem
, where the
standard deviation and mean are taken over all memory samples collected during
synthesis. MSC values below 0.15 indicate stable plateau behavior, while values at or
above 0.15 suggest oscillations due to garbage collection or memory pressure.
Throughput is calculated as Throughput=
## )
## ./0123
## !
generation

## (
tokens/sec
## )
, using the token
count logged by the OpenAudio S1-Mini/Fish-Speech model during semantic
generation.











Figure 3.6 Subsystem C: TTS Extraction and Real-time Monitoring (A)



## 42

Subsystem C: TTS Extraction and Real-time Monitoring (B)

Subsystem C provides execution monitoring through monitoring.py and
opt_engine.py using thread-safe synchronization.



## 43
When a synthesis request arrives via the /tts endpoint in backend/app/py,
the backend calls monitor.start_synthesis(request_id,
estimated_tokens) prior to the inference, creating a time stamp anchor point,
and initializing the metrics tracking by ThreadSafeQue.
The monitoring routine runs in a separate thread, collecting system state metrics
once every second using psutil.virtual_memory().used,
torch.cuda.memory_allocated(), as well as cpu per-core utilization with
psutil.cpu_percent(percpu=True).

## 3.5    Data Collection

## 3.5.1 Benchmark
To strictly control input variance for equal testing, a fixed prompt was used for all
100% of the trials.
Text Input: “Hello! My name is Bart! I love taking care of my garden and going for
a walk.”
## • Length: 77 Characters, 17 Words.
The above fixed prompt minimizes variance yet lacks generalizability. An empirical
validation requires inclusion of various input lengths, e.g., 100, 200, 400, and 800
characters for testing the projection in Section 4.5.



## 44
- Complexity: Consisting of both punctuation marks and proper sentence
length to fit the Transformer's Context Window, resulting in autoregressive memory
buildup.
Reference Audio: 20.1-second mono Microsoft WAV file with a sample rate of
44.1kHz.
## Generation Parameters:
## • Temperature: 0.7
## • Top-p: 0.9
## • Repetition Penalty: 1.2
## • Max Tokens: 2047.
## 3.5.1 Benchmark
The system creates three datasets collected for every run:
- hardware_specs.json is a detected profile.
- realtime_metrics.csv is a Time-series data
## (
## 푡=0	푡표	푡
## *+$
## )
containing columns:
[timestamp, cpu_%, memory_mb, gpu_util_%, temp_c]
- synthesis_summary.csv aggregate metrics for the run.






## 45
3.6 Performance Metrics and Evaluation Criteria

3.6.1 Real-Time Factor (RTF)

RTF measures the latency of the system relative to the audio output.
## 푅푇퐹=
## !
generation
## !
## )*+,-
## Eq. (3.1)
## 푤ℎ푒푟푒,푡푎푟푔푒푡	푅푇퐹	≤30,퐹푎푖푙	푅푇퐹	>	70
An RTF of ≤ 30.0 serves to set the limit within which offline generation processes
are deemed suitable, where a 10-second audio clip can be synthesized in less than 5
minutes (300 seconds). This is done keeping in mind the constraints posed by
consumer-grade equipment while ensuring that there is still usefulness for the
application, as is the case with audiobook recording and podcasting. The failed state,
where RTF > 70. denotes the point where synthesis is impractical for offline use too,
taking more than 10 minutes per sentence spoken.
3.6.2 Memory Stability Coefficient (MSC)


To quantify the risk of memory leaks or aggressive garbage collection spikes, we
define the MSC:
## 푀푆퐶=
## ,
## 454
## -
## 454
## Eq. (3.2)
## Where 휎
## .*.
is the standard deviation of the Resident Set Size (RSS) during
generation. A value <	0.15 indicates stability



## 46
- MSC = 0.05 = Very stable (5% variation)
- MSC = 0.15 = Moderately stable (15% variation)
- MSC = 0.30 = Unstable (30% variation, risk of memory spikes)

## 3.6.3 Throughput
Defined as the speed of the autoregressive semantic token generation, isolating
the LLM component from the VQ-GAN decoder.

## 푇ℎ푟표푢푔ℎ푝푢푡=
## /
## 6-7589
## !
## :585;)6,-8

## (
## 푡표푘푒푛푠/푠푒푐
## )
## Eq. (3.3)

## 3.6.4 Success Rate

A trial is marked Success only if:
- Synthesis Completes without crashes, memory overflow, or system freeze.
- Output WAV file generated is valid and cloned the referenced voice.
- File duration matches expected duration.

## 3.6.5 Output Quality Metrics

The present experiment focuses on efficiency and stability measures. In view of
the impact of INT8 quantization and CPU fallback on the naturalness of synthesis,
future experiments should include at least one subjective measure such as Mean



## 47
Opinion Score (MOS), comparative MOS, or ASR WER besides RTF, MSC, throughput,
and success rate.

## 3.7 Data Analysis Methods

Analysis is performed using python (pandas, numpy, seaborn).
- We calculate the percentage improvement via the Comparative Delta (%∆)
between the Baseline (Unoptimized) and the Treatment (Smart Backend)
conditions.

## %훥=
## 0!1
## <)95
## 30!1
## -=6
## 0!1
## <)95

## ×100	    Eq. (3.4)

- Thermal Correlation for the M1 Air, a Pearson correlation coefficient (r) is
calculated between die_temperature and tokens_per_second to
statistically quantify thermal throttling.

3.8 Validity and Limitations

With the random seed fixed at seed = 42, sampling behavior is controlled, but
cross-platform differences in kernels and instruction sets still introduce small
numerical non-determinism. As reflected in Table 4.1, token counts vary modestly
(98–108) across backends. We therefore treat single-trial execution as an



## 48
approximation that is sufficient for the relative comparisons in this study, while
acknowledging this source of variability.
On windows systems lacking LibreHardwareMonitor, thermal data is
excluded.
This study validates inference only. Training dynamics (which require
backpropagation and significantly higher VRAM) are outside of the scope of this
methodology.



## CHAPTER 4 RESULTS AND DISCUSSION



## 4.1    Introduction


This chapter presents the validation of the Smart Adaptive Backend. The data was
obtained through the quasi-experimental protocol defined in Chapter 3, benchmarking
five distinct hardware configurations. The analysis evaluates the system’s ability to
balance  Computational  Efficiency  (RTF),  Resource  Stability  (Memory  Safety),  and
## Architectural Adaptability.

## 4.2    Aggregate System Stability

## 4.2.1     Rate Validation
The primary hypotheses of this study is that hardware-aware resource budgeting
would eliminate failures on constrained device.
Result: All synthesis trials achieved a 100% completion rate, generating valid audio
files within expected duration tolerances. This validates the core design objective:
preventing the memory overflow failures that would occur on GPU execution on sub-
6GB VRAM systems.





## 50
## Table 4.1 System Stability Summary
## CONFIG DEVICE STRATEGY APPLIED OUTCOME RTF TOKENS THROUGHPUT
V100 (C4) CUDA BASELINE (FP16) SUCCESS 8.65x 101 2.51
INTEL i5
## (C3)
CPU INT8 QUANTIZATION SUCCESS 27.52x 94 0.79
## M1 MPS
## (C1)
## MPS FP16 / UNIFIED
## MEMORY
SUCCESS 32.83x 107 0.66
## M1 CPU
## (C5)
CPU FP32 (No
quantization)
SUCCESS 33.40x 94 0.65
## RYZEN
## (C2)
## CPU INT8 + ONNX
## RUNTIME
SUCCESS 56.10x 108 0.37

(Note: Minor variations in generated token counts [98 – 108] are attributed to
floating-point  non-determinism  across  different  backend  instructions  sets
Configuration C1 (M1 MPS) was tested during the experimental phase to measure
memory bloat. Based on these findings, we have disabled MPS and defaults to C5 (CPU-
only) for all Apple Silicon devices.)
Table 4.2 Consolidated efficiency and stability metrics across hardware configurations.
## CONFIGURATION MODE  RTF THROUGHPUT PEAK MEMORY MSC
## V100 (C4) CUDA (FP16)   8.6
## 5x
2.51 tokens/s 12.77 GB 0.005
INTEL i5
## (C3)
## CUPE INT8 +
## ONNX
## 27.5
## 2x
0.79 tokens/s 14.0 GB 0.010
## M1 MPS
## (C1)
## MPS (FP16)  32.8
## 3x
0.66 tokens/s 7.06 GB 0.1348
## M1 CPU
## (C5)
## CPU (FP32)  33.
## 40x
0.65 tokens/s 4.12 GB 0.0815
## RYZEN
## (C2)
## CPU INT +
## ONNX
## 56.1
## 0x
0.37 tokens/s 7.3 GB 0.042


The efficacy of the safety protocol is best illustrated by the AMD Ryzen/RTX 4050
configuration. Despite the physical presence of a discrete GPU, the Smart Backend
detected 5.996 GB of usable VRAM, missing the 6.0 GB safety threshold. The system
automatically engaged the mobile_efficient fallback strategy, forcing CPU fallback.



## 51
While this resulted in a higher Real-Time Factor (56.10x), it successfully prevented the
immediate Out-Of-Memory (OOM) crash that occurs when forcing this model onto
6GB cards, verifying Hypothesis 1.

## 4.3    Computational Efficiency Analysis

4.3.1     Real-Time Factor (RTF) Hierarchy
Figure 4.1 Comparative analysis of Real-Time Factor (RTF) across hardware

The  NVIDIA  V100  GRID  configuration  demonstrated  the  highest  performance,
However, the RTF of 8.65x indicates significant overhead. It should be noted that due
to operating under the WDDM (Windows Display Driver Model) rather than the Linux-
specific TCC (Tesla Compute Cluster) mode, there might be kernel latency issues, and
virtualization could cause problems, which may indicate that the pure processing



## 52
power of the Tensor Cores is still insufficient for real-time operation if one does not
optimize OS-level operations.
The Intel i5 and the Apple M1 machines clustered around the 30x mark, showing
that  modern  CPUs,  once  optimized  (INT8),  are  able  to  consistently  perform  the
inferences, albeit slower. The AMD Ryzen 5, forced into CPU fallback to prevent VRAM
overflow but still able to produce valid audio.

4.3.2     The “MPS” Paradox

What sets MPS Paradox apart is that it makes use of the controlled variable –
presence of Apple's MPS backend, making it the most controlled comparison in the
study. In this case, both C1 and C5 use the same hardware: physical MacBook Air M1.
While C1 uses MPS for inference and gets an RTF of 32.83x using 7.06 GB of unified
memory, C5 without MPS shows a similar RTF of 33.40x, which is only 1.7% slower,
consuming 4.12 GB peak memory.
The drop in memory use by a whooping 71% means that the hierarchy for GPU
acceleration has been inverted for the Dual-AR Transformer plus GAN-vocoder: in
terms of inference times, CPU execution is not significantly slower and is much safer
when there's pressure on the unified memory. Thus, the default setting for the Smart
Adaptive Backend for OpenAudio S1-Mini on 8 GB Apple Silicon devices is disabling
MPS, making the CPU version the primary choice.




## 53
4.4    Resource Utilization and Management

4.4.1 Memory Safety and Budgeting
Figure 4.2 Left: Absolute memory consumption and Safety Thresholds.

Figure 4.2 reveals the efficacy of the memory budgeting algorithm. Intel i5 and M1
MPS configurations operated at 89.8% and 88.25% of total RAM respectively. The
system successfully dodged OOM in every test. If it had the backend allocated even
200MB more, the OS would trigger a process kill. The absence of crashes confirms the
precision  of  the  memory  budgeting  algorithm: Budget_safe=(Ram_total) –
3.0GB formula for unified memory architectures, and x  0.85 for discrete GPU
configurations (Algorithm 3.2).






## 54
## 4.4.2 Memory Timeline Stability
Figure 4.3 Temporal Analysis of Memory Allocation Across Processors.

The temporal analysis of memory allocation in Figure 4.3 demonstrates three
distinct memory management stability profiles cross the hardware configurations:
## Phase 1: Modeling Loading (t = 0 - 30s)
All configurations exhibit rapid memory allocation during initial model loading but
with characteristic signatures:
- V100 GRID (green) shows moderate ascent from 11GB to 12.7GB, with large
baseline due to existing GPU memory allocation.
- AMD Ryzen 5 (purple) shows an abrupt spike to 7GB with high initial variance
(6.5-7.3GB  oscillation),  indicating  memory  allocation  struggles  under
constrained 7.2GB total RAM
- Intel i5 (red) has the steepest gradient, climbing from ~2GB to 14GB within 10
seconds, reflecting aggressive pre-allocation of the full model into system RAM.



## 55
- M1 Air (CPU) exhibits a very unique decline from 4GB to 3.5GB with an MSC =
0.0815, representing successful incremental garbage collection. This behavior
confirms that explicit tensor cleanup in the backend is effective and that the
unified  memory  architecture  enables  dynamic  reallocation  to  system
processes.
## Phase 2: Stable Synthesis
Once the initialization process is over, one can notice how the post-initialization
behavior is different from machine to machine in terms of memory stability. First off,
the V100 machine holds consistently at its 12.77 GB plateau, as expected of enterprise-
grade hardware (Memory Stability Coefficient (MSC) = 0.004, σ < 50 MB). Intel i5
shows a consistent 14 GB plateau, having an MSC of 0.010 (σ < 150 MB) despite its 89.8%
RAM utilization.
AMD Ryzen 5 has a volatile plateau near 7.3 GB, showing MSC = 0.042 (σ ~ 300 MB),
well below the previously mentioned instability threshold of 0.15 (Section 3.6.2).
Lastly, the MacBook Air M1 (with MPS) has a plateau at a similarly volatile 7.06 GB,
showing an MSC of 0.1348, close to the previously mentioned 0.15 instability threshold.
This volatility compared to the 0.0815 of MacBook Air M1 (CPU) further emphasizes
the MPS paradox: in addition to causing greater consumption of peak memory, Apple's
MPS backend is less stable than the alternative (as shown in Figure 4.3).



## 56
Thus, the volatility of the Unified Memory in this case cannot be blamed on the lack
of memory leaks: as can be seen in the figure above, there's no memory drift in any
configuration.

4.4.3 CPU Utilization and Threading
Figure 4.4 Kernel density estimation of CPU utilization.

The probability density distributions in Figure 4.4 highlight thread scheduling efficacy:
- Intel i5 CPU shows a bimodal distribution peaking at 100%, validating effective
saturation of all 12 logical cores. The clear separation between idle and active
states indicates well optimized parallelism, with minimal thread contention or
scheduling overhead.
- M1 Air CPU shows a lower median utilization (~20%), confirming that the
backend successfully restricted thread to Performance Cores (P-Cores) only,
leaving Efficiency Cores (E-Core) idle to manage thermal headroom. This pattern



## 57
is consistent with the backends’ 4-thread allocation strategy targeting M1’s
performance cores.

4.5    Scalability and Optimization Efficacy

4.5.1 Impact of Quantization in Performance

Figure 4.5 Efficacy of INT8 Quantization on RTF and Throughput.

The Intel i5 performance (RTF 27.52x) validates Hypotheses 2. By utilizing ONNX
Runtime with INT8 quantization, the CPU achieved throughput comparable to the
Apple M1, despite the M1 having raw memory bandwidth. This confirms that software-
level  quantization  can  bridge  the  gap  between  x86  and  ARM  architectures  on
consumer hardware.






## 58
4.5.2 Impact of Quantization in Performance

Figure 4.6 Latency Decomposition by Pipeline Stage.

Decomposing the synthesis time reveals the primary bottleneck:
Autoregressive generation accounts for ~85% of total time on CPU configs. While
the vocoder overhead (vs 20s on CPU). This finding pinpoints the root cause of the
MPS inefficiency: the GAN-based vocoder relies on operations poorly optimized for
the Metal API.



## 59
4.5.3 Scalability Projection (Model-Based)








Figure 4.7 Projected Synthesis Time as a Function of Input Text Length.

Figure 4.7 should be interpreted as a projection model rather than a direct multi-
length  experiment.  The  observed  77-character  benchmark  establishes  the  per-
configuration latency baseline, while the longer-text behavior is estimated from linear
autoregressive scaling. A stronger validation should rerun the benchmark at 100, 200,
400, and 800 characters to confirm the projected 400-character usability wall.
## Table 3-2 Hypothesis Verification
## Hypotheses Verdict  Evidence
## H1 VRAM
## THRESHOLD –
## ENFORCING CPU
## FALLBACK ON <6GB
## GPU PREVENTS
## CRASHES
## VALIDATED
AMD Ryzen 5 configuration
(5.996 VRAM) successfully
diverted to CPU execution,
achieving RTF = 56.10x without
OOM crashes. GPU execution
would have required ~5.97GB
VRAM, exceeding available
capacity and triggering system
failure.

## H2 PRECISION
## EFFICIENCY –
## PLATFORM-AWARE
## PRECISION (FP16
## VALIDATED
(1) M1 MPS with FP16 achieved
RTF = 32.83x, avoiding INT8
regression due to
unoptimized Metal kernels.




## 60
## FOR MPS, INT8 FOR
## CPU) MAXIMIZES
## PERFORMANCE
(2) Intel i5 with INT8
quantization achieved ~30%
improvement over
estimated FP32 baseline
based on literature
benchmarks. Cross-platform
strategy has prevented
configuration paradox.

## H3 THERMAL
## STABILITY – BURST
## SCHEDULING
## REDUCES THERMAL
## VARIANCE ON
## FANLESS DEVICES.
## PARTIALLY VALIDATED
Logs confirm successful thread
pinning to P-cores (4 threads
selected on M1, reducing
contention. Quantitative thermal
was unavailable due to sensor
API restrictions on
Windows/macOS user mode.



Figure 4.8 Normalized Performance Heatmap of Tested Configurations.

The  experimental  results  confirm  that  the  Smart  Adaptive  Backend  improves
reliability  through  dynamic  configuration,  with  the  MPS  Paradox  as  the  clearest
deployment insight. Disabling MPS on the MacBook Air M1 reduced memory pressure
dramatically while preserving nearly identical RTF, shifting the recommended Apple



## 61
Silicon  strategy  from  GPU-first  to  memory-safe  CPU  execution  for  this  S1-Mini
workload. The results also show that while real-time inference (RTF < 1.0) remains
outside  the  tested  consumer  devices,  reliability  (100%  completion)  is  achievable
through hardware-aware software optimization.





## CHAPTER 5   SUMMARY


5.1    Summary of Contributions

This research presents a Smart Adaptive Backend framework for enabling efficient
and stable inference of the OpenAudio S1-Mini TTS model across a variety of consumer
computer hardware. This includes resource constrained hardware such as sub-6GB
GPUs, fanless devices, etc.
The backend dynamically profiles hardware capabilities, enforces memory safety
thresholds,  applies  platform-aware  precision  and  quantization  strategies,  and
performs  a  thermal  aware  thread  scheduling  to  deliver  stable  inference  with
significantly reduced failure rates. Evaluation across five configurations, ranging from
NVIDIA V100 cloud GPUs to Integrated Intel i5 CPUs and Apple M1 devices validates the
ability to maintain inference success rates of 100% while optimizing for Real-Time factor
(RTF) and throughput.

## 5.2    Findings

- Strict VRAM threshold enforcement for GPU offloading prevents OOM crashes
consumer  grade  devices  (e.g.,  RTX  4050  laptops  with  <6GB  of  VRAM)  without
sacrificing throughput on capable GPUs.



## 63
- Platform-aware precision application, namely INT8 quantization on supported
CPU/CUDA paths and FP16 or CPU execution on Apple Silicon, avoids indiscriminate
INT8 use and prevents severe regressions on Apple MPS backends.
- Thermal-aware bursts scheduling on fanless Apple devices successfully controls
thread affinity to performance cores, reducing thermal throttling variance, although
longer sustained testing is required for conclusive validations.
- The framework generalizes across tested hardware architectures by adapting
to hardware specifications without user input; however, its model-level assumptions
are still tailored to OpenAudio S1-Mini and should be validated on other Dual-AR TTS
models before broader claims are made.

## 5.3 Limitations

The backend currently applies conservative approach such as 6Gb VRAM gating
that may underutilized some mid-range GPUs. Thermal scheduling strategies rely on
macOS powermetrics and are ONLY partially validates under short test durations.
Further integration of GPU power and utilization telemetry is limited by the absence
of NVIDIA Management Library (NVML) support during development.
The current evaluation does not include a formal ablation study isolating H1, H2, and
H3. A stronger experimental section should report performance with each heuristic
disabled  in  turn,  for  example  no  VRAM  gate,  universal  INT8,  and  no  thermal
scheduling, to quantify each component’s independent contribution.



## 64
## REFERENCES

Apple. (2020, June 23). Optimize Metal Performance for Apple silicon Macs. Apple
Developer. https://developer.apple.com/videos/play/wwdc2020/10631/
Atienza, R. (2023). EfficientSpeech: An on-device text-to-speech model. arXiv preprint
arXiv:2305.13905. https://arxiv.org/abs/2305.13905
Bataev, V., Ginsburg, B., & Shliazhko, O. (2025). End-to-end speech synthesis with
neural     transducer.     arXiv     preprint     arXiv:2501.06320.
https://arxiv.org/abs/2501.06320
Beysolow  II,  T.  (2024).  Optimizing  deep  learning  efficiency  through  algorithm-
hardware co-design. Journal of Artificial Intelligence Technology, 4(4), 197-211.
Black, A. W. (2006). Statistical parametric speech synthesis. In 2006 IEEE International
Conference on Acoustics Speech and Signal Processing (Vol. 1).
Chen, W., Gong, X., Liu, X., Zhang, Q., Li, Y., & Wang, Z. (2022). Content-dependent fine-
grained speaker embedding for zero-shot speaker adaptation in text-to-speech
synthesis. In Proceedings of INTERSPEECH 2022 (pp. 5208-5212).
Ciklum.  (2025,  October  30).  Optimizing  deep  neural  networks  for  edge  devices.
https://www.ciklum.com/blog/optimizing-deep-neural-networks-for-edge-
devices/
Cooper, E., Lai, C. I., Yasuda, Y., Fang, F., Wang, X., Chen, N., & Yamagishi, J. (2020).
Zero-shot  multi-speaker  text-to-speech  with  state-of-the-art  neural  speaker
embeddings.     In     ICASSP     2020     (pp.     6184-6188).
https://doi.org/10.1109/ICASSP40776.2020.9053512
DataCamp.  (2025,  November  11).  ONNX:  Train  in  any  framework,  deploy  on  any
hardware. https://www.datacamp.com/tutorial/onnx
Défossez, A., Copet, J., Synnaeve, G., & Adi, Y. (2022). High fidelity neural audio
compression.  arXiv  preprint  arXiv:2210.13438.  https://arxiv.org/abs/2210.13438
(Note: this entry appears twice in your original list — consider removing the
duplicate)
Du, C., Yu, K., Song, H., Chen, K., Ma, Y., Wu, Z., Wang, H., Huang, Y., Zhang, J., & Meng,
H. (2024). VALL-T: Decoder-only generative transducer for robust and decoding-
controllable    text-to-speech.    arXiv    preprint    arXiv:2401.14321.
https://arxiv.org/abs/2401.14321
Explosion  AI.  (2022,  November  23).  Fast  transformer  inference  with  Metal
Performance Shaders. https://explosion.ai/blog/metal-performance-shaders
Fayyazi, A., Kamal, M., & Pedram, M. (2025). MARCO: Multi-agent reinforcement
learning with conformal optimization for hardware-aware neural architecture
search.
Feng, D., Xu, Z., Wang, R., & Lin, F. X. (2025). Profiling Apple Silicon performance for
ML training. arXiv. https://arxiv.org/pdf/2501.14925.pdf
FishAudio   (2024).   OpenAudio   S1-Mini   Model   Card.   Hugging   Face.
https://huggingface.co/fishaudio/s1-mini



## 65
Frankle, J., & Carbin, M. (2019). The lottery ticket hypothesis: Finding sparse, trainable
neural networks. ICLR 2019. https://arxiv.org/abs/1803.03635
Gholami, A., Kim, S., Dong, Z., Yao, Z., Mahoney, M. W., & Keutzer, K. (2021). A survey
of quantization methods for efficient neural network inference. arXiv preprint
arXiv:2103.13630. https://arxiv.org/abs/2103.13630
Guo, H. H., Wang, J., Huang, F., Wang, J., Li, X., Wang, Y., Liu, J., Ye, Z., Zhu, P., Zhao,
Z., Liu, Z., Ma, X., He, L., & Qian, Y. (2024). FireRedTTS: A foundation text-to-speech
framework  for  industry-level  generative  speech  applications.  arXiv  preprint
arXiv:2409.03283. https://arxiv.org/abs/2409.03283
Guo, Y., Zhang, J., Chen, Y., Zhang, H., & Hong, Q. (2024). ControlSpeech: Towards
simultaneous zero-shot speaker cloning and zero-shot language style control with
decoupled codec. arXiv preprint arXiv:2406.01205.
https://arxiv.org/abs/2406.01205
Ham, T. J., Choi, S. J., Suh, K., Choi, H., Kim, B., Jung, D., & Lee, J. W. (2021). ELSA:
Hardware-software co-design for efficient, lightweight self-attention mechanism
in neural networks. In 2021 ACM/IEEE 48th Annual International Symposium on
Computer Architecture (ISCA) (pp. 692-705).
https://doi.org/10.1109/ISCA52012.2021.00060
Han, S., Mao, H., & Dally, W. J. (2015). Deep compression: Compressing deep neural
networks with pruning, trained quantization and Huffman coding. arXiv preprint
arXiv:1510.00149. https://arxiv.org/abs/1510.00149
Hinton, G., Vinyals, O., & Dean, J. (2015). Distilling the knowledge in a neural network.
arXiv preprint arXiv:1503.02531. https://arxiv.org/abs/1503.02531
Hohman, F., Wang, C., Lee, J., Görtler, J., Moritz, D., Bigham, J. P., Ren, Z., Foret, C.,
Shan, Q., & Zhang, X. (2024). Talaria: Interactively optimizing machine learning
models for efficient inference. In Proceedings of the 2024 CHI Conference on
Human Factors in Computing Systems. Association for Computing Machinery.
https://arxiv.org/html/2404.03085v1
Hubner, P., Hu, Y., Peng, I. B., & Markidis, S. (2025). Evaluating the Apple Silicon M-
series  SoCs  for  HPC  workloads.  arXiv  preprint  arXiv:2502.15481.
https://arxiv.org/abs/2502.15481
HuggingFace.    (n.d.).    Metal    Performance    Shaders    (MPS).
https://huggingface.co/docs/transformers/perf_infer_gpu_one#metal-
performance-shaders-mps
Hunt, A. J., & Black, A. W. (1996). Unit selection in a concatenative speech synthesis
system using a large speech database. In 1996 IEEE International Conference on
Acoustics, Speech, and Signal Processing (Vol. 1, pp. 373-376).
Intel.  (2024,  June  4).  Optimize  PyTorch  inference  performance  on  GPUs.
https://www.intel.com/content/www/us/en/developer/articles/technical/optimize
## -pytorch-performance-gpu.html
Jiang, Z., Liu, Y., Gao, Y., Shang, W., Lu, Z., Xie, Y., Ruan, Y., & Wang, X. (2023). Mega-
TTS 2: Boosting prompting mechanisms for zero-shot speech synthesis. arXiv
preprint arXiv:2307.07218. https://arxiv.org/abs/2307.07218



## 66
Klatt, D. H. (1987). Review of text-to-speech conversion for English. The Journal of the
Acoustical Society of America, 82(3), 737-793.
Kong, J., Kim, J., & Bae, J. (2020). HiFi-GAN: Generative adversarial networks for
efficient  and  high  fidelity  speech  synthesis.  arXiv  preprint  arXiv:2010.05646.
https://arxiv.org/abs/2010.05646
Łajszczak, M., Cámbara, G., Li, Y., Beyhan, F., van Korlaar, A., Yang, F., Joly, A., Martín-
Cortinas, Á., Abbas, A., Michalski, A., Moinet, A., Karlapati, S., Muszyńska, E., Guo,
H., Putrycz, B., López Gambino, S., Yoo, K., Sokolova, E., & Drugman, T. (2024).
BASE TTS: Lessons from building a billion-parameter text-to-speech model on
100K   hours   of   data.   arXiv   preprint   arXiv:2402.08093.
https://arxiv.org/abs/2402.08093
Le, M., Vyas, A., Shi, B., Karrer, B., Sari, L., Moritz, R., Williamson, M., Manohar, V., Adi,
Y., Mahadeokar, J., & Hsu, W. (2024). HALL-E: Hierarchical neural codec language
model for minute-long zero-shot text-to-speech synthesis.
Lee, S. H., Chung, S. W., & Jung, J. W. (2024). Multi-modal adversarial training for zero-
shot    voice    cloning.    arXiv    preprint    arXiv:2408.15916.
https://arxiv.org/abs/2408.15916
Medoid AI. (2025, September 9). A hands-on walkthrough on model quantization.
https://medoid.ai/blog/model-quantization/
Memeti,  S.,  &  Pllana,  S.  (2021).  Optimization  of  heterogeneous  systems  with  AI
planning  heuristics  and  machine  learning:  A  performance  and  energy  aware
approach. Journal of Computational Science, 52, 101327.
Mentor  Graphics.  (2019,  December  11).  Optimizing  power  and  performance  for
machine   learning   at   the   edge.   Semiconductor   Engineering.
https://semiengineering.com/optimizing-power-and-performance-for-machine-
learning-at-the-edge/
Microsoft.  (2024,  November  18).  Cross-platform  edge  AI  made  easy  with  ONNX
## Runtime. Microsoft Tech Community.
https://techcommunity.microsoft.com/blog/aiplatformblog/cross-platform-edge-
ai-made-easy-with-onnx-runtime/4293256
Microsoft.  (2025,  August  6).  Performance  evaluations  for  embedded  speech.
Microsoft  Learn.  https://learn.microsoft.com/en-us/azure/ai-services/speech-
service/embedded-speech-performance
Ning, Y., He, S., Wu, Z., Xing, C., & Zhang, L. J. (2019). A review of deep learning based
speech synthesis. Applied Sciences, 9(19), 4050.
NVIDIA. (2022, August 20). Maximizing unified memory performance in CUDA. NVIDIA
Developer  Blog.  https://developer.nvidia.com/blog/maximizing-unified-memory-
performance-in-cuda/
Okamoto, T., Ohtani, Y., & Kawai, H. (2024). Mobile PresenTra: NICT fast neural text-
to-speech system on smartphones with incremental inference of MS-FC-HiFi-GAN
for low-latency synthesis. Proceedings of INTERSPEECH 2024.
ONNX Runtime. (n.d.). ONNX Runtime | Home. https://onnxruntime.ai/
Prenger, R., Valle, R., & Catanzaro, B. (2019). WaveGlow: A flow-based generative
network for speech synthesis. In ICASSP 2019 (pp. 3617-3621).



## 67
Qin, Y., Tang, Y., Liang, D., Chen, L., Zhou, T., Zhang, Y., & Wang, L. (2024). OpenVoice:
Versatile   instant   voice   cloning.   arXiv   preprint   arXiv:2312.01479.
https://arxiv.org/abs/2312.01479
Siuzdak, H. (2023). Vocos: Closing the gap between time-domain and Fourier-based
neural vocoders. arXiv preprint arXiv:2306.00814.
https://arxiv.org/abs/2306.00814
Tan, C., Ge, J., Zeng, Y., & Feng, Y. (2025). SupertonicTTS: Towards highly scalable and
efficient text-to-speech system.
Tan, J., & Cao, H. (2024). TASA: Temperature-aware scheduler for deep neural network
inference in mobile systems. IEEE Transactions on Mobile Computing, 23(5), 4146-
- https://doi.org/10.1109/TMC.2023.3287796
Tan, X., Chen, J., Liu, H., Cong, J., Zhang, C., Liu, Y., ... & Qin, T. (2021). A survey on neural
speech synthesis. arXiv preprint arXiv:2106.15561. https://arxiv.org/abs/2106.15561
Ting, H. N., Yeo, S. F., Pratama, M., Lee, C. K., Ooi, K. B., Tan, G. W., & Wong, L. W.
(2024).  Iterative  knowledge  distillation  and  pruning  for  model  compression.
Expert Systems with Applications, 237, 121489.
van den Oord, A., Dieleman, S., Zen, H., Simonyan, K., Vinyals, O., Graves, A., ... &
Kavukcuoglu,  K.  (2016).  WaveNet:  A  generative  model  for  raw  audio.  arXiv
preprint arXiv:1609.03499. https://arxiv.org/abs/1609.03499
Virtanen,  J.,  Räsänen,  O.,  &  Alku,  P.  (2022).  Exact  prosody  cloning  in  zero-shot
multispeaker text-to-speech. In Proceedings of INTERSPEECH 2022 (pp. 5194-
## 5198).
Wang, Z., Pei, J., Wen, J., Chen, Z., Ma, X., Ye, Z., Gong, Y., Liu, S., & Yu, K. (2024).
MaskGCT: Zero-shot text-to-speech with masked generative codec transformer.
arXiv preprint arXiv:2409.00750. https://arxiv.org/abs/2409.00750
Wilson, M., Maniati, G., Choi, J., & Venugopalan, S. (2025). Towards lightweight and
stable zero-shot TTS with self-distilled representation disentanglement.
Wu, G., Zhai, Y., Xu, Y., Li, X., Zhao, Y., & Bian, K. (2024). SQ-DM: Accelerating diffusion
models with aggressive quantization and sparsity.
Yang, T. J., Liao, Y. L., & Emer, J. (2020). Hardware/software co-exploration of neural
architectures. IEEE Transactions on Computer-Aided Design of Integrated Circuits
and Systems, 39(12), 4805-4815.
Zen, H., Senior, A., & Schuster, M. (2013). Statistical parametric speech synthesis using
deep neural networks. In 2013 IEEE International Conference on Acoustics, Speech
and Signal Processing (pp. 7962-7966).
Zhang, Y., Wang, X., Zhao, Y., Jiang, H., & Zhao, L. (2021). PQK: Model compression via
pruning, quantization, and knowledge distillation. arXiv preprint arXiv:2106.14681.
https://arxiv.org/abs/2106.14681
Zhao,  Y.  (2022).  Software  and  hardware  co-design  for  efficient  neural  networks
[Doctoral dissertation, University of Cambridge].
Zhou, S., Zhou, Y., Li, W., Chen, J., Ye, R., Wu, W., Lin, Z., Lei, S., & Wu, Z. (2024). The
codec language model-based zero-shot spontaneous style TTS system for CoVoC
## Challenge 2024.



## 68
Zhu, Q. (2023). Zero-shot voice cloning with minimal data: Impact of reference audio
length  on  synthesis  quality  [Master's  thesis,  University  of  Groningen].
https://campus-fryslan.studenttheses.ub.rug.nl/708/.


























## 69
1:  import psutil
2:  import torch
3:  import platform
4:  import subprocess
## 5:
6:  def detect_hardware():
## 7:      """
8:      Detects system hardware capabilities and returns
profile dictionary.
## 9:
10:     Profiles CPU, GPU, memory, and platform-specific
features (thermal
11:     monitoring, AVX-512 VNNI, unified memory allocation).
## 12:
## 13:     Returns:
14:         dict: Hardware profile with keys:
15:             - device: Selected execution device ('cuda',
## 'mps', 'cpu')
16:             - physical_cores: Physical CPU core count
17:             - pcores: Performance core count (Apple
Silicon only)
18:             - vram_gb: Available GPU memory (GB)
## APPENDICES

Appendix A: Smart adaptive backend implementation details
## A.1 HARDWARE PROFILING (SUBSYSTEM A)
Subsystem  A  performs  the  detection  of  hardware  resources  at  app  startup,
building a normalized HardwareProfile structure.



## 70
19:             - avx512_vnni: Boolean for INT8 acceleration
support
20:             - thermal_capable: Boolean for thermal
monitoring availability
21:             - memory_gb: System RAM (GB)
## 22:     """
## 23:
## 24:     #
## ═══════════════════════════════════════════════════════════
25:     # CPU Core Detection
## 26:     #
## ═══════════════════════════════════════════════════════════
27:     physical_cores = psutil.cpu_count(logical=False)
28:     logical_cores = psutil.cpu_count(logical=True)
## 29:
## 30:     #
## ═══════════════════════════════════════════════════════════
31:     # Platform-Specific Configuration (macOS/Darwin)
## 32:     #
## ═══════════════════════════════════════════════════════════
33:     if platform.system() == "Darwin":
34:         # Check for powermetrics presence (thermal
monitoring)
35:         thermal_capable = subprocess.call(['which',
## 'powermetrics']) == 0
## 36:
37:         # Apple Silicon P-core count (M1/M2 = 4, M1
Pro/Max = 8)
38:         pcores = 4  # Conservative estimate for M1 Air
baseline
## 39:
## 84:     #
## ═══════════════════════════════════════════════════════════
## 85:     # Return Hardware Profile
## 86:     #
## ═══════════════════════════════════════════════════════════




## 71


VRAM cutoff at 6.0GB. prohibits GPU offload on borderline devices to avoid OOM. 60% unified
memory allocation on Apple Silicon reserved for model footprint. Thermal monitoring enabled
on macOS only, based on off of powermetrics. AVX-512 VNNI flag parsed from
/proc/cpuinfo on Linux to determine INT8 acceleration availability.

40:         # Unified memory allocation
41:         memory_gb = psutil.virtual_memory().total / 1e9
## 42:
43:         # Reserve 3.0GB for macOS system overhead
(Equation 3.5)
44:         gpu_allocation = memory_gb - 3.0
## 45:
46:     else:
47:         thermal_capable = False
48:         pcores = physical_cores
49:         gpu_allocation = 0
## 50:
## 51:     #
## ═══════════════════════════════════════════════════════════
52:     # GPU Detection & VRAM Measurement
## 53:     #
## ═══════════════════════════════════════════════════════════
54:     if torch.cuda.is_available():
55:         vram_bytes =
torch.cuda.get_device_properties(0).total_memory
56:         vram_gb = vram_bytes / 1e9
## 57:
58:         # H1: VRAM threshold gating (6.0GB minimum,
## Section 4.3)
59:         device = "cuda" if vram_gb >= 6.0 else "cpu"
## 60:
61:     elif torch.backends.mps.is_available():
62:         # H2: MPS disabled due to 71% memory bloat
(Section 4.4.2)
## 70:
## 71:     #
## ═══════════════════════════════════════════════════════════
72:     # AVX-512 VNNI Detection (Linux only)
## 73:     #
## ═══════════════════════════════════════════════════════════



## 72

63:         # Force CPU mode on all Apple Silicon devices
64:         device = "cpu"  # Override MPS detection
65:         vram_gb = gpu_allocation  # Log unified memory
allocation
## 66:
67:     else:
68:         device = "cpu"
69:         vram_gb = 0
## 70:
## 71:     #
## ═══════════════════════════════════════════════════════════
72:     # AVX-512 VNNI Detection (Linux only)
## 73:     #
## ═══════════════════════════════════════════════════════════
74:     # Required for hardware-accelerated INT8
quantization
75:     avx512_vnni = False
76:     if platform.system() == "Linux":
77:         try:
78:             with open("/proc/cpuinfo") as cpuinfo_file:
79:                 cpuinfo = cpuinfo_file.read()
80:                 avx512_vnni = "avx512_vnni" in
cpuinfo.lower()
81:         except FileNotFoundError:
82:             avx512_vnni = False  # Fallback for
restricted environments

## ,
94:         "memory_gb": memory_gb,
## 95:     }



## 73


VRAM cutoff at 6.0GB. prohibits GPU offload on borderline devices to avoid
OOM. 60% unified memory allocation on Apple Silicon reserved for model footprint.
Thermal monitoring enabled on macOS only, based on off of powermetrics.
AVX-512 VNNI flag parsed from /proc/cpuinfo on Linux to determine INT8
acceleration availability.





## 83:
## 84:     #
## ═══════════════════════════════════════════════════════════
## 85:     # Return Hardware Profile
## 86:     #
## ═══════════════════════════════════════════════════════════
87:     return {
88:         "device": device,
89:         "physical_cores": physical_cores,
90:         "pcores": pcores,
91:         "vram_gb": vram_gb,
92:         "avx512_vnni": avx512_vnni,
93:         "thermal_capable": thermal_capable
94:         "memory_gb": memory_gb,
## 95:     }



## 74
FUNCTION select_configuration(profile) → config
## INPUT:
profile: HardwareProfile containing:
- device_type ∈ {'cuda', 'mps', 'cpu'}
- gpu_memory_gb: Available VRAM (GB)
- memory_gb: System RAM (GB)
- compute_capability: (major, minor) tuple
- cpu_tier ∈ {'m1_air', 'low_end', 'mid_range',
## 'high_end'}
- thermal_capable: Boolean

## OUTPUT:
config: Dictionary with optimized inference settings

1:  config ← EmptyDictionary()
## 2:
## 3:  // ═══════════════════════════════════════════════════════════
4:  // H1: VRAM Threshold Enforcement (Section 4.3)
## 5:  // ═══════════════════════════════════════════════════════════
## 6:

7:  // RTX 3050 (4GB) → OOM crash | RTX 4050 (6GB) →
## Stable
## 8:
9:  IF profile.device_type == "cuda":
10:   vram_gb ← profile.gpu_memory_gb
11:   IF vram_gb ≥ 6.0:
12:     config["device"] ← "cuda"
## 13:   ELSE:
## A.2 CONFIGURATION ENGINE (SUBSYSTEM B)
Subsystem B translates the HardwareProfiler and model requirements into an
OptimalConfig dict, enforcing the optimization hypotheses.



## 75

10:   vram_gb ← profile.gpu_memory_gb
11:   IF vram_gb ≥ 6.0:
12:     config["device"] ← "cuda"
## 13:   ELSE:
14:     config["device"] ← "cpu"  // Insufficient VRAM
fallback
## 15:   END IF
## 16: ELSE:
17:   config["device"] ← profile.device_type
## 18: END IF
## 19:
## 20: // ═══════════════════════════════════════════════════════════
21: // H2: Platform-Aware Precision Selection (Section 4.4)
## 22: // ═══════════════════════════════════════════════════════════
23: // Finding: MPS has 71% memory bloat (7.06GB vs 4.12GB
## CPU)
24: // Performance delta: 32.83x (MPS) vs 33.40x (CPU) =
1.7% difference
## 25:
26: IF config["device"] == "cuda":
27:   compute_cap ← profile.compute_capability
28:   config["precision"] ← "fp16"
## 29:
30:   // INT8 quantization requires Tensor Cores (Ampere+)
31:   IF compute_cap[0] ≥ 8:
32:     config["quantization"] ← "int8"
## 33:   ELSE:
34:     config["quantization"] ← "none"
## 35:   END IF
## 36:
37:   config["use_onnx"] ← False
## 38:



## 76

## 36:
37:   config["use_onnx"] ← False
## 38:
39: ELSE IF config["device"] == "mps":
40:   // Override MPS → CPU (71% memory bloat mitigation)
41:   config["device"] ← "cpu"
42:   config["precision"] ← "fp32"
43:   config["quantization"] ← "int8"
44:   config["use_onnx"] ← True
## 45:
46: ELSE:  // CPU-only execution
47:   config["precision"] ← "fp32"
48:   config["quantization"] ← "int8"  // Software INT8
via ONNX
49:   config["use_onnx"] ← True
## 50: END IF
## 51:
## 52: // ═══════════════════════════════════════════════════════════
53: // Memory Budget & Chunk Size (Equation 3.5)
## 54: // ═══════════════════════════════════════════════════════════
55: // CUDA: Budget = VRAM × 0.85 (15% driver overhead)
56: // CPU:  Budget = RAM - 3.0GB (OS + system processes)
## 57:
58: IF config["device"] == "cuda":
59:   available_mem_gb ← profile.gpu_memory_gb × 0.85
60:   IF available_mem_gb ≥ 8:
61:     config["chunk_length"] ← 1024
## 62:   ELSE:
63:     config["chunk_length"] ← 512
## 64:   END IF
## 65:
66: ELSE IF config["device"] == "cpu":



## 77

63:     config["chunk_length"] ← 512
## 64:   END IF
## 65:
66: ELSE IF config["device"] == "cpu":
67:   available_mem_gb ← profile.memory_gb - 3.0
68:   IF available_mem_gb ≥ 5:
69:     config["chunk_length"] ← 1024
## 70:   ELSE:
71:     config["chunk_length"] ← 512
## 72:   END IF
## 73:
## 74: ELSE:
75:   config["chunk_length"] ← 512  // Conservative
fallback
## 76: END IF
## 77:
## 78: // ═══════════════════════════════════════════════════════════
79: // H3: Thermal-Aware Scheduling (Section 4.5, M1 Air
## Only)
## 80: // ═══════════════════════════════════════════════════════════
81: // Finding: M1 Air throttles at 85°C → 40% throughput
loss
82: // Mitigation: Burst scheduling on P-cores maintains
60°C baseline
## 83:
84: IF profile.thermal_capable AND profile.cpu_tier ==
## "m1_air":
85:   config["burst_scheduling"] ← True
86:   config["thread_affinity"] ← [0, 1, 2, 3]  // Pin to
performance cores
## 87: ELSE:
88:   config["burst_scheduling"] ← False
89:   config["thread_affinity"] ← "all_cores"



## 78


It is important to note that INT8 quantization was disabled on Apple MPS to avoid
fallback to CPU causing a 70-90x slowdown in the RTF observed in profiling. Chunk
sizes dynamically adjusted based on available memory after safety margins. Thread
affinity pinned to M1 performance cores to avoid efficiency core thermal throttling.

## 87: END IF
## 88:
89: RETURN config
## END FUNCTION



## 79
FUNCTION collect_metrics(queue, inference_running)
## INPUT:
queue: Shared list for storing time-series metrics
inference_running: Threading event flag (Boolean
state)

## OUTPUT:
Populates queue with real-time system metrics at 1Hz
sampling rate

1:// Real-Time Metrics Collection Loop (1-second
intervals)
2:  // Captures: RAM, VRAM, CPU utilization, thermal data
(macOS only)
## 3:
4:  WHILE inference_running.is_set() == True:
5:    timestamp ← CurrentUnixTime()  // Seconds since
epoch
## 6:
7:    // Memory Metrics (Resident Set Size)
8:   ram_mb ← SystemMemory.used / (1024 × 1024)  //
Convert bytes → MB
## 9:
10:   // GPU Memory Allocation (CUDA only)

14:     vram_mb ← CUDA.memory_allocated() / (1024 × 1024)
## 15:   ELSE:
16:     vram_mb ← 0  // CPU-only or MPS mode
## 17:   END IF
## A.3 TTS EXECUTION AND MONITORING (SUBSYSTEM C)
Subsystem C arranges the inference with fine-grained monitoring. The monitoring
thread collects metrics at 1Hz and ensures synchronization with inference start and
end.







## 80

4:  WHILE inference_running.is_set() == True:
5:    timestamp ← CurrentUnixTime()  // Seconds since
epoch
## 6:
7:    // Memory Metrics (Resident Set Size)
8:   ram_mb ← SystemMemory.used / (1024 × 1024)  //
Convert bytes → MB
## 9:
10:   // GPU Memory Allocation (CUDA only)
10:   // GPU Memory Allocation (CUDA only)
11:   IF CUDA.is_available() == True:
12:      // Calculate allocated VRAM
## 13:
14:      vram_mb ← CUDA.memory_allocated() / (1024 × 1024)
## 15:   ELSE:
16:      vram_mb ← 0  // CPU-only or MPS mode
## 17:   END IF
## 18:
19:   // CPU Utilization (instantaneous measurement)
20:   cpu_percent ← CPU.utilization(interval=None)
## 21:
22:   // Thermal Metrics (Platform-Specific)
23:   IF Platform == "Darwin":  // macOS only
24:     temp_c ← ReadThermalSensor("CPU_die_temperature")
## 25:   ELSE:
26:     temp_c ← NULL  // Windows/Linux thermal collection
omitted





## 81

Note: The monitoring runs concurrently with synthesis thread; synchronized using
threading events. Data saved as CSV used for calculating performance metrics (RTF,
MSC) as described in Chapter 3. Thermal sensors polled only on macOS; others return
null. Metrics collection ensures reproducible time windows over which stability and
throughput are computed.




## 27:   END IF
## 28:
29:   // Append metrics snapshot to shared queue
30:   metric_snapshot ← {
31:     "timestamp": timestamp,
32:     "ram_mb": ram_mb,
33:     "vram_mb": vram_mb,
34:     "cpu_percent": cpu_percent,
35:     "temp_c": temp_c
## 36:   }
37:   queue.append(metric_snapshot)
## 38:
39:   Sleep(1.0)  // 1Hz sampling frequency
## 40: END WHILE
## 41:
## END FUNCTION



## 82
Appendix B: Turnitin AI and Similarity Report
## Similarity Report:

AI Report:









## 83
Appendix C: Certificate of Substantial Use







## BIONOTE



Julian Salas is a Computer Science student at Caraga State
University, Philippines, with a strong interest in technology,
programming, and mathematics. He enjoys building software
projects and exploring how different systems work. Some of his
projects include TradeTrack, a web-based POS system and
Clocked Out, a hand-tracking game using TensorFlow and Three.js. These experiences led to
his undergraduate thesis on the Smart Adaptive Backend, which focuses on improving the
performance of speech recognition systems through hardware-based optimization. He is also
involved in campus organizations such as the Computer Science Society and the Robotics
## Enthusiasts Club.

Alethea Joy Montoyo is a Computer Science student at Caraga
State University in the Philippines. She is interested in
technology, problem solving, and continuous learning,
especially in the areas of software development and emerging
technologies. As a co-author of this thesis, she contributed to
the design and testing of the Smart Adaptive Backend,
including benchmarking across different hardware platforms such as Apple Silicon and
NVIDIA GPUs. Outside of academics, she enjoys running, going to the gym, listening to music,
and spending time with family and friends.