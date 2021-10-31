'''
Python में, yield Keyword का प्रयोग Function से एक से ज्यादा Value को Return करने के लिए किया जाता है। अतः yield एक ऐसा Keyword है जो
Function से Value को Return करता है और Function के Local Variable का मान नष्ट नहीं करता है और जब Function को Call किया जाता है तो यह फिर से
आरंभ न होकर अपने पिछले Local Variable (yield Statements) के मान से शुरू होता है।

Python में yield एक Generator की तरह कार्य करता है। अतः Python में कोई भी Function जिसमें yield का प्रयोग किया गया है वह एक Generator Function होता है।
yield Keyword का प्रयोग प्रायः ही होता है लेकिन इसकी उपयोगिता बहुत बड़ी होती है। नीचे दिए गए Syntax के अनुसार yield Keyword का प्रयोग करते है।
'''


def Topten():


    n = 1

    while n <= 10:
        sq = n*n
        yield sq
        n += 1


values = Topten()

for i in values:
    print(i)