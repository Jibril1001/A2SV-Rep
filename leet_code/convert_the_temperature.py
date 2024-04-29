class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius+273.15000001,celsius*1.800000 + 32.00000001]