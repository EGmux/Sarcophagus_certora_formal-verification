using SarcophagusHarness as sarcophagus;
using Types as types;
using Keys as keys;
using ACMtoken as acm;
using Loop as loop;

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
    function accuseArchaeologist(
        bytes32 identifier,
        bytes memory singleHash,
        address paymentAddress
    ) external returns (bool);
    function updateArchaeologist(
        bytes memory newPublicKey,
        string memory endpoint,
        address paymentAddress,
        uint256 feePerByte,
        uint256 minimumBounty,
        uint256 minimumDiggingFee,
        uint256 maximumResurrectionTime,
        uint256 freeBond
    ) external returns (bool); 
    function loop(
        Sarcophagus calldata sarc,
        uint256 n,bytes memory publicKey, 
        string memory endpoint,
         address paymentAddress, 
         uint256 feePerByte, 
         uint256 minimumBounty,
          uint256 minimumDiggingFee,
           uint256 maximumRessurectionTime) external returns (bool);
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

function cvlRegisterNewPoorArcheologist(env e, bytes publicKey, string endpoint, address paymentAddress) returns uint256{
    uint256 feePerByte;
    uint256 minimumBounty;
    uint256 minimumDiggingFee;
    uint256 maximumResurrectionTime;
    uint256 freeBond;
    require(feePerByte == 1);
    require(minimumBounty == 1);
    require(minimumDiggingFee == 1);
    require(maximumResurrectionTime > 0);
    require(freeBond == 3);
    return sarcophagus.registerArchaeologist(e,publicKey,endpoint,paymentAddress,feePerByte,minimumBounty,minimumDiggingFee,maximumResurrectionTime,freeBond);
}

function cvlUpdateArchaeologist(bytes publicKey, string endopoint, address paymentAddress, uint256 feePerByte, uint256 minimumBounty, uint256 minimumDiggingFee, uint256 maximumRessurectionTime, uint256 freeBond){
    loop.loop(sarcophagus,publicKey, endpoint, paymentAddress, feePerByte, minimumBounty, minimumDiggingFee, maximumResurrectionTime,freeBond);    
}



function cvlCreateNewCheapSarcophagus(env e,address archaeologist, bytes32 id, bytes pubKey) returns uint256{
        string name;
        require(name == "SE_EU_ACREDITO_ACONTECE");
        uint256 resurrectionTime;
        uint256 storageFee;
        uint256 diggingFee;
        uint256 bounty;
        require(diggingFee == 1);
        require(bounty == 1);
        require(storageFee == 1);
        return sarcophagus.createSarcophagus(e,name, archaeologist, resurrectionTime, storageFee, diggingFee, bounty, id, pubKey);
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

function cvlAccuseArcheologist(env e, bytes32 id,address accuserAddress) returns bool{
    bytes singleHash;
   
    require(keccak256(id) == keccak256(keccak256(singleHash)));
    return sarcophagus.accuseArchaeologist(e,id,singleHash,accuserAddress);
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
    assert sarc.state == Types.SarcophagusStates.Exists;
    // assert beforeState == Types.SarcophagusHarness.Exists;
    
    address embalmer = sarc.embalmer;
    uint256 balance_old = sarcophagus.sarcoToken.balanceOfACM(e,sarc.embalmer);
    bool didRewrap = cvlRewrapSarcophagus(e,id, embalmer);
    
    uint256 balance_new  = sarcophagus.sarcoToken.balanceOfACM(e,sarc.embalmer);
    Types.SarcophagusStates afterState = sarc.state;

    assert afterState == beforeState;
    assert sarc.embalmer == paymentAddress <=> balance_new - balance_old == sarc.currentCursedBond + sarc.diggingFee + sarc.bounty;
}

// the embalmer gets all (cursedBond, diggingFe) <=> d
rule accuseArchaeologistGivesAlltoCaller(env e){
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
    assert sarc.state == Types.SarcophagusStates.Exists;
    uint256 balance_old = sarcophagus.sarcoToken.balanceOfACM(e,sarc.embalmer);
    cvlAccuseArcheologist(e,id, paymentAddress);
    uint256 balance_new  = sarcophagus.sarcoToken.balanceOfACM(e,sarc.embalmer);

    assert sarc.embalmer == paymentAddress <=> balance_new - balance_old == sarc.currentCursedBond + sarc.diggingFee + sarc.bounty;
}

// tokens are give to archaeologist
rule unwrapSarcophagusGivesTokensToArchaeologist(env e){
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

    mathint balance_old = to_mathint(sarcophagus.sarcoToken.balanceOfACM(e,sarc.embalmer));
    bool didUnwrap = cvlUnwrapSarcophagus(e,id,privateKey);

    mathint balance_new = to_mathint(sarcophagus.sarcoToken.balanceOfACM(e,sarc.embalmer));

    assert sarc.state == Types.SarcophagusStates.Exists;

    mathint delta = to_mathint(sarc.diggingFee) + to_mathint(sarc.bounty);
    
    assert balance_new - balance_old == delta <=> didUnwrap;
    }


rule createdSarcophagusAfterCancelReturnsthevalueofDiggingFeeButNotBountyToArchaeologist(env e){
    bytes publicKey;
    string endpoint;
    address paymentAddress;
    bytes32 privateKey;
    bytes32 id;
    
    require(publicKey == keys.selectPublicKey(0));
    require(privateKey == keys.selectPrivateKey(0));
    require(endpoint == "ACM_NAO_NOS_REPROVE.com");
    require(paymentAddress == keys.selectAddress(0));

    uint256 index = cvlRegisterNewArcheologist(e,publicKey,endpoint,paymentAddress);
    uint256 sarc_index= cvlCreateNewSarcophagus(e,paymentAddress, id, publicKey);
    Types.Sarcophagus sarc = sarcophagus.sarcophagus(id); 

    address embalmer = sarc.embalmer;
    uint256 balance_old = sarcophagus.sarcoToken.balanceOfACM(e,paymentAddress);
    bool didCancel = cvlCancelSarcophagus(e, id, embalmer);
    
    uint256 balance_new = sarcophagus.sarcoToken.balanceOfACM(e,paymentAddress);
    
    assert (balance_new == balance_old + sarc.diggingFee) <=> didCancel;
}


// trying to Unwrap twice reverts the secondf one
rule unwrapSarcophagusAvoidDoubleSpend(env e){
    
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

    mathint balance_old = to_mathint(sarcophagus.sarcoToken.balanceOfACM(e,sarc.embalmer));
    bool didUnwrap1 = sarcophagus.unwrapSarcophagus@norevert(e,id, privateKey);
    bool didUnwrap2 = sarcophagus.unwrapSarcophagus@withrevert(e,id, privateKey);
    
    assert didUnwrap1 && !didUnwrap2;
    Types.Archaeologist arch = sarcophagus.archaeologists(id);
    
}

//archeologist cant update and then get a new sarcophagus with no freebond left.
rule ArchaeologistIsNotBankerNoFractionalReserve(env e){
    bytes publicKey;
    string endpoint;
    address paymentAddress;
    bytes32 privateKey;
    bytes32 id;
    bytes32 id2;
    uint256 feePerByte;
    uint256 minimumBounty;
    uint256 minimumDiggingFee;
    uint256 maximumResurrectionTime;

    require(publicKey == keys.selectPublicKey(0));
    require(privateKey == keys.selectPrivateKey(0));
    require(endpoint == "ACM_NAO_NOS_REPROVE.com");
    require(paymentAddress == keys.selectAddress(0));
    cvlRegisterNewPoorArcheologist(e,publicKey,endpoint,paymentAddress);
    cvlCreateNewCheapSarcophagus(e,paymentAddress, id, publicKey);
    Types.Archaeologist arch= sarcophagus.archaeologists(id);
    cvlUpdateArchaeologist(e,publicKey,endpoint,paymentAddress,feePerByte,minimumBounty,minimumDiggingFee,maximumResurrectionTime);
        
    sarcophagus.createSarcophagus@withrevert(e,name, archaeologist, resurrectionTime, storageFee, diggingFee, bounty, id2, pubKey);
    assert true;
}


rule IdempotencyOfUpdateArchaeologist(env e) {
    bytes publicKey;
    string endpoint;
    address paymentAddress;
    bytes32 privateKey;
    bytes32 id;
    uint256 n;
    address id_arch;
    uint256 feePerByte;
    uint256 minimumBounty;
    uint256 minimumDiggingFee;
    uint256 maximumResurrectionTime;
    uint256 freeBond;


    require(publicKey == keys.selectPublicKey(0));
    require(privateKey == keys.selectPrivateKey(0));
    require(endpoint == "ACM_NAO_NOS_REPROVE.com");
    require(paymentAddress == keys.selectAddress(0));
    require(id_arch == e.msg.sender);
    cvlRegisterNewArcheologist(e,publicKey,endpoint,paymentAddress);
    cvlCreateNewSarcophagus(e,paymentAddress, id, publicKey);
    sarcophagus.updateArchaeologist(e,publicKey,endpoint,paymentAddress,feePerByte,minimumBounty,minimumDiggingFee,maximumResurrectionTime,freeBond);
    Types.Archaeologist arch1= sarcophagus.archaeologists(id);
    cvlUpdateArchaeologist(e,sarcophagus,publicKey,endpoint,paymentAddress,feePerByte,minimumBounty,minimumDiggingFee,maximumResurrectionTime,freeBond);
    Types.Archaeologist arch2 = sarcophagus.archaeologists(id);
    //verify if sarch changed
    if (arch1 != arch2){
        assert false;
    }
    assert true;
}

