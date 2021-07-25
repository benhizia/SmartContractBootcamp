from brownie import ERC20Basic, config, accounts, network
 
def main():
    account = accounts.add(config["wallets"]["from_key"])
    myERC20Contract = ERC20Basic[-1] #-1 means most rescent deployment of the contract 
    #tx = myERC20Contract.setNumber(123456,{'from': account})
    #tx.wait(1)
    input = 55
    print("totalSupply is =", myERC20Contract.totalSupply())
    print(f"MyBalance = ", myERC20Contract.balanceOf("0xF36f1b90E30eae99763b1630cAd13C88B7738c0F"))
    myERC20Contract.transferFrom(from="0xce83E9cAD9CF6720f7E7f4E17b0cfdBf4b6D6701", to="0xF36f1b90E30eae99763b1630cAd13C88B7738c0F", 55)
    print(f"MyBalance after transfer = ", myERC20Contract.balanceOf("0xF36f1b90E30eae99763b1630cAd13C88B7738c0F"))
    print("totalSupply after transfer is =", myERC20Contract.totalSupply())
    



