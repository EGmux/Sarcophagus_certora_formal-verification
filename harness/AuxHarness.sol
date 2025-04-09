
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "../src/@openzeppelin/contracts-upgradeable/proxy/utils/Initializable.sol";
import "../src/@openzeppelin/contracts/token/ERC20/IERC20.sol";

import "../src/contracts/libraries/Events.sol";
import "../src/contracts/libraries/Types.sol";
import "./DatasHarness.sol"; 
import "./ArchaeologistsHarness.sol";
import "./SarcophagusHarness.sol";


function FindArch(address target, Datas.Data storage data) returns (uint256){
    uint archLength = data.archaeologists.length;
    Datas.Arch[] storage archs = data.archaeologists;
    for(uint index=0; index < archLength; ++index ){
        if(archs[index].archaeologistAddress == target){
            return index;
        }
    }
    return type(uint256).max;
}


function FindEmbalmer(address target, Datas.Data storage data) returns (uint256){
    uint embalmersLength = data.embalmers.length;
    Datas.Embalmer[] storage embalmers = data.embalmers;
    for(uint index=0; index < embalmersLength; ++index ){
        if(embalmers[index].embalmerAddress == target){
            return index;
        }
    }
    return type(uint256).max;
}

function FindRecipient(address target, Datas.Data storage data) returns (uint256){
    uint recipientLength = data.recipients.length;
    Datas.Recipient[] storage recipients = data.recipients;
    for(uint index=0; index < recipientLength; ++index ){
        if(recipients[index].recipientAddress == target){
            return index;
        }
    }
    return type(uint256).max;
}


function FindSarcophagus(bytes32 target, Datas.Data storage data) returns (uint256){
    uint256 sarcophagusLength = data.sarcophaguses.length;
    Datas.Sarcophagus[] storage sarcophaguses = data.sarcophaguses;
    for(uint index=0; index < sarcophagusLength; ++index ){
        if(sarcophaguses[index].sarcophagusIdentifier == target){
            return index;
        }
    }
    return type(uint256).max;
}


function FindKeys(bytes storage target, Datas.Data storage data) returns (uint256){   
    uint256 keysLength = data.usedKeys.length;
    Datas.Keys[] storage keys = data.usedKeys;
    for(uint256 index=0; index < keysLength; ++index ){
        if(keccak256(keys[index].keyidentifier) == keccak256(target)){
            return index;
        }
    }
    return  type(uint256).max;
}
