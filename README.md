# Sarcophagus Formal Verification

## 🤔 What is Formal Verification and Certora?

Formal verification is the act of proving or disproving hypotheses about a system by verifying the correctness of a set of properties.

Certora is one of the available tools in the blockchain ecosystem capable of formal verification. The tool has two main concepts for defining such hypotheses: the first being a **rule**, and the second an **invariant**. A rule is any set of properties that must hold under specific conditions during runtime, while invariants must hold throughout the entire runtime.

Certora uses CVL (Certora Verification Language) as a DSL to describe rules and invariants. Valid CVL files require the `.spec` file extension to be recognized by the Certora compiler. Additionally, one can provide a `.conf` file to avoid passing command-line flags to the CLI tool provided by Certora to verify a `.spec` file.

## ⚰️ What is [Sarcophagus](https://github.com/sarcophagus-org/sarcophagus-contracts)?

Sarcophagus is a decentralized, cryptographically secure digital dead man’s switch that releases sensitive data (a secret) only if a user fails to check in within a predetermined timeframe. It allows individuals to manage the secure transfer of digital secrets — such as a private key to a crypto wallet, a master password, or even a password manager database — under their own terms, without relying on centralized intermediaries. By giving users full control over how and when information is shared, Sarcophagus offers a reliable and autonomous solution for safeguarding critical data in an increasingly digital world.

The project combines cutting-edge decentralized technologies to ensure security, permanence, and autonomy. Ethereum powers the smart contracts that govern the logic of the switch, while Arweave provides immutable, permanent file storage. This integration enables Sarcophagus to function as a trustless, censorship-resistant platform for managing sensitive information across a variety of use cases.  
**Some of the initial use cases for Sarcophagus include:**

- Data-at-rest Security/Continuity  
- Crypto Key Management  
- Will and Trust  
- Emergency Communications  
- Political Activism & Journalism  
- Password & Credential Recovery  
- Time Capsule

## 🧰 Sarcophagus Architecture

The application has two users: the creator (the **embalmer**) and the recipient of a secret.

### Create a Sarcophagus

#### The user provides the following inputs:

- **Payload**  
  The file (of any type) containing the secret to be released if the switch is triggered.

- **Recipient Public Key**  
  The public key of the designated recipient; only the holder of the corresponding private key can access the Payload.  
  - Optionally, users can generate a new Ethereum keypair and download a shareable PDF wallet.  
  - To make the Payload public upon release, the private key can be published.

- **Resurrection Time**  
  A specific future date/time when the Payload will be released if the user fails to attest.  
  - This can be updated by the user at any time before the switch is triggered.

- **Nodes Info**  
  Information related to the nodes (**archaeologists**) employed to safeguard the secret.

- **Payments**  
  - **ETH** to cover Arweave file storage costs.  
  - **$SARCO (ERC-20 token)** to pay node operators (archaeologists) for their service.

Both the user (**embalmer**) and the node (**archaeologist**) deposit $SARCO tokens into a contract for the duration of the switch. If the node behaves maliciously, its tokens are slashed and returned to the user. This staking mechanism incentivizes nodes to remain active and follow the protocol rules.

### Attestation (Rewrapping)

After creating a sarcophagus, the user must periodically **attest to the contract** before the resurrection time to prove continued control — essentially a "proof of life." This is done through a simple crypto transaction that resets the resurrection date. During attestation, the user must provide a new resurrection time and pay a fresh round of $SARCO tokens to the nodes for the upcoming period.

Once the user attests, the previously bonded $SARCO tokens are released to the nodes as payment (**digging fee**). A node might need to stake again if during the ongoing period it decides on an increase in payment, conversely it can receive a fraction of staked tokens if it decides to reduce the fees. This cycle repeats indefinitely until the user either fails to attest (triggering the payload release) or manually ends the contract.

### Burying the Sarcophagus

If a user decides to stop using the application without triggering the payload release, they can choose to **bury** the sarcophagus. This action ends the contract, pays the nodes for their service, and releases the locked $SARCO bond tokens back to the nodes. Although the encrypted payload remains permanently stored on Arweave, the nodes stop monitoring the contract, and all associated decryption keys are purged from their systems.

### Resurrection

If the user fails to attest by the designated resurrection time, the nodes will publish their portion of the release key to the blockchain. This allows the designated recipient to download and decrypt the encrypted payload from Arweave. No additional fees or transactions are required for the recipient to access the file. Once the release keys are published, the nodes' responsibilities are fulfilled — they receive their payment from the contract, and their bonded $SARCO tokens are returned to their wallets.

## 🔍 What Has Been Verified?

- If the sarcophagus has been unwrapped, ensure its internal state is not that of a wrapped sarcophagus.  
  **Note**: A wrapped sarcophagus has the `EXISTS` state, an unwrapped one has the `DONE` state.

- If the sarcophagus has been rewrapped, ensure the archaeologist receives their due payment in digging fees.  
  **Note**: A rewrap should only happen if the user decides to extend their timer.

- If someone accuses an archaeologist of opening the sarcophagus early, ensure the accuser receives half of the locked bond and the embalmer receives the other half, as well as the digging fee and bounty.  
  **Note**: We assumed the embalmer could be a valid accuser.

- If the sarcophagus has been unwrapped, ensure the archaeologists receive their due payment in digging fees and bounty.

- If the sarcophagus has been created but is canceled by the embalmer, the archaeologist should still receive digging fees.

- If the sarcophagus is unwrapped once, ensure that if archaeologists try to unwrap it again, it reverts.  
  **Note**: This avoids double-spending — after being unwrapped, they receive digging fees and bounty.

## 📎 Overall Experience

We had to apply the following workarounds while using the tool:

- We had to call `balanceOf` provided in OpenZeppelin's library, but this function is already an override.  
  **Solution**: Create a contract that inherits the `ERC20` superclass and implement a function that internally calls the `balanceOf` function provided by the OpenZeppelin implementation.

- Although the tool is capable of generating a valid triple (public key, private key, address), we opted to use hardcoded values for performance reasons.


## 🐋 How to run the spec file

install docker

[guide on installing docker](https://docs.docker.com/engine/install/)

- docker requires the user in the docker group if running as non root

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```
- logout and login again or reboot the system
- provide you certora key in bootstrap.sh
- run the bootstrap script
```bash
chmod +x ./bootstrap.sh
./bootstrap.sh
```
- run the following command inside the container
```bash
certoraRun /certora/conf/sarcophagus.conf --optimistic_hashing
```
