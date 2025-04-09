
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "../src/@openzeppelin/contracts-upgradeable/proxy/utils/Initializable.sol";
import "../src/@openzeppelin/contracts/token/ERC20/IERC20.sol";

import "../src/contracts/libraries/Events.sol";
import "../src/contracts/libraries/Types.sol";
import "./DatasHarness.sol"; 
import "./ArchaeologistsHarness.sol";
import "./SarcophagusHarness.sol";


function FindArch(address target, Datas.Data data) returns (int){
    uint archLength = data.archaeologists.length;
    Datas.Arch archs = data.archaeologist;
    for(uint index=0; index < archLength; ++index ){
        if(archs[index].embalmerAddress == target){
            return index;
        }
    }
    return -1;
}


function FindEmbalmer(address target, Datas.Data data) returns (int){
    uint embalmersLength = data.embalmers.length;
    Datas.Embalmer embalmers = data.embalmers;
    for(uint index=0; index < embalmersLength; ++index ){
        if(embalmers[index].embalmerAddress == target){
            return index;
        }
    }
    return -1;
}

function FindRecipient(address target, Datas.Data data) returns (int){
    uint recipientLength = data.recipients.length;
    Datas.Recipient recipients = data.recipients;
    for(uint index=0; index < recipientLength; ++index ){
        if(recipients[index].recipientAddress == target){
            return index;
        }
    }
    return -1;
}


function FindSarcophagus(bytes32 target, Datas.Data data) returns (int){
    uint sarcophagusLength = data.sarcophaguses.length;
    Datas.Sarcophagus sarcophaguses = data.sarcophaguses;
    for(uint index=0; index < sarcophagusLength; ++index ){
        if(sarcophaguses[index].sarcophagusIdentifier == target){
            return index;
        }
    }
    return -1;
}


function FindKeys(bytes32 target, Datas.Data data) returns (int){
    uint keysLength = data.keys.length;
    Datas.Keys keys = data.usedKeys;
    for(uint index=0; index < keysLength; ++index ){
        if(keys[index].keyidentifier == target){
            return index;
        }
    }
    return -1;
}
