# healthcare-blockchain-system
🏥 Healthcare Blockchain Patient Record System
📌 Project Overview

This project demonstrates a blockchain-based healthcare patient record management system using Python, Solidity, and Web3.py.

It ensures data integrity, immutability, and secure access control for storing and managing sensitive patient medical records.

The system combines:

A custom blockchain (Python) for learning core blockchain concepts
A smart contract (Solidity on Ethereum) for real-world decentralised application
Web3.py integration for off-chain interaction with the blockchain
🎯 Objectives
Secure storage of patient medical records
Prevent data tampering using cryptographic hashing
Implement Proof-of-Work consensus mechanism
Enable role-based access control (RBAC)
Demonstrate blockchain + healthcare integration
Connect Python application with Ethereum testnet
🛠️ Technologies Used
Python 🐍
Solidity 🧾
Web3.py 🔗
Ethereum (Sepolia Testnet)
Infura RPC
SHA-256 Cryptography
Remix IDE
MetaMask Wallet
🧱 System Architecture

The system consists of three main layers:

1. Python Blockchain Layer
Custom blockchain implementation
SHA-256 hashing
Proof-of-Work mining
Longest chain consensus algorithm
2. Smart Contract Layer (Ethereum)
Patient record creation
Provider approval system
Record transfer between providers
Event logging for transparency
3. Web3 Integration Layer
Connects Python with Ethereum network
Reads and writes blockchain data
Executes smart contract functions
🔑 Key Features
🔐 Immutable patient record storage
⛏️ Proof-of-Work mining mechanism
👨‍⚕️ Role-Based Access Control (RBAC)
🔄 Secure transfer of medical records
📡 Ethereum event logging system
🧪 Blockchain integrity validation
⚡ Off-chain + on-chain hybrid architecture
📁 Project Structure
healthcare-blockchain-system/
│
├── python_blockchain/
│   ├── healthcare_chain_practical.py
│   └── test_healthcare_chain_practical.py
│
├── web3_integration/
│   └── python_interact_patient_contract.py
│
├── solidity_contract/
│   └── PatientRecordContract.sol
│
├── images/
│   └── (screenshots of output, remix, deployment)
│
├── report/
│   └── project_report.pdf
│
└── README.md
🚀 How to Run the Project
1. Install dependencies
pip install web3
2. Run blockchain simulation
python healthcare_chain_practical.py
3. Run unit tests
python test_healthcare_chain_practical.py
4. Run Web3 interaction script
python python_interact_patient_contract.py
🧪 Testing

The system includes comprehensive testing:

Python Blockchain Tests
Genesis block creation
Block linkage verification
Proof-of-Work validation
Tamper detection
Consensus mechanism testing
Smart Contract Tests
Provider approval system
Access control validation
Medical file creation
Record transfer verification
Edge case handling
📊 Results & Validation
Successfully implemented tamper detection using SHA-256 hashing
Verified blockchain integrity under multiple test cases
Smart contract deployed and tested on Sepolia testnet
Web3.py successfully retrieved and updated blockchain data
Event logs confirmed via Etherscan
🔐 Security Features
SHA-256 cryptographic hashing
Proof-of-Work mining difficulty control
Role-based access control (RBAC)
Require-based input validation in smart contracts
Immutable blockchain ledger structure
⚠️ Limitations
Not suitable for storing large medical files on-chain
Ethereum gas fees limit scalability
Blockchain immutability conflicts with GDPR “Right to be Forgotten”
Requires hybrid off-chain storage for real-world deployment
📌 Future Improvements
Integration with IPFS for off-chain storage
Implementation of Zero-Knowledge Proofs (ZKP)
Migration to Layer-2 scaling solutions
Frontend DApp development (React/Web3 UI)
👨‍🎓 Learning Outcomes
Blockchain architecture design
Smart contract development using Solidity
Python-based blockchain implementation
Ethereum testnet deployment
Web3 integration for decentralized applications
Cryptographic security principles
📜 Author

Raghava Krishna Anumari
MSc Data Science – York St John University (London Campus)
GitHub: https://github.com/Raghava7328
LinkedIn: https://linkedin.com/in/anumari-raghava-krishna-47aa2a24b
