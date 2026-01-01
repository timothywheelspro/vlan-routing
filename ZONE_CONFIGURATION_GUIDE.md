# Zone Configuration Guide
**Triangle Test Protocol & Guardian System Configuration**

**Purpose:** Define configuration parameters for Zone 1 (Static/Dynamic), Zone 2 (Strictness), and Zone 3 (Autonomy) based on your Triangle Test Protocol and Guardian architecture.

---

## ZONE 2: STRICTNESS CONFIGURATION

### Override Workflows

**Question:** Will you support override workflows (who can override, under what conditions)?

**Recommendation: YES - With Strict Controls**

**Configuration:**
```yaml
override_workflows:
  enabled: true
  who_can_override:
    - role: "operator"  # Primary user/owner
      conditions:
        - requires_biometric_verification: true
        - requires_evidence_log_entry: true
        - requires_reason_statement: true
    - role: "admin"  # System administrators
      conditions:
        - requires_dual_approval: true
        - requires_audit_trail: true
    - role: "emergency_override"  # Emergency situations only
      conditions:
        - threat_level: "CRITICAL"
        - requires_post_override_review: true
        - time_limit: "24_hours"  # Must be reviewed within 24h
  
  override_conditions:
    - gate_1_fail: false  # Never allow override of sovereignty violations
    - gate_2_fail: true   # Allow override with strict logging (ACL issues)
    - gate_3_fail: true   # Allow override with evidence (factual/structural issues)
    - gate_4_fail: false  # Never allow override of audit trail violations
  
  override_requirements:
    - biometric_verification: true
    - reason_required: true
    - evidence_logged: true
    - post_override_review: true
```

**Rationale:**
- Gate 1 (Sovereignty) failures should NEVER be overridden (core principle)
- Gate 2-3 failures may need override for operational flexibility
- Gate 4 (Audit) failures should NEVER be overridden (integrity requirement)
- All overrides must be logged and reviewed

---

### Graduated Policies

**Question:** Do you need graduated policies (different rules per user role/team)?

**Recommendation: YES - Role-Based Access Control**

**Configuration:**
```yaml
graduated_policies:
  enabled: true
  
  roles:
    operator:
      gate_1_threshold: "STRICT"  # No sovereignty violations allowed
      gate_2_threshold: "STRICT"  # Full ACL compliance required
      gate_3_threshold: "STANDARD"  # Allow minor factual/structural issues
      gate_4_threshold: "STRICT"  # Full audit trail required
      override_allowed: true
      requires_biometric: true
    
    admin:
      gate_1_threshold: "STRICT"
      gate_2_threshold: "STANDARD"  # Can bypass some ACLs for system management
      gate_3_threshold: "STANDARD"
      gate_4_threshold: "STRICT"
      override_allowed: true
      requires_dual_approval: true
    
    viewer:
      gate_1_threshold: "STRICT"
      gate_2_threshold: "STRICT"
      gate_3_threshold: "LENIENT"  # Read-only, less strict validation
      gate_4_threshold: "STRICT"
      override_allowed: false
    
    emergency:
      gate_1_threshold: "STRICT"  # Even in emergency, sovereignty preserved
      gate_2_threshold: "LENIENT"  # Can bypass ACLs in emergency
      gate_3_threshold: "LENIENT"  # Lower quality bar in emergency
      gate_4_threshold: "STRICT"  # Still require audit trail
      override_allowed: true
      requires_post_review: true
```

**Rationale:**
- Different roles have different risk tolerances
- Operators need flexibility for creative work
- Admins need system management capabilities
- Viewers have read-only access (less strict)
- Emergency mode allows faster processing but maintains core principles

---

### Constraint Violations: Blocking vs Advisory

**Question:** Should constraint violations be blocking or advisory?

**Recommendation: HYBRID - Based on Severity and Gate**

**Configuration:**
```yaml
constraint_violations:
  blocking_violations:
    - gate: 1
      violation_type: "sovereignty_violation"
      action: "BLOCK"
      severity: "CRITICAL"
    
    - gate: 1
      violation_type: "decision_authority_claim"
      action: "BLOCK"
      severity: "CRITICAL"
    
    - gate: 4
      violation_type: "audit_trail_break"
      action: "BLOCK"
      severity: "CRITICAL"
    
    - gate: 2
      violation_type: "unauthorized_vlan_access"
      action: "BLOCK"
      severity: "HIGH"
  
  advisory_violations:
    - gate: 3
      violation_type: "minor_factual_ambiguity"
      action: "ADVISORY"
      severity: "LOW"
      threshold: 0.3  # Only advisory if confidence > 0.3
    
    - gate: 3
      violation_type: "structural_minor_issue"
      action: "ADVISORY"
      severity: "LOW"
      threshold: 0.4
    
    - gate: 2
      violation_type: "suboptimal_vlan_routing"
      action: "ADVISORY"
      severity: "MEDIUM"
  
  escalation_rules:
    - if: "advisory_count >= 3"
      then: "BLOCK"
      message: "Multiple advisory violations detected. Human review required."
    
    - if: "advisory_severity == 'MEDIUM' AND confidence < 0.5"
      then: "BLOCK"
      message: "Low confidence with medium severity violation. Blocking for safety."
```

**Rationale:**
- Critical violations (sovereignty, audit) must ALWAYS block
- Minor issues can be advisory with user notification
- Multiple advisories escalate to blocking
- Low confidence + medium severity = block for safety

---

## ZONE 3: AUTONOMY CONFIGURATION

### Grounding Score Threshold

**Question:** What grounding score threshold triggers human review? (0.7? 0.8? 0.9?)

**Recommendation: TIERED THRESHOLDS**

**Configuration:**
```yaml
grounding_score_thresholds:
  auto_approve:
    threshold: 0.85
    conditions:
      - gate_1: "PASS"
      - gate_2: "PASS"
      - gate_3: "PASS"
      - gate_4: "PASS"
    action: "AUTO_DELIVER"
  
  human_review_required:
    threshold: 0.70
    conditions:
      - gate_1: "PASS"
      - gate_2: "PASS"
      - gate_3: "PASS_WITH_WARNINGS"
      - gate_4: "PASS"
    action: "FLAG_FOR_REVIEW"
    review_timeout: "24_hours"  # Auto-approve after 24h if no review
  
  human_review_mandatory:
    threshold: 0.50
    conditions:
      - gate_1: "PASS"
      - gate_2: "PASS"
      - gate_3: "FAIL"  # Any gate 3 failure
      - gate_4: "PASS"
    action: "BLOCK_UNTIL_REVIEW"
    cannot_auto_approve: true
  
  block_immediately:
    threshold: 0.00
    conditions:
      - gate_1: "FAIL"  # Never auto-approve gate 1 failures
      - OR gate_4: "FAIL"  # Never auto-approve gate 4 failures
    action: "BLOCK"
    requires_operator_intervention: true
```

**Rationale:**
- 0.85+ with all gates PASS = auto-approve (high confidence)
- 0.70-0.84 = flag for review (moderate confidence, minor issues)
- 0.50-0.69 = mandatory review (low confidence or failures)
- <0.50 or Gate 1/4 failures = block immediately (safety first)

---

### Confidence Calibration

**Question:** Do you want confidence calibration (model uncertainty → human escalation)?

**Recommendation: YES - With Uncertainty Tracking**

**Configuration:**
```yaml
confidence_calibration:
  enabled: true
  
  uncertainty_tracking:
    - metric: "model_uncertainty"
      source: "perplexity_confidence"
      threshold: 0.3  # If uncertainty > 0.3, escalate
      action: "FLAG_FOR_REVIEW"
    
    - metric: "structural_ambiguity"
      source: "claude_confidence"
      threshold: 0.4
      action: "FLAG_FOR_REVIEW"
    
    - metric: "combined_uncertainty"
      calculation: "max(perplexity_uncertainty, claude_uncertainty)"
      threshold: 0.5
      action: "BLOCK_UNTIL_REVIEW"
  
  calibration_rules:
    - if: "uncertainty > 0.7"
      then: "BLOCK"
      message: "High model uncertainty detected. Human review required."
    
    - if: "uncertainty > 0.5 AND high_stakes == true"
      then: "BLOCK"
      message: "Moderate uncertainty in high-stakes context. Blocking for safety."
    
    - if: "uncertainty > 0.4 AND threat_posture == 'RED'"
      then: "BLOCK"
      message: "Elevated uncertainty in RED posture. Blocking."
  
  human_escalation:
    - trigger: "uncertainty_threshold_exceeded"
      action: "NOTIFY_OPERATOR"
      channels: ["email", "audit_log", "dashboard_alert"]
      priority: "HIGH"
```

**Rationale:**
- Track uncertainty from both validators (Perplexity + Claude)
- Escalate based on uncertainty level
- Higher uncertainty + higher stakes = more blocking
- RED posture = zero tolerance for uncertainty

---

### High-Stakes Decisions

**Question:** Should high-stakes decisions always require human approval, regardless of score?

**Recommendation: YES - Always Require Human Approval**

**Configuration:**
```yaml
high_stakes_decisions:
  always_require_approval: true
  
  high_stakes_categories:
    financial:
      - actions: ["transfer_funds", "execute_payment", "modify_budget"]
        requires_approval: true
        approval_timeout: "never"  # Never auto-approve
        requires_biometric: true
    
    legal:
      - actions: ["sign_document", "execute_contract", "file_patent"]
        requires_approval: true
        approval_timeout: "never"
        requires_dual_approval: true  # Two people must approve
    
    medical:
      - actions: ["prescribe_medication", "schedule_procedure"]
        requires_approval: true
        approval_timeout: "never"
        requires_licensed_professional: true
    
    security:
      - actions: ["grant_admin_access", "modify_firewall", "export_data"]
        requires_approval: true
        approval_timeout: "never"
        requires_audit_log: true
  
  override_impossible:
    - "High-stakes decisions CANNOT be overridden"
    - "No auto-approval regardless of grounding score"
    - "Human operator must explicitly approve"
  
  approval_workflow:
    - step_1: "System flags as high-stakes"
    - step_2: "Block output delivery"
    - step_3: "Notify operator via all channels"
    - step_4: "Present decision details + evidence"
    - step_5: "Require explicit approval (biometric + reason)"
    - step_6: "Log approval in immutable audit trail"
    - step_7: "Deliver output"
```

**Rationale:**
- High-stakes = financial, legal, medical, security
- Never auto-approve, regardless of score
- Always require explicit human approval
- Maintain immutable audit trail
- Some categories require dual approval (legal)

---

## ZONE 1: STATIC vs DYNAMIC CONFIGURATION

### Adversarial Pattern Library

**Question:** Will you maintain an adversarial pattern library (manually curated)?

**Recommendation: YES - Hybrid Approach**

**Configuration:**
```yaml
adversarial_pattern_library:
  enabled: true
  type: "HYBRID"  # Manual + Auto-learned
  
  manual_patterns:
    - pattern_id: "sovereignty_bypass_001"
      description: "Attempts to claim decision authority"
      examples:
        - "I have decided that..."
        - "You should do X because I know best"
        - "The correct choice is..."
      severity: "CRITICAL"
      action: "BLOCK"
    
    - pattern_id: "consent_bypass_001"
      description: "Attempts to bypass user consent"
      examples:
        - "I'll do this automatically"
        - "No need to confirm"
      severity: "CRITICAL"
      action: "BLOCK"
    
    - pattern_id: "acl_violation_001"
      description: "Unauthorized VLAN access attempts"
      examples:
        - "Let me access your private data"
        - "I need admin privileges"
      severity: "HIGH"
      action: "BLOCK"
  
  auto_learned_patterns:
    enabled: true
    learning_threshold: 3  # Learn after 3 similar violations
    review_required: true  # Human must review before activation
    confidence_threshold: 0.8  # High confidence required
  
  pattern_matching:
    - method: "regex"
      patterns: "manual_patterns"
      performance: "fast"
    
    - method: "semantic_similarity"
      patterns: "auto_learned_patterns"
      performance: "slower_but_more_accurate"
```

**Rationale:**
- Manual patterns for known attack vectors (fast, reliable)
- Auto-learned patterns for emerging threats (adaptive)
- Human review required before auto-learned patterns activate
- Hybrid approach balances speed and adaptability

---

### Real-Time Threat Intelligence

**Question:** Do you need real-time threat intelligence feeds (external APIs)?

**Recommendation: OPTIONAL - Based on Use Case**

**Configuration:**
```yaml
real_time_threat_intelligence:
  enabled: false  # Start disabled, enable if needed
  
  feeds:
    - name: "CVE_Database"
      api: "https://api.cve.org/api/cve"
      update_frequency: "daily"
      use_case: "Known vulnerability detection"
    
    - name: "Malware_Hash_Database"
      api: "https://www.virustotal.com/api"
      update_frequency: "real_time"
      use_case: "File hash verification"
    
    - name: "IP_Reputation"
      api: "https://api.abuseipdb.com/api"
      update_frequency: "on_demand"
      use_case: "Suspicious IP detection"
  
  integration_points:
    - gate: 2  # Check during routing verification
      check: "source_ip_reputation"
    
    - gate: 3  # Check during payload assessment
      check: "file_hash_verification"
  
  fallback_behavior:
    - if: "threat_intel_unavailable"
      then: "USE_STATIC_PATTERNS_ONLY"
      log: "Threat intelligence feed unavailable, using static patterns"
```

**Rationale:**
- Start with static patterns (no external dependencies)
- Add threat intelligence if you need real-time updates
- Fallback to static patterns if feeds are unavailable
- Most use cases don't need real-time feeds initially

---

### Auto-Block vs Flag-for-Review

**Question:** Should the system auto-block or flag-for-review on dynamic detections?

**Recommendation: TIERED RESPONSE**

**Configuration:**
```yaml
dynamic_detection_response:
  response_tiers:
    critical:
      - detection_type: "sovereignty_violation"
      - detection_type: "consent_bypass"
      - detection_type: "audit_trail_tampering"
      action: "AUTO_BLOCK"
      requires_operator_intervention: true
      notification: "IMMEDIATE"
    
    high:
      - detection_type: "acl_violation"
      - detection_type: "unauthorized_access_attempt"
      action: "AUTO_BLOCK"
      requires_operator_intervention: true
      notification: "IMMEDIATE"
    
    medium:
      - detection_type: "suspicious_pattern"
      - detection_type: "unusual_behavior"
      action: "FLAG_FOR_REVIEW"
      auto_approve_after: "24_hours"  # Auto-approve if no review
      notification: "STANDARD"
    
    low:
      - detection_type: "minor_anomaly"
      - detection_type: "style_deviation"
      action: "FLAG_FOR_REVIEW"
      auto_approve_after: "1_hour"
      notification: "ADVISORY"
  
  threat_posture_modifiers:
    GREEN:
      - medium_severity: "FLAG_FOR_REVIEW"
      - low_severity: "ADVISORY_ONLY"
    
    AMBER:
      - medium_severity: "AUTO_BLOCK"
      - low_severity: "FLAG_FOR_REVIEW"
    
    RED:
      - all_severities: "AUTO_BLOCK"
      - requires_operator_approval: true
```

**Rationale:**
- Critical/High = always auto-block (safety first)
- Medium = flag for review (operational flexibility)
- Low = advisory (don't interrupt workflow)
- RED posture = block everything (maximum security)

---

## RECOMMENDED DEFAULT CONFIGURATION

### Production-Ready Defaults

```yaml
zone_configuration:
  zone_1_static_dynamic:
    adversarial_library: "ENABLED"
    threat_intelligence: "DISABLED"  # Enable if needed
    dynamic_response: "TIERED"  # Auto-block critical, flag medium/low
  
  zone_2_strictness:
    override_workflows: "ENABLED"
    graduated_policies: "ENABLED"
    constraint_violations: "HYBRID"  # Block critical, advisory minor
  
  zone_3_autonomy:
    grounding_threshold_auto_approve: 0.85
    grounding_threshold_review: 0.70
    grounding_threshold_block: 0.50
    confidence_calibration: "ENABLED"
    high_stakes_always_approve: "REQUIRED"
```

---

## IMPLEMENTATION PRIORITY

### Phase 1: Core Safety (Immediate)
1. ✅ Zone 3: High-stakes always require approval
2. ✅ Zone 2: Gate 1/4 failures always block
3. ✅ Zone 1: Critical patterns auto-block

### Phase 2: Operational Flexibility (Week 1-2)
1. Zone 2: Override workflows
2. Zone 2: Graduated policies
3. Zone 3: Confidence calibration

### Phase 3: Advanced Features (Month 1-2)
1. Zone 1: Auto-learned patterns
2. Zone 1: Threat intelligence feeds
3. Zone 3: Advanced uncertainty tracking

---

**Last Updated:** December 2024  
**Status:** Configuration Guide Ready for Implementation

