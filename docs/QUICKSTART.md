# Quickstart

This is the shortest useful path from clone to first task.

## 1. Install

```sh
sh scripts/install.sh
```

## 2. Verify

```sh
sh scripts/doctor.sh
```

## 3. Start With A Scoped Request

```text
$meruem inspect this repository and create the first decision brief for making it production-ready
```

## Strong Request Patterns

Feature:

```text
$meruem add <feature>. Create a ticket first. Keep scope to <boundary>. Use local docs only.
```

Bug:

```text
$meruem fix <bug>. Read the failing path first, patch the smallest cause, and run the lightest verification.
```

UI:

```text
$meruem improve <screen>. Use the coordinated design skills, cover empty/loading/error states, and avoid generic mockup styling.
```

Architecture:

```text
$meruem evaluate <decision>. Compare 2-3 options, use local council if warranted, and create a decision brief before any implementation.
```

Knowledge graph:

```text
$meruem model <domain concept>. Query Graphify first and reuse existing graph structures.
```

## Good Defaults

- Ask for a decision brief when the work is broad.
- Ask for a ticket when implementation starts.
- Say whether external research is allowed.
- Name non-goals explicitly.
- Keep verification proportional to risk.
