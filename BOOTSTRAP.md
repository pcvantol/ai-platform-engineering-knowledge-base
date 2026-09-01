# Knowledge Base development bootstrap

Start with the committed generic projection in `docs/ai-development/`, then
read `AI_PLATFORM_ENGINEERING_KB_DEVELOPMENT_EXTENSION.md`, this repository's
`README.md`, `docs/README.md`, and the applicable lifecycle/governance source.
The local repository is sufficient; registered Knowledge Sources are read-only
and are not required as live checkouts. Validate the projection with:

```sh
python3 docs/ai-development/validate_projection.py \
  --profile ai-platform-engineering-knowledge-base \
  --source-commit ec070e399ff4dbd92e760370002995fe4f4d52d6 \
  --extension-identity AI_PLATFORM_ENGINEERING_KB_DEVELOPMENT_EXTENSION
```
