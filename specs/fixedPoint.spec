methods {
    testAdd (uint256, uint256) returns uint256 envfree
    testSub (uint256, uint256) returns uint256 envfree
    testMul (uint256, uint256, uint256) returns uint256 envfree
    expectedAdd (uint256, uint256) returns uint256 envfree
    expectedMul (uint256, uint256, uint256) returns uint256 envfree
    testFPI (uint256) returns uint256 envfree
}

definition MAXINT() returns uint256 = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF;

rule testFPI(uint256 a)
description "test fpi" 
{
    uint256 c = sinvoke testFPI(a);
    assert a == c, "failed conversion test";
}

rule testExpectedAddition(uint256 a, uint256 b)
description "test addition" 
{
    uint256 expected = sinvoke expectedAdd(a, b);
    assert expected == a + b, "failed addition test";
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

rule testMultiplication(uint256 a, uint256 b)
description "test multiplication" 
{   
    uint256 c = sinvoke testMul(a, b, 18);
    uint256 expected = invoke expectedMul(a, b, 18);
    assert c <= expected, "failed multiplication test";
}
