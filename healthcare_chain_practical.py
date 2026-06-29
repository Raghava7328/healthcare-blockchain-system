# ============================================================
# Healthcare Blockchain System for Patient Record Management
# ============================================================
# This program demonstrates a basic blockchain implementation
# for managing hospital patient records.
#
# Features Included:
# 1. Block Structure
# 2. Genesis Block Creation
# 3. Proof-of-Work Mining
# 4. Adding New Patient Record Blocks
# 5. Blockchain Validation
# 6. Longest Chain Consensus Rule
# ============================================================

import hashlib
import json
import time
from dataclasses import dataclass


# ============================================================
# Block Class
# This class represents a single block in the blockchain.
# ============================================================

@dataclass
class HealthBlock:

    # Unique block number
    block_no: int

    # Hash value of the previous block
    parent_digest: str

    # Timestamp of block creation
    created_at: float

    # Patient data stored inside the block
    record_payload: dict

    # Nonce value used during mining
    proof_number: int = 0

    # Final generated hash of the block
    digest: str = ""

    # --------------------------------------------------------
    # Function: generate_digest()
    # Purpose:
    # Generates SHA-256 hash for the current block.
    # --------------------------------------------------------
    def generate_digest(self):

        # Convert block data into dictionary format
        block_content = {
            "block_no": self.block_no,
            "parent_digest": self.parent_digest,
            "created_at": self.created_at,
            "record_payload": self.record_payload,
            "proof_number": self.proof_number
        }

        # Convert dictionary into JSON string
        encoded_block = json.dumps(
            block_content,
            sort_keys=True
        ).encode("utf-8")

        # Generate SHA-256 hash
        return hashlib.sha256(encoded_block).hexdigest()


# ============================================================
# Blockchain Class
# This class controls the blockchain operations.
# ============================================================

class HealthcareRecordLedger:

    # --------------------------------------------------------
    # Constructor Function
    # Initializes blockchain and mining difficulty.
    # --------------------------------------------------------
    def __init__(self, mining_level=3):

        # Mining difficulty level
        self.mining_level = mining_level

        # Main blockchain list
        self.ledger = []

        # Create genesis block
        self._start_ledger()

    # --------------------------------------------------------
    # Function: _start_ledger()
    # Purpose:
    # Creates the first block of the blockchain.
    # --------------------------------------------------------
    def _start_ledger(self):

        # Create the initial genesis block
        first_block = HealthBlock(
            block_no=1,
            parent_digest="NO_PREVIOUS_BLOCK",
            created_at=time.time(),
            record_payload={
                "message": "Initial hospital blockchain block",
                "organisation": "HealthCare Innovations Ltd."
            }
        )

        # Generate hash for genesis block
        first_block.digest = first_block.generate_digest()

        # Add genesis block to blockchain
        self.ledger.append(first_block)

    # --------------------------------------------------------
    # Function: latest_entry()
    # Purpose:
    # Returns the most recent block in the chain.
    # --------------------------------------------------------
    def latest_entry(self):
        return self.ledger[-1]

    # --------------------------------------------------------
    # Function: _mine_proof()
    # Purpose:
    # Performs proof-of-work mining.
    # A valid hash must start with required zeros.
    # --------------------------------------------------------
    def _mine_proof(self, block):

        # Required hash prefix based on difficulty
        required_prefix = "0" * self.mining_level

        while True:

            # Generate new hash
            current_digest = block.generate_digest()

            # Check whether mining condition is satisfied
            if current_digest.startswith(required_prefix):

                # Store final valid hash
                block.digest = current_digest

                return block

            # Increment nonce value and try again
            block.proof_number += 1

    # --------------------------------------------------------
    # Function: insert_patient_record()
    # Purpose:
    # Adds a new patient record block into blockchain.
    # --------------------------------------------------------
    def insert_patient_record(
        self,
        patient_id,
        patient_name,
        diagnosis,
        doctor,
        department
    ):

        # Get latest block
        previous_entry = self.latest_entry()

        # Create patient record data
        medical_record = {
            "patient_id": patient_id,
            "patient_name": patient_name,
            "diagnosis": diagnosis,
            "doctor": doctor,
            "department": department,
            "record_status": "Created"
        }

        # Create new block
        new_entry = HealthBlock(
            block_no=len(self.ledger) + 1,
            parent_digest=previous_entry.digest,
            created_at=time.time(),
            record_payload=medical_record
        )

        # Mine the block using proof-of-work
        mined_entry = self._mine_proof(new_entry)

        # Add mined block to blockchain
        self.ledger.append(mined_entry)

        print(f"\nPatient record successfully added for {patient_id}")

    # --------------------------------------------------------
    # Function: verify_ledger()
    # Purpose:
    # Verifies blockchain integrity and security.
    # --------------------------------------------------------
    def verify_ledger(self):

        # Start checking from second block
        for position in range(1, len(self.ledger)):

            current_entry = self.ledger[position]
            previous_entry = self.ledger[position - 1]

            # Verify current hash integrity
            if current_entry.digest != current_entry.generate_digest():
                return False

            # Verify chain connection
            if current_entry.parent_digest != previous_entry.digest:
                return False

            # Verify proof-of-work rule
            if not current_entry.digest.startswith(
                "0" * self.mining_level
            ):
                return False

        return True

    # --------------------------------------------------------
    # Function: apply_longest_chain_rule()
    # Purpose:
    # Implements consensus mechanism.
    # The longest blockchain is accepted.
    # --------------------------------------------------------
    def apply_longest_chain_rule(self, external_ledger):

        # Compare blockchain lengths
        if len(external_ledger) > len(self.ledger):

            # Replace current chain
            self.ledger = external_ledger

            return "External blockchain accepted."

        return "Current blockchain retained."

    # --------------------------------------------------------
    # Function: show_ledger()
    # Purpose:
    # Displays complete blockchain information.
    # --------------------------------------------------------
    def show_ledger(self):

        print("\n========== HOSPITAL BLOCKCHAIN ==========")

        # Display each block
        for entry in self.ledger:

            print("\n----------------------------------------")
            print(f"Block Number    : {entry.block_no}")
            print(f"Timestamp       : {time.ctime(entry.created_at)}")
            print(f"Previous Hash   : {entry.parent_digest}")
            print(f"Current Hash    : {entry.digest}")
            print(f"Nonce Value     : {entry.proof_number}")

            print("\nPatient Record Data:")
            print(json.dumps(entry.record_payload, indent=4))


# ============================================================
# Main Program
# ============================================================

def run_practical_demo():

    # Create blockchain object
    hospital_ledger = HealthcareRecordLedger(mining_level=3)

    # Add first patient record
    hospital_ledger.insert_patient_record(
        patient_id="HC-001",
        patient_name="Michael Brown",
        diagnosis="Asthma",
        doctor="Dr. Emma Wilson",
        department="Respiratory Care"
    )

    # Add second patient record
    hospital_ledger.insert_patient_record(
        patient_id="HC-002",
        patient_name="Sophia Green",
        diagnosis="Hypertension",
        doctor="Dr. James Miller",
        department="Cardiology"
    )

    # Add third patient record
    hospital_ledger.insert_patient_record(
        patient_id="HC-003",
        patient_name="Daniel Clark",
        diagnosis="Fracture",
        doctor="Dr. Olivia Taylor",
        department="Orthopaedics"
    )

    # Display complete blockchain
    hospital_ledger.show_ledger()

    # Validate blockchain
    print("\nBlockchain Validation Result:")
    print(hospital_ledger.verify_ledger())


# ============================================================
# Program Execution Starts Here
# ============================================================

if __name__ == "__main__":
    run_practical_demo()