# AI-development contract semantic-equivalence receipt

## Scope

- Repository: `pcvantol/ai-platform-engineering-knowledge-base`
- Projection source: `pcvantol/ai-development-contracts`
- Source commit: `ec070e399ff4dbd92e760370002995fe4f4d52d6`
- Profile: `ai-platform-engineering-knowledge-base`
- Extension identity: `AI_PLATFORM_ENGINEERING_KB_DEVELOPMENT_EXTENSION`
- Projection digest: `34d04daa1668d5ee1288a22d77aa143fecf4e167cb7fdc443d4082cb3ed45d77`

## Section-level classification

| Surface | Semantic role | Classification | Surviving authority |
| --- | --- | --- | --- |
| `BOOTSTRAP.md` | generic repository-development bootstrap and local navigation | `GENERIC_PROJECTED` | committed projection; local navigation retained |
| `HANDOFF.md` | generic handoff flow | `GENERIC_PROJECTED` | committed projection |
| `docs/ai-development/AI_PLATFORM_ENGINEERING_KB_DEVELOPMENT_EXTENSION.md` | source read-only rule, lifecycle, traceability, certification, publication, and AI proposal boundary | `KB_DEVELOPMENT_EXTENSION` | local extension |
| `sources/**`, `observations/**`, `ingestion/**`, `extraction/**` | Knowledge Source and evidence handling | `KB_PRODUCT_DOMAIN_AUTHORITY` | Knowledge Base domain documentation |
| `candidates/**`, `concepts/**`, `generalized/**`, `certified/**`, `certification/**`, `publications/**` | knowledge lifecycle and certification | `KB_PRODUCT_DOMAIN_AUTHORITY` | Knowledge Base domain documentation |
| `governance/**`, `principles/**`, `templates/**` | knowledge governance and publication policy | `KB_PRODUCT_DOMAIN_AUTHORITY` | Knowledge Base domain documentation |
| `baselines/**` | dated assessment evidence | `HISTORICAL` | immutable baseline evidence |

## Result

The projection supplies all generic AI-development semantics. Knowledge Source
read-only behavior, observations, ingestion/extraction, candidate-to-certified
lifecycle, certification, publication, knowledge governance, and AI proposal
boundaries remain solely in the Knowledge Base.

- Unresolved sections: **0**
- Independently maintained generic contracts retired: **0**
- Remaining independently maintained generic contracts: **0**
- Knowledge Base domain authority preserved: **YES**
- Hosted projection validation: **ENFORCED** by `knowledge-base-validation.yml`
