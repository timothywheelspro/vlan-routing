# THE TRIANGLE TEST
## AI Decision Sovereignty Protocol — 1-Page Executive Summary

**Version:** 1.0 | **Date:** January 2026 | **Author:** Timothy I. Wheels, Contruil LLC

---

## THE PROBLEM

**As AI moves from "creative assistant" to "autonomous agent," the risk shifts from hallucinated text to unauthorized action.**

Today's solutions (fine-tuning, safety filters, log audits) don't create **architectural sovereignty** over AI decisions.

**The Question:** How do we prove an AI system is acting within its boundaries?

---

## THE SOLUTION: THE TRIANGLE TEST

A deterministic validation protocol that enforces **AI decision sovereignty** at the architectural level.

### Three Immutable Vertices

```
┌─────────────────────────────────────────┐
│                                         │
│         [AI Decision Request]          │
│                                         │
│              ╱│╲                        │
│             ╱ │ ╲                       │
│            ╱  │  ╲                      │
│           ╱  │  ╲                      │
│    ZONE 1╱   │   ╲ZONE 2              │
│   INTENT ╱   │   ╲CONSTRAINT          │
│         ╱    │    ╲                    │
│        ╱     │     ╲                   │
│       ╱      │      ╲                  │
│      ╱       │       ╲                 │
│     ╱        │        ╲                │
│    ╱         │         ╲              │
│   ╱          │          ╲              │
│  ╱           │           ╲             │
│ ╱            │            ╲            │
│╱             │             ╲           │
│──────────────┼───────────────         │
│              │                          │
│         ZONE 3: COHERENCE              │
│                                         │
└─────────────────────────────────────────┘
```

**1. INTENT** → Is the request safe and aligned with goals?  
**2. CONSTRAINT** → Is the action authorized by policy?  
**3. COHERENCE** → Is the output grounded in verified truth?

**If any vertex fails → Decision is BLOCKED, ROUTED, or FLAGGED**

---

## THE 4-GATE GUARDIAN ARCHITECTURE

```
User Request
    ↓
[Gate 1: Input Sovereignty] → BLOCK unsafe inputs
    ↓
[Gate 2: Context Alignment] → REDIRECT misrouted requests
    ↓
[Gate 3: Resource & Fact Verification] → HOLD low-confidence outputs
    ↓
[Gate 4: Output Safety & Audit] → LOG everything to immutable ledger
    ↓
Trusted Action / Response
```

**Non-Negotiable:** Gates 1 & 4 can never be overridden by the model.

---

## OPERATIONAL POSTURE

| 🟢 **GREEN** | 🟡 **AMBER** | 🔴 **RED** |
|-------------|-------------|------------|
| Standard Operations | Elevated Caution | Crisis / Lockdown |
| High automation | Human-in-the-Loop | Zero-Trust |
| Auto-approve ≥ 0.85 | Tighter thresholds | All actions require approval |
| Periodic audits | Expanded logging | Biometric verification |

---

## USE CASES & RESULTS

### Financial Services
- **Challenge:** Unauthorized investment strategies or transfers
- **Solution:** Zone 2 blocks unauthorized actions; Zone 3 verifies against SEC/MiFID compliance
- **Result:** 40–50% reduction in high-risk incidents; 60%+ faster audit cycles

### Healthcare
- **Challenge:** Hallucinated diagnoses or blurred information/prescription lines
- **Solution:** Zone 1 detects critical symptoms; Gate 4 enforces mandatory disclosures
- **Result:** Clearer guidance vs. diagnosis separation; reduced liability exposure

### Enterprise Operations
- **Challenge:** AI agents modifying safety-critical SOPs
- **Solution:** Zone 3 rejects protocol revisions below 0.95 Safety Score
- **Result:** Strong separation between "suggestion" and "authorization"

---

## THE GLASS BOX EVIDENCE CHAIN

Every interaction generates a **cryptographic hash chain**:

- **Input Hash:** What was asked
- **Decision Hash:** Why it was approved/blocked/escalated
- **Output Hash:** What the system returned/executed

**Result:** Tamper-evident chain of custody for regulators, auditors, and litigation readiness.

---

## IMPLEMENTATION: 6–8 WEEKS

```
Weeks 1–2: Foundation
├─ Landscape assessment
├─ Configuration draft
└─ Governance alignment

Weeks 3–4: Integration
├─ Guardian middleware integration
├─ Ground truth curation
└─ Pilot testing

Weeks 5–6: Scaling
├─ Gradual rollout
├─ Monitoring & dashboards
└─ Team training

Weeks 7–8: Optimization
├─ Fine-tune thresholds
├─ Compliance mapping
└─ Expansion to new domains
```

---

## KEY DIFFERENTIATORS

✅ **Platform-Agnostic** → Wraps around existing LLM stack (OpenAI, Anthropic, Gemini, Llama)  
✅ **Deterministic** → Not "we trust the model" but "we verify the system"  
✅ **Adaptive** → GREEN/AMBER/RED postures respond to threat environment  
✅ **Auditable** → Immutable cryptographic evidence chain for every decision  
✅ **Sovereignty-Preserving** → Human operator retains ultimate control

---

## CALL TO ACTION

**Don't Just Deploy AI. Command It.**

Request your **Triangle Test Enterprise Assessment:**

1. Architecture Review
2. Trust Gap Analysis
3. Deployment Blueprint
4. ROI & Risk Reduction Projection

**Contact:** [documentation@cyw-os.com](mailto:documentation@cyw-os.com)  
**Reference:** "Triangle Test Protocol – Public White Paper v1.0"

---

**Triangle Test Protocol** • Public White Paper v1.0  
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)  
**Author:** Timothy I. Wheels, Contruil LLC – Control Your World (CYW) OS

