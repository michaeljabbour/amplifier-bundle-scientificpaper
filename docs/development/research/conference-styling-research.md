# Scientific Paper Styling and Formatting Guidelines Research

A comprehensive guide to formatting requirements for major scientific conferences and institutions.

---

## 1. NeurIPS (Neural Information Processing Systems)

### Official Resources
- **Official Style Files**: https://neurips.cc/Conferences/2025/PaperInformation/StyleFiles
- **Formatting Instructions (2025)**: https://arxiv.org/html/2505.10292v1
- **Overleaf Template**: https://www.overleaf.com/latex/templates/neurips-2024/tpsbbrdqcmsh

### LaTeX Template & Requirements
- **Style File**: `neurips_2025.sty` (required for LaTeX 2ε)
- **Supported Software**: LaTeX only; no Word or RTF templates supported
- **Important**: Tweaking style files may be grounds for rejection

### Text Layout & Typography
- **Page Size**: Standard (8.5" × 11")
- **Text Area**: 5.5 inches (33 picas) wide × 9 inches (54 picas) long
- **Left Margin**: 1.5 inches (9 picas)
- **Font**: Times New Roman (preferred, selected by default)
- **Font Size**: 10 point text with 11 point vertical spacing (leading)

### Title & Section Formatting
- **Title**: 17 point, bold, initial caps/lower case, centered between two horizontal rules
  - Top rule: 4 points thick
  - Bottom rule: 1 point thick
- **Abstract**: Centered, bold, 12 point type

### References
- Font size can be reduced to 9 point for references
- Reference section does NOT count towards page limit
- Citation Style: Flexible (author-year or numeric acceptable)
- **natbib Package**: Loaded by default
- Any consistent citation style is acceptable (plain, abbrv, unsrt, etc.)

### Page Limits & Structure
- **Main Paper**: 8 pages maximum
- **Additional Content**: Unlimited pages for references and appendices
- **Consistent Formatting**: Internal consistency required throughout

---

## 2. ICML (International Conference on Machine Learning)

### Official Resources
- **Official Instructions**: https://icml.cc/Conferences/2026/AuthorInstructions
- **Example Paper (2025)**: https://media.icml.cc/Conferences/ICML2025/Styles/example_paper.pdf
- **Formatting Guide (2025)**: https://arxiv.org/html/2501.09783v1
- **Overleaf Template**: https://www.overleaf.com/latex/templates/icml2025-template/dhxrkcgkvnkt

### LaTeX Template & Requirements
- **Supported Software**: LaTeX only (no Word support)
- **File Format**: PDF submission required with embedded Type-1 fonts only
  - Verify fonts using `pdffonts` (Linux) or File/DocumentProperties/Fonts (Acrobat)
- **File Size**:
  - Submission: Maximum 50MB
  - Camera-ready: Maximum 20MB

### Text Layout & Typography
- **Page Size**: Standard
- **Font**: 10 point type with 11 point vertical spacing
- **Format**: Two-column layout (do not alter)

### Title & Abstract
- **Title**: Content words capitalized
- **Abstract Heading**: Centered, bold, 11 point
- **Abstract Body**: 10 point type, 11 point spacing
- **Abstract Margin**: Indented 0.25 inches on left and right
- **Abstract Length**: One paragraph, 4–6 sentences

### Author Information
- **Review Type**: Double-blind review
- **Requirement**: No identifying author information on title page or in paper

### Figures & Tables
- **Figure Captions**:
  - Placed under figures (not inside graphic)
  - 9-point type
  - Centered (unless 2+ lines, then flush left)
  - At least 0.1 inches space before and after caption
- **Table Captions**:
  - Placed above tables
  - 9-point type
  - Centered (unless 2+ lines, then flush left)
  - At least 0.1 inches space before and after title

### References & Citations
- Any consistent citation style acceptable
- Reference formatting flexible

### Page Limits & Structure
- **Main Paper**: 8 pages maximum
- **References & Appendices**: Unlimited
- **Important**: Do not compress format by reducing vertical spaces

---

## 3. ACL (Association for Computational Linguistics)

### Official Resources
- **Official Style Files GitHub**: https://github.com/acl-org/acl-style-files
- **Formatting Guidelines**: https://acl-org.github.io/ACLPUB/formatting.html
- **ACL 2023 Style Guide**: https://2023.aclweb.org/calls/style_and_formatting/
- **Overleaf Template**: https://www.overleaf.com/latex/templates/association-for-computational-linguistics-acl-conference/jvxskxpnznfj

### LaTeX Template & Requirements
- **Supported Software**: LaTeX (preferred)
- **Style File**: Official `acl.sty` provided
- **Important**: Do not modify style files or use templates from other conferences

### Page Size & Layout
- **Page Format**: A4 paper (21 cm × 29.7 cm) ONLY
- **Column Layout**: Two-column format (required)
- **Note**: Papers submitted with any other page size will be rejected

### Typography
- **Font**: Times New Roman (standard)
- **Font Size**: Consistent with provided templates

### References & Citations
- **Citation Package**: natbib (strongly encouraged)
- **Citation Commands**:
  - `\citet`: Author (year) format
  - `\citep`: (Author, year) format
  - `\citealp`: Author, year format (useful within parentheses)
- **Bibliography Style**: `acl_natbib.bst` (follows APA format roughly)
- **Bibliography Files Included**:
  - LaTeX style file (`acl.sty`)
  - Bibliography style (`acl_natbib.bst`)
  - Example bibliography (`custom.bib`)
  - ACL Anthology bibliography (`anthology.bib`)

### Structure Types
- **Long Papers**: Follow ACL two-column format
- **Short Papers**: Follow ACL two-column format
- **Extended Abstracts**: Follow ACL two-column format

### Paper Categories
- Long papers (varies by year, typically 8 pages)
- Short papers (varies by year, typically 4 pages)
- References do not count toward page limit

---

## 4. IEEE Formatting Guidelines

### Official Resources
- **IEEE Formatting Guide**: https://www.scribbr.com/ieee/ieee-paper-format/
- **Paper Format**: https://www.ieee-ies.org/conferences/paper-format-for-conferences
- **Guidelines**: https://ewh.ieee.org/conf/powerafrica/docs/authors_kit/guidelineshtml.html
- **IEEE Template Selector**: Available at IEEE website for various publication types

### Page Size & Margins
- **Page Format**: Letter (8.5" × 11") or A4 (21 cm × 29.7 cm)
- **Standard Margins**:
  - Left and right: 0.7 inches (18mm)
  - Top and bottom: 1 inch (25mm)
- **A4 Specific Margins**:
  - Top: 19mm (0.75")
  - Bottom: 43mm (1.69")
  - Left and right: 14.32mm (0.56")

### Typography
- **Font**: Times New Roman (primary), or acceptable alternatives:
  - Nimbus Roman No 9
  - Liberation fonts
- **Font Sizes**:
  - Title: 24 point
  - Body text: 10-12 point
  - Recommended: 10 point

### Column Layout
- **Format**: Two-column layout (required)
- **Column Separation**: White space of 0.25" (6.35mm)

### Figures & Tables
- **Figure Captions**:
  - Placed under figures
  - Format: "Fig. [number]. [title]"
  - Example: "Fig. 3. Citation errors in undergraduate papers, 2005-2015"
- **Table Captions**:
  - Placed above tables
  - Format: "TABLE [number (Roman numerals)]. [CAPTION IN CAPITALS]"
- **Labeling**: Parts labeled with lowercase letters in parentheses: (a), (b), (c), etc.
- **Numbering**: Figures, tables, and equations numbered separately and consecutively
- **Font in Graphics**:
  - Recommended font size: 9-10 points
  - Acceptable fonts: Helvetica, Times New Roman, Arial, Cambria, Symbol
  - Use consistent font throughout all graphics

### References & Citations
- **Citation Format**: Bracketed numbers [1], [2], [3]
- **Sequential Citations**: [1, 2] or [1]-[3]
- **Citation Style**: Numbered/sequential format
- **Reference List**: Alphabetical by lead author's last name

### Templates
- **Available Formats**: Microsoft Word and LaTeX
- **Template Selector**: Use IEEE's template selector for publication type and format

### Paper Length
- Varies by publication and conference (typically 6-8 pages)

---

## 5. ACM Formatting Guidelines

### Official Resources
- **CHI Publication Formats**: https://chi2026.acm.org/chi-publication-formats/
- **ACM Reference Formatting**: https://www.acm.org/publications/authors/reference-formatting
- **CHI 2019 Format Guide**: https://chi2019.acm.org/authors/chi-proceedings-format/
- **ACM SIGCHI Document Formats**: https://github.com/sigchi/Document-Formats

### Document Format
- **Review Phase Format**: Single-column layout (optimized for TAPS workflow)
- **Publication Format**: Final format determined by conference
- **Important**: Using different templates may result in desk rejection

### Available Templates
- LaTeX template (recommended)
- Microsoft Word template with ACM fonts
- Overleaf template for online collaborative writing

### Typography
- **Font**: Primary fonts specified in template
- **Figure Captions**: Times New Roman, 9-point bold
- **Caption Format**: Spelled-out labels (e.g., "Table 1", "Figure 2", not "Tab. 1")

### References & Citations
- **Citation Format**: Bracketed sequential numbers [1]
- **Multiple Citations**: [1, 2] or [1]-[3]
- **Citation Style**: ACM SIGCHI Proceedings style
- **Bibliography**: Numerical order, organized by citation order
- **Full Names Preferred**: ACM prefers full author names over initials
- **Citation Management**: Zotero can select "ACM SIGCHI Proceedings" style

### Accessibility Requirements
- **Accessible Submissions**: Required for reviewer access
- **Guide**: Follow SIGCHI's Guide to an Accessible Submission
- **Format**: Ensure proper document structure and alt text

### Paper Length
- **Papers**: Typically 8-10 pages for main content
- **Extended Abstracts**: Shorter format (varies by year)
- **References**: Do not count toward page limit

---

## 6. arXiv Best Practices

### Official Resources
- **Submission Guidelines**: https://info.arxiv.org/help/submit/index.html
- **Format Requirements**: https://info.arxiv.org/help/policies/format_requirements.html
- **Submission Guide**: https://www.cardenas.sites.wfu.edu/arxiv/

### File Format & Submission Requirements
- **Supported Format**: TeX/LaTeX (strongly recommended)
- **NOT Accepted**:
  - DVI files
  - PostScript (PS) files
  - PDF created from TeX/LaTeX source
  - Scanned documents
- **File Naming**: Case sensitive (myfile.tex ≠ MyFile.tex)
- **Prohibited Characters**: Spaces, question marks, asterisks in filenames

### Figure Requirements
- **PDFLaTeX**: Figures must be .pdf, .jpg, or .png
- **Traditional (La)TeX**: Figures must be .ps or .eps
- **Important**: arXiv does NOT perform format conversion; ensure correct format before upload

### File Organization
- **Source Structure**: Organize all source files properly
- **Bibliography**: Include compiled `.bbl` file (pre-compiled bibliography)
- **Required Files**: All auxiliary files, style files, custom packages

### Pre-Submission Preparation
- **Testing**: Compile document locally or on trusted platform (Overleaf)
- **Comments**: Remove internal LaTeX comments and sensitive information
  - Source files are publicly accessible
  - Clean out proprietary or confidential notes
- **Common Mistakes** (top 5):
  1. Mixed figure file formats
  2. Case mismatch between TeX source and figure filenames
  3. Default hyperref failures
  4. Missing or differing versions of custom style files
  5. Missing, misnamed, or locally-pathed figure file references

### Submission Requirements
- **Endorsements**: New users or new category submissions may require endorsements
- **Licensing**: Grant arXiv.org irrevocable license to distribute work
- **Agreements**: Accept Submittal Agreement, Code of Conduct, Moderation and Privacy Policies

### General Formatting
- Follow conference guidelines if submitting for specific venue
- Example templates for NeurIPS, ICML, ICLR, COLM available on arXiv

---

## 7. Stanford Computer Science Paper Guidelines

### Official Resources
- **Dissertation Format Requirements**: https://studentservices.stanford.edu/my-academics/earn-my-degree/graduate-degree-progress/dissertations-and-theses/prepare-your-work-0
- **Stanford PhD Thesis Template**: https://www.overleaf.com/latex/templates/stanford-university-phd-thesis-template-suthesis-2e-dot-sty/bdbjhjrmrvkv
- **GitHub Example**: https://github.com/dcroote/stanford-thesis-example
- **Dissertation FAQ**: https://studentservices.stanford.edu/faqs-dissertation-thesis
- **CS Thesis Proposal Requirements**: https://www.cs.stanford.edu/phd-program-requirements-thesis-proposal

### Page Size & Margins
- **Page Format**: Standard U.S. letter size (8.5" × 11")
- **Margins**:
  - Binding edge (left): 1.5 inches
  - All other sides: 1 inch
  - Consistent with standard academic formatting

### Typography
- **Font Size**: 10, 11, or 12 point (required)
- **Acceptable Fonts**:
  - Times New Roman (preferred)
  - Courier
  - Courier Bold
  - Courier Oblique
  - Helvetica
  - Times
  - Symbol
  - Computer Modern
- **Line Spacing**: 1.5 or 2 (double-spacing preferred for theses)

### Document Format
- **Submission Format**: PDF (final electronic submission)
- **Tool Choice**: Student choice between Microsoft Word or LaTeX
- **LaTeX Support**: `suthesis-2e.sty` available for LaTeX users

### Pagination & Structure
- **Title Page**: Not physically numbered (counts as "i")
- **Copyright & Signature Pages**: Must be REMOVED from electronic submission
- **Page Numbering Starts**: "iv" at Abstract
- **Pagination Rule**: Follow title page with abstract, starting at "iv"

### Computer Science Specific Requirements
- **Thesis Proposal**:
  - Provides formative feedback opportunity
  - Private session with advisor/co-advisor and reading committee
  - Allows iteration before final dissertation
- **Reading Committee**: Required for all CS theses

### Committee & Approval
- **Approval Page**: Required in bound dissertation
- **Electronic Version**: Remove approval page from electronic PDF

---

## Summary Comparison Table

| Aspect | NeurIPS | ICML | ACL | IEEE | ACM | Stanford |
|--------|---------|------|-----|------|-----|----------|
| **Primary Software** | LaTeX | LaTeX | LaTeX | Word/LaTeX | LaTeX/Word | Word/LaTeX |
| **Page Size** | Standard | Standard | A4 Only | Letter/A4 | Variable | 8.5"×11" |
| **Columns** | 2 | 2 | 2 | 2 | 1 (review) | N/A |
| **Font** | 10pt Times | 10pt | Standard | 10-12pt Times | Template | 10-12pt |
| **Main Pages** | 8 | 8 | 6-9* | 6-8* | 8-10* | Variable |
| **Margins** | 1.5"L, others | Standard | Standard | 0.7" L/R, 1" T/B | Standard | 1.5"L, 1" others |
| **Citation Style** | Flexible | Flexible | natbib | Numbered | Numbered | N/A |
| **Figure Captions** | Under | Under | Standard | Under | Standard | N/A |
| **Table Captions** | Over | Over | Standard | Over | Standard | N/A |
| **Refs Count** | No | No | No | Varies | No | No |

*varies by specific conference and year

---

## Key Takeaways for Authors

### Formatting Best Practices
1. **Always use official templates** - Custom modifications risk rejection
2. **Verify font embedding** - Required for arXiv and ICML (Type-1 fonts only)
3. **Test locally first** - Compile on your machine before submission
4. **Maintain consistency** - Citation and reference styles must be uniform
5. **Read specific conference requirements** - Guidelines vary by year and venue

### Common Mistakes to Avoid
- Modifying style files (especially NeurIPS)
- Using wrong paper size (ACL requires A4 only)
- Incorrect figure/table caption placement
- Mixed figure file formats (arXiv)
- Compressed formatting to fit page limits

### File Management
- Use lowercase, simple filenames (no spaces)
- Include all necessary files in submission
- Pre-compile bibliography (.bbl file)
- Verify all figure references are correct
- Remove sensitive comments from LaTeX source

### Citation Strategy
- Check venue's preferred citation style
- Maintain internal consistency throughout
- Understand natbib vs. numbered systems
- Test bibliography compilation locally

---

## Additional Resources

- **Overleaf Templates**: https://www.overleaf.com (search venue-specific templates)
- **GitHub Style Files**: Check official organization repositories for each conference
- **ArXiv Submission**: https://info.arxiv.org/help/submit/index.html
- **ACM Publications**: https://www.acm.org/publications/authors/

---

*Last Updated: February 2026*
*Research compiled from official conference and institution guidelines*
