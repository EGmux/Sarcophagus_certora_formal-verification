## THe following Functions are found at:  https://github.com/sarcophagus-org/sarcophagus-contracts/blob/develop/contracts/libraries/Sarcophaguses.sol

### splitSend

* value increase in address sarc.embalmer >= value increase in paymentAddress
* o retorno da função é uma tupla de 2 uint que devem se o mesmo numero
* cursedbon should go to zero (I could not find a function to get the archeologist cursed bond, so this 2 lines should do it:
  ```
  Types.Archaeologist storage arch = data.archaeologists[archAddress];
  arch.cursedBond //here is the value
    ```

### createSarcophagus
* the sum of the value in msg.sender + diggingFee + bounty + storageFee is a constant
```
        sarcoToken.transferFrom(
            msg.sender,
            address(this),
            diggingFee + bounty + storageFee
        );

```
* the archeologist free bond decreases:     arch.freeBond before <  arch.freeBond after
```
    Types.Archaeologist storage arch = data.archaeologists[archAddress];
    );
    arch.freeBond;
```

* the archeologist freeBond + cursedBond is a constant
