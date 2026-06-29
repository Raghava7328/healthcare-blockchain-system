from web3 import Web3

# Sepolia RPC URL
RPC_URL = "https://sepolia.infura.io/v3/62eff8cba6824f60a18bd4eb59b2e49c"

# Deployed smart contract address
CONTRACT_ADDRESS = "0xAeddBbe48BC44a003B4fe285D9119d6D1C156587"

# Contract ABI
ABI = [
    {
        "inputs": [],
        "name": "getAdministrator",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "totalRecords",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "uint256", "name": "fileNumber", "type": "uint256"}],
        "name": "viewMedicalFile",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "string", "name": "", "type": "string"},
            {"internalType": "string", "name": "", "type": "string"},
            {"internalType": "string", "name": "", "type": "string"},
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "bool", "name": "", "type": "bool"}
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

# Connect to Sepolia network
web3 = Web3(Web3.HTTPProvider(RPC_URL))

if web3.is_connected():
    print("Connected to Sepolia test network")
else:
    print("Connection failed")
    exit()

# Load deployed contract
contract = web3.eth.contract(
    address=Web3.to_checksum_address(CONTRACT_ADDRESS),
    abi=ABI
)

# Read administrator address
admin = contract.functions.getAdministrator().call()
print("\nContract Administrator:")
print(admin)

# Read total patient records
total_records = contract.functions.totalRecords().call()
print("\nTotal Records:")
print(total_records)

# Read first medical file
record = contract.functions.viewMedicalFile(1).call()

print("\nPatient Medical File:")
print("File Number:", record[0])
print("Patient Code:", record[1])
print("Patient Name:", record[2])
print("Medical Condition:", record[3])
print("Assigned Provider:", record[4])
print("Created Timestamp:", record[5])
print("Active Status:", record[6])