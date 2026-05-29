# amplifier-bundle-scientificpaper — DEPRECATED

> **This bundle has been merged into [amplifier-bundle-research](https://github.com/michaeljabbour/amplifier-bundle-research) and is no longer maintained.**

scientificpaper was a strict subset of the research bundle. All of its
capabilities — LaTeX authoring, multi-conference formatting (NeurIPS, ICML,
ACL, IEEE, ACM, arXiv), citation management, and PaperBanana figure
generation — now live in **amplifier-bundle-research**, maintained as a single
source of truth.

## Migrate

Full research workflow (recommended):
```bash
amplifier bundle add --app git+https://github.com/michaeljabbour/amplifier-bundle-research@main
```

Lean "just write a paper" experience (the former scientificpaper surface),
via the `paper-only` variant in that repo:
```bash
amplifier run --bundle ./bundles/paper-only.yaml "Draft a NeurIPS paper on ..."
```

This repository is archived (read-only) for historical reference.
