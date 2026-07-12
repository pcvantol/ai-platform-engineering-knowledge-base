# EO-DJCONNECT-008: Raspberry Pi and Windows clients recorded Profile Platform adoption with client-specific boundaries

## Metadata

| Field | Value |
| --- | --- |
| Identifier | `EO-DJCONNECT-008` |
| Lifecycle state | Repository Observation |
| Knowledge Source | `KS-DJCONNECT-001` |
| Source repositories | `pcvantol/djconnect-pi`, `pcvantol/djconnect-windows` |
| Repository locations | `https://github.com/pcvantol/djconnect-pi`, `https://github.com/pcvantol/djconnect-windows` |
| Engineering domain | Client Engineering, Embedded Systems |
| Observation type | Capability addition |
| Observation date | 2026-07-10 |
| Extraction date | 2026-07-12 |
| Confidence | High |
| Candidate status | Not created |

## Summary

The `pcvantol/djconnect-pi` and `pcvantol/djconnect-windows` repositories recorded Profile Platform adoption with different client-specific boundaries.

## Observed Evidence

The evidence file `PI_PROFILE_ADOPTION_REPORT.md` records Raspberry Pi Ambient Client profile adoption. It states that the Raspberry Pi default model is Room to Household to Shared DJ, that the Pi sends canonical Profile Platform request context, and that Home Assistant resolves the DJConnect Profile.

The same Pi evidence records that the Pi does not infer a person from touch usage, playback state, Home Assistant user hints or recent activity.

The evidence file `WINDOWS_PROFILE_ADOPTION_REPORT.md` records Windows Profile Platform adoption. It states that Windows sends request context and renders the response while Home Assistant remains the authority for Profile resolution, Music DNA, Ask DJ history, recommendations, privacy policy and backend routing.

The Windows evidence records parity with Apple for request context, Ask DJ, Music DNA, Discover, Track Insight, private session contract support and structured Profile Platform errors, while deferring Profile CRUD, household management, export/import and profile switching UI.

## Traceability References

- Knowledge Source: `KS-DJCONNECT-001`
- Repository: `pcvantol/djconnect-pi`
- Evidence file: `PI_PROFILE_ADOPTION_REPORT.md`
- Evidence commit: `35585114ef0f745044e17eea1fcce57ab45e60ff`
- Commit date: 2026-07-10
- Commit subject: `Review Pi foundation sync and ambient profile context (#32)`
- Engineering activity: Raspberry Pi Profile Platform adoption record

- Repository: `pcvantol/djconnect-windows`
- Evidence file: `WINDOWS_PROFILE_ADOPTION_REPORT.md`
- Evidence commit: `37710090d05fbebe5cfb37f6f275ef7af528f569`
- Commit date: 2026-07-10
- Commit subject: `Adopt Profile Platform contract on Windows (#7)`
- Engineering activity: Windows Profile Platform adoption record

## Related Repositories

- `pcvantol/djconnect`
- `pcvantol/djconnect-app`

## Observation Boundary

This observation records repository-specific client evidence only. It does not create a Knowledge Candidate or generalize cross-client Profile Platform adoption.
