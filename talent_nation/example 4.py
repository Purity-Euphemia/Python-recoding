def solution(meters):
    meters = float(meters)
    centimeters = meters * 100
    millimeters = meters * 1000

    return f"Centimeters: {centimeters:.1f}\nMillimeters: {millimeters:.1f}"