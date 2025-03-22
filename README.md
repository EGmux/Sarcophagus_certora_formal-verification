# formal_verfication_certora(name subject to change)

# how to run you first spec

- provide you certora key in bootstrap.sh
- run the bootstrap script
```bash
chmod +x ./bootstrap.sh
./bootstrap.sh
```
- run the following command inside the container
```bash
certoraRun src/ERC20Fixed.sol --verify ERC20Fixed:specs/ERC20Fixed.spec
```

