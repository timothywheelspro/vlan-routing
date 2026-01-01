# THE TRIANGLE TEST
## Slide Deck Outline — AI Decision Sovereignty Protocol

**Version:** 1.0 | **Date:** January 2026 | **Author:** Timothy I. Wheels, Contruil LLC

---

## SLIDE 1: TITLE SLIDE

**Title:** THE TRIANGLE TEST  
**Subtitle:** A Protocol for AI Decision Sovereignty & Algorithmic Integrity

**Version:** 1.0 (Public Release)  
**Date:** January 2026  
**Author:** Timothy I. Wheels, Contruil LLC  
**Framework:** Control Your World (CYW) OS

**[CYW OS Logo]**

---

## SLIDE 2: THE TRUST GAP

**Headline:** As AI moves from "creative assistant" to "autonomous agent," the primary risk shifts from hallucinated text to **unauthorized action**.

**The Question:**
> **How do we prove an AI system is acting within its boundaries?**

**Current Answers (Insufficient):**
- ❌ Model fine-tuning and prompt engineering
- ❌ Generic "safety" filters
- ❌ After-the-fact audits of logs

**The Gap:** None of these create **architectural sovereignty** over AI decisions.

---

## SLIDE 3: FROM BLACK BOX TO GLASS BOX

**Headline:** The Triangle Test: Deterministic Validation at the Architectural Level

**Key Concept:**
Instead of asking the model to judge itself, the Triangle Test wraps every interaction in an external **Guardian layer**.

**The Shift:**
- **From:** "We trust the model"
- **To:** "We verify the system"

**The Result:**
The Black Box becomes a **Glass Box**—observable, explainable, and auditable.

---

## SLIDE 4: THE TRIANGLE — THREE VERTICES

**Visual:** Triangle diagram with three zones

**Zone 1: INTENT**
- **Question:** Is the request safe, non-adversarial, and aligned with declared goals?
- **Mechanism:** Static patterns + dynamic analysis
- **Failure State:** **BLOCK**

**Zone 2: CONSTRAINT**
- **Question:** Does the agent have the authority and permissions to act?
- **Mechanism:** ACLs, RBAC, context-aware routing
- **Failure State:** **REDIRECT**

**Zone 3: COHERENCE**
- **Question:** Is the output grounded in verified reality and prior commitments?
- **Mechanism:** Grounding checks + consistency evaluation
- **Failure State:** **FLAG**

**If any vertex fails → System automatically intervenes**

---

## SLIDE 5: THE 4-GATE GUARDIAN ARCHITECTURE

**Visual:** Flowchart showing Guardian middleware

**Architecture:**
```
User / Upstream System
    ↓
Guardian Layer (4 Gates)
    ↓
Trusted Action / Response
```

**Gate 1: Input Sovereignty**
- **Check:** Is the input adversarial or hijacking?
- **Policy:** Zero Tolerance
- **Outcome:** Reject unsafe inputs

**Gate 2: Context Alignment**
- **Check:** Does this belong in this domain?
- **Policy:** Strict Routing
- **Outcome:** Redirect misrouted requests

**Gate 3: Resource & Fact Verification**
- **Check:** Does the answer match authoritative sources?
- **Policy:** Trust but Verify
- **Outcome:** Hold below-threshold answers

**Gate 4: Output Safety & Audit**
- **Check:** Safety, compliance, and disclosure requirements
- **Policy:** Mandatory Logging
- **Outcome:** Immutable audit trail

**Non-Negotiable:** Gates 1 & 4 can never be overridden.

---

## SLIDE 6: OPERATIONAL POSTURE — GREEN / AMBER / RED

**Visual:** Three-column comparison table

| 🟢 GREEN | 🟡 AMBER | 🔴 RED |
|---------|----------|--------|
| **Standard Operations** | **Elevated Caution** | **Crisis / Lockdown** |
| Focus: Efficiency & speed | Focus: Risk mitigation | Focus: System integrity |
| High automation | Human-in-the-Loop | Zero-Trust |
| Auto-approve ≥ 0.85 | Tighter thresholds | All actions require approval |
| Periodic audits | Expanded logging | Biometric verification |

**Adaptive Response:** The Guardian behaves differently in peace vs. crisis.

---

## SLIDE 7: USE CASE 1 — FINANCIAL SERVICES

**Challenge:** Conversational advisor suggests unlicensed investment strategies or unauthorized transfers.

**Triangle Test Application:**
- **Zone 2 (Constraint):** Blocks all "execute trade / move funds" for general users
- **Zone 3 (Coherence):** Verifies against SEC, MiFID II, and firm-specific compliance rules

**Results:**
- ✅ 40–50% reduction in high-risk recommendation incidents
- ✅ 60%+ faster audit and compliance review cycles

---

## SLIDE 8: USE CASE 2 — HEALTHCARE

**Challenge:** LLM-powered triage tools hallucinate diagnoses or blur information vs. prescription.

**Triangle Test Application:**
- **Zone 1 (Intent):** Detects critical-symptom language and routes to emergency/clinician paths
- **Gate 4 (Safety):** Enforces mandatory disclosures and logs high-risk interactions

**Outcomes:**
- ✅ Increased clarity between guidance vs. diagnosis
- ✅ Reduced liability exposure and improved trust

---

## SLIDE 9: USE CASE 3 — ENTERPRISE OPERATIONS

**Challenge:** AI agents attempt to modify safety-critical SOPs (warehouse protocols, factory settings).

**Triangle Test Application:**
- **Zone 3 (Coherence):** Rejects protocol revisions with Safety Score < 0.95
- **Gate 2 (Context Alignment):** Ensures only certified roles can request changes

**Outcomes:**
- ✅ Strong separation between "suggestion" and "authorization"
- ✅ Clear attribution of manager approvals

---

## SLIDE 10: TECHNICAL IMPLEMENTATION — HIGH-LEVEL VIEW

**Platform-Agnostic:** Wraps around existing LLM stack (OpenAI, Anthropic, Gemini, Llama, internal models).

**Architecture Components:**
- **Guardian Middleware:** Intercepts all requests and responses
- **Triangle Engine:** Evaluates Intent, Constraint, and Coherence
- **Ground Truth Store:** Policies, manuals, contracts, curated data
- **Immutable Ledger:** Cryptographic record of each decision

**Sample Configuration:**
```yaml
mode: "strict_financial"
zones:
  intent: enabled
  constraint: strict
  coherence: min_grounding_score: 0.85
```

---

## SLIDE 11: THE GLASS BOX EVIDENCE CHAIN

**Headline:** Every interaction generates a cryptographic hash chain.

**Three Hashes:**
1. **Input Hash:** What was asked
2. **Decision Hash:** Why it was approved/blocked/escalated
3. **Output Hash:** What the system returned/executed

**Result:** Tamper-evident chain of custody for:
- Regulators
- Auditors
- Litigation readiness

**Visual:** Hash chain diagram showing linked cryptographic blocks

---

## SLIDE 12: IMPLEMENTATION ROADMAP — 6–8 WEEKS

**Visual:** Timeline with four phases

**Phase 1: Foundation (Weeks 1–2)**
- Landscape assessment
- Configuration draft
- Governance alignment

**Phase 2: Integration (Weeks 3–4)**
- Middleware integration
- Ground truth curation
- Pilot testing

**Phase 3: Scaling (Weeks 5–6)**
- Gradual rollout
- Monitoring & dashboards
- Team training

**Phase 4: Optimization (Weeks 7–8)**
- Fine-tune thresholds
- Compliance mapping
- Expansion to new domains

---

## SLIDE 13: INITIAL IMPLEMENTATION CHECKLIST

**Six Critical Steps:**

1. ✅ **System Mapping:** Identify critical decision points and agents
2. ✅ **Baseline Establishment:** Define "normal" behavior and thresholds
3. ✅ **Guardian Configuration:** Stand up production.yaml, gate_guardian.yaml, triangle_test.yaml
4. ✅ **Ground Truth Index:** Connect policies, manuals, and contracts
5. ✅ **Monitoring Setup:** Implement dashboards and alert rules
6. ✅ **Team Training:** Educate stakeholders on four gates and three zones

---

## SLIDE 14: KEY DIFFERENTIATORS

**Why Triangle Test?**

✅ **Platform-Agnostic** → Works with any LLM stack  
✅ **Deterministic** → "We verify the system" not "we trust the model"  
✅ **Adaptive** → GREEN/AMBER/RED postures respond to threat environment  
✅ **Auditable** → Immutable cryptographic evidence chain  
✅ **Sovereignty-Preserving** → Human operator retains ultimate control

**The Difference:**
- A **chatbot** you "hope" behaves
- vs. **Critical infrastructure** you can defend in front of a regulator, board, or judge

---

## SLIDE 15: CALL TO ACTION

**Headline:** Don't Just Deploy AI. Command It.

**Request Your Triangle Test Enterprise Assessment:**

**What You Receive:**
1. **Architecture Review** — Current AI use cases, agents, and risk profile
2. **Trust Gap Analysis** — Where Intent, Constraint, or Coherence are unguarded
3. **Deployment Blueprint** — 6–8 week roadmap tailored to your stack
4. **ROI & Risk Reduction Projection** — Quantified impact on efficiency, audit time, and risk exposure

**Next Steps:**
- **Email:** [documentation@cyw-os.com](mailto:documentation@cyw-os.com)
- **Reference:** "Triangle Test Protocol – Public White Paper v1.0"
- **Availability:** Limited complimentary assessments each quarter

---

## SLIDE 16: CREDITS & RESOURCES

**Triangle Test Protocol** • Public White Paper v1.0

**Document Classification:** PUBLIC • DISTRIBUTION UNLIMITED

**Author & Steward:**
Timothy I. Wheels  
Contruil LLC – Control Your World (CYW) OS

**Primary Contact:**
[documentation@cyw-os.com](mailto:documentation@cyw-os.com)

**License:**
Creative Commons Attribution 4.0 International (CC BY 4.0)

**Next Tier Resources (by request):**
- Triangle Test Enterprise Governance Guide (v2.0)
- Full YAML reference configurations
- 4-Gate Guardian Python SDK (beta)
- Compliance mapping worksheets (SOC 2, ISO, GDPR, HIPAA)

**Updates:** Protocol revisions published semi-annually (Q1, Q3)

---

## SLIDE DESIGN NOTES

### Visual Style Recommendations:

1. **Color Scheme:**
   - Primary: Deep blue (#1565c0) for trust and technology
   - Accent: Orange (#f57c00) for alerts and action
   - Success: Green (#2e7d32) for approved states
   - Warning: Amber/Yellow (#ffd700) for caution
   - Danger: Red (#d32f2f) for blocked/escalated states

2. **Typography:**
   - Headlines: Bold, sans-serif (e.g., Inter, Helvetica Neue)
   - Body: Clean, readable sans-serif
   - Code: Monospace (e.g., Fira Code, Monaco)

3. **Visual Elements:**
   - Triangle diagrams for the three zones
   - Flowcharts for the 4-Gate Guardian
   - Timeline graphics for implementation roadmap
   - Hash chain visualization for evidence chain
   - Comparison tables for GREEN/AMBER/RED postures

4. **Logo Placement:**
   - Title slide: Large, centered
   - Footer: Small, bottom-right on all slides

5. **Slide Count:**
   - Total: 16 slides (including title and credits)
   - Presentation time: ~20–25 minutes
   - Q&A: Additional 10–15 minutes

---

**END OF SLIDE DECK OUTLINE**

