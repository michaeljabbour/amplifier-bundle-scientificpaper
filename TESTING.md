# Testing Instructions

## ✅ Final Cleanup Complete

**Repository Status:** Professional, clean, ready for production use  
**GitHub:** https://github.com/michaeljabbour/amplifier-bundle-scientificpaper  
**Latest Commit:** 94d5ff9 - Final cleanup with LICENSE

---

## 🧪 How to Test the Bundle

### Step 1: Refresh Your Bundle Cache

Since the repository was just cleaned up, get the latest version:

```bash
# Remove old cached version
amplifier bundle remove scientificpaper
rm -rf ~/.amplifier/cache/amplifier-bundle-scientificpaper-*

# Download fresh from GitHub
amplifier bundle add git+https://github.com/michaeljabbour/amplifier-bundle-scientificpaper@master

# Activate it
amplifier bundle use scientificpaper

# Start a new session
amplifier
```

---

### Step 2: Verify Agents Load

Once in the session, check that all scientificpaper agents are available:

```
"what agents are available?"
```

**Expected to see:**
- ✅ scientificpaper:paper-architect
- ✅ scientificpaper:latex-expert
- ✅ scientificpaper:figure-artist
- ✅ scientificpaper:citation-manager

(Plus all the foundation agents)

---

### Step 3: Test Basic Agent Delegation

**Test paper-architect:**
```
"help me structure a NeurIPS paper on attention mechanisms"
```
Expected: Should delegate to paper-architect, provide IMRaD outline

**Test latex-expert:**
```
"what are ACL's formatting requirements?"
```
Expected: Should delegate to latex-expert, mention A4 paper requirement

**Test figure-artist:**
```
"what colors should I use for publication figures?"
```
Expected: Should mention ColorBrewer palettes, quality veto rules

**Test citation-manager:**
```
"how do I create a bibtex entry?"
```
Expected: Should provide BibTeX template and guidance

---

### Step 4: Test PaperBanana Integration

**Simple PaperBanana test:**
```
"create a methodology diagram using PaperBanana for a 3-stage training pipeline"
```

Expected:
- Delegates to figure-artist
- Mentions tool-paperbanana
- Explains it will use Gemini/Imagen for generation
- Asks for GOOGLE_API_KEY if not set

**Complex multi-figure test** (the one that worked before):
```
"I need publication-quality figures for my NeurIPS paper on multi-modal attention mechanisms. Create:
1. Architecture diagram showing 3-stage pipeline with visual and text inputs
2. Attention heatmap (12x12)
3. Performance comparison with 4 panels

Use PaperBanana quality validation."
```

Expected:
- Should orchestrate across agents
- Apply 8 quality veto rules
- Generate publication-ready figures

---

### Step 5: Test Conference Format Knowledge

```
"what's the difference between NeurIPS and ICML formatting?"
```

Expected: Single-column vs two-column, citation styles, page limits

```
"can I submit a 10-page paper to NeurIPS?"
```

Expected: No - 9 pages max excluding references

---

### Step 6: Test Recipe Workflow (Advanced)

```
"run the paperbanana-figure recipe"
```

Expected:
- Multi-stage workflow with approval gates
- Planning → Generation → Refinement
- Quality validation with structured JSON output

---

## 🔍 Verification Checklist

After testing, verify:

- [ ] All 4 scientificpaper agents are discoverable
- [ ] Agent delegation triggers correctly
- [ ] Conference format knowledge is accurate
- [ ] PaperBanana tool is mentioned for complex figures
- [ ] Quality veto rules are referenced
- [ ] No errors about missing modules or imports

---

## ⚠️ Known Requirements

### For PaperBanana to Actually Generate Images

**Required:**
```bash
# Install Google Generative AI SDK
pip install google-genai

# Set API key
export GOOGLE_API_KEY="your-key-here"
```

**Without API key:**
- Bundle still works for all other features
- PaperBanana will explain it needs the key
- Can still use matplotlib/tikz for figures

---

## 🐛 If Something Doesn't Work

### Agent not found
```bash
# Make sure you refreshed the cache
rm -rf ~/.amplifier/cache/amplifier-bundle-scientificpaper-*
amplifier bundle add git+https://github.com/michaeljabbour/amplifier-bundle-scientificpaper@master
```

### Python import errors
```bash
# Install all dependencies
pip install -r requirements.txt
pip install google-genai  # For PaperBanana
```

### Bundle won't load
```bash
# Validate bundle syntax
cd /Users/michaeljabbour/dev/amplifier-bundle-scientificpaper
python3 -c "import yaml; yaml.safe_load(open('bundle.md').read().split('---')[1])"
```

---

## ✅ Success Indicators

You'll know everything is working when:

1. ✅ All 4 scientificpaper agents show in the list
2. ✅ "help me structure a paper" delegates to paper-architect
3. ✅ "what are ACL's requirements?" mentions A4 paper
4. ✅ "create a figure with PaperBanana" mentions tool-paperbanana
5. ✅ Conference knowledge is detailed and accurate

---

**Start with Step 1-3 to validate basic functionality, then try the advanced PaperBanana tests!**
