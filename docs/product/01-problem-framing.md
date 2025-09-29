# 📄 Problem Statement — Shared Display (LAN)

**Author:** You
**Date:** 2025-09-29
**Version:** 0.1

---

## Problem Statement

Software engineers and gamers want to mirror their Windows PC screen to an Android device over the same Wi-Fi with **ultra-low latency (<50 ms)** and **1080p60 clarity**. Existing tools introduce noticeable lag, require accounts/paywalls, or route video through the cloud — creating **privacy and performance concerns**. Our solution delivers **LAN-only, secure, high-fidelity mirroring** with simple QR pairing, optimized for fast-motion content like games and coding demos.

---

## Who (Target Users)

* **Primary:**

  * **Gamers** — need smooth, real-time mirroring with no stutter.
  * **Software engineers** — want a portable display for debugging, demos, and coding.
* **Secondary:**

  * Streamers, students, presenters who can benefit from a portable second screen.
* **Environment:** Windows 11 host + Android 12+ client, connected via 5 GHz Wi-Fi.

---

## Why Now

* Consumer CPUs/GPUs (Intel Core Ultra + Arc iGPU) provide **hardware encoding (QSV)** capable of real-time 1080p60 with low latency.
* Modern Android devices have **efficient H.264/H.265 decoders**.
* **WebRTC** enables secure, adaptive, encrypted transport over LAN without cloud dependence.
* Growing demand for **privacy-first, local-only tools** in dev/gaming communities.

---

## Jobs-To-Be-Done (JTBD)

* **JTBD-1:** *When I’m gaming,* I want my Android phone to mirror my PC **with <50 ms latency**, so the experience feels live.
* **JTBD-2:** *When I connect a new device,* I want to scan a **QR code** to pair instantly, instead of typing IPs or creating accounts.
* **JTBD-3:** *When Wi-Fi bandwidth fluctuates,* I want the stream to **adapt gracefully** (fps/bitrate), not freeze.
* **JTBD-4:** *When on LAN,* I want **local-only encrypted traffic**, so no data leaves my network.
* **JTBD-5 (stretch):** *When reading code or text,* I want **1440p headroom**, so fonts stay sharp.

---

## Assumptions (v1)

* **Scope:** LAN-only (no internet/TURN).
* **Platform:** Windows 11 host; Rust media core + Python control backend.
* **Clients:** Native **Android app** first; iOS/iPadOS later.
* **Quality:** 1080p60, latency goal **p50 ≤80 ms / p95 ≤100 ms**.
* **Hardware:** Intel Core Ultra 5 + Intel Arc (QSV encoder) + 16 GB RAM.
* **UX:** Username/password + **short-lived QR token** pairing.
* **Network:** 5 GHz Wi-Fi baseline.

---

## Non-Goals (v1)

* Internet/TURN remote access.
* True second-monitor virtualization or input capture (view-only).
* DRM integration.

---

## Risks & Unknowns

* Intel Arc QSV driver stability under sustained load.
* Mid-range Android phones may drop frames at 1080p60.
* Wi-Fi congestion may raise latency beyond 100 ms.

