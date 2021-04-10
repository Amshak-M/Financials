from src.interest import CompoundInterest
from dataclasses import dataclass


@dataclass
class FDdata:
    principle: float = 10000
    rate: float = 7
    time_yy: int = 10
    ci_year: int = 1


@dataclass
class SIPData:
    principle: float = 13000
    rate: float = 12
    time_yy: int = 15
    incriment: float = 0


print(f"Testing class details : {CompoundInterest().__doc__}\n")

# Annual compounding function test
result_ci = CompoundInterest.annual_ci(
    principle=FDdata.principle, rate=FDdata.rate, time=FDdata.time_yy, ci_year=FDdata.ci_year)
print(f"Amount after compounding is {result_ci}")


# SIP Mutual funds test
maturity = CompoundInterest.mutualfund_sip(
    principle=SIPData.principle, rate=SIPData.rate, time_yy=SIPData.time_yy, incriment_yy=SIPData.incriment)
print(f"Rs.{SIPData.principle} invested in MF via SIP with expected {SIPData.rate}% return for {SIPData.time_yy} years with Rs.{SIPData.incriment}  yearly incriment\nAmount at maturity = {maturity}")
