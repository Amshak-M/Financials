class CompoundInterest():
    """ Contains all the calculations related to compounding"""
    @staticmethod
    def annual_ci(principle, rate, time, ci_year=1) -> float:
        """ Yearly Compounding interest
        principle -> Invested one time amt
        rate -> ROI
        time -> Invested time
        ci_year -> Yearly compounding frequency. Quaterly => 4"""
        return principle * ((1+((rate/100)/ci_year))**(ci_year * time))

    @staticmethod
    def mutualfund_sip(principle: float, rate: float, time_yy: int, incriment_yy: float = 0):
        """ Mutual Funds through SIP 
        principle -> Monthly investment
        rate -> ROI
        time -> Invested time
        ci_year -> Yearly compounding frequency. Quaterly => 4"""
        time_mm = time_yy * 12
        ci_mm = rate/(100 * 12)
        return principle * (((1+ci_mm) ** time_mm) - 1) * (1+ci_mm)/ci_mm

    @staticmethod
    def mutualfund_sip_cf(principle: float, rate: float, time_yy: int, incriment_yy: float = 0):
        """ Mutual Fund SIP with yearly increment """
        carry_forword_amt = 0
        matured_amt = 0
        for i in range(0, time_yy):
            if(incriment_yy and i > 1):
                principle = principle + incriment_yy
                total_investment_yy = principle * 12
            else:
                total_investment_yy = principle * 12
            interest_earned = (total_investment_yy +
                               carry_forword_amt) * rate/100
            carry_forword_amt = principle + interest_earned + carry_forword_amt
        matured_amt = carry_forword_amt
        return matured_amt
