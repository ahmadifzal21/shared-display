# Shared Display (LAN)

Shared Display is a **real-time screen mirroring system** that lets a Windows 11 PC act as a host/server and stream its screen to Android and iOS clients over the **same Wi-Fi** with **ultra-low latency (<50 ms)** and **1080p60 clarity**.  
Unlike existing tools that introduce lag, privacy risks, or subscription walls, this project is **LAN-only, secure, and open-source friendly**.

---

## 📖 Background

For problem framing, assumptions, and user personas, see the [Problem Framing Document](./docs/product/01-problem-framing.md).

---

## 🏗️ Architecture

The system is split into two logical planes for clarity and scalability:

- **Control Plane (Python):**  
  Handles authentication, pairing (QR + short token), session lifecycle, and device management. Exposed via REST/gRPC APIs.

- **Data Plane (Rust):**  
  Captures frames with Windows Desktop Duplication, encodes with GPU hardware (Intel QSV, NVENC, or AMF), and streams via WebRTC with DTLS-SRTP encryption. Designed for <50 ms LAN latency at 1080p60, with headroom for 1440p.

All `.proto` schemas and API definitions live in the `/proto` directory.  
Architecture decisions are logged in `/docs/design/decisions/`.

---

## 📚 Documentation

- `/docs/product` → product management docs (problem framing, outcomes, roadmap).  
- `/docs/design` → system architecture, ADRs, threat models.  
- `/docs/ops` → future runbooks, metrics, deployment notes.

---

## 🚀 Roadmap

- **Phase 0: Foundations**  
  Repo layout, coding standards, threat model outline, CI skeleton.  

- **Phase 1: Capture Core**  
  Windows Desktop Duplication prototype + latency instrumentation.  

- **Phase 2: Encode & Transport**  
  GPU encode path + WebRTC loopback prototype, end-to-end under 80 ms.  

- **Phase 3: Auth & Discovery**  
  Credential store, QR pairing, mDNS signaling, session logs.  

- **Phase 4: Client Builds**  
  Android app (Kotlin) first; iOS (Swift) later. Adaptive bitrate, telemetry overlay.  

- **Phase 5: Hardening**  
  Multi-client fan-out, wired link validation, threat review, packaging.

---

## 🛠️ Development Prerequisites

- **Rust (stable)** → media core (screen capture + encoding + WebRTC).  
- **Python 3.11+** → control plane (APIs, pairing, session management).  
- **Protobuf (`protoc`)** → for gRPC schema compilation.  
- **Android Studio** → build/test Android client.  
- **Xcode (optional)** → for iOS client (macOS required).  
- **FFmpeg (CLI)** → encoder testing & debugging.  

---

## 🤝 Contributing

Contributions are welcome! Please see `/docs/design/decisions/` for architecture choices before proposing changes, and open a discussion or issue for significant updates.
