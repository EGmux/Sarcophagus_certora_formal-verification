using SarcophagusHarness as sarcophagus;
using Types as types;
using Keys as keys;


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
    function SarcophagusesHarness.rewrapSarcophagus(
        // Datas.Data storage data,
        bytes32 identifier,
        uint256 resurrectionTime,
        uint256 diggingFee,
        uint256 bounty
        // IERC20 sarcoToken // adapt this 
    ) external returns (bool);
    function SarcophagusHarness.initialize(address _sarcoToken) external;
    function SarcophagusHarness.archaeologistAddresses(uint256 index) external returns (address) envfree;
    function SarcophagusHarness.archaeologists(address account) external returns (Types.Archaeologist) envfree;
    function Keys.selectPublicKey(uint8 num) external returns (bytes) envfree;
    function Keys.selectAddress(uint8 num) external returns (address) envfree;
    function Keys.selectPrivateKey(uint8 num) external returns (bytes32) envfree;
    function SarcophagusesHarness.accuseArchaeologist(Datas.Data storage data,
        bytes32 ,
        bytes,
        address,
        IERC20 )
    ) public returns (bool);
    function sarcoToken.balanceof(addres) external returns (bytes32) envfree;

}

// o embalmer recebe tudo se, e somente se, ele for o caller fo accuseArchaeologist
rule accuseArchaeologistGivesAlltoCaller( Datas.Data storage data,
                                            bytes32 identifier,
                                            bytes memory singleHash,
                                            address paymentAddress,
                                            IERC20 sarcoToken){
    
    uint256 balance_old = sarcoToken.balanceof(sarc.embalmer);
    accuseArchaeologist(data, identifier,singleHash,paymentAddress,sarcoToken)
    uint256 balance_new  = sarcoToken.balanceof(sarc.embalmer);

    sarc.embalmer == paymentAddress <=> balance_new - balance_old == sarc.cursedBond + sarc.diggingFee + sarc.bounty
}

rule 