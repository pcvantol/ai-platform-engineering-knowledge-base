# Principles

This area contains the principles that constrain knowledge engineering work in the Knowledge Base.

Principles define how knowledge is accepted, refined, generalized, certified, and published. They protect the repository from becoming a product documentation set, software repository, or blueprint collection.

All principles must support the canonical role of certified knowledge.

## Read-Only Knowledge Source Principle

Every registered Knowledge Source is read-only by default. The Knowledge Base consumes repository evidence; it does not write back to source repositories during knowledge operations.

```text
Knowledge Source Repository
->
Knowledge Base

Never implicitly:

Knowledge Base
->
Knowledge Source Repository
```

The principle applies to source files, documentation, branches, version numbers, commit history, commits, pushes, and pull requests. Repository modification is permitted only through a separately invoked engineering action requested by an engineer. The action must preserve traceability from Certified Knowledge through the engineering recommendation and repository change to the resulting commit.
