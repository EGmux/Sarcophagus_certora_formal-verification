pragma solidity 0.8 0;

import "../src/contracts/Sarcophagus.sol";

function loop(Sarcophagus sarc,uint256 n,bytes memory publicKey, string memory endpoint, address paymentAddress, uint256 feePerByte, uint256 minimumBounty, uint256 minimumDiggingFee, uint256 maximumRessurectionTime, uint256 freeBond) returns (bool){
    for(uint256 i=0; i < n ; i++){
        sarc.updateArchaeologist(endpoint,publicKey,paymentAddress,feePerByte,minimumBounty,minimumDiggingFee,maximumRessurectionTime, freeBond);
    }
    return true;
}
