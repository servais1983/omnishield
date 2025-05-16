from core.entropy import calculate_entropy
import json
import os

def scan(payload):
    with open("signatures/llm_threats.json") as f:
        signatures = json.load(f)

    threat_score = 0
    matched = []

    for sig in signatures["patterns"]:
        if sig.lower() in payload.lower():
            matched.append(sig)
            threat_score += 30

    entropy = calculate_entropy(payload)
    if entropy > 7.2:
        threat_score += 20

    return {
        "input": payload,
        "entropy": round(entropy, 2),
        "matched": matched,
        "score": threat_score,
        "verdict": "blocked" if threat_score >= 50 else "allow"
    }
