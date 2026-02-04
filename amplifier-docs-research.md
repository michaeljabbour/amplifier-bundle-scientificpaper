# Amplifier Bundle Development - Comprehensive Research Notes

**Research Date:** 2026-02-04  
**Sources:** microsoft/amplifier-foundation, microsoft/amplifier

---

## Table of Contents

1. [Bundle Composition Patterns](#bundle-composition-patterns)
2. [Module Development Guidelines](#module-development-guidelines)
3. [Context File Best Practices](#context-file-best-practices)
4. [Agent Authoring Patterns](#agent-authoring-patterns)
5. [Template and Asset Handling](#template-and-asset-handling)
6. [Anti-Patterns to Avoid](#anti-patterns-to-avoid)
7. [Quick Reference](#quick-reference)

---

## Bundle Composition Patterns

### The Thin Bundle Pattern (RECOMMENDED)

**Most bundles should be thin** - inheriting from foundation and adding only unique capabilities.

```yaml
---
bundle:
  name: my-capability
  version: 1.0.0
  description: Adds X capability

includes:
  - bundle: git+https://github.com/microsoft/amplifier-foundation@main
  - bundle: my-capability:behaviors/my-capability
---

# My Capability

@my-capability:context/instructions.md

---

@foundation:context/shared/common-system-base.md
```

**Key Benefits:**
- No duplication of foundation's capabilities
- Automatic updates from foundation
- Minimal maintenance burden
- Clear separation of concerns

### The Behavior Pattern

Behaviors are reusable capability add-ons that bundle agents + context + tools.

```yaml
# behaviors/my-capability.yaml
bundle:
  name: my-capability-behavior
  version: 1.0.0
  description: Adds X capability with agents and context

# Optional: Add tools specific to this capability
tools:
  - module: tool-my-capability
    source: git+https://github.com/microsoft/amplifier-bundle-my-capability@main#subdirectory=modules/tool-my-capability

# Declare agents this behavior provides
agents:
  include:
    - my-capability:agent-one
    - my-capability:agent-two

# Declare context files
context:
  include:
    - my-capability:context/instructions.md
```

**When to Use Behaviors:**
- Adding capability to any bundle (reusability)
- Want others to compose your capability onto their bundles
- Separating concerns cleanly
- Creating modular, mix-and-match capabilities

### Agent Definition Patterns

**Pattern 1: Include (Recommended)**
```yaml
agents:
  include:
    - my-bundle:my-agent      # Loads agents/my-agent.md
```

**Pattern 2: Inline (Valid for tool-scoped agents)**
```yaml
agents:
  my-agent:
    description: "Agent with bundle-specific tool access"
    instructions: my-bundle:agents/my-agent.md
    tools:
      - module: tool-special
        source: ./modules/tool-special
```

| Scenario | Pattern | Why |
|----------|---------|-----|
| Standard agent with own instructions | Include | Cleaner separation, context sink pattern |
| Agent needs specific tools | Inline | Can specify `tools:` for just this agent |
| Agent reused across bundles | Include | Separate file is more portable |
| Agent tightly coupled to bundle | Inline | Keep definition with bundle config |

### Directory Conventions

```
my-bundle/
├── bundle.md                 # Root bundle - thin entry point
├── behaviors/
│   └── my-capability.yaml    # Reusable behavior
├── agents/                   # Agent definitions
│   ├── agent-one.md
│   └── agent-two.md
├── context/
│   └── instructions.md       # Consolidated instructions
├── modules/                  # Local modules (when needed)
│   └── tool-my-capability/
│       ├── pyproject.toml
│       └── my_module/
├── docs/                     # Documentation
├── README.md
├── LICENSE
├── SECURITY.md
└── CODE_OF_CONDUCT.md
```

**Directory Purposes:**

| Directory | Purpose |
|-----------|---------|
| `/bundle.md` | Root bundle - establishes namespace |
| `/bundles/*.yaml` | Pre-composed standalone variants |
| `/behaviors/*.yaml` | "The value this repo provides" - compose onto YOUR bundle |
| `/providers/*.yaml` | Provider configurations to compose |
| `/agents/*.md` | Specialized agent definitions |
| `/context/*.md` | Shared instructions, knowledge |
| `/modules/` | Tool implementations specific to this bundle |
| `/docs/` | Guides, references, examples |

### Composition Merge Rules

| Section | Rule |
|---------|------|
| `session` | Deep merge (nested dicts merged recursively) |
| `spawn` | Deep merge (later overrides earlier) |
| `providers`, `tools`, `hooks` | Merged by module ID (configs deep-merged) |
| `agents` | Merged by agent name (later wins) |
| `context` | Accumulates with namespace prefix |
| `instruction` | Replace entirely (later wins) |

### Structural vs Conventional Classification

Bundles have TWO independent classification systems:

| Bundle | Structural | Conventional |
|--------|------------|--------------|
| `/bundle.md` | Root (`is_root=True`) | Root bundle |
| `/bundles/with-anthropic.yaml` | Nested (`is_root=False`) | Standalone bundle |
| `/behaviors/my-capability.yaml` | Nested (`is_root=False`) | Behavior bundle |
| `/providers/anthropic-opus.yaml` | Nested (`is_root=False`) | Provider bundle |

**Key Insight:** A "standalone bundle" (conventional) is still a "nested bundle" (structural) when loaded via `namespace:bundles/foo.yaml`.

---

## Module Development Guidelines

### Module Types

**Orchestrators** - Control AI agent execution loop
- `loop-basic` - Standard sequential execution
- `loop-streaming` - Real-time streaming with extended thinking
- `loop-events` - Event-driven with hook integration

**Providers** - Connect to AI model providers
- `provider-anthropic`, `provider-openai`, `provider-azure-openai`
- `provider-gemini`, `provider-vllm`, `provider-ollama`
- `provider-mock` - Testing without API calls

**Tools** - Extend AI capabilities
- `tool-filesystem`, `tool-bash`, `tool-web`
- `tool-search`, `tool-task`, `tool-todo`
- `tool-skills`, `tool-mcp`, `tool-slash-command`

**Context Managers** - Manage conversation state
- `context-simple` - In-memory with automatic compaction
- `context-persistent` - File-backed persistent context

**Hooks** - Extend lifecycle events
- `hooks-logging`, `hooks-redaction`, `hooks-approval`
- `hooks-streaming-ui`, `hooks-status-context`

### Development Workflows

**Scenario 1: Quick Fix to Single Module**
```bash
# Clone module repo
git clone https://github.com/microsoft/amplifier-module-tool-bash
cd amplifier-module-tool-bash

# Make changes
# ... edit code ...

# Test with environment override (temporary)
export AMPLIFIER_MODULE_TOOL_BASH=$(pwd)
cd ~/your-project
amplifier run "test bash changes"
```

**Scenario 2: Working on Multiple Modules**
```bash
# Set up workspace
mkdir ~/amplifier-workspace
cd ~/amplifier-workspace

# Clone modules
git clone https://github.com/microsoft/amplifier-module-tool-bash
git clone https://github.com/microsoft/amplifier-module-provider-anthropic

# Create project config
cat > .amplifier/settings.yaml << 'EOF'
sources:
  tool-bash: file://./amplifier-module-tool-bash
  provider-anthropic: file://./amplifier-module-provider-anthropic
EOF
```

**Scenario 3: Full Dev Workspace (Zero-Config Convention)**
```bash
# Create workspace
mkdir amplifier-workspace && cd amplifier-workspace

# Clone repos
git clone https://github.com/microsoft/amplifier-core
git clone https://github.com/microsoft/amplifier-app-cli
git clone https://github.com/microsoft/amplifier-module-tool-bash

# Use workspace convention for auto-discovery
amplifier module dev init
# Creates .amplifier/modules/ and offers to link modules

# Check status
amplifier module dev status
```

### Module Structure Contract

```toml
# pyproject.toml
[project]
name = "amplifier-module-tool-myfeature"
requires-python = ">=3.11"
dependencies = []   # NO amplifier-core (it's a peer dependency)

[project.entry-points."amplifier.modules"]
tool-myfeature = "amplifier_module_tool_myfeature"

[tool.uv.sources.amplifier-core]
git = "https://github.com/microsoft/amplifier-core"
branch = "main"
```

**CRITICAL:** Module ID must match entry point key (`tool-myfeature`)

### Implement Protocol

```python
# amplifier_module_tool_myfeature/__init__.py
from amplifier_core.protocols import Tool

class MyFeatureTool(Tool):
    def get_schema(self):
        return {
            "name": "my_feature",
            "description": "Does something useful",
            "input_schema": {
                "type": "object",
                "properties": {
                    "param": {"type": "string"}
                },
                "required": ["param"]
            }
        }

    async def execute(self, **kwargs):
        return {"result": f"Processed: {kwargs['param']}"}
```

### Module Dev Commands

```bash
# Initialize workspace
amplifier module dev init

# Link module to workspace
amplifier module dev link <module-id> [<path>]

# List workspace modules
amplifier module dev list

# Show workspace status
amplifier module dev status

# Test module
amplifier module dev test <module-id>
```

### Best Practices

1. **Keep Modules Focused** - One responsibility per module
2. **Follow Protocol Contracts** - Implement only what's required
3. **Test Behavior, Not Implementation** - Test public interface
4. **Document Public Interface** - Clear docstrings with examples
5. **No Runtime Dependencies** - `amplifier-core` is a peer dependency

### Override Strategies

| Method | Scope | Persistence | Use Case |
|--------|-------|-------------|----------|
| Env var | Terminal session | Temporary | Quick debugging |
| Workspace | Project | Permanent | Multi-module dev |
| Project config | Project | Permanent | Team overrides |
| User config | Global | Permanent | Personal forks |
| Bundle source | Bundle-specific | Permanent | Distribution |

---

## Context File Best Practices

### Consolidate Instructions Pattern

**Problem:** Inline instructions in bundle.md cause duplication and maintenance issues.

**Solution:** Create consolidated context files.

```markdown
# context/instructions.md
# My Capability Instructions

You have access to the my-capability tool for [purpose].

## Available Agents

- **my-agent** - Does X, useful for Y

## Usage Guidelines

[Instructions for the AI on how to use this capability]
```

Reference from behavior:
```yaml
# behaviors/my-capability.yaml
context:
  include:
    - my-capability:context/instructions.md
```

Reference from bundle.md:
```markdown
---
bundle:
  name: my-capability
includes:
  - bundle: foundation
  - bundle: my-capability:behaviors/my-capability
---

# My Capability

@my-capability:context/instructions.md

---

@foundation:context/shared/common-system-base.md
```

### @Mention Resolution

**In Markdown Body (bundle.md, agents/*.md):**
```markdown
@namespace:path/to/file.md
```

**In YAML Sections:**
```yaml
context:
  include:
    - namespace:path/to/file.md    # NO @ prefix!
```

**CRITICAL:** The `@` prefix is ONLY for markdown. Using `@` in YAML causes silent failure.

### context.include vs @mentions - Different Semantics!

| Pattern | Composition Behavior | Use When |
|---------|---------------------|----------|
| `context.include` | **ACCUMULATES** - propagates to including bundles | Behaviors that inject context into parents |
| `@mentions` | **REPLACES** - stays with this instruction only | Direct references in your own instruction |

**Use `context.include` in behaviors (.yaml files):**
```yaml
# behaviors/my-behavior.yaml
# This context propagates to ANY bundle that includes this behavior
context:
  include:
    - my-bundle:context/behavior-instructions.md
```

**Use `@mentions` in root bundles (.md files):**
```markdown
# Instructions
@my-bundle:context/my-instructions.md    # Stays with THIS instruction
```

### Load-on-Demand Pattern (Soft References)

**Problem:** Every `@mention` loads content eagerly, consuming tokens immediately.

**Solution:** Reference files WITHOUT `@` prefix for on-demand loading.

```markdown
**Documentation (load on demand):**
- Schema: recipes:docs/RECIPE_SCHEMA.md
- Examples: recipes:examples/code-review-recipe.yaml
- Guide: foundation:docs/BUNDLE_GUIDE.md
```

The AI can load these via `read_file` when actually needed.

| Pattern | Syntax | Loads | Use When |
|---------|--------|-------|----------|
| **@mention** | `@bundle:path` | Immediately | Content is ALWAYS needed |
| **Soft reference** | `bundle:path` (no @) | On-demand | Content is SOMETIMES needed |
| **Agent delegation** | Delegate to expert agent | When spawned | Content belongs to a specialist |

### Context Sink Pattern

Expert agents serve as **context sinks** - they carry heavy documentation that would bloat every session.

```yaml
---
meta:
  name: my-expert
  description: "Expert for X domain. Delegate when user needs..."
---

# My Expert

[Role description]

## Knowledge Base

@my-bundle:docs/FULL_GUIDE.md        # Heavy docs - loaded only when spawned
@my-bundle:docs/REFERENCE.md         # More heavy docs
@my-bundle:docs/PATTERNS.md          # Even more

---

@foundation:context/shared/common-agent-base.md
```

**Pair with thin awareness pointer in behavior:**

```yaml
# behaviors/my-expert.yaml
bundle:
  name: behavior-my-expert
  version: 1.0.0

agents:
  include:
    - my-bundle:my-expert    # Heavy agent file

context:
  include:
    - my-bundle:context/my-awareness.md  # Thin pointer (~30 lines)
```

The awareness file tells root sessions: "This domain exists. Delegate to `my-bundle:my-expert`."

---

## Agent Authoring Patterns

### Key Insight: Agents ARE Bundles

Agents use the same file format and are loaded via `load_bundle()`. The only difference is the frontmatter key.

```yaml
# Bundle frontmatter          # Agent frontmatter
bundle:                        meta:
  name: my-bundle                name: my-agent
  version: 1.0.0                 description: "..."
```

### The meta.description Field (CRITICAL)

This is THE critical field for agent discoverability. Answer three questions:

1. **WHEN** should I use this agent? (Activation triggers)
2. **WHAT** does it do? (Core capability)
3. **HOW** do I invoke it? (Examples)

**Template:**
```yaml
meta:
  name: my-agent
  description: |
    [ONE SENTENCE: What this agent does and why it matters]
    
    Use PROACTIVELY when [primary trigger condition].
    
    **Authoritative on:** [comma-separated domain terms/keywords]
    
    **MUST be used for:**
    - [Condition 1]
    - [Condition 2]
    
    <example>
    user: '[Example user request]'
    assistant: 'I'll delegate to [agent] because [reason].'
    <commentary>
    [Why this triggers the agent - helps LLMs learn the pattern]
    </commentary>
    </example>
```

**Real Example:**
```yaml
meta:
  name: bug-hunter
  description: |
    Specialized debugging expert. Use PROACTIVELY when user reports errors,
    unexpected behavior, or test failures.
    
    Examples:
    
    <example>
    user: 'The pipeline is throwing a KeyError somewhere'
    assistant: 'I'll use bug-hunter to systematically track down this KeyError.'
    <commentary>Bug reports trigger bug-hunter delegation.</commentary>
    </example>
```

### Description Requirements

Every agent description MUST include:

1. **WHY** - The Purpose
2. **WHEN** - Activation Triggers (use keywords: MUST, REQUIRED, ALWAYS, PROACTIVELY)
3. **WHAT** - Domain/Taxonomy Terms (Pattern: `**Authoritative on:** term1, term2, term3`)
4. **HOW** - Usage Examples (Use `<example>` blocks with `<commentary>`)

**Audit Checklist:**
- [ ] >100 words (not a one-liner)
- [ ] Has explicit trigger conditions
- [ ] Lists domain terms ("Authoritative on:")
- [ ] Includes at least one example
- [ ] Explains the value proposition

### Instruction Structure

```markdown
# Agent Name

[One-line role description]

**Execution model:** You run as a one-shot sub-session. Work with what 
you're given and return complete results.

## Operating Principles
1. [Principle 1]
2. [Principle 2]

## Workflow
1. [Step 1]
2. [Step 2]

## Output Contract

Your response MUST include:
- [Required element 1]
- [Required element 2]

---

@foundation:context/shared/common-agent-base.md
```

**Always end with the @mention** to include shared base instructions.

### Agent Spawning Patterns

```python
# Load agent as bundle
agent_bundle = await load_bundle("./agents/bug-hunter.md")

# Spawn sub-session
result = await prepared.spawn(
    child_bundle=agent_bundle,
    instruction="Find the bug in auth.py",
    compose=True,            # Compose with parent bundle (default: True)
    parent_session=session,  # Inherit UX from parent
    session_id=None,         # Or provide ID to resume existing sub-session
)

# Returns: {"output": response, "session_id": child_id}
print(result["output"])
```

### Spawning with Provider Preferences

```python
from amplifier_foundation import ProviderPreference

result = await prepared.spawn(
    child_bundle=agent_bundle,
    instruction="Quick analysis task",
    provider_preferences=[
        ProviderPreference(provider="anthropic", model="claude-haiku-*"),
        ProviderPreference(provider="openai", model="gpt-4o-mini"),
    ],
)
```

### Controlling Agent Tool Inheritance

```yaml
# In your bundle.md
tools:
  - module: tool-task
    source: git+https://github.com/microsoft/amplifier-module-tool-task@main
    config:
      exclude_tools: [tool-task]  # Agents inherit all EXCEPT these
```

Or use explicit allowlist:
```yaml
tools:
  - module: tool-task
    config:
      inherit_tools: [tool-filesystem, tool-bash]  # Agents get ONLY these
```

**Common pattern:** Prevent agents from delegating further:
```yaml
tools:
  - module: tool-task
    config:
      exclude_tools: [tool-task]  # Spawned agents can't delegate
```

---

## Template and Asset Handling

### Hybrid Bundle Pattern (Rare)

**When do you need this?** Only when your bundle provides a **standalone CLI tool** (installed via `uv tool install`) that **requires bundle assets at runtime**.

**Most bundles don't need this.** Use the standard pure bundle pattern for typical bundles.

```
my-hybrid-bundle/
├── pyproject.toml            # Python package config
├── src/my_package/           # Python code
│   ├── __init__.py
│   ├── cli.py
│   └── _bundle/              # Bundle assets INSIDE package
│       ├── bundle.yaml
│       ├── agents/
│       └── context/
├── modules/                  # Tool modules (separate packages)
│   └── tool-my-tool/
├── bundle.md                 # Root entry point
└── README.md
```

**Key pattern:** Bundle assets go in a `_bundle/` subdirectory INSIDE the Python package.

**pyproject.toml for hybrid bundles:**
```toml
[project]
name = "my-hybrid-bundle"
version = "0.1.0"
dependencies = [...]

[project.scripts]
my-cli = "my_package.cli:main"

[tool.hatch.build.targets.wheel]
packages = ["src/my_package"]

[tool.hatch.build.targets.wheel.force-include]
# Assets go INSIDE package, in _bundle/ subdirectory
"bundle.yaml" = "my_package/_bundle/bundle.yaml"
"agents" = "my_package/_bundle/agents"
"context" = "my_package/_bundle/context"
```

**Testing hybrid packages:**
```bash
uv build --wheel
uv pip install dist/*.whl --force-reinstall
python -c "from my_package import SomeClass"  # Verify imports work
```

### URI Formats

| Format | Example |
|--------|---------|
| **Local file** | `/path/to/bundle.md`, `./relative.md` |
| **Local directory** | `/path/to/bundle/` (finds `bundle.md` inside) |
| **Git HTTPS** | `git+https://github.com/org/repo@main` |
| **Git SSH** | `git+ssh://git@github.com/org/repo@main` |
| **Subdirectory** | `git+https://github.com/org/repo@main#subdirectory=path/to/bundle` |

### Namespace Resolution with Subdirectories

**The namespace is ALWAYS the `bundle.name` field from YAML frontmatter, NOT the git URL.**

```
# Repository structure:
amplifier-expert-cookbook/          # Git repo root
└── cli-tool-builder/               # Subdirectory containing bundle
    ├── bundle.md                   # Has: bundle.name: cli-tool-builder
    └── context/
        └── instructions.md
```

When loaded via:
```
git+https://github.com/org/amplifier-expert-cookbook@main#subdirectory=cli-tool-builder
```

| Question | Answer |
|----------|--------|
| **Namespace is:** | `cli-tool-builder` (from `bundle.name`) |
| **Namespace is NOT:** | `amplifier-expert-cookbook` (the repo name) |

**Path resolution is relative to the bundle root:**
```yaml
# ❌ WRONG: Including subdirectory in path
context:
  include:
    - cli-tool-builder:cli-tool-builder/context/instructions.md  # Duplicates path!

# ✅ CORRECT: Path relative to bundle root
context:
  include:
    - cli-tool-builder:context/instructions.md
```

### Source URI Formats for Modules

```yaml
tools:
  - module: tool-name
    source: ./modules/tool-name               # Local path (relative to bundle)
  
  - module: tool-external
    source: git+https://github.com/org/repo@main
  
  - module: tool-nested
    source: git+https://github.com/org/repo@main#subdirectory=modules/foo
```

---

## Anti-Patterns to Avoid

### ❌ Duplicating Foundation

```yaml
# DON'T DO THIS when you include foundation
includes:
  - bundle: foundation

tools:
  - module: tool-filesystem     # Foundation has this!
    source: git+https://...

session:
  orchestrator:                 # Foundation has this!
    module: loop-streaming
```

**Fix:** Remove duplicated declarations. Foundation provides them.

### ❌ Inline Instructions in bundle.md

```yaml
---
bundle:
  name: my-bundle
---

# Instructions

[500 lines of instructions here]
```

**Fix:** Move to `context/instructions.md` and reference with `@my-bundle:context/instructions.md`.

### ❌ Skipping the Behavior Pattern

```yaml
# DON'T DO THIS for capability bundles
---
bundle:
  name: my-capability

includes:
  - bundle: foundation

agents:
  include:
    - my-capability:agent-one
---

[All instructions inline]
```

**Fix:** Create `behaviors/my-capability.yaml` with agents + context, then include it.

### ❌ Using @ Prefix in YAML

```yaml
# DON'T DO THIS - @ prefix is for markdown only
context:
  include:
    - "@my-bundle:context/instructions.md"   # ❌

# DO THIS
context:
  include:
    - my-bundle:context/instructions.md      # ✅
```

### ❌ Using Repository Name as Namespace

```yaml
# If loading: git+https://github.com/microsoft/amplifier-bundle-recipes@main
# And bundle.name is: "recipes"

# DON'T DO THIS
agents:
  include:
    - amplifier-bundle-recipes:recipe-author   # ❌ Repo name

# DO THIS
agents:
  include:
    - recipes:recipe-author                    # ✅ bundle.name value
```

### ❌ Including Subdirectory in Paths

```yaml
# If loading: git+https://...@main#subdirectory=bundles/foo
# And bundle.name is: "foo"

# DON'T DO THIS
context:
  include:
    - foo:bundles/foo/context/instructions.md   # ❌ Redundant path

# DO THIS
context:
  include:
    - foo:context/instructions.md               # ✅ Relative to bundle location
```

### ❌ force-include Shadowing Python Namespace

```toml
# DON'T DO THIS - shadows the Python package!
[tool.hatch.build.targets.wheel]
packages = ["src/my_package"]

[tool.hatch.build.targets.wheel.force-include]
"agents" = "my_package/agents"        # ❌ Creates my_package/ with no __init__.py!

# DO THIS - use _bundle/ subdirectory
[tool.hatch.build.targets.wheel.force-include]
"agents" = "my_package/_bundle/agents"      # ✅ Inside package, won't shadow
```

### ❌ Declaring amplifier-core as Runtime Dependency

```toml
# DON'T DO THIS in modules/tool-*/pyproject.toml
[project]
dependencies = [
    "amplifier-core>=1.0.0",           # ❌ Not on PyPI, will fail
]

# DO THIS
[project]
dependencies = []   # ✅ amplifier-core is a peer dependency
```

### ❌ Heavy Docs in Always-Loaded Context

```yaml
# ❌ BAD: Heavy docs in behavior context (loads for everyone)
context:
  include:
    - my-bundle:docs/FULL_GUIDE.md      # 500 lines in every session!

# ✅ GOOD: Thin pointer in behavior, heavy docs in agent
context:
  include:
    - my-bundle:context/awareness.md    # 30 lines: "domain exists, delegate"
```

### ❌ Vague Agent Descriptions

```yaml
# ❌ Too vague
meta:
  description: "Helps with code stuff"

# ✅ Clear triggers + capability + examples
meta:
  description: |
    Use PROACTIVELY when user reports errors or test failures.
    Systematic debugging with hypothesis-driven root cause analysis.
    
    <example>
    user: 'The build is failing'
    assistant: 'I'll use bug-hunter to investigate.'
    </example>
```

---

## Quick Reference

### Bundle File Structure

```markdown
---
bundle:
  name: my-bundle
  version: 1.0.0
  description: What this bundle provides

includes:
  - bundle: foundation
  - bundle: my-bundle:behaviors/x

tools:
  - module: tool-name
    source: ./modules/tool-name
    config:
      setting: value

spawn:
  exclude_tools: [tool-task]

agents:
  include:
    - my-bundle:agent-name

hooks:
  - module: hooks-custom
    source: git+https://github.com/...
---

# System Instructions

Your markdown instructions here.

@my-bundle:docs/GUIDE.md
```

### Agent File Structure

```markdown
---
meta:
  name: my-agent
  description: |
    [WHY/WHEN/WHAT/HOW with examples]
---

# Agent Name

[Instructions]

---

@foundation:context/shared/common-agent-base.md
```

### Key Commands

```bash
# Bundle management
amplifier bundle add git+https://github.com/org/bundle@main
amplifier bundle use foundation
amplifier bundle current
amplifier bundle update --check

# Module development
amplifier module dev init
amplifier module dev link <module-id>
amplifier module dev status
amplifier module dev test <module-id>

# Testing
export AMPLIFIER_MODULE_TOOL_NAME=$(pwd)
uv run pytest
uv run pytest --cov
```

### Decision Framework

**When to Include Foundation:**
- ✅ Adding capability to AI assistants
- ✅ Need base tools (filesystem, bash, web)
- ✅ Building on existing bundle
- ❌ Creating standalone tool

**When to Use Behaviors:**
- ✅ Adding agents + context
- ✅ Adding tool + agents
- ✅ Want others to use your capability
- ❌ Creating a simple bundle variant

**When to Create Local Modules:**
- ✅ Tool is bundle-specific
- ❌ Tool is generally useful → Extract to separate repo
- ❌ Multiple bundles need the tool → Extract to separate repo

### Policy Behaviors

Policy behaviors are app-level capabilities composed at runtime:
- **App-context-dependent** - CLI wants notifications; headless service doesn't
- **Root-session-only** - Don't fire for sub-agents or recipe steps
- **User-configurable** - Enabled/disabled via `settings.yaml`

```yaml
# settings.yaml
config:
  notifications:
    desktop:
      enabled: true
      suppress_if_focused: true
    push:
      enabled: true
      service: ntfy
      topic: "my-topic"
```

### Exemplar Repository

**amplifier-bundle-recipes** - Canonical example of thin bundle + behavior pattern:
- Thin bundle.md (14 lines of YAML)
- Behavior pattern for capability
- Context de-duplication
- Local module with source reference
- No duplication from foundation

https://github.com/microsoft/amplifier-bundle-recipes

---

## Additional Resources

**Core Documentation:**
- [BUNDLE_GUIDE.md](https://github.com/microsoft/amplifier-foundation/blob/main/docs/BUNDLE_GUIDE.md) - Comprehensive bundle creation guide
- [MODULES.md](https://github.com/microsoft/amplifier/blob/main/docs/MODULES.md) - Component catalog
- [MODULE_DEVELOPMENT.md](https://github.com/microsoft/amplifier/blob/main/docs/MODULE_DEVELOPMENT.md) - Development workflows
- [AGENT_AUTHORING.md](https://github.com/microsoft/amplifier-foundation/blob/main/docs/AGENT_AUTHORING.md) - Agent-specific guidance
- [PATTERNS.md](https://github.com/microsoft/amplifier-foundation/blob/main/docs/PATTERNS.md) - Common usage patterns
- [CONCEPTS.md](https://github.com/microsoft/amplifier-foundation/blob/main/docs/CONCEPTS.md) - Mental model and core concepts
- [URI_FORMATS.md](https://github.com/microsoft/amplifier-foundation/blob/main/docs/URI_FORMATS.md) - Source URI reference
- [POLICY_BEHAVIORS.md](https://github.com/microsoft/amplifier-foundation/blob/main/docs/POLICY_BEHAVIORS.md) - App-level policies

**Additional Foundation Docs:**
- API_REFERENCE.md - API index
- DOMAIN_VALIDATOR_GUIDE.md - Validation patterns

**Additional Amplifier Docs:**
- DEVELOPER.md - Getting started with development
- LOCAL_DEVELOPMENT.md - Local setup
- REPOSITORY_RULES.md - Repository standards
- TESTING_GUIDE.md - Testing strategies
- USER_GUIDE.md - User-facing documentation
- USER_ONBOARDING.md - Onboarding guide

---

**Research completed:** 2026-02-04  
**Total documentation size:** ~120KB across 8 primary documents  
**Confidence level:** High - All information sourced from official Microsoft Amplifier repositories
