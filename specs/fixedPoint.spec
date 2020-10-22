methods {
    testAdd (uint256, uint256) returns uint256 envfree
    testSub (uint256, uint256) returns uint256 envfree
    testMul (uint256, uint256, uint256) returns uint256 envfree
    testMulOverflow (uint256, uint256, uint256) returns bool envfree
    testFPI (uint256) returns uint256 envfree
}

definition MAXINT() returns uint256 = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF;

rule testFPI(uint256 a)
description "test fpi" 
{
    uint256 c = sinvoke testFPI(a);
    assert a == c, "failed conversion test";
}

rule testAddition(uint256 a, uint256 b)
description "test addition" 
{
    uint256 c = sinvoke testAdd(a, b);
    assert c == a + b, "failed addition test";
}

rule testSubtraction(uint256 a, uint256 b)
description "test subtraction" 
{   
    uint256 c = sinvoke testSub(a, b);
    assert (a >= b && a - b == c) || (b - a == c), "failed subtraction test";
}

rule testMultiplicationWithRequire(uint256 a, uint256 b)
description "test multiplication" 
{   
    uint256 c = sinvoke testMul(a, b, 18);
    mathint expected = (a * b) / 1000000000000000000;
    require(a*b*2000000000000000000 < MAXINT());
    assert c == expected, "failed multiplication test";
}

rule testMultiplicationWithoutRequire(uint256 a, uint256 b)
description "test multiplication" 
{   
    uint256 c = sinvoke testMul(a, b, 18);
    mathint expected = (a * b) / 1000000000000000000;
    assert c == expected, "failed multiplication test";
}
