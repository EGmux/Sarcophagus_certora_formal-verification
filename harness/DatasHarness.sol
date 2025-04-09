
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "../src/contracts/libraries/Types.sol";

/**
 * @title A library implementing data structures for the Sarcophagus system
 * @notice This library defines a Data struct, which defines all of the state
 * that the Sarcophagus system needs to operate. It's expected that a single
 * instance of this state will exist.
 */
library Datas {
    // struct Data {
    //     // archaeologists
    //     address[] archaeologistAddresses;
    //     mapping(address => Types.Archaeologist) archaeologists;
    //     // archaeologist stats
    //     mapping(address => bytes32[]) archaeologistSuccesses;
    //     mapping(address => bytes32[]) archaeologistCancels;
    //     mapping(address => bytes32[]) archaeologistAccusals;
    //     mapping(address => bytes32[]) archaeologistCleanups;
    //     // archaeologist key control
    //     mapping(bytes => bool) archaeologistUsedKeys;
    //     // sarcophaguses
    //     bytes32[] sarcophagusIdentifiers;
    //     mapping(bytes32 => Types.Sarcophagus) sarcophaguses;
    //     // sarcophagus ownerships
    //     mapping(address => bytes32[]) embalmerSarcophaguses;
    //     mapping(address => bytes32[]) archaeologistSarcophaguses;
    //     mapping(address => bytes32[]) recipientSarcophaguses;
    // }
    
    struct Data {
        Arch[] archaeologists;
        Sarcophagus[] sarcophaguses;
        Recipient[] recipients;
        Embalmer[] embalmers;
        Keys[] usedKeys;
    }
    
    struct Arch {
        address archaeologistAddress;
        Types.Archaeologist archaeologist;
        bytes32[] archaeologistSuccess;
        bytes32[] archaeologistCancel;
        bytes32[] archaeologistAccusal;
        bytes32[] archaeologistCleanup;
        bytes32[] archaeologistSarcophaguses;
    }
    
    struct Keys {
        bytes keyidentifier;
        bool archaeologistUsedKey;
    }
    
    struct Sarcophagus {
        bytes32 sarcophagusIdentifier;
        Types.Sarcophagus sarcophagus;
    }
    
    struct Embalmer {
        address embalmerAddress;
        bytes32[] embalmerSarcophaguses;
    }
    
    struct Recipient{
        address recipientAddress;        
        bytes32[] recipientSarcophaguses;
    }
}

