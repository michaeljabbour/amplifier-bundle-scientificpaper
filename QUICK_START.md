# Quick Start Guide

## ✅ Bundle Is Ready

**Status:** Production-ready, git repository initialized, 2 commits created  
**Location:** `/Users/michaeljabbour/dev/amplifier-bundle-scientificpaper`

---

## 🚀 How to Use From GitHub

### Step 1: Push to GitHub (One-Time Setup)

**If you have GitHub CLI (`gh`):**
```bash
cd /Users/michaeljabbour/dev/amplifier-bundle-scientificpaper

# Create repo and push in one command
gh repo create amplifier-bundle-scientificpaper --public --source=. --push
```

**If you don't have `gh` (manual method):**
```bash
# 1. Go to https://github.com/new
# 2. Create repo named: amplifier-bundle-scientificpaper
# 3. Don't initialize with anything
# 4. Then run:
git remote add origin https://github.com/YOUR_USERNAME/amplifier-bundle-scientificpaper.git
git push -u origin master
```

### Step 2: Use the Bundle

**From anywhere:**
```bash
amplifier --bundle github:YOUR_USERNAME/amplifier-bundle-scientificpaper
```

**Or add to your config** (`~/.amplifier/config.yaml`):
```yaml
bundles:
  paper: github:YOUR_USERNAME/amplifier-bundle-scientificpaper
```

Then:
```bash
amplifier --bundle paper
```

---

## 🎯 What You Can Do With This Bundle

### Create Papers
```
"Create a NeurIPS paper on transformer efficiency"
"Structure a paper on neural architecture search"
"Help me outline an ICML paper"
```

### Generate Figures
```
"Create a training curve plot with error bars"
"Generate a transformer architecture diagram"
"Plot a confusion matrix heatmap"
```

### Compile and Format
```
"Compile my paper for ACL format"
"Convert my NeurIPS paper to IEEE format"
"Validate my paper against ICML requirements"
```

### Manage Citations
```
"Add a BibTeX entry for DOI: 10.1234/example"
"Convert my citations to author-year style"
"Check my bibliography for duplicates"
```

---

## 📦 What's Included

- **4 Specialist Agents** - paper-architect, latex-expert, figure-artist, citation-manager
- **6 Conference Formats** - NeurIPS, ICML, ACL, IEEE, ACM, arXiv
- **Publication Figures** - Matplotlib, TikZ, PlotNeuralNet, quality veto rules
- **LaTeX Tools** - Compilation, validation, error diagnosis
- **Templates** - ACL and IEEE included, others documented

---

## 🔧 First-Time Setup

### Install Python Dependencies
```bash
cd amplifier-bundle-scientificpaper
pip install -r requirements.txt
```

### Download Additional Templates (Optional)
```bash
# Automated download for some conferences
python scripts/download_templates.py --all

# For NeurIPS, ICML, ACM: see templates/DOWNLOAD_INSTRUCTIONS.md
```

---

## 🧪 Test It

```bash
# Test locally before pushing
amplifier --bundle /Users/michaeljabbour/dev/amplifier-bundle-scientificpaper

# Try these commands:
"What agents are available?"
"Help me structure a research paper"
"What conferences are supported?"
```

---

**Ready to go!** Just push to GitHub and you can use it anywhere with:
```bash
amplifier --bundle github:YOUR_USERNAME/amplifier-bundle-scientificpaper
```
