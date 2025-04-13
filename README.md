# Sarcophagus formal verification

## 🤔 What is formal verification and Certora?

Formal verification is the act of proving or disproving hypothesis about a system by verifying
the validity of a set of properties.

Certora is one of the available tools in the blockchain ecosystem capable of formal
verification. The tool has two main concepts for defining such hypothesis the first being a rule
and the second an invariant. A rule is any set of properties that must hold under specific
conditions during runtime while invariants must hold during the whole runtime.

Certora uses the CVL(certora verification language) as an DSL to describe rules and invariants.
A valid CVL files require the .spec file extension to be recognized by the Certora compiler,
also one could provide a .conf file to avoid passing command line flags to the cli tool
provided by certora to verify a .spec file.

## ⚰️ What is sarcophagus?

The Sarcophagus smart contract allows blockchain users to leave a digital heritage to
someone they trust after misfortune happens. To better understand the sociopolitical impact
of such contract consider the following scenario: you are a political activist and your life could
be threatened at any moment.

Due to your situation you also posses highly sensitive documents that could change the
current ruling party in your country, if you were to be killed, arrested or disappeared
someone else must have access to such documents to continue fighting for the cause, what
you need is a dead man switch.(paragraph subject to change)

Sarcophagus is a digital dead man switch that provides security, reliability, efficiency and
privacy and can be deployed in the ethereum network.

## 🧰 Sarcophagus Architecture

The smart contract has the following entities: archaeologist, embalmer, user, recipient, sarco
token and sarcophagus. An user receives the recipient public key and encrypt a digital secret,
select from a set of archaeologists and provide a timer. Each chosen archaeologist is
provided a share of the whole secret and encrypt such share with his/her private key after the
second encryption the shares are sent to an embalmer that stores then until the timer expires
and if so the archaeologists have the right to retrieve their shares and assemble the secret
that can only be unencrypted by the recipient private key or the user can increase the timer
attesting to the fact that his/her is alive.(require proof reading)

If the timer is increased each archaeologist receives digging fees in sarco tokens and if
unwrapped digging fees and a bounty, each archaeologist can select their minimum
acceptance value for each of these payments.(require proof reading)

For a node to work as an archaeologist is required an upfront investment called bonds in
sarco tokens. This system forces a node to only supervise a set of sarcophagus if and only if
his/her has enough bonds available, bonds can increase by unwrapping or if the embalmer
cancel's the sarcophagus creation and decrease by creating a sarcophagus or being accused
of opening early a sarcophagus, before the timer expires.(require proof reading)

## 🔍 What has been verified?

If the sarcophagus has been unwraped make sure his internal state is not of a wrapped
sarcophagus. obs: a wrapped sarcophagus has EXISTS state an unwrapped one has
DONE state.

If the sarcophagus has been rewrapped make sure thhe archaeologist receives his due
payment in digging fees obs: a rewrap should only happen if the user decides to extend
his/hers timer.

If someone accuses one of the archaeologists from opening earlier the corresponding
sarcophagus make sure this person receives half of the locked bond and the embalmer
receives the other half as well as the digging fee and bounty. obs: we assumed the
embalmer could be a valid accuser.

If the sarcophagus has been unwraped make sure the archaeologists receive their due
payment in digging fees and bounty

If the sarcophagus has been created but the embalmer cancels it the archaeologist
should receive digging fees.

If the sarcophagus is unwrapped once make sure if the archaeologists try to unwrap it
agains revert. obs: avoid the double spending, remember after being unwrapped they
receive digging fees and bounty.

## 📎 Overall experience

We had to apply the following workarounds while using the tool

We had to call the balanceof function provided in OpenZeppelin's library, but this function is
already an override. The solution: create a contract that inherits the ERC20 superclass and
implement a function that inside it's body calls the balanceof function provided in ERC20
implementation provided by OpenZepellin.

This tool won't support for or while loops, so to verify if a rule preserved idempotency we
had to create auxiliary files, note that this rule is current wip.

The tool seems to be capable of generating a valid pair of triples (public key, private key,
address) however we opted for hardcoded value for performance reasons.

## 🐋 How to run the spec file

install docker

guide on installing docker

https://docs.docker.com/engine/install/

docker requires the user in the docker group if running as non root

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```
# how to run the spec

- install docker

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
certoraRun /project/conf/sarcophagus.conf --optimistic_hashing
```
