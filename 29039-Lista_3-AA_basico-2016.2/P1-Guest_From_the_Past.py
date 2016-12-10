def buyGlassBottle(money, purchasePrice, salePrice):
    quantity = 0
    if (money >= purchasePrice):
        quantity = ((money - purchasePrice)/(purchasePrice - salePrice)) + 1
        money = money - (purchasePrice * quantity)
        money = money + salePrice * quantity
    return quantity, money

def buyPlasticBottle(money, bottlePrice):
    total = 0
    restOTMoney = money
    if (money >= bottlePrice):
        total = money / bottlePrice
        cost = bottlePrice * total
        restOTMoney = money - cost

    return total, restOTMoney



rubles = int(raw_input())
plasticBottle = int(raw_input())
glassBottle = int(raw_input())
glassPrice = int(raw_input())


#buyPlasticBottleFirst
stPlasticQuantity, stMoney = buyPlasticBottle(rubles, plasticBottle)
stGlassQuantity, restStMoney = buyGlassBottle(stMoney, glassBottle, glassPrice)
firstToal = stPlasticQuantity + stGlassQuantity

#buyGlassBottleFirst
ndGlassQuantity, ndMoney = buyGlassBottle(rubles, glassBottle, glassPrice)
ndPlasticQuantity, restNdMoney = buyPlasticBottle(ndMoney, plasticBottle)
secondTotal = ndGlassQuantity + ndPlasticQuantity

print max(firstToal, secondTotal)
