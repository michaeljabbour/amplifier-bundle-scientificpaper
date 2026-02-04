# Amplifier Bundle Development Documentation - Research Compilation

**Compiled from:**
- Microsoft Amplifier Foundation Repository
- Microsoft Amplifier Repository
- Date: February 4, 2026

---

## Table of Contents

1. [Core Concepts & Philosophy](#core-concepts--philosophy)
2. [Bundle Development](#bundle-development)
3. [Module Development](#module-development)
4. [Agent Authoring](#agent-authoring)
5. [Patterns & Best Practices](#patterns--best-practices)
6. [Testing & Quality](#testing--quality)
7. [Local Development Setup](#local-development-setup)
8. [Running & Using Amplifier](#running--using-amplifier)

---

## Core Concepts & Philosophy

### What is Amplifier?

Amplifier is an **AI-assisted development platform** built on a Linux kernel model philosophy:
- Ultra-thin core (amplifier-core) containing only mechanisms
- Modular ecosystem handling everything else
- Stable interfaces that modules implement
- Text-first design emphasizing markdown and YAML (no binary formats)

**Key Philosophy**: "Mechanism, not policy"—providing composition infrastructure without dictating bundle selection or configuration decisions.

### Design Approach

The platform embraces an **AI-assisted development model** where "you specify what you want, Amplifier generates the module code for you." This represents a shift from traditional manual coding to specification-driven module creation.

### Bundle Concept

A **bundle** is a composable configuration unit that produces a mount plan for AmplifierSession.

**Key Principle**: "Bundles are configuration, not Python packages. A bundle repo does not need a root pyproject.toml."

**Data Flow**: Bundle → to_mount_plan() → Mount Plan → AmplifierSession

### Mount Plans vs Bundles

Mount plans are the final configuration dictionary consumed by AmplifierSession, containing:
- session
- providers
- tools
- hooks
- agents sections

**Important**: Bundles are optional for creating mount plans—developers can build configurations directly without bundles. Bundles exist primarily for sharing and remixing purposes.

### @Mention Resolution

Instructions reference context files from composed bundles using **@namespace:path** syntax.

During composition, each bundle's base_path is tracked by namespace (from bundle.name), and PreparedBundle resolves these references against the original bundle's location.

---

## Bundle Development

### Bundle File Format

Bundles are markdown files with YAML frontmatter containing:

```yaml
---
bundle:
  name: bundle-name
  version: 1.0.0
session:
  orchestrator: loop-basic
  context_manager: in-memory
providers:
  - provider-anthropic
  - provider-openai
tools:
  - tool-bash
  - tool-filesystem
hooks:
  - hook-logger
agents:
  specialist-agent:
    model: claude-opus
context:
  - context/instructions.md
spawn:
  inherit_tools: false
---

# Bundle Name

[System instruction - markdown body]

---

@namespace:context/additional-context.md
```

### Bundle Composition and Merge Rules

Bundles compose through layering: **result = base.compose(overlay)** (Later overrides earlier)

Merging follows specific patterns:
- **session**: Deep merge of nested dictionaries
- **providers/tools/hooks**: Merge by module ID (same ID = update, new ID = add)
- **spawn**: Deep merge with later values winning
- **instruction**: Complete replacement

### Root vs Nested Bundles

**Root Bundles**:
- Located at `/bundle.md` or `/bundle.yaml`
- Establish namespace and root directory
- Their namespace derives from **bundle.name**, not repository URL

**Nested Bundles**:
- Loaded via subdirectory URIs or @namespace:path references
- Share the root's namespace but resolve paths relative to their location

### Structural vs Conventional Classification

Bundles have two independent classification systems:

**Structural** (enforced by code):
- Determines how bundles load and register namespaces
- Root bundles vs nested bundles

**Conventional** (pattern-based):
- Used for maximum utility and reusability
- Examples: "standalone bundle", "behavior bundle", "thin bundle"

These classifications are independent and non-contradictory. For example, `bundle.md` is structurally a root bundle while files in `bundles/` are nested, but conventionally they might be classified differently based on their purpose.

### Bundle Organization Patterns

#### Single-File Bundles

Work well for simple configurations combining:
- Bundle metadata
- Session settings
- Providers
- System prompt

All in one markdown file.

#### Multi-File Bundles

Organize related components into directories:
- **agents/** - Agent definitions
- **behaviors/** - Behavior modules
- **context/** - Shared instructions and knowledge
- **modules/** - Local tool implementations
- **bundles/** - Pre-composed standalone variants

Main bundle references these via `include` declarations.

#### Thin Bundle Pattern (Recommended)

The thin bundle approach minimizes duplication by:
- Inheriting from foundation
- Adding only unique capabilities
- Avoiding redeclaring tools, session config, and hooks already provided by foundation
- Avoiding version conflicts from overlapping declarations

**Benefits**:
- Eliminates maintenance burden of keeping multiple copies synchronized
- Keeps bundle.md minimal and focused

A thin bundle typically includes foundation, optionally includes its own behavior, and references consolidated context files.

### Directory Conventions

Standard layout includes:
```
bundle.md                  # Root entry point establishing namespace
behaviors/                 # Reusable capabilities for composition
  my-capability.md
agents/                    # Specialized agent definitions
  specialist-agent.md
context/                   # Shared instructions and knowledge
  instructions.md
  common-knowledge.md
modules/                   # Local tool implementations
bundles/                   # Pre-composed standalone variants
  with-provider-a.md
  with-provider-b.md
```

### Behavior Pattern

**Behaviors** are reusable capability add-ons containing:
- Agents
- Context
- Optional tools/hooks

They live in `behaviors/` and enable:
- **Reusability** across bundles
- **Modularity** through clean separation of concerns
- **Composition** by mixing multiple behaviors

Behavior files declare which agents and context files they provide. They can be:
- Included from the root bundle
- Composed onto other bundles externally

Root bundles typically include their own behavior (DRY pattern), while standalone bundles combine the root with provider choices for convenience.

### Agent Definition Patterns

#### Include Pattern (Recommended)

References a separate agent file (`agents/my-agent.md`):
- Supports the context sink pattern
- More portable across bundles

#### Inline Pattern

Defines the agent directly in bundle configuration with bundle-specific tools:
- Useful when an agent needs unique tool configurations
- Different from the parent bundle

Both patterns are intentionally supported for different use cases.

### Context De-duplication

Store instructions in consolidated context files (`context/instructions.md`) rather than inline in bundle.md.

**Benefits**:
- Eliminates duplication when referenced by behaviors and bundles
- Keeps bundle.md lean and maintainable
- Enables reuse across multiple configurations

### Key Anti-Patterns to Avoid

1. **Duplicating foundation declarations in thin bundles** - Use inheritance instead
2. **Inlining instructions directly in bundle.md** - Extract to consolidated context files
3. **Creating fat bundles when simple capabilities suffice** - Keep bundles focused
4. **Using repository names as namespaces** - Use bundle.name instead
5. **Declaring amplifier-core as a runtime dependency** - Not needed in bundle repos
6. **Including subdirectories in reference paths** - Use proper path structure

### Session Capabilities

**session.working_dir**: Registers the session's working directory as a capability, critical for server deployments where Path.cwd() returns the server's directory rather than the user's project path.

**bundle_package_paths**: Lists src/ directories from bundles requiring sys.path inclusion for module imports.

---

## Module Development

### Module Categories

The Amplifier ecosystem organizes modules into six primary functional types:

#### 1. Orchestrators

Control AI agent execution loops:
- **loop-basic** - Sequential request/response flows
- **loop-streaming** - Real-time responses
- **loop-events** - Event-driven orchestration

#### 2. Providers

Connect to AI model services:
- Anthropic Claude
- OpenAI GPT
- Azure OpenAI
- Google Gemini
- vLLM servers
- Ollama
- Mock providers for testing

#### 3. Tools

Extend agent capabilities:
- File operations
- Shell commands
- Web search
- Code searching
- Task delegation
- Todo management
- Skills loading
- Model Context Protocol integration

#### 4. Context Managers

Maintain conversation state and history:
- In-memory contexts with automatic compaction
- File-backed persistent storage across sessions

#### 5. Hooks

Extend lifecycle events and observability:
- Logging
- Redaction
- Approval gates
- Backup
- UI/notification capabilities

#### 6. Agents

Specialized sub-sessions for focused tasks.

### Module Architecture Principles

All modules follow a consistent pattern:
- Implement a `mount(coordinator, config)` entry point
- Register capabilities with the coordinator
- Handle errors gracefully without crashing the kernel
- Adhere to stable interfaces

### Module Development Workflows

Three primary scenarios for module work:

#### Quick Fixes

Developers can modify a single module using temporary environment variable overrides:
```bash
AMPLIFIER_MODULE_<MODULE_ID>=<path> amplifier run --bundle foundation "test"
```

This approach leaves no persistent changes to the filesystem.

#### Multi-Module Work

Teams managing interdependent modules can organize them within a unified directory structure:
```bash
mkdir -p .amplifier/modules
# Create symlinks to related codebases
ln -s /path/to/module-a .amplifier/modules/module-a
```

#### Full Workspace Setup

Large-scale development benefits from the workspace convention, supporting simultaneous work across core systems, CLI tools, and numerous modules through auto-discovery mechanisms.

### Essential Development Commands

The CLI provides a dedicated `amplifier module dev` namespace:

```bash
amplifier module dev init              # Establishes workspace structure
amplifier module dev link              # Connects individual modules
amplifier module dev status            # Reports current activation
amplifier module dev test              # Executes module's test suite
```

### Best Practices for Modules

#### Keep Modules Focused

**Single Responsibility**: Each module should handle one concern rather than bundling multiple capabilities.

#### Protocol Adherence

Implementations must follow established protocol contracts without adding unnecessary extensions or internal complexity.

#### Testing Strategy

Test observable behavior through public interfaces rather than internal implementation details.

#### Documentation

Clear docstrings and usage examples in public APIs enable better adoption and reduce integration friction.

### Module Setup Prerequisites

Developers need:
- Python 3.11+
- UV package manager
- Git

#### Installation

```bash
cd <your-workspace>
scripts/install-dev.sh
```

This script handles initial package installation from GitHub repositories, then automatically reinstalls libraries as editable for local development work.

### Module Resolution Priority

The system checks module locations in this order:

1. Environment variables (`AMPLIFIER_MODULE_<MODULE_ID>=<path>`)
2. Workspace convention (`.amplifier/modules/<module-id>/`)
3. Project configuration (`.amplifier/settings.yaml`)
4. User configuration (`~/.amplifier/settings.yaml`)
5. Bundle source definitions
6. Installed Python packages

### Module Usage Methods

Modules are typically loaded through bundle configurations rather than directly. Users can also manage modules via command line:

```bash
amplifier module add <module-id>
amplifier module list
amplifier module show <module-id>
```

### AI-Assisted Module Creation

The recommended four-phase approach:

#### Design Phase

Use zen-architect to specify module requirements and architecture.

#### Implementation Phase

Use modular-builder to generate complete code with proper structure:
```bash
amplifier run "Create a module for X functionality"
```

#### Testing & Refinement

Create comprehensive tests and identify edge cases.

#### Documentation & Publishing

Generate README, pyproject.toml, and publish to GitHub.

---

## Agent Authoring

### What are Agents?

Agents are **specialized AI configurations that run as sub-sessions** for focused tasks.

**Critical Concept**: Agents ARE bundles—they use identical file formats and load via `load_bundle()`, differing only in the frontmatter key:
- Bundles use: `bundle:` with name and version
- Agents use: `meta:` with name and description

### Agent File Format

```yaml
---
meta:
  name: agent-name
  description: |
    [Detailed discovery-focused description]
---

# Agent Name

[System prompt and instructions]

---

@foundation:context/shared/common-agent-base.md
```

### Critical Description Requirements

Every agent description must include four essential elements:

#### 1. WHY: The Problem Solved

Describe the value provided and problems solved.

#### 2. WHEN: Explicit Activation Triggers

Use keywords like:
- "PROACTIVELY"
- "MUST"
- "Use when..."
- Specific trigger conditions

#### 3. WHAT: Domain/Taxonomy Terms

Prefix with "Authoritative on:" to identify subject matter expertise.

#### 4. HOW: Concrete Usage Examples

Include at least one example block with commentary explaining delegation rationale.

**Critical Rule**: "One-liner descriptions are unacceptable" for discoverability. Descriptions should exceed 100 words and include at least one example block.

### Agent Design Patterns

#### Context Sinks Pattern (Recommended)

Expert agents serve as **context sinks**—carrying heavy documentation loaded only when spawned, not in every session.

**Structure**: Pair a thin behavior file (30 lines of awareness pointers) with a heavy agent file containing all `@mention` references to documentation.

**Benefits**:
- Maintains token efficiency for parent sessions
- Loads documentation only when needed
- Enables sophisticated agent specialization

**Anti-pattern**: Loading substantial documentation in behavior context includes, which bloats all sessions using that behavior.

#### Instruction Structure

Recommended organization:
1. One-line role description
2. Execution model clarification
3. Operating principles
4. Workflow steps
5. Output contract (required response elements)
6. Shared base @mention at conclusion

### Common Agent Authoring Mistakes

1. **Vague descriptions without trigger conditions** - Must include WHEN they activate
2. **Missing @foundation:context/shared/common-agent-base.md reference** - Include shared base
3. **Undefined output contracts** - Specify expected response format
4. **Heavy documentation in always-loaded behavior context** - Use context sink pattern
5. **Treating agents differently from bundles** - Remember agents are bundles

### Agent Spawning Patterns

Agents are spawned as child sessions using the `spawn()` method:

```python
child_agent = parent_bundle.spawn(
    child_bundle,
    compose_parent=True,  # Inherit parent capabilities
    providers=[...],       # Optional provider preferences
)
```

#### Provider Preferences

Specify ordered provider chains for routing agent requests:
- Use glob patterns for model version matching
- Fallback chains for resilience
- Priority ordering for preferred models

#### Tool Inheritance Control

Restrict tool access by configuring:
- `exclude_tools` - Blacklist specific tools
- `inherit_tools` - Whitelist permitted tools

Prevents delegation chains when agents should perform work directly.

### Specialized Agents in Amplifier

The dev bundle includes focused agents:

- **zen-architect** - Architecture and design analysis
- **bug-hunter** - Systematic hypothesis-driven debugging
- **researcher** - Content synthesis and documentation analysis
- **modular-builder** - Code implementation from specifications

---

## Patterns & Best Practices

### Bundle Composition Patterns

#### Base + Environment Layering

Create a foundational bundle, then overlay environment-specific configurations (dev, prod) using composition methods.

**Benefit**: Prevents duplicating core settings across environments.

#### Includes Chain

Use declarative `includes:` directives in bundle YAML to layer configurations rather than programmatic composition.

**Benefit**: Improves readability and maintainability.

#### Feature Bundles

Compose functionality additively by creating partial bundles for discrete features:
- Filesystem tools bundle
- Web capabilities bundle
- Search and analysis bundle

Then combine only needed components.

### Provider Configuration

**Support multiple providers** with priority ordering for resilience. Configure fallback chains so systems gracefully degrade when primary providers become unavailable.

**Mock providers** simplify testing by returning predetermined responses without requiring external API access.

### Session Management Patterns

#### Basic Flow

1. Load bundle
2. Prepare bundle
3. Create session
4. Execute commands
5. Handle responses

#### Multi-Turn Conversations

Sessions automatically maintain context across sequential executions, eliminating manual state management.

#### Session Resumption

Store session IDs to reconnect to existing conversations, enabling long-running interactions across application restarts.

```bash
amplifier session list                    # Show project sessions
amplifier continue                        # Resume most recent
amplifier session resume <id>             # Resume specific session
```

### Validation Strategies

Validate bundles before use to catch configuration issues early.

Implement custom validators extending base validators for application-specific requirements:
- Mandatory tool requirements
- Configuration constraints
- Security policies

### Registry & Discovery

Register named bundles for consistent reference across your system. Implement resolution functions mapping agent names to bundle definitions for dynamic agent selection.

### Performance Optimization

**Key Pattern**: Prepare bundles once, then create multiple sessions against the prepared bundle to avoid repeated initialization overhead.

Cache resolved bundles when resolution involves filesystem or network operations.

---

## Testing & Quality

### Core Testing Philosophy

**Pragmatic Testing**: "Tests should catch real bugs, not duplicate code inspection."

Focus on:
- Runtime invariants
- Edge cases
- Integration behavior
- Convention enforcement

Avoid:
- Obvious implementation details
- Code duplication

### Test Pyramid Structure

- **60%** unit tests (isolated functions/classes)
- **30%** integration tests (module + amplifier-core interaction)
- **10%** end-to-end tests (complete workflows)

### Test Organization

Directory structure places tests in a `tests/` folder with subdirectories for fixtures and organized by test type:

```
tests/
  fixtures/
    sample_data.py
  unit/
    test_parser.py
  integration/
    test_module_mounting.py
  e2e/
    test_full_workflow.py
```

### Test Framework

The project uses **pytest**:

```bash
uv run pytest                    # Run all tests
pytest -v                        # Verbose output
pytest --cov                     # Coverage reports
pytest -m "not slow"             # Skip integration tests
```

### Writing Tests

#### Test Structure Pattern: Arrange-Act-Assert

1. **Arrange** - Setup data and preconditions
2. **Act** - Execute operations being tested
3. **Assert** - Verify results

#### Best Practices

1. **Descriptive Naming**: Use action-oriented names
   ```python
   test_read_file_returns_content_when_file_exists()
   test_bash_tool_handles_permission_denied_error()
   ```

2. **One Assertion Focus**: Separate tests for distinct behaviors

3. **Edge Cases**: Test:
   - Path traversal
   - Missing files
   - Permission errors
   - Empty inputs
   - Boundary conditions

4. **Parametrization**: Use `@pytest.mark.parametrize` for multiple input scenarios
   ```python
   @pytest.mark.parametrize("input,expected", [
       ("test1", "result1"),
       ("test2", "result2"),
   ])
   def test_function(input, expected):
       assert process(input) == expected
   ```

5. **Markers**: Tag tests for organization
   ```python
   @pytest.mark.integration
   @pytest.mark.asyncio
   def test_async_operation():
       pass
   ```

### Module-Specific Testing

#### Tool Modules

Test:
- Execution success and error cases
- Permissions handling
- Resource cleanup
- Event emission

#### Provider Modules

Test:
- Completions generation
- Error handling (rate limits, timeouts)
- Token counting accuracy
- Streaming functionality

#### Orchestrator Modules

Test:
- Turn execution flow
- Tool call handling
- Context management
- Multi-turn conversations

#### Hook Modules

Test:
- Event handling
- Error isolation
- Data transformation
- No interference with core logic

### Mocking Strategies

Use `unittest.mock` for external APIs:
```python
from unittest.mock import Mock, patch

@patch('module.external_service')
def test_with_mock(mock_service):
    mock_service.return_value = expected_result
    assert function_under_test() == expected
```

Use `amplifier_module_provider_mock.MockProvider` for deterministic provider testing:
```python
from amplifier_module_provider_mock import MockProvider

def test_with_mock_provider():
    provider = MockProvider(responses=[...])
    # Test against mock provider
```

Mock fixtures enable isolated, repeatable tests without external dependencies.

### Coverage Goals

The framework emphasizes testing behaviors difficult to verify through code inspection alone, avoiding redundant test maintenance.

---

## Local Development Setup

### Quick Start Installation

Begin with a development environment installation:

```bash
cd <your-workspace>
scripts/install-dev.sh
```

This script:
- Handles initial package installation from GitHub repositories
- Automatically reinstalls libraries as editable for local development

### Configuration for Module Development

Copy the configuration template:

```bash
cp .amplifier/settings.yaml.template .amplifier/settings.yaml
vim .amplifier/settings.yaml
```

Specify which modules to develop locally using file paths:

```yaml
sources:
  loop-basic: file://./amplifier-module-loop-basic
  provider-anthropic: file://./amplifier-module-provider-anthropic
  tool-bash: file://./amplifier-module-tool-bash
```

### Development Workflow

#### Testing Modules Locally

```bash
cd amplifier-module-tool-bash
uv run pytest
```

#### Running Amplifier with Local Overrides

```bash
amplifier run --bundle foundation "test message"
```

The loader prioritizes local paths in your settings file over remote repositories.

### Module Resolution Priority

The system checks module locations in this order:

1. Environment variables (`AMPLIFIER_MODULE_<MODULE_ID>=<path>`)
   ```bash
   AMPLIFIER_MODULE_provider_anthropic=/path/to/module amplifier run "prompt"
   ```

2. Workspace convention (`.amplifier/modules/<module-id>/`)
   ```
   .amplifier/modules/
     provider-anthropic/
     tool-bash/
   ```

3. Project configuration (`.amplifier/settings.yaml`)

4. User configuration (`~/.amplifier/settings.yaml`)

5. Bundle source definitions

6. Installed Python packages

### Cache Management

When switching between branches, clear cached modules safely:

```bash
amplifier reset --remove cache -y
```

**Important Warning**: Never manually delete `~/.amplifier/cache/`—use the CLI's reset command instead, which handles editable install dependencies properly.

---

## Running & Using Amplifier

### Core Commands

#### Installation

```bash
uv tool install git+https://github.com/microsoft/amplifier
```

#### Initialization

```bash
amplifier init
```

### Execution Modes

#### Single Command Mode

Execute one task and exit:

```bash
amplifier run "Create a Python function to parse CSV files"
```

#### Interactive Chat Mode

Persistent multi-turn conversations:

```bash
amplifier
```

### Available Bundles

| Bundle | Purpose | Tools | Agents |
|--------|---------|-------|--------|
| `foundation` | Minimal setup | filesystem, bash | None |
| `dev` | Full development | base + web, search, task | Multiple specialized agents |
| `recipes` | Multi-step workflows | base + task | Recipe execution agents |
| `full` | Complete capabilities | All tools | All agents |

### Core Configuration Dimensions

Amplifier provides four configurable layers:

- **Provider**: Which AI service (Anthropic/OpenAI/Azure OpenAI/Ollama)
- **Bundle**: Capability sets (foundation/dev/recipes/full)
- **Module**: Specific tools, hooks, and agents
- **Source**: Where modules originate (git/local/package)

### Running with Specific Bundles

```bash
amplifier run --bundle dev "Analyze this code"
amplifier run --bundle foundation "List files"
```

### Session Management

Sessions auto-save per project at `~/.amplifier/projects/<project-slug>/sessions/`

Commands:
```bash
amplifier session list                 # Show project sessions
amplifier continue                     # Resume most recent session
amplifier session resume <id>          # Resume specific session
```

### Chat Commands (Interactive Mode)

Within interactive mode:

```
/help                    # Command reference
/agents                  # List available agents
/think                   # Enable planning mode
/do                      # Enable modification mode
/clear                   # Clear context
```

### Specialized Agents

The dev bundle includes focused agents for different tasks:

- **zen-architect** - For architecture and design decisions
- **bug-hunter** - For systematic hypothesis-driven debugging
- **researcher** - For content synthesis and documentation
- **modular-builder** - For code implementation from specifications

**Usage**:
```
@zen-architect Design a module for real-time notifications
@bug-hunter Why is my API returning 500 errors?
@researcher Summarize this documentation
@modular-builder Create a tool that calls REST APIs
```

---

## Additional Resources

### Key Documentation Files Available

**amplifier-foundation repository:**
- AGENT_AUTHORING.md - Agent creation guidelines
- API_REFERENCE.md - API documentation
- BUNDLE_GUIDE.md - Bundle development
- CONCEPTS.md - Core concepts
- DOMAIN_VALIDATOR_GUIDE.md - Domain validation
- PATTERNS.md - Design patterns
- POLICY_BEHAVIORS.md - Policy specifications
- URI_FORMATS.md - URI standards

**amplifier repository:**
- DEVELOPER.md - Developer guidance
- LOCAL_DEVELOPMENT.md - Environment setup
- MODULES.md - Module overview
- MODULE_DEVELOPMENT.md - Module creation
- README.md - Main entry point
- REPOSITORY_RULES.md - Contribution standards
- TESTING_GUIDE.md - Testing procedures
- USER_GUIDE.md - User reference
- USER_ONBOARDING.md - Getting started

### Repository Structures

**amplifier-foundation:**
- agents/ - Agent configurations
- behaviors/ - Behavioral patterns
- bundles/ - Bundle variants
- context/ - Contextual documentation
- docs/ - Primary documentation
- examples/ - Usage examples
- providers/ - Provider implementations
- tests/ - Test suites

**amplifier:**
- Similar structure with additional focus on CLI tools and development support

---

## Summary: Key Takeaways

### For Bundle Development

1. **Use the thin bundle pattern** - Inherit from foundation, add only unique capabilities
2. **Organize with directories** - agents/, behaviors/, context/, modules/
3. **De-duplicate context** - Use consolidated context files with @mention references
4. **Support multiple providers** - Include fallback chains for resilience
5. **Validate early** - Check bundle configuration before creating sessions

### For Module Development

1. **Keep modules focused** - Single responsibility principle
2. **Follow the mount pattern** - Implement mount(coordinator, config) entry point
3. **Use AI assistance** - Use zen-architect and modular-builder for design and implementation
4. **Test observable behavior** - Focus on public interfaces, not internal details
5. **Document clearly** - Provide usage examples and clear docstrings

### For Agent Authoring

1. **Write detailed descriptions** - Include WHEN, WHAT, WHY, HOW (100+ words)
2. **Use context sink pattern** - Load heavy documentation only when spawned
3. **Include common agent base** - Reference @foundation:context/shared/common-agent-base.md
4. **Define output contracts** - Specify expected response format
5. **Avoid heavy behavior contexts** - Keep always-loaded content minimal

### For Development Workflow

1. **Use local overrides** - Configure .amplifier/settings.yaml for local module development
2. **Test with mock providers** - Use MockProvider for deterministic testing
3. **Follow module resolution order** - Environment variables → workspace → config → user → bundle → packages
4. **Clear cache properly** - Use `amplifier reset` instead of manual deletion
5. **Prepare bundles once** - Create multiple sessions from prepared bundles for performance

### Platform Philosophy

- **Text-first** - Markdown and YAML, no binary formats
- **Mechanism over policy** - Infrastructure without dictation
- **AI-assisted creation** - Specify requirements, let Amplifier generate code
- **Composable units** - Mix and match behaviors and bundles
- **Stable interfaces** - Protocol contracts that don't break

---

**Document compiled from Microsoft Amplifier Foundation and Microsoft Amplifier GitHub repositories**
