using Sarcophagus as sarcophagus;
using Types as types;
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
    ) external returns (uint256);
    function Sarcophaguses.rewrapSarcophagus(
        // Datas.Data storage data,
        bytes32 identifier,
        uint256 resurrectionTime,
        uint256 diggingFee,
        uint256 bounty
        // IERC20 sarcoToken // adapt this 
    ) external returns (bool);
    function Sarcophagus.initialize(address _sarcoToken) external;
    function Sarcophagus.archaeologistAddresses(uint256 index) external returns (address) envfree;
    function Sarcophagus.archaeologists(address account) external returns (Types.Archaeologist) envfree;
}

// Initialization of a new Sarcophagus contract
function cvlInitNewSarcoToken(env e){
    address sarcoTokenAddress;
    sarcophagus.initialize(e,sarcoTokenAddress);
}


function cvlRegisterNewArcheologist(env e, address sarcophagusInstance) returns uint256{
    calldataarg args;
    return sarcophagusInstance.registerArchaeologist(e,args);
}

// // the archeologist total bond is constant if no rewrap happens
rule archeologistBondIsFixedIfNoRewrap(env e) {
    // init new instance of Sarcophagus
    cvlInitNewSarcoToken(e);
    // Add new archeologist
    uint256 archIndex = cvlRegisterNewArcheologist(e, sarcophagus);
    // get the memory address of new archeologist
    address archAddress =  sarcophagus.archaeologistAddresses(archIndex);
    // access the archaeologist profile
    Types.Archaeologist arch = sarcophagus.archaeologists(archAddress);
    // make sure this condition holds
    mathint archTotal = arch.freeBond + arch.cursedBond;

    // boilereplate
    method m;
    calldataarg args;

    // call Sarcophagus methods 
    sarcophagus.m(e,args);
    if(m.selector == sig:rewrapSarcophagus( bytes32 ,uint256 ,uint256,uint256).selector){
        assert true;
    }
  //  assert totalSupplyAfter > totalSupplyBefore => f.selector == sig:mint(address,uint256).selector;

    assert (archTotal == (arch.freeBond + arch.cursedBond));
}

// // /*
// // ┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
// │ Rule: the number of archeologists must increase by one after every call to registerArchaeologist
// └─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
// // */
    
// rule increaseArcheologistCountByOneForEveryCallToRegisterArchaeologist() {
//     address sarcophagus; // constructor is implicit in the Sarcophagus contract
//     calldataarg args;
//     method m;
//     env e;
    
//     uint256 totalArcheologists = sarcophagus.archaeologistCount(e); // expect to be 0
//     sarcophagus.m(e,args);
//     // if selected method has the below signature then the rule must be valid, otherwise is valid by vacuity
//     if(m.selector == sig:registerArchaeologist(bytes, string, address, uint256, uint256, uint256, uint256, uint256).selector) {
//         assert (totalArcheologists + 1 == sarcophagus.archaeologistCount(e));
//     }
//     else {
//         assert true;
//     }
// }