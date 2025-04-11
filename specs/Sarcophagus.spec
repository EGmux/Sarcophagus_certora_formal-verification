using SarcophagusHarness as sarcophagus;
using Types as types;
using Keys as keys;
using ACMtoken as acm;

methods {
    function SarcophagusHarness.archaeologistCount() external returns (uint256) envfree;
    function SarcophagusHarness.registerArchaeologist(
        bytes  currentPublicKey,
        string  endpoint,
        address paymentAddress,
        uint256 feePerByte,
        uint256 minimumBounty,
        uint256 minimumDiggingFee,
        uint256 maximumResurrectionTime,
        uint256 freeBond,
        address sarcoToken
    ) external returns (uint256);
   function SarcophagusesHarness.createSarcophagus(
        string memory name,
        address archaeologist,
        uint256 resurrectionTime,
        uint256 storageFee,
        uint256 diggingFee,
        uint256 bounty,
        bytes32 identifier,
        bytes memory recipientPublicKey
    ) external returns (uint256); 
    function SarcophagusHarness.archaeologistAddresses(uint256 index) external returns (address) envfree;
    function SarcophagusHarness.archaeologists(address account) external returns (Types.Archaeologist) envfree;
    function Keys.selectPublicKey(uint8 num) external returns (bytes) envfree;
    function Keys.selectAddress(uint8 num) external returns (address) envfree;
    function Keys.selectPrivateKey(uint8 num) external returns (bytes32) envfree;
    function SarcophagusHarness.unwrapSarcophagus(bytes32 identifier, bytes32 privateKey) external returns (bool);
    function SarcophagusHarness.sarcophagus(bytes32 identifier) external returns (Types.Sarcophagus) envfree;
    function SarcophagusesHarness.cancelSarcophagus(bytes32 identifier) external returns bool;
    function SarcophagusesHarness.rewrapSarcophagus(
        bytes32 identifier,
        uint256 resurrectionTime,
        uint256 diggingFee,
        uint256 bounty) external returns bool;
    function ACMtoken.balanceOfACM(address account) external returns (uint256);
    
}


function cvlRegisterNewArcheologist(env e, bytes publicKey, string endpoint, address paymentAddress) returns uint256{
    uint256 feePerByte;
    uint256 minimumBounty;
    uint256 minimumDiggingFee;
    uint256 maximumResurrectionTime;
    uint256 freeBond;
    require(feePerByte > 0);
    require(minimumBounty > 0);
    require(minimumDiggingFee > 0);
    require(maximumResurrectionTime > 0);
    require(freeBond > 0);
    return sarcophagus.registerArchaeologist(e,publicKey,endpoint,paymentAddress,feePerByte,minimumBounty,minimumDiggingFee,maximumResurrectionTime,freeBond);
}

function cvlCreateNewSarcophagus(env e,address archaeologist, bytes32 id, bytes pubKey) returns uint256{
        string name;
        require(name == "SE_EU_ACREDITO_ACONTECE");
        uint256 resurrectionTime;
        uint256 storageFee;
        uint256 diggingFee;
        uint256 bounty;
        return sarcophagus.createSarcophagus(e,name, archaeologist, resurrectionTime, storageFee, diggingFee, bounty, id, pubKey);
}


function cvlUnwrapSarcophagus(env e, bytes32 identifier, bytes32 privateKey) returns bool{
        return sarcophagus.unwrapSarcophagus(e,identifier, privateKey);
}


function cvlCancelSarcophagus(env e, bytes32 identifier, address embalmer) returns bool{
        require(e.msg.sender == embalmer);
        return sarcophagus.cancelSarcophagus(e,identifier);
}

function cvlRewrapSarcophagus(env e, bytes32 id, address embalmer ) returns bool
{
    require(e.msg.sender == embalmer);
    uint256 resurrectionTime;
    uint256 diggingFee;
    uint256 bounty;
    return sarcophagus.rewrapSarcophagus(e, id, resurrectionTime, diggingFee, bounty);
    
}

ghost  storeArchsCount() returns uint256 {
    init_state axiom storeArchsCount() == 0;
}


hook CALL(uint g, address addr, uint value, uint argOffs, uint argLength, uint retOffset, uint retLength) uint rc {
    if(selector == sig:sarcophagus.registerArchaeologist(bytes, string, address, uint256, uint256, uint256, uint256,uint256).selector){
        havoc storeArchsCount assuming
            storeArchsCount@new() == storeArchsCount@old() + 1;
    }
}



// // the archeologist total bond is constant if no rewrap happens
rule archeologistBondIsFixedIfNoRewrap(env e) {

    // Add new archeologist
    bytes publicKey;
    string endpoint;
    address paymentAddress;

    require(publicKey == keys.selectPublicKey(0));
    require(endpoint == "ACM_NAO_NOS_REPROVE.com");
    require(paymentAddress == keys.selectAddress(0));
    uint256 index = cvlRegisterNewArcheologist(e,publicKey,endpoint,paymentAddress);

    assert storeArchsCount() == to_mathint(sarcophagus.archaeologistCount());
}

rule sarcophagusWasUnwrapedAsExpected(env e) {
    
    bytes publicKey;
    string endpoint;
    address paymentAddress;
    bytes32 privateKey;
    bytes32 id;
    
    require(publicKey == keys.selectPublicKey(0));
    require(privateKey == keys.selectPrivateKey(0));
    require(endpoint == "ACM_NAO_NOS_REPROVE.com");
    require(paymentAddress == keys.selectAddress(0));

    cvlRegisterNewArcheologist(e,publicKey,endpoint,paymentAddress);
    cvlCreateNewSarcophagus(e,paymentAddress, id, publicKey);
    bool didUnwrap = cvlUnwrapSarcophagus(e,id,privateKey);
    Types.Sarcophagus sarc = sarcophagus.sarcophagus(id); 
    
    assert (sarc.state == Types.SarcophagusStates.Done) <=> didUnwrap;
}



rule afterArewrapingTheArcheologistsReceiveDiggingFees(env e){
    bytes publicKey;
    string endpoint;
    address paymentAddress;
    bytes32 privateKey;
    bytes32 id;
    
    require(publicKey == keys.selectPublicKey(0));
    require(privateKey == keys.selectPrivateKey(0));
    require(endpoint == "ACM_NAO_NOS_REPROVE.com");
    require(paymentAddress == keys.selectAddress(0));
    cvlRegisterNewArcheologist(e,publicKey,endpoint,paymentAddress);
    cvlCreateNewSarcophagus(e,paymentAddress, id, publicKey);
    Types.Sarcophagus sarc = sarcophagus.sarcophagus(id); 

    Types.SarcophagusStates beforeState = sarc.state; // expect to be exists
    // assert beforeState == Types.SarcophagusHarness.Exists;
    
    address embalmer = sarc.embalmer;
    bool didRewrap = cvlRewrapSarcophagus(e,id, embalmer);
    
    //TODO: raafm, need to check if digging fees have been sent
    Types.SarcophagusStates afterState = sarc.state;
    uint256 money = sarcophagus.sarcoToken.balanceOfACM(e,paymentAddress);
    assert afterState == beforeState;
}