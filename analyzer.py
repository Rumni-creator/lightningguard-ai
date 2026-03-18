import requests

def get_address_data(address):
    url = f"https://mempool.space/api/address/{address}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "tx_count": data["chain_stats"]["tx_count"],
        "funded": data["chain_stats"]["funded_txo_sum"] / 100000000,  # BTC
        "spent": data["chain_stats"]["spent_txo_sum"] / 100000000
    }


def analyze_address(address):
    data = get_address_data(rumni33@blink.sv)

    if not data:
        return {"error": "Invalid address or API error"}

    score = 0

    # Rule-based "AI"
    if data["tx_count"] > 100:
        score += 2
    if data["funded"] > 1:
        score += 2
    if data["spent"] == 0:
        score += 1  # suspicious inactive wallet

    if score >= 4:
        risk = "High Risk"
    elif score >= 2:
        risk = "Suspicious"
    else:
        risk = "Low Risk"

    return {
        "risk": risk,
        "data": data
    }