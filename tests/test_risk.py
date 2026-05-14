from src.models.predict import assign_risk

def test_assign_risk():
    assert assign_risk(0.1) == "Low"
    assert assign_risk(0.3) == "Medium"
    assert assign_risk(0.7) == "High"
    assert assign_risk(0.95) == "Critical"