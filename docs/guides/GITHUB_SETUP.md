# GitHub Setup and Usage Guide

**Bundle:** Scientific Paper Bundle for Amplifier  
**Status:** ✅ Git repository initialized, ready to push  
**Commit:** `6fbd7bc` - Initial release with 84 files

---

## 🚀 Quick Start: Push to GitHub

### Step 1: Create GitHub Repository

1. Go to GitHub: https://github.com/new
2. Fill in repository details:
   - **Repository name:** `amplifier-bundle-scientificpaper`
   - **Description:** `AI-assisted scientific paper authoring with LaTeX, figure generation, and multi-conference formatting`
   - **Visibility:** Public (recommended) or Private
   - ⚠️ **DON'T check:** "Initialize with README" (we have our own)
   - ⚠️ **DON'T add:** .gitignore or license (we have those)
3. Click "Create repository"

### Step 2: Push Your Code

GitHub will show you commands. Use these:

```bash
cd /Users/michaeljabbour/dev/amplifier-bundle-scientificpaper

# Add GitHub remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/amplifier-bundle-scientificpaper.git

# Push to GitHub
git push -u origin master

# Or if you use 'main' as default branch:
git branch -M main
git push -u origin main
```

### Step 3: Verify

Visit your repository:
```
https://github.com/YOUR_USERNAME/amplifier-bundle-scientificpaper
```

You should see:
- ✅ README.md displaying as home page
- ✅ All 84 files committed
- ✅ Initial commit message
- ✅ Directory structure (behaviors/, agents/, scripts/, etc.)

---

## 📦 How to Use the Bundle

### Method 1: Direct GitHub Reference (Easiest)

```bash
# Use the bundle directly from GitHub
amplifier --bundle github:YOUR_USERNAME/amplifier-bundle-scientificpaper
```

**Amplifier will:**
- Download and cache the bundle automatically
- Load all agents and behaviors
- Make the bundle available for the session

### Method 2: Named Bundle (Convenient)

Add to your `~/.amplifier/config.yaml`:

```yaml
bundles:
  scientificpaper: github:YOUR_USERNAME/amplifier-bundle-scientificpaper
  # Or use a shorter alias:
  paper: github:YOUR_USERNAME/amplifier-bundle-scientificpaper
```

Then use with:
```bash
amplifier --bundle scientificpaper
# Or
amplifier --bundle paper
```

### Method 3: Clone Locally

```bash
# Clone the repository
cd ~/dev
git clone https://github.com/YOUR_USERNAME/amplifier-bundle-scientificpaper.git

# Use the local bundle
cd amplifier-bundle-scientificpaper
amplifier --bundle .

# Or from anywhere:
amplifier --bundle ~/dev/amplifier-bundle-scientificpaper
```

---

## 🎯 Testing the Bundle

### After Loading

Once you load the bundle (any method above), try these commands:

```
"What capabilities does this bundle provide?"
"What agents are available?"
"What conferences are supported?"
```

**Expected response:**
- Shows 4 agents: paper-architect, latex-expert, figure-artist, citation-manager
- Shows 6 supported conferences
- Describes LaTeX authoring, figure generation, citation management

### Test Agent Delegation

```
"Help me structure a NeurIPS paper on transformer efficiency"
```

**Expected:**
- Delegates to paper-architect agent
- Provides IMRaD structure outline
- Suggests section allocations

```
"Create a matplotlib plot showing training curves"
```

**Expected:**
- Delegates to figure-artist agent
- Generates matplotlib code with scientific styling
- Provides tikzplotlib conversion

```
"Compile my paper for ACL format"
```

**Expected:**
- Delegates to latex-expert agent
- Uses ACL templates (available in templates/acl/)
- Handles compilation

---

## 🔧 Optional: Add Missing Templates

The bundle includes ACL and IEEE templates. To add others:

### Quick Template Setup

```bash
cd /Users/michaeljabbour/dev/amplifier-bundle-scientificpaper

# Try automated download
python scripts/download_templates.py --all

# For templates that need manual download (NeurIPS, ICML, ACM):
# See templates/DOWNLOAD_INSTRUCTIONS.md
```

**Or test without templates:**
- Use ACL or IEEE format (templates included)
- Use system-wide LaTeX packages (if you have TeX Live)
- Use generic article class

---

## 📝 Repository Setup Recommendations

### Add a License

```bash
# Add MIT License (recommended)
cat > LICENSE << 'EOF'
MIT License

Copyright (c) 2026 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy...
EOF

git add LICENSE
git commit -m "docs: Add MIT License"
git push
```

### Add GitHub Topics

On your GitHub repository page:
1. Click "⚙️ Settings"
2. Scroll to "Topics"
3. Add topics: `amplifier`, `latex`, `scientific-writing`, `ai-agent`, `conference-papers`

### Enable GitHub Pages (Optional)

To display documentation:
1. Go to Settings → Pages
2. Source: Deploy from branch `master` or `main`
3. Directory: `/docs` (or root)
4. Your README will be visible at: `https://YOUR_USERNAME.github.io/amplifier-bundle-scientificpaper`

---

## 🌐 Sharing the Bundle

### For Public Use

Once pushed to GitHub, others can use your bundle:

```bash
# Anyone can use it with:
amplifier --bundle github:YOUR_USERNAME/amplifier-bundle-scientificpaper
```

### For Amplifier Ecosystem

If you want to contribute to the Amplifier ecosystem:
1. Push to GitHub (public repository)
2. Consider opening a PR to add your bundle to the official registry
3. Join the Amplifier community discussions

---

## 📊 What's Been Committed

### Initial Commit: `6fbd7bc`

**Commit message:**
```
feat: Initial release of Scientific Paper Bundle v1.0

Complete Amplifier bundle for AI-assisted scientific paper authoring.

Features:
- 4 production-quality agents (paper-architect, latex-expert, figure-artist, citation-manager)
- 6 conference format specifications (NeurIPS, ICML, ACL, IEEE, ACM, arXiv)
- 4 Python utility scripts (compile, validate, generate, download)
- 6 comprehensive LaTeX style guides (2,607 lines)
- Multi-conference template support (ACL and IEEE included)
- Publication-quality figure generation with quality veto rules
- Complete documentation and research artifacts

Architecture:
- Thin bundle pattern (inherits from foundation)
- Context sink architecture (heavy docs in agents)
- Foundation-expert validated
- All Python scripts type-checked (pyright + ruff)

Total: 12,182+ lines of production code
Files: 84

🤖 Generated with Amplifier
Co-Authored-By: Amplifier <240397093+microsoft-amplifier@users.noreply.github.com>
```

**Files committed:** 84 total
- Core bundle files
- Agents and behaviors
- Context and documentation
- Scripts and templates
- Style guides and research

---

## 🎯 Usage Examples

### Example 1: Create a Paper from GitHub

```bash
# Start Amplifier with the bundle from GitHub
amplifier --bundle github:YOUR_USERNAME/amplifier-bundle-scientificpaper

# Then create a paper
"Create a NeurIPS paper on attention mechanisms in transformers"

# The paper-architect agent will:
# → Design paper structure (IMRaD)
# → Create section outline
# → Set up LaTeX project
```

### Example 2: Generate Figures

```bash
amplifier --bundle github:YOUR_USERNAME/amplifier-bundle-scientificpaper

"Create a training curve plot comparing three models"

# The figure-artist agent will:
# → Generate matplotlib plot with scientific styling
# → Convert to TikZ via tikzplotlib
# → Provide LaTeX integration code
# → Apply quality veto rules
```

### Example 3: Format Conversion

```bash
amplifier --bundle github:YOUR_USERNAME/amplifier-bundle-scientificpaper

"Convert my NeurIPS paper to ACL format"

# The latex-expert agent will:
# → Load both conference specifications
# → Adjust document class and margins
# → Update citation style (flexible → author-year)
# → Validate formatting
```

---

## 🔄 Future Updates

### To Update the Bundle

```bash
cd /Users/michaeljabbour/dev/amplifier-bundle-scientificpaper

# Make changes to files
# ...

# Commit changes
git add .
git commit -m "feat: Add [description]"
git push

# Users automatically get updates on next cache refresh
```

### Versioning

Consider using semantic versioning in `bundle.md`:

```yaml
bundle:
  name: scientificpaper
  version: 1.0.0  # Bump when making updates
```

---

## 📞 Support and Issues

### If Users Encounter Issues

Direct them to:
1. **README.md** - Usage guide and examples
2. **ARCHITECTURE.md** - Design and patterns
3. **templates/DOWNLOAD_INSTRUCTIONS.md** - Template setup
4. **GitHub Issues** - For bug reports and feature requests

### Enabling GitHub Issues

1. Go to repository Settings
2. Check "Issues" under Features
3. Users can report problems or request features

---

## ✅ Checklist Before Going Public

If making the repository public:

- [x] Initial commit created
- [x] All files included
- [x] .gitignore configured
- [ ] LICENSE file added (recommend MIT or Apache 2.0)
- [x] README.md complete and informative
- [ ] GitHub repository created
- [ ] Code pushed to GitHub
- [ ] Repository description set
- [ ] Topics added (amplifier, latex, scientific-writing)
- [ ] Tested bundle loading from GitHub URL

---

## 🎉 Summary

Your bundle is **ready to push to GitHub** and share!

**Current status:**
- ✅ Git repository initialized
- ✅ 84 files committed (57,769 lines)
- ✅ Clean working directory
- ⏳ Ready to push to GitHub (create repo + push)

**After pushing, users can:**
```bash
amplifier --bundle github:YOUR_USERNAME/amplifier-bundle-scientificpaper
```

---

**Next Action:** Create GitHub repository and push, or test locally first!
