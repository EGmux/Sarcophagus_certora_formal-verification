pragma solidity ^0.8.0;

import "../../src/@openzeppelin/contracts-upgradeable/proxy/utils/Initializable.sol";
import "../../src/@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "../../src/@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract ERC20token is ERC20{
    string tokenName = "ERC20token";
    string tokenSymbol = "ERC20";
    constructor() ERC20(tokenName,tokenSymbol){
    }

    function balanceOfERC20(address account) public view returns (uint256)  {
        return ERC20.balanceOf(account);
    }
    
}