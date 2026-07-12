# Governance

This area contains governance for the Knowledge Base.

Governance defines how knowledge is stewarded, reviewed, certified, maintained, deprecated, continuously evolved, quality-reviewed, operated, qualified, synthesized, automated, source-onboarded, integrated across projects, capability-extended, goal-orchestrated, mission-orchestrated, agent-orchestrated, and published. It also protects the repository from project-specific drift.

Lifecycle governance is defined in [../lifecycle/README.md](../lifecycle/README.md). Review and promotion governance is defined in [../review-promotion/README.md](../review-promotion/README.md). Certification governance is defined in [../certification/README.md](../certification/README.md). Continuous evolution governance is defined in [../continuous-evolution/README.md](../continuous-evolution/README.md). Quality and repository health governance is defined in [../quality-health/README.md](../quality-health/README.md). Operating model governance is defined in [../operating-model/README.md](../operating-model/README.md). Engineering Operating System qualification governance is defined in [../qualification/README.md](../qualification/README.md). Synthesis governance is defined in [../synthesis/README.md](../synthesis/README.md). Automation governance is defined in [../automation/README.md](../automation/README.md). Source onboarding governance is defined in [../source-onboarding/README.md](../source-onboarding/README.md). Multi-project integration governance is defined in [../multi-project-integration/README.md](../multi-project-integration/README.md). Multi-agent runtime governance is defined in [../multi-agent-runtime/README.md](../multi-agent-runtime/README.md). Capability extension governance is defined in [../capabilities/README.md](../capabilities/README.md). Goal-driven orchestration governance is defined in [../goal-orchestration/README.md](../goal-orchestration/README.md). Autonomous Engineering Mission Runtime governance is defined in [../mission-runtime/README.md](../mission-runtime/README.md). Generation 2 corpus baseline governance is recorded in [../baselines/generation-2/README.md](../baselines/generation-2/README.md). Detailed governance rules may evolve later, but certification state, lifecycle movement, continuous evolution, quality review, operating model decisions, qualification decisions, synthesis, automation, source onboarding, multi-project integration, capability activation, goal planning, mission planning, mission checkpoints, agent orchestration, baseline closure, and publication derivation must always be governed deliberately.

## Read-Only Knowledge Source Governance

Knowledge extraction, lifecycle movement, knowledge evolution, certification, validation, retrieval, improvement, and source status reporting are independent of repository modification. They may create governed records in this Knowledge Base, but they must never modify a registered Knowledge Source.

Repository modification requires an explicit engineering workflow initiated by an engineer. Before a repository change can be accepted as engineering evidence, its traceability must preserve the following lineage:

```text
Certified Knowledge
->
Engineering Recommendation
->
Explicit Engineering Action
->
Repository Change
->
Commit
->
Knowledge Source
```

No knowledge operation may create a commit, push, pull request, branch change, version change, or source-file change on behalf of an engineer.
