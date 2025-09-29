# ADR-0001: Separate Control and Data Channels

- **Status:** Proposed
- **Date:** (YYYY-MM-DD)

## Context and Problem Statement

We need to decide on the communication architecture between the sharing client (server) and the viewing clients. Should control messages (e.g., start/stop, quality change) and the actual screen data (video stream) use the same communication channel or separate ones?

## Decision Drivers

- Performance and latency for the video stream.
- Reliability of control messages.
- Scalability of the architecture.

## Considered Options

1.  Single channel for both control and data.
2.  Separate channels for control (e.g., WebSockets) and data (e.g., WebRTC).

## Decision Outcome

Chosen option: [TBD], because [TBD].

## Consequences

- **Positive:** ...
- **Negative:** ...

