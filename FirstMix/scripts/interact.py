from brownie import MyFirstContract, config, accounts, network
 
def main():
    account = accounts.add(config["wallets"]["from_key"])
    myFirstContract = MyFirstContract[-1] #-1 means most rescent deployment of the contract 
    tx = myFirstContract.setNumber(123456,{'from': account})
    tx.wait(1)
    input = 55
    print("Number is", myFirstContract.getNumber())
    print(f"Number Summed with {input} =", myFirstContract.getNumberSum(input))
    
