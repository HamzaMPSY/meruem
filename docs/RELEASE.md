# Release Checklist

Use this before publishing a new Meruem version.

## Version

1. Update `meruem.manifest.json`.
2. Update `CHANGELOG.md`.
3. Confirm `README.md` install instructions still match `scripts/install.sh`.
4. Confirm `docs/SKILL_SOURCES.md` lists every bundled skill.

## Bundle Integrity

Run:

```sh
find skills -maxdepth 2 -name SKILL.md | sort
sh scripts/doctor.sh
CODEX_HOME=/tmp/meruem-release-test sh scripts/install.sh
CODEX_HOME=/tmp/meruem-release-test sh scripts/doctor.sh
```

Expected bundled skills:

- `aura`
- `meruem`
- `codebase-explainer`
- `deep-research`
- `design-taste-frontend`
- `emil-design-eng`
- `frontend-design`
- `graphify`
- `impeccable`
- `karpathy-guidelines`
- `prompt-preflight`

## Public Safety

- No private tokens.
- No machine-local absolute paths in public install docs.
- No copied private skill content unless it is intended to be published.
- `scripts/uninstall.sh` still requires explicit confirmation.
- License is present.

## Publish

1. Commit the release.
2. Tag it with the manifest version.
3. Push the tag.
4. Test installation from a fresh clone.
