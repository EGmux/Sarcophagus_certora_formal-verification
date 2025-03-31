// 
methods {
    function Sarcophagus.archaeologistCount() external returns (uint256) envfree;
    function Sarcophagus.registerArchaeologist(
        bytes  currentPublicKey,
        string  endpoint,
        address paymentAddress,
        uint256 feePerByte,
        uint256 minimumBounty,
        uint256 minimumDiggingFee,
        uint256 maximumResurrectionTime,
        uint256 freeBond
    ) external returns (uint256) envfree;
}

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Rule: the number of archeologists must increase by one after every call to registerArchaeologist
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
    
rule increaseArcheologistCountByOneForEveryCallToRegisterArchaeologist() {
    address sarcophagus; // constructor is implicit in the Sarcophagus contract
    calldataarg args;
    method m;
    env e;
    
    uint256 totalArcheologists = sarcophagus.archaeologistCount(e); // expect to be 0
    sarcophagus.m(e,args);
    // if selected method has the below signature then the rule must be valid, otherwise is valid by vacuity
    if(m.selector == sig:registerArchaeologist(bytes, string, address, uint256, uint256, uint256, uint256, uint256).selector) {
        assert (totalArcheologists + 1 == sarcophagus.archaeologistCount(e));
    }
    else {
        assert true;
    }
}