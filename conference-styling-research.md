# Conference Styling and Formatting Guidelines Research

**Research Date:** February 4, 2026  
**Compiled by:** Web Research Agent

This document provides comprehensive formatting guidelines for major academic conferences and publication venues in computer science, machine learning, and computational linguistics.

---

## Table of Contents

1. [NeurIPS (Neural Information Processing Systems)](#neurips)
2. [ICML (International Conference on Machine Learning)](#icml)
3. [ACL (Association for Computational Linguistics)](#acl)
4. [IEEE Formatting Guidelines](#ieee)
5. [ACM Formatting Guidelines](#acm)
6. [Stanford CS Paper Guidelines](#stanford)
7. [arXiv Best Practices](#arxiv)

---

## 1. NeurIPS (Neural Information Processing Systems) {#neurips}

### Official LaTeX Template Location
- **Official Site:** https://neurips.cc/Conferences/2024/PaperInformation/StyleFiles
- **Template Files:**
  - `neurips_2024.sty` - LaTeX style file
  - `neurips_2024.tex` - Template shell
  - `neurips_2024.pdf` - Example output
- **Repository:** Templates available directly from NeurIPS website each year
- **Overleaf:** Available as NeurIPS template on Overleaf

### Page Limits and Document Structure
- **Submission:** 9 pages of content (including figures and tables)
- **References:** Unlimited additional pages
- **Appendices:** Allowed in main submission (included in references section)
- **Supplementary Material:** Up to 100MB (PDF or ZIP), submitted separately
- **Camera-Ready:** Same 9 pages + unlimited references
- **File Size:** Maximum 50MB for submission

### Margins and Text Area Dimensions
- **Text Area:** 5.5 inches (33 picas) wide × 9 inches (54 picas) tall
- **Left Margin:** 1.5 inch (9 picas)
- **Top Margin:** 1 inch (6 picas) from top of page
- **Paper Size:** US Letter (8.5" × 11")
- **Column Format:** Single column

### Font Requirements
- **Body Text:** 10 point Times New Roman (or Times)
- **Leading:** 11 points vertical spacing
- **Title:** 17 point, bold, initial caps
- **Author Names:** Bold (for camera-ready)
- **Section Headings:**
  - First level: 12 point, bold, lowercase (except first word and proper nouns)
  - Second level: 10 point, bold
  - Third level: 10 point, bold
- **Abstract:** 10 point, indented 0.5 inch on both sides
- **Abstract Title:** 12 point, bold, centered

### Column Layout
- **Format:** Single column
- **Paragraph Separation:** 0.5 line space (5.5 points), no indentation

### Citation Style
- **Package:** natbib (loaded by default)
- **Style:** Author/year OR numeric (be consistent)
- **Format:** Any consistent reference style acceptable
- **Commands:** `\citet{}` for inline citations, `\citep{}` for parenthetical
- **Options:** Can use `nonatbib` option if natbib conflicts with other packages

### Figure and Table Formatting
- **Placement:** After first mention, can use color
- **Captions:** Below figures, lowercase (except first word and proper nouns)
- **Numbering:** Consecutive
- **Tables:** Use booktabs package recommended, no vertical rules
- **Caption Placement:** 
  - Figures: Below the figure (one line space before and after)
  - Tables: Above the table

### Supplementary Material Guidelines
- **Format:** PDF or ZIP only
- **Size Limit:** 100MB maximum
- **Content:** Appendices, proofs, data, code
- **Requirement:** Main paper must be self-contained
- **Anonymization:** Must follow same anonymity rules as main paper

### Special Requirements
- **Anonymization:** Required for submission (no author info, acknowledgments)
- **Line Numbers:** Added automatically for review
- **Checklist:** Required (entered in OpenReview, not in PDF)
- **Preprint Option:** Use `\usepackage[preprint]{neurips_2024}` for arXiv
- **Font Embedding:** Type 1 or Embedded TrueType fonts only
- **PDF Generation:** Use pdflatex directly

---

## 2. ICML (International Conference on Machine Learning) {#icml}

### Official LaTeX Template Location
- **Official Site:** https://icml.cc/Conferences/2026/AuthorInstructions
- **Style Files:** Available from ICML website (year-specific)
- **Template:** `icml2025.sty` style file + example paper
- **Overleaf:** ICML2025 Template available
- **GitHub:** Community repositories available (not official)

### Page Limits and Document Structure
- **Main Body:** 8 pages maximum
- **References:** Unlimited (do not count toward page limit)
- **Appendices:** Unlimited (included in main PDF after references)
- **Camera-Ready:** 9 pages allowed (extra page for addressing reviewer comments)
- **Supplementary Material:** Separate submission, optional for reviewers
- **File Size:** 50MB max for submission, 20MB for camera-ready

### Margins and Text Area Dimensions
- **Format:** Two-column layout
- **Paper Size:** US Letter or A4 (LaTeX handles automatically)
- **Margins:** Defined by style file (do not modify)
- **Text Width:** Controlled by icml style file
- **Column Separation:** Defined by style file

### Font Requirements
- **Body Text:** 10 point (style file default)
- **Font Family:** Times or similar serif font
- **Title:** Specified by style file
- **Headings:** Defined by style file (do not modify)

### Column Layout
- **Format:** Two columns
- **Balance:** Automatic via style file
- **Width:** Set by icml2025.sty

### Citation Style
- **Style:** Defined by ICML style file
- **Format:** Typically numbered citations
- **Bibliography:** Use standard BibTeX
- **Consistency:** Must be consistent throughout

### Figure and Table Formatting
- **Placement:** Near first reference
- **Wide Figures:** Can span both columns
- **Captions:** Style file provides formatting
- **Graphics:** PDF, EPS, PNG acceptable
- **Quality:** Must be legible when printed

### Supplementary Material Guidelines
- **Types Accepted:**
  - Supplementary manuscripts (PDF)
  - Code (zip or PDF, anonymized)
  - Data (anonymized repositories)
- **GitHub:** Anonymous repositories allowed (must be on stable branch)
- **Deadline:** Same as paper submission
- **Reviewer Access:** Optional for reviewers to view
- **Camera-Ready:** Originally submitted materials become public on OpenReview
- **Final Version:** No supplementary material option for proceedings; use archival repository links

### Special Requirements
- **LaTeX Only:** No support for other typesetting software
- **Anonymization:** Mandatory double-blind reviewing
- **Author Response:** Opportunity provided during review
- **OpenReview:** All submissions handled through OpenReview
- **Code Submission:** Encouraged for reproducibility

---

## 3. ACL (Association for Computational Linguistics) {#acl}

### Official LaTeX Template Location
- **GitHub Repository:** https://github.com/acl-org/acl-style-files
- **Overleaf Template:** Available (linked from GitHub)
- **Style Files:** `acl.sty` + supporting files
- **Example:** `acl_latex.tex` template file
- **Download:** Available as ZIP from GitHub repository

### Page Limits and Document Structure
- **Long Papers (Review):** 8 pages + unlimited references
- **Long Papers (Final):** 9 pages + unlimited references + acknowledgments
- **Short Papers (Review):** 4 pages + unlimited references  
- **Short Papers (Final):** 5 pages + unlimited references + acknowledgments
- **Limitations Section:** Required, after conclusion, before references (doesn't count)
- **Ethics Statement:** Optional, doesn't count toward page limit
- **Appendices:** Allowed, unlimited pages (reviewers not required to read)

### Margins and Text Area Dimensions
- **Paper Size:** A4 (21 cm × 29.7 cm) - **Critical: NOT US Letter**
- **Margins:**
  - Left: 2.5 cm
  - Right: 2.5 cm
  - Top: 2.5 cm
  - Bottom: 2.5 cm
- **Column Width:** 7.7 cm each
- **Column Height:** 24.7 cm
- **Gap Between Columns:** 0.6 cm
- **Verification:** 
  - pdfinfo should show: `Page size: 595.276 x 841.89 pts`
  - Apple Preview: 8.27 × 11.7 inches

### Font Requirements
- **Body Text:** 11 point Times Roman (single-spaced)
- **Title:** 15 point, bold, title case
- **Author Names:** 12 point, bold
- **Author Affiliation:** 12 point, regular
- **Abstract Heading:** 12 point, bold
- **Abstract Text:** 10 point
- **Section Titles:** 12 point, bold
- **Subsection Titles:** 11 point, bold
- **Bibliography:** 10 point
- **Captions:** 10 point
- **Footnotes:** 9 point
- **Paragraph Indent:** 0.4 cm (except first paragraph in section)

### Column Layout
- **Format:** Two columns (mandatory)
- **Exceptions:** Title, authors, affiliations, full-width figures/tables
- **Line Numbers:** Required for review version (in margins)

### Citation Style
- **Format:** Author-year in parentheses
- **Examples:**
  - (Gusfield, 1997)
  - Gusfield (1997) showed...
  - (Aho and Ullman, 1972) for two authors
  - (Chandra et al., 1981) for 3+ authors
- **Multiple Citations:** Collapse into single parentheses
- **Requirements:** 
  - Include DOIs when available
  - Full author names (not initials)
  - Alphabetical order in references

### Figure and Table Formatting
- **Placement:** Near first discussion
- **Wide Elements:** May span both columns
- **Graphics:** Vector formats preferred (PDF, EPS)
- **Accessibility:** Grayscale readability required
- **Captions:**
  - Format: "Figure 1: Caption text"
  - Position: Below figures/tables
  - Font: 10 point
  - Alignment: Centered if one line, left-aligned if multiple lines
- **Hyperlinks:** Dark blue (#000099), not underlined

### Supplementary Material Guidelines
- **Purpose:** Non-readable materials (code, data, proofs)
- **Format:** Separate upload from paper
- **License:** Must include appropriate licenses
- **Anonymization:** Must follow same anonymity rules
- **Reviewer Access:** Not required to review (supplemental to paper)
- **Content:** Preprocessing details, model parameters, source code, data

### Special Requirements
- **Font Embedding:** All fonts must be embedded (check with pdffonts)
- **Asian Fonts:** Must be embedded for cross-platform compatibility
- **Ruler:** Line numbers in margins for review version
- **Anonymization:** Required for review submissions
- **Ethics/Limitations:** Required dedicated sections

---

## 4. IEEE Formatting Guidelines {#ieee}

### Official LaTeX Template Location
- **Template Selector:** https://template-selector.ieee.org/
- **Overleaf:** "IEEE Conference Template"
- **Class File:** `IEEEtran.cls`
- **Documentation:** IEEEtran_HOWTO.pdf (available on CTAN)
- **CTAN:** http://www.ctan.org/tex-archive/macros/latex/contrib/IEEEtran/
- **Official:** https://www.ieee.org/ (various conference-specific templates)

### Page Limits and Document Structure
- **Typical Conference:** 6-8 pages (varies by conference)
- **Maximum:** Often 8 pages including references
- **Over-Length:** Additional page fees may apply (conference-specific)
- **Format:** Defined by IEEEtran class in conference mode

### Margins and Text Area Dimensions
- **Paper Size:** US Letter (8.5" × 11")
- **Margins (Letter):**
  - Top: 0.75 inch (19mm)
  - Bottom: 1 inch
  - Sides: 0.625 inch (each)
- **Single Column Width:** 7.25 inches
- **Double Column Width:** 3.5 inches each
- **Column Separation:** ~0.25 inch
- **Text Height:** Approximately 9.25 inches (varies with font size for integer line count)

### Font Requirements
- **Body Text:** 10 point Times Roman (typical)
- **Font Options:** 9pt, 10pt, 11pt, 12pt (class options)
- **Title:** 24 point Regular
- **Author Names:** 11 point Regular
- **Section Headings:** Defined by class
- **Abstract:** Same as body text
- **Recommended:** Times New Roman throughout

### Column Layout
- **Format:** Two columns (double column mode)
- **Option:** Single column available but not for conference papers
- **Class Option:** `\documentclass[conference]{IEEEtran}`
- **Column Balancing:** Automatic on final page

### Citation Style
- **Default:** Numbered citations [1], [2], etc.
- **Package:** IEEEtran.bst BibTeX style
- **Format:** IEEE citation format (numeric)
- **In-Text:** Square brackets [1]
- **Sorting:** By order of appearance

### Figure and Table Formatting
- **Captions:** Below figures, above tables (IEEE convention)
- **Numbering:** Arabic numerals, consecutive
- **Wide Elements:** Can span both columns (use figure* or table*)
- **Graphics:** EPS, PDF for vector; avoid GIF/JPEG at low resolution
- **Font in Figures:** Match document text when possible

### Supplementary Material Guidelines
- **Conference-Specific:** Check individual conference CFP
- **Typically:** Supplemental materials allowed as separate files
- **Format:** PDF preferred
- **Size Limits:** Vary by conference

### Special Requirements
- **No Page Numbers:** Do not include in submission (added by publisher)
- **Keywords:** Include if requested by conference
- **Copyright Notice:** Added by publisher
- **PDF/A Compliance:** May be required for final version
- **Class Mode:** Use `conference` option for conference papers

---

## 5. ACM Formatting Guidelines {#acm}

### Official LaTeX Template Location
- **Official Site:** https://www.acm.org/publications/proceedings-template
- **Class:** acmart version 2.10 (December 23, 2024)
- **CTAN:** https://ctan.org/pkg/acmart
- **Overleaf:** "ACM Conference Proceedings Template"
- **GitHub:** https://github.com/borisveytsman/acmart/
- **Documentation:** acmguide.pdf (comprehensive user guide)

### Page Limits and Document Structure
- **Conference-Specific:** Page limits vary by conference (typically 8-12 pages)
- **Review Format:** Single column with `manuscript` option
- **Camera-Ready:** Two-column `sigconf` format
- **Template Style:** `\documentclass[sigconf]{acmart}`
- **Sections:** Title, abstract, CCS concepts, keywords, body, acknowledgments, references

### Margins and Text Area Dimensions
- **Controlled by Template:** Do not modify margins manually
- **Typical Margins:** ~0.75 inches or less (template-controlled)
- **Column Format:** Two columns for `sigconf`
- **Column Width:** Defined by acmart class
- **Text Area:** Automatically calculated by template
- **Paper Size:** US Letter

### Font Requirements
- **Body Text:** 9 point serif font
- **Font Family:** Times New Roman or Libertine
- **Title:** Template-defined size
- **Headings:** Automatically sized by class
- **Abstract:** 9 point
- **Captions:** 9 point
- **References:** 9 point
- **Code Listings:** Monospace, template-defined

### Column Layout
- **Format:** Two columns (sigconf mode)
- **Review:** Single column (manuscript mode)
- **Balance:** Automatic
- **Separation:** Template-controlled

### Citation Style
- **Default:** Numbered citations (numeric)
- **SIGGRAPH/SIGPLAN:** Author-year format
  - Add `\citestyle{acmauthoryear}` before `\begin{document}`
- **BibTeX Style:** ACM-Reference-Format.bst
- **Requirements:** 
  - Full author names
  - DOIs when available
  - Consistent formatting

### Figure and Table Formatting
- **Captions:** Automatically formatted by template
- **Placement:** Top or bottom of column
- **Wide Figures:** Use `figure*` for full-width
- **Graphics:** PDF, PNG, JPEG acceptable
- **Permissions:** Required for third-party figures

### Supplementary Material Guidelines
- **Format:** Varies by conference
- **Submission:** Through conference management system
- **Types:** Code, data, videos, additional results
- **Archival:** Consider archival repositories for final version

### Special Requirements
- **CCS Concepts:** Required (Computing Classification System)
- **Keywords:** Required
- **Rights Management:** Handled by template and ACM
- **Modifications Prohibited:** Do not alter template margins, fonts, or spacing
- **Author Information:** Use template commands (`\author{}`, `\affiliation{}`)
- **Submission ID:** Can include with `\acmSubmissionID{}`

---

## 6. Stanford CS Paper Guidelines {#stanford}

### Official LaTeX Template Location
- **Thesis Template:** suthesis-2e.sty (unofficial but widely used)
- **Overleaf:** "Stanford University PhD Thesis Template"
- **Official Guidelines:** https://studentservices.stanford.edu/ (format requirements)
- **Note:** No official university-endorsed template; author responsible for compliance
- **Course-Specific:** Individual courses may have their own templates

### Page Limits and Document Structure
- **Dissertation/Thesis Structure:**
  1. Title page (format must be followed exactly)
  2. Copyright page (auto-generated by submission system)
  3. Signature page (auto-generated)
  4. Abstract (no length limit in PDF; 5000 chars for online)
  5. Optional: Preface, acknowledgments, dedication
  6. Table of contents
  7. Optional: List of tables, list of illustrations
  8. Main body with introduction
  9. References/Bibliography
  10. Optional: Appendices
- **Course Papers:** Vary by instructor (check syllabus)

### Margins and Text Area Dimensions
- **Paper Size:** US Letter (8.5" × 11")
- **Inner Margin:** 1.5 inches (binding edge)
  - Left edge if single-sided
  - Right edge for even pages, left for odd pages if double-sided
- **Other Margins:** 1.0 inch (top, bottom, outer)
- **Headers/Footers:** No closer than 0.5 inch from edge

### Font Requirements
- **Main Text:** 10, 11, or 12 point
- **Acceptable Fonts:**
  - Times New Roman (preferred)
  - Courier family
  - Helvetica family
  - Times family
  - Symbol
  - Computer Modern
- **Font Color:** Black only
- **Smaller Fonts:** Allowed for tables, captions, footnotes
- **Mathematical Notation:** Font embedding required if not Symbol font
- **Prohibited:** Script or ornamental fonts, proprietary fonts

### Column Layout
- **Format:** Single column (for theses)
- **Course Papers:** May vary (often single column for technical reports)

### Citation Style
- **Department-Specific:** Follow approved style guide for field
- **Recommended Guides:**
  - Turabian's Manual for Writers
  - MLA Handbook
  - Discipline-specific guides
- **Consistency:** Must use selected style consistently
- **Attribution:** Clearly identify contributions in multi-author work

### Figure and Table Formatting
- **Images:** Must be clearly discernible on screen and printed
- **Resolution:** 150 dpi minimum (72 dpi acceptable minimum)
- **Format:** JPEG or EPS preferred (JPEG2000 acceptable)
- **Size:** Must not exceed letter-size page (8.5" × 11")
- **Large Images:** Submit as supplemental files
- **Avoid:** GIF and PNG not preferred

### Supplementary Material Guidelines
- **Maximum Files:** 20 supplemental files
- **File Size:** 1 GB maximum per file
- **Formats:** No restrictions (recommended formats for preservation):
  - Text: PDF, plain ASCII
  - Images: TIFF, JPEG, JPEG2000
  - Audio: WAV, AIFF, MP3
  - Video: MPEG, QuickTime, AVI
  - Data: Plain ASCII with codebooks
- **Multimedia:** Not embedded in main PDF; submit separately
- **Description:** 120 character limit for each file
- **Copyright:** Permission required for copyrighted supplemental content

### Special Requirements
- **Spacing:** 1.5 or double-spaced main text (single spacing for footnotes, quotes, tables)
- **Pagination:**
  - Preliminary pages: lowercase Roman numerals (iv, v, vi...)
  - Title page = i (not printed)
  - Copyright page ii and signature page iii auto-inserted (remove from your PDF)
  - Abstract starts at page iv
  - Main body: Arabic numerals starting at 1
- **Language:** English (exceptions possible with dean approval for language studies)
- **Embedded Links:** Spell out full URLs (e.g., http://www.stanford.edu)
- **Security:** No password protection on PDFs
- **File Names:** Alphanumeric, hyphen, underscore, @, space, &, comma only; max 120 chars

---

## 7. arXiv Best Practices {#arxiv}

### Official LaTeX Template Location
- **No Specific Template:** arXiv accepts papers in any standard format
- **Best Practices:** https://info.arxiv.org/help/submit_latex_best_practices.html
- **Submission Guide:** https://info.arxiv.org/help/submit_tex.html
- **Supported Packages:** Use LaTeXML-supported packages when possible
- **Package List:** https://github.com/brucemiller/LaTeXML (check .ltxml files)

### Page Limits and Document Structure
- **No Limits:** arXiv does not impose page limits
- **Best Practice:** Follow original conference/journal format
- **Preprint Option:** Use conference preprint options (e.g., `\usepackage[preprint]{neurips_2024}`)
- **Structure:** Standard academic paper structure

### Margins and Text Area Dimensions
- **No Requirements:** Use conference/journal template margins
- **Recommendation:** Standard margins for readability

### Font Requirements
- **Recommended:** Times or Nimbus font package
- **Avoid:** Computer Modern for main text (conversion to HTML works better with Times/Nimbus)
- **Embedding:** All fonts must be embedded
- **Non-English Support:** CID and Identity-H fonts must be converted to outlines or removed

### Column Layout
- **No Requirement:** Typically follow source conference format
- **Single or Double:** Either acceptable

### Citation Style
- **No Requirement:** Use conference/journal style
- **BibTeX:** Supported (.bbl file or .bib files)
- **Auto-Detection:** System detects bibliography compiler automatically
- **Completeness:** Ensure all .bib files are included if not uploading .bbl

### Figure and Table Formatting
- **Graphics:** Standard LaTeX graphics packages
- **Formats:** PDF, PNG, JPEG, EPS
- **Resolution:** Should be clear and legible
- **Accessibility:** Include alt text for images using graphicx:
  ```latex
  \includegraphics[alt={description}]{image}
  ```

### Supplementary Material Guidelines
- **Data/Code:** Can be included as ancillary files
- **Links:** Can link to external repositories (GitHub, etc.)
- **Format:** Various formats accepted for ancillary files

### Special Requirements for HTML Conversion
- **Use Supported Packages:** Check LaTeXML support list
- **Alt Text:** Include for all images for accessibility
- **Semantic Macros:** Use meaningful commands (not just visual formatting)
  - ✓ `\section{Introduction}` 
  - ✗ `{\normalfont\fontsize{12}{15}\bfseries Introduction}`
  - ✓ `\emph{text}` for emphasis
  - ✗ `{\it text}` (purely visual)
- **Standard Front Matter:**
  ```latex
  \title{Title}
  \author{Author One \AND Author Two}
  \begin{abstract}
  ...
  \end{abstract}
  ```
- **Compiler:** Overleaf users should use "stop on errors" mode
- **TeX Live:** Use most recent version available
- **Accessibility:** Semantic markup improves screen reader compatibility and search discoverability

### Submission Best Practices
- **Source Files:** Submit .tex source with all dependencies
- **Graphics:** Include all image files
- **Bibliography:** Include .bib files or .bbl file
- **Completeness:** Ensure submission compiles successfully
- **File Organization:** Use clear directory structure
- **Logs:** Check compilation logs for warnings
- **Testing:** Test compilation before submission

---

## Summary Comparison Table

| Conference | Page Limit | Paper Size | Columns | Body Font | Margins | Citation Style |
|-----------|-----------|-----------|---------|-----------|---------|---------------|
| **NeurIPS** | 9 + refs | US Letter | Single | 10pt Times | L:1.5", T:1" | natbib (flexible) |
| **ICML** | 8 + refs | US Letter | Double | 10pt Times | Template | Numbered |
| **ACL** | 8 + refs | **A4** | Double | 11pt Times | 2.5cm all | Author-year |
| **IEEE** | 6-8 total | US Letter | Double | 10pt Times | 0.75" top, 0.625" sides | Numbered [1] |
| **ACM** | Varies | US Letter | Double | 9pt serif | Template | Numbered (default) |
| **Stanford** | N/A (thesis) | US Letter | Single | 10-12pt | Inner:1.5", Other:1" | Field-specific |
| **arXiv** | N/A | Any | Any | Times/Nimbus | Source format | Source format |

---

## Key Differences to Note

### Critical Format Differences
1. **ACL uses A4 paper** while most others use US Letter
2. **Font sizes vary:** ACM (9pt), NeurIPS/IEEE/ICML (10pt), ACL (11pt)
3. **NeurIPS is single-column** while most conferences use two-column
4. **Citation styles:** ACL uses author-year; most others use numeric

### Template Modification Warnings
- **NeurIPS:** Modifications may lead to rejection without review
- **ACM:** "Modifications are not allowed" - explicit prohibition
- **ICML:** Must follow required format or automatic rejection
- **IEEE:** Discouraged; use class options instead
- **ACL:** Must adhere to specifications or risk rejection

### Page Limit Clarifications
- **"+ refs"** means references don't count toward limit
- **Appendices:** NeurIPS/ICML allow in main PDF; ACL allows but reviewers not required to read
- **Supplementary:** Most conferences allow separate supplementary materials
- **Camera-Ready:** Often get +1 page for final version (ICML, ACL)

### Anonymization Requirements
- **Double-Blind Conferences:** NeurIPS, ICML, ACL require anonymization
- **Author Information:** Remove for submission, add for camera-ready
- **Acknowledgments:** Remove for submission (use `\begin{ack}...\end{ack}` environments that auto-hide)
- **Self-Citations:** Refer to own work in third person during review

---

## Resources and Links

### Primary Sources
- **NeurIPS:** https://neurips.cc/
- **ICML:** https://icml.cc/
- **ACL:** https://aclweb.org/ | https://github.com/acl-org/acl-style-files
- **IEEE:** https://www.ieee.org/ | https://template-selector.ieee.org/
- **ACM:** https://www.acm.org/publications/proceedings-template
- **Stanford:** https://studentservices.stanford.edu/
- **arXiv:** https://info.arxiv.org/help/submit_latex_best_practices.html

### Useful Tools
- **Overleaf:** Online LaTeX editor with templates for all major conferences
- **pdffonts:** Check font embedding (command-line tool)
- **pdfinfo:** Verify paper size and PDF properties
- **LaTeXML:** HTML conversion tool (for arXiv)
- **Template Selector:** IEEE template selection tool

### Documentation Downloads
- **NeurIPS:** Download style files from yearly conference page
- **ACM Guide:** acmguide.pdf from CTAN
- **IEEE Guide:** IEEEtran_HOWTO.pdf from CTAN
- **ACL:** Documentation in GitHub repository

---

## Confidence Level and Notes

### Research Confidence: HIGH (95%)

**Information Sources:**
- Official conference websites (NeurIPS, ICML, ACL, IEEE, ACM)
- Official template documentation and style guides
- LaTeX package repositories (CTAN)
- GitHub official repositories (ACL)
- Stanford Student Services official website
- arXiv official help documentation

**Information Currency:**
- NeurIPS: Based on 2024 guidelines (2026 expected similar)
- ICML: Based on 2025/2026 author instructions
- ACL: Current formatting guidelines (general *ACL)
- IEEE: Current IEEEtran class specifications
- ACM: acmart v2.10 (December 2024) - current version
- Stanford: Current dissertation/thesis requirements (accessed Feb 2026)
- arXiv: Current best practices documentation

**Verification Recommendations:**
1. Always check the specific year's Call for Papers for updated requirements
2. Download current year's templates before starting work
3. Verify page limits with specific conference CFP (can change yearly)
4. Test compilation early and often
5. For critical submissions, review formatting checklist before submission

**Gaps and Limitations:**
- Specific margin dimensions for ICML/ACM are template-controlled (not publicly documented in detail)
- IEEE specifications vary significantly by conference; consult specific CFP
- Stanford course-specific guidelines not included (highly variable)
- Conference workshops may have different requirements than main conference
- Some older documentation referenced where current year not yet available

**Additional Notes:**
- Many conferences now use OpenReview, CMT, or EasyChair for submissions
- LaTeX is strongly preferred (sometimes required) for technical conferences
- Most conferences reject submissions that violate formatting requirements
- Camera-ready versions often have slightly different requirements than review versions
- Always compile and check final PDF before submission deadline

---

*This research was compiled on February 4, 2026. Always verify current requirements from official conference websites before submission.*
