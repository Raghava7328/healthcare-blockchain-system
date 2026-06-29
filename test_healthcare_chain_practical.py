import unittest
from healthcare_chain_practical import (
    HealthcareRecordLedger,
    HealthBlock
)


# ============================================================
# Unit Test Suite for Healthcare Blockchain System
# ------------------------------------------------------------
# This test suite validates the functionality, security,
# integrity, and consensus mechanisms implemented within the
# HealthcareRecordLedger blockchain application.
# ============================================================

class TestHealthcareRecordLedger(unittest.TestCase):

    # --------------------------------------------------------
    # Test Case 1
    # Purpose:
    # Verify that the Genesis Block is created correctly
    # when the blockchain is initialized.
    # --------------------------------------------------------
    def test_genesis_block_created(self):

        ledger = HealthcareRecordLedger(mining_level=3)

        self.assertEqual(len(ledger.ledger), 1)
        self.assertEqual(ledger.ledger[0].block_no, 1)
        self.assertEqual(
            ledger.ledger[0].parent_digest,
            "NO_PREVIOUS_BLOCK"
        )

    # --------------------------------------------------------
    # Test Case 2
    # Purpose:
    # Verify that latest_entry() returns the most recent
    # block stored within the blockchain.
    # --------------------------------------------------------
    def test_latest_entry(self):

        ledger = HealthcareRecordLedger(mining_level=3)

        latest_block = ledger.latest_entry()

        self.assertEqual(
            latest_block,
            ledger.ledger[-1]
        )

    # --------------------------------------------------------
    # Test Case 3
    # Purpose:
    # Verify that patient records are successfully converted
    # into blockchain blocks and stored in the ledger.
    # --------------------------------------------------------
    def test_insert_patient_record(self):

        ledger = HealthcareRecordLedger(mining_level=3)

        ledger.insert_patient_record(
            patient_id="HC-001",
            patient_name="Michael Brown",
            diagnosis="Asthma",
            doctor="Dr. Emma Wilson",
            department="Respiratory Care"
        )

        self.assertEqual(len(ledger.ledger), 2)

        self.assertEqual(
            ledger.ledger[1].record_payload["patient_id"],
            "HC-001"
        )

    # --------------------------------------------------------
    # Test Case 4
    # Purpose:
    # Verify that each block correctly references the hash
    # value of the previous block.
    # --------------------------------------------------------
    def test_parent_digest_link(self):

        ledger = HealthcareRecordLedger(mining_level=3)

        ledger.insert_patient_record(
            patient_id="HC-002",
            patient_name="Sophia Green",
            diagnosis="Hypertension",
            doctor="Dr. James Miller",
            department="Cardiology"
        )

        self.assertEqual(
            ledger.ledger[1].parent_digest,
            ledger.ledger[0].digest
        )

    # --------------------------------------------------------
    # Test Case 5
    # Purpose:
    # Verify that Proof-of-Work mining generates hashes
    # satisfying the predefined difficulty requirement.
    # --------------------------------------------------------
    def test_proof_of_work_mining(self):

        ledger = HealthcareRecordLedger(mining_level=3)

        ledger.insert_patient_record(
            patient_id="HC-003",
            patient_name="Daniel Clark",
            diagnosis="Fracture",
            doctor="Dr. Olivia Taylor",
            department="Orthopaedics"
        )

        self.assertTrue(
            ledger.ledger[1].digest.startswith(
                "0" * ledger.mining_level
            )
        )

    # --------------------------------------------------------
    # Test Case 6
    # Purpose:
    # Verify that blockchain validation succeeds when no
    # modifications have been made to stored records.
    # --------------------------------------------------------
    def test_verify_ledger_valid(self):

        ledger = HealthcareRecordLedger(mining_level=3)

        ledger.insert_patient_record(
            patient_id="HC-001",
            patient_name="Michael Brown",
            diagnosis="Asthma",
            doctor="Dr. Emma Wilson",
            department="Respiratory Care"
        )

        self.assertTrue(
            ledger.verify_ledger()
        )

    # --------------------------------------------------------
    # Test Case 7
    # Purpose:
    # Verify that blockchain validation detects data
    # tampering and reports an invalid chain.
    # --------------------------------------------------------
    def test_verify_ledger_after_tampering(self):

        ledger = HealthcareRecordLedger(mining_level=3)

        ledger.insert_patient_record(
            patient_id="HC-001",
            patient_name="Michael Brown",
            diagnosis="Asthma",
            doctor="Dr. Emma Wilson",
            department="Respiratory Care"
        )

        # Simulate unauthorized modification
        ledger.ledger[1].record_payload[
            "diagnosis"
        ] = "Hacked Data"

        self.assertFalse(
            ledger.verify_ledger()
        )

    # --------------------------------------------------------
    # Test Case 8
    # Purpose:
    # Verify that the consensus mechanism correctly accepts
    # a longer blockchain according to the longest-chain rule.
    # --------------------------------------------------------
    def test_longest_chain_rule(self):

        ledger = HealthcareRecordLedger(mining_level=3)

        external_ledger = ledger.ledger.copy()

        external_ledger.append(
            HealthBlock(
                block_no=2,
                parent_digest=ledger.ledger[0].digest,
                created_at=ledger.ledger[0].created_at,
                record_payload={
                    "message": "External Block"
                }
            )
        )

        result = ledger.apply_longest_chain_rule(
            external_ledger
        )

        self.assertEqual(
            result,
            "External blockchain accepted."
        )


# ============================================================
# Execute Unit Test Suite
# ============================================================
if __name__ == "__main__":
    unittest.main()