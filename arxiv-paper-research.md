# ArXiv Paper Research: PaperBanana

**Paper ID**: arXiv:2601.23265  
**Title**: PaperBanana: Automating Academic Illustration for AI Scientists  
**Submission Date**: January 30, 2026  
**Authors**: Dawei Zhu, Rui Meng, Yale Song, Xiyu Wei, Sujian Li, Tomas Pfister, Jinsung Yoon  
**Institutions**: Peking University, Google Cloud AI Research  

## Research Summary

PaperBanana addresses the labor-intensive bottleneck of generating publication-ready illustrations in the AI research workflow. It's an agentic framework that automates the creation of methodology diagrams and statistical plots for academic papers, achieving superior results in faithfulness, conciseness, readability, and aesthetics compared to baseline approaches.

## Paper Topic and Focus

### Core Problem
Despite rapid advances in autonomous AI scientists powered by language models, generating publication-ready illustrations remains a manual, time-consuming process that slows down research publication workflows.

### Solution Overview
PaperBanana is a reference-driven agentic framework that orchestrates multiple specialized agents to automatically generate publication-quality academic illustrations, including:
- Methodology diagrams
- Statistical plots
- Enhanced versions of human-drawn diagrams

## Technical Architecture

### Multi-Agent System
The framework orchestrates **five specialized agents**:

1. **Retriever Agent**: Identifies relevant reference examples to guide downstream agents
2. **Planner Agent**: Acts as the cognitive core, translating context into detailed textual descriptions
3. **Stylist Agent**: Ensures adherence to academic aesthetic standards by synthesizing guidelines from references
4. **Visualizer Agent**: Transforms textual descriptions into visual output or executable code
5. **Critic Agent**: Inspects generated images/plots against the source to provide feedback for refinement

### Technology Stack

**Foundation Models**:
- **Gemini-3-Pro**: Serves as the VLM (Vision Language Model) judge and agentic backbone
- **Nano-Banana-Pro**: Functions as the specialized image generation model

**Key Technical Features**:
- Reference-driven approach (learns from existing high-quality examples)
- Iterative refinement via self-critique
- Hybrid approach supporting both code generation and direct image generation
- State-of-the-art VLM and image generation model integration

## APIs, Tools, and Systems

### Core Components
- **Vision Language Models (VLMs)**: For understanding and critiquing visual content
- **Image Generation Models**: For rendering diagrams and plots
- **Agentic Orchestration**: Coordinating multiple specialized agents
- **Reference Database**: Curated examples from academic publications

### Workflow Pipeline
1. Reference retrieval from similar papers
2. Content and style planning based on source context
3. Image rendering (via code or direct generation)
4. Self-critique and iterative refinement

## Benchmark: PaperBananaBench

### Dataset Construction
- **Size**: 584 valid samples total
  - 292 test cases
  - 292 reference cases
- **Source**: Curated from NeurIPS 2025 publications
- **Coverage**: Diverse research domains and illustration styles
- **Quality Assurance**: Four-stage pipeline (Collection & Parsing, Filtering, Categorization, Human Curation)

### Statistics
- Average source context length: 3,020.1 words
- Average figure caption length: 70.4 words

### Evaluation Dimensions
1. **Faithfulness**: Accuracy to source content
2. **Conciseness**: Information density without verbosity
3. **Readability**: Clarity and comprehension
4. **Aesthetics**: Visual appeal and professional quality

## Relevance to Scientific Paper Generation

### High Relevance for Automated Scientific Workflows
PaperBanana is directly applicable to automated scientific paper generation systems:

1. **Last-Mile Automation**: Completes the research workflow by automating the final bottleneck of illustration creation
2. **Integration with AI Scientists**: Designed to work with autonomous AI scientist systems powered by language models
3. **Publication-Ready Output**: Generates production-quality illustrations that meet academic standards
4. **End-to-End Research Automation**: Enables complete paper generation from conception to publication-ready output

### MCP (Model Context Protocol) Integration Potential
The architecture demonstrates patterns relevant to MCP systems:
- Multi-agent orchestration with specialized roles
- Context accumulation and reference retrieval
- Iterative refinement with feedback loops
- Tool invocation (code execution for plot generation)

## Figure Generation and Visualization Techniques

### Methodology Diagram Generation
**Approach**: Reference-driven visual synthesis
- Retrieves similar diagrams from reference database
- Plans content hierarchy and component relationships
- Applies aesthetic guidelines from references
- Renders using image generation models
- Iteratively refines based on self-critique

**Advantages over baseline**:
- More concise (less verbose text)
- Modern aesthetic (updated color schemes, typography)
- Maintains faithfulness to source context

### Statistical Plot Generation

**Dual Approach Support**:
1. **Code-Based Generation**: 
   - Higher content fidelity
   - Precise numerical accuracy
   - Traditional approach with programmatic control

2. **Image Generation**:
   - Superior visual aesthetics
   - More flexible styling
   - Risk of numerical hallucination or element repetition

**Trade-offs Identified**:
- Image generation excels in presentation but can have faithfulness errors
- Code generation ensures accuracy but may be less visually appealing

### Aesthetic Enhancement
**Novel Application**: Can enhance existing human-drawn diagrams by:
- Applying auto-summarized style guidelines
- Modernizing color schemes
- Improving typography
- Refining graphical elements

## Experimental Results

### Performance
PaperBanana **consistently outperforms leading baselines** across all evaluation dimensions:
- Faithfulness ✓
- Conciseness ✓
- Readability ✓
- Aesthetics ✓

### Known Limitations
**Primary Failure Mode**: Connection errors in diagrams
- Redundant connections
- Mismatched source-target nodes
- Critic model fails to identify these issues
- Likely stems from foundation model's perception limitations

## Research Context and Significance

### Timing and Relevance
- Published January 2026 (very recent)
- Part of the broader trend toward autonomous AI scientists
- Addresses a practical bottleneck in research automation
- From Google Cloud AI Research and Peking University collaboration

### Subjects
- Primary: Computation and Language (cs.CL)
- Secondary: Computer Vision and Pattern Recognition (cs.CV)

## Source Links

- **ArXiv Abstract**: https://arxiv.org/abs/2601.23265
- **ArXiv PDF**: https://arxiv.org/pdf/2601.23265
- **Project Website**: https://dwzhu-pku.github.io/PaperBanana/
- **GitHub Repository**: https://github.com/dwzhu-pku/PaperBanana
- **Hugging Face**: https://huggingface.co/papers/2601.23265
- **DOI**: https://doi.org/10.48550/arXiv.2601.23265

## Key Takeaways for Scientific Paper Generation Systems

1. **Illustration Automation is Critical**: Visual elements are the remaining manual bottleneck in automated research workflows
2. **Multi-Agent Orchestration Works**: Specialized agents with clear responsibilities produce better results than monolithic approaches
3. **Reference-Driven Learning**: Using curated examples from high-quality publications improves output quality
4. **Iterative Refinement Essential**: Self-critique and refinement loops significantly improve output quality
5. **Dual Generation Strategies**: Supporting both code and image generation provides flexibility for different visualization needs
6. **Benchmark-Driven Development**: PaperBananaBench provides rigorous evaluation framework for academic illustration quality

## Confidence Level

**High Confidence** - Information sourced from:
- Official arXiv abstract page
- Project website maintained by authors
- GitHub repository
- Multiple secondary sources corroborating details

**Note**: PDF was unavailable due to timeout, but abstract, project website, and GitHub provided comprehensive technical details about the system architecture, evaluation, and results.

---

*Research compiled on: February 4, 2026*  
*Research agent: foundation:web-research*
