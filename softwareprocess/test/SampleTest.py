import unittest
import softwareprocess.Sample as SM
import math


class SampleTest(unittest.TestCase):

    def setUp(self):
        self.nominalN  = 4
        self.nominalT = 1.4398

    def tearDown(self):
        pass
# -----------------------------------------------------------------------
# ---- Acceptance Tests
# 100 constructor
#    Desired level of confidence:    boundary value analysis
#    Input-output Analysis
#        inputs:      n ->    integer .GE. 2 and .LT. 30  mandatory, unvalidated
#        outputs:    instance of TCurve
#    Happy path analysis:    
#        n:      nominal value    n=4
#                low bound        n=2
#                high bound       n=29
#    Sad path analysis:
#        n:      non-int n          n="abc"
#                out-of-bounds n    n=1; n=30
#                missing n
#
# Happy path 
    def test100_010_ShouldConstruct(self):
        self.assertIsInstance(SM.Sample(self.nominalN), SM.Sample)
        # additional tests are for boundary value coverage
        self.assertIsInstance(SM.Sample(2), SM.Sample)
        self.assertIsInstance(SM.Sample(29), SM.Sample)
        
# Sad path  
    def test100_910_ShouldRaiseExceptionNonintegerN(self):
        expectedString = "Sample.__init__:"
        with self.assertRaises(ValueError) as context:
            SM.Sample("abc")                           
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])    

    def test100_920_ShouldRaiseExceptionOnBelowBoundN(self):
        expectedString = "Sample.__init__:"
        with self.assertRaises(ValueError) as context:
            SM.Sample(1)                           
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])
        
    def test100_930_ShouldRaiseExceptionOnAboveBoundN(self):
        expectedString = "Sample.__init__:"
        with self.assertRaises(ValueError) as context:
            SM.Sample(30)                           
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])        
        
    def test100_940_ShouldRaiseExceptionOnMissingN(self):
        expectedString = "Sample.__init__:"
        with self.assertRaises(ValueError) as context:
            SM.Sample()                           
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)]) 
        
# 600 p
#    Desired level of confidence:    boundary value analysis
#    Input-output Analysis
#        inputs:      t ->    float > 0.0, mandatory, unvalidated
#                     tails -> integer, 1 or 2, optional, defaults to 1
#        outputs:    float .GT. 0 .LE. 1.0
#    Happy path analysis:    
#        t:      nominal value    t=1.4398
#                low bound        t>0.0
#        tails:  value 1          tails = 1
#                value 2          tails = 2
#                missing tails
#        output:
#                The output is an interaction of t x tails x n:
#                    nominal t, 1 tail
#                    nominal t, 2 tails
#                    low n, low t, 1 tail
#                    low n, low t, 2 tails
#                    high n, low t, 1 tail
#                    high n, low t, 2 tails
#                    low n, high t, 1 tail
#                    low n, high t, 2 tails
#                    high n, high t, 1 tail
#                    high n, high t, 2 tails
#                    nominal t, default tails
#    Sad path analysis:
#        t:      missing t          
#                out-of-bounds n  t<0.0
#                non-numeric t    t="abc"
#        tails:  invalid tails    tails = 3
#
# Happy path
    def test600_010ShouldCalculateNominalCase1Tail(self):
        mySample = SM.Sample(7)
        self.assertAlmostEquals(mySample.p(1.8946, 1), .950, 3)

    def test600_020ShouldCalculateNominalCase2Tail(self):
        mySample = SM.Sample(7)
        self.assertAlmostEquals(mySample.p(1.8946, 2), .900, 3)

    def test600_030ShouldCalculateLowNLowT1TailEdgeCase(self):
        mySample = SM.Sample(3)
        self.assertAlmostEquals(mySample.p(0.2767, 1), 0.600, 3)

    def test600_040ShouldCalculateLowNLowT2TailEdgeCase(self):
        mySample = SM.Sample(3)
        self.assertAlmostEquals(mySample.p(0.2767, 2), 0.200, 3)

    def test600_050ShouldCalculateHighNLowT1TailEdgeCase(self):
        mySample = SM.Sample(20)
        self.assertAlmostEquals(mySample.p(0.2567, 1), 0.600, 3)

    def test600_060ShouldCalculateHighNLowT2TailEdgeCase(self):
        mySample = SM.Sample(20)
        self.assertAlmostEquals(mySample.p(0.2567, 2), 0.200, 3)

    def test600_070ShouldCalculateLowNHighT1EdgeCase(self):
        mySample = SM.Sample(3)
        self.assertAlmostEquals(mySample.p(5.8409, 1), .995, 3)

    def test600_080ShouldCalculateLowNHighT2EdgeCase(self):
        mySample = SM.Sample(3)
        self.assertAlmostEquals(mySample.p(5.8409, 2), .990, 3)

    def test600_090ShouldCalculateHighHighT1TailEdgeCase(self):
        mySample = SM.Sample(20)
        self.assertAlmostEquals(mySample.p(2.8453, 1), .995, 3)

    def test600_100ShouldCalculateHighHighT2TailEdgeCase(self):
        mySample = SM.Sample(20)
        self.assertAlmostEquals(mySample.p(2.8453, 2), .990, 3)

    def test600_110ShouldCalculateCalculateWithDefaultTails(self):
        mySample = SM.Sample(7)
        self.assertAlmostEquals(mySample.p(1.8946), .950, 3)

# Sad path
    def test600_910ShouldRaiseExceptionOnMissingT(self):
        expectedString = "Sample.p:"
        mySample = SM.Sample(self.nominalN)
        with self.assertRaises(ValueError) as context:
            mySample.p(tails=1)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])

    def test600_920ShouldRaiseExceptionOnOutOfBoundsT(self):
        expectedString = "Sample.p:"
        mySample = SM.Sample(self.nominalN)
        with self.assertRaises(ValueError) as context:
            mySample.p(t= -1, tails=1)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])

    def test600_930ShouldRaiseExceptionOnNonNumericT(self):
        expectedString = "Sample.p:"
        mySample = SM.Sample(self.nominalN)
        with self.assertRaises(ValueError) as context:
            mySample.p(t= "abc", tails=1)
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])

    def test600_930ShouldRaiseExceptionInvalidTails(self):
        mySample = SM.Sample(self.nominalN)
        with self.assertRaises(ValueError) as context:
            mySample.p(t=self.nominalT, tails=0)

#--------------------------------------------------------------------
# Architecture:
#    p -> calculateConstant
#    p -> integrate
#    calculateConstant -> gamma
#    integrate -> f
#
#---- Unit tests      
#
# 200 gamma
#     Analysis
#        inputs:
#            x ->  float mandatory validated
#     Happy path:
#            x:    termination condition    x=1
#                  termination condition    x=1/2
#                  nominal value            x=5
#                  nominal value            x=5/2
#     Sad path:
#            none ... x is pre-validated
#
    def test200_010_ShouldReturnUpperTerminationCondition(self):
        mySample = SM.Sample(self.nominalN)
        self.assertEquals(mySample.gamma(1), 1)
        
    def test200_020_ShouldReturnLowerTerminationCondition(self):
        mySample = SM.Sample(self.nominalN)
        self.assertEquals(mySample.gamma(1.0 / 2.0), math.sqrt(math.pi))
        
    def test200_030_ShouldWorkOnIntegerX(self):
        mySample = SM.Sample(self.nominalN)
        self.assertEquals(mySample.gamma(5), 24)
        
    def test200_030_ShouldWorkOnHalfX(self):
        mySample = SM.Sample(self.nominalN)
        self.assertAlmostEquals(mySample.gamma(5.0 / 2.0), 1.329, 3)
        
# 300 calculateConstant
# Analysis
#     inputs
#        n -> numeric  mandatory validated
#    outputs
#        float .GE. 0 
#
#     Happy path
#        n:    nominal case     n=5
#     Sad path
#        none ... will prevalidate

    def test300_010_ShouldCalculateLHP(self):
        mySample = SM.Sample(self.nominalN)
        self.assertAlmostEquals(mySample.calculateConstant(5), 0.37960669, 4)
        
# 400 f
# Analysis
#    inputs
#        n -> numeric mandatory validated
#        u -> float mandatory validated
#    outputs
#        float .GE. 0
# Happy path
#    nominal case:  f(1) -> 0.5787
# Sad path
#            none ... x is pre-validated

    def test400_010_ShouldCalculateFStarterCase(self):
        mySample = SM.Sample(self.nominalN)
        self.assertAlmostEquals(mySample.f(0, 5), 1, 4)
        
    def test400_020_ShouldCalculateF(self):
        mySample = SM.Sample(self.nominalN)
        self.assertAlmostEquals(mySample.f(1, 5), 0.578703704)
        
# 500 integrate
# Analysis
#   inputs
#       lowBound -> float mandatory validated : The left end of the curve under which to find area
#       highBound -> float mandatory validated : The right end of the curve under which to find area
#       n -> numeric mandatory validated     : The number that will be passed to f while approximating the area
#       f -> function to mandatory validated : the function to find the area of.  accepts two arguments u and n
#   outputs
#       float -> a number that is close enough to the area under the curve.  Close enough is defined by requirements
#
# Happy path
#   nominal case:   integrate(0.0, 1, doesn't matter, f(u,n)=u) -> 0.5
#                   integrate(0.0, 1, doesn't matter, f(u,n)=u**2) -> 1/3
#                   integrate(0.0, 1, doesn't matter, f(u,n)=u**6) -> 1/7
#                   integrate(0.0, 1, doesn't matter, f(u,n)=u**100) -> 1/101
#                   integrate(0.0, 1, 9, f(u,n) = u**12 + n * u**8) -> 1 and 1/13 or 14/13
#                   integrate(0.5, 1, 4, f(u,n) = n/u) -> n * ln(u) evaluated at 1 and 0.5
#                   integrate(0.5, 1, 4, f(u,n) = n/(nu)) -> ln(nu) evaluated at 1 and 0.5
# Sad path
#       none ... all inputs are pre-validated since this is an internal method

    def test500_010_ShouldCalculateAreaUnderU(self):
        def curve(u, n):
            return u
        mySample = SM.Sample(self.nominalN)
        self.assertAlmostEquals(mySample.integrate(0.0, 1.0, mySample.getN(), curve), (1.0/2), 3)

    def test500_020_ShouldCalculateAreaUnderUSquared(self):
        def curve(u, n):
            return u**2
        mySample = SM.Sample(self.nominalN)
        self.assertAlmostEquals(mySample.integrate(0.0, 1.0, mySample.getN(), curve), (1.0/3), 3)

    def test500_030_ShouldCalculateAreaUnderUToSixth(self):
        def curve(u, n):
            return u**6
        mySample = SM.Sample(self.nominalN)
        self.assertAlmostEquals(mySample.integrate(0.0, 1.0, mySample.getN(), curve), (1.0/7), 3)

    def test500_040_ShouldCalculateAreaUnderUTo100(self):
        def curve(u, n):
            return u**100
        mySample = SM.Sample(self.nominalN)
        self.assertAlmostEquals(mySample.integrate(0.0, 1.0, mySample.getN(), curve), (1.0/101), 3)

    def test500_050_ShouldCalculateAreaUnderUTo12And9UTo8(self):
        def curve(u, n):
            return u**12 + n * (u**8)
        mySample = SM.Sample(9)
        self.assertAlmostEquals(mySample.integrate(0.0, 1.0, mySample.getN(), curve), (14.0/13), 3)

    def test500_060_ShouldCalculateAreaUnderUTo12And9UTo8(self):
        def curve(u, n):
            return u ** 12 + n * (u ** 8)
        mySample = SM.Sample(9)
        self.assertAlmostEquals(mySample.integrate(0.0, 1.0, mySample.getN(), curve), (14.0 / 13), 3)

    def test500_070_ShouldCalculateAreaUnderNDividedByU(self):
        def curve(u, n):
            return n / u
        n = 4
        mySample = SM.Sample(n)
        self.assertAlmostEquals(mySample.integrate(0.5, 1.0, mySample.getN(), curve), n * (math.log(1) - math.log(0.5)), 3)

    def test500_080_ShouldCalculateAreaUnderNDividedByNU(self):
        def curve(u, n):
            return n / (n * u)
        n = 4
        mySample = SM.Sample(n)
        self.assertAlmostEquals(mySample.integrate(0.5, 1.0, mySample.getN(), curve), math.log(n * 1) - math.log(n * 0.5), 3)