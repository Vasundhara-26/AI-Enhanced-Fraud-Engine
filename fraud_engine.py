class FraudDetectionEngine:
    def __init__(self, threshold=75):
        self.threshold = threshold

    def evaluate_transaction(self, amount, velocity_score, is_high_risk_geo):
        """Calculates a cumulative risk score based on transaction parameters."""
        risk_score = 0
        
        # Rule-based weighted risk factors
        if amount > 50000:
            risk_score += 40
        
        risk_score += (velocity_score * 10)  # Frequent transactions in short window
        
        if is_high_risk_geo:
            risk_score += 30
            
        # Anomaly / Fraud Decision
        is_flagged = risk_score >= self.threshold
        status = "FLAGGED FOR FRAUD REVIEW" if is_flagged else "APPROVED"
        
        return {
            "amount": amount,
            "risk_score": risk_score,
            "status": status
        }

if __name__ == "__main__":
    engine = FraudDetectionEngine()
    print("Running Financial Fraud Detection Engine...")
    
    # Test Case 1: High risk transaction
    print(engine.evaluate_transaction(75000, 4, True))
    
    # Test Case 2: Normal transaction
    print(engine.evaluate_transaction(3400, 1, False))