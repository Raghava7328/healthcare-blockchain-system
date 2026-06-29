// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/*
    PatientRecordContract
    This smart contract manages basic patient record creation
    and transfer of record responsibility between authorised
    healthcare providers.
*/

contract PatientRecordContract {

    // Stores the account that deployed the contract
    address private administrator;

    // Counts the total number of patient records created
    uint256 public totalRecords;

    // Structure used to store patient record details
    struct MedicalFile {
        uint256 fileNumber;
        string hospitalPatientCode;
        string fullName;
        string medicalCondition;
        address assignedProvider;
        uint256 createdOn;
        bool active;
    }

    // Stores patient records using record number as key
    mapping(uint256 => MedicalFile) private medicalFiles;

    // Stores approved healthcare provider addresses
    mapping(address => bool) public approvedProviders;

    // Triggered when a new patient record is created
    event MedicalFileCreated(
        uint256 indexed fileNumber,
        string hospitalPatientCode,
        address indexed provider
    );

    // Triggered when a patient record is transferred
    event MedicalFileReassigned(
        uint256 indexed fileNumber,
        address indexed oldProvider,
        address indexed newProvider
    );

    // Restricts selected functions to contract administrator
    modifier onlyAdministrator() {
        require(
            msg.sender == administrator,
            "Only administrator can perform this action"
        );
        _;
    }

    // Restricts selected functions to approved healthcare providers
    modifier onlyApprovedProvider() {
        require(
            approvedProviders[msg.sender] == true,
            "Healthcare provider is not approved"
        );
        _;
    }

    // Constructor runs once when contract is deployed
    constructor() {
        administrator = msg.sender;
        approvedProviders[msg.sender] = true;
    }

    // Allows administrator to approve a healthcare provider
    function approveProvider(address providerAddress)
        public
        onlyAdministrator
    {
        require(providerAddress != address(0), "Invalid provider address");
        approvedProviders[providerAddress] = true;
    }

    // Allows administrator to remove provider approval
    function revokeProvider(address providerAddress)
        public
        onlyAdministrator
    {
        require(providerAddress != administrator, "Administrator cannot be revoked");
        approvedProviders[providerAddress] = false;
    }

    // Creates a new patient record
    function createMedicalFile(
        string memory hospitalPatientCode,
        string memory fullName,
        string memory medicalCondition
    )
        public
        onlyApprovedProvider
    {
        totalRecords++;

        medicalFiles[totalRecords] = MedicalFile({
            fileNumber: totalRecords,
            hospitalPatientCode: hospitalPatientCode,
            fullName: fullName,
            medicalCondition: medicalCondition,
            assignedProvider: msg.sender,
            createdOn: block.timestamp,
            active: true
        });

        emit MedicalFileCreated(
            totalRecords,
            hospitalPatientCode,
            msg.sender
        );
    }

    // Transfers patient record responsibility to another approved provider
    function reassignMedicalFile(
        uint256 fileNumber,
        address newProvider
    )
        public
        onlyApprovedProvider
    {
        require(medicalFiles[fileNumber].active == true, "Medical file not found");
        require(
            medicalFiles[fileNumber].assignedProvider == msg.sender,
            "Only assigned provider can transfer this file"
        );
        require(
            approvedProviders[newProvider] == true,
            "New provider is not approved"
        );

        address oldProvider = medicalFiles[fileNumber].assignedProvider;
        medicalFiles[fileNumber].assignedProvider = newProvider;

        emit MedicalFileReassigned(
            fileNumber,
            oldProvider,
            newProvider
        );
    }

    // Returns complete patient record details
    function viewMedicalFile(uint256 fileNumber)
        public
        view
        returns (
            uint256,
            string memory,
            string memory,
            string memory,
            address,
            uint256,
            bool
        )
    {
        require(medicalFiles[fileNumber].active == true, "Medical file not found");

        MedicalFile memory file = medicalFiles[fileNumber];

        return (
            file.fileNumber,
            file.hospitalPatientCode,
            file.fullName,
            file.medicalCondition,
            file.assignedProvider,
            file.createdOn,
            file.active
        );
    }

    // Returns administrator wallet address
    function getAdministrator()
        public
        view
        returns (address)
    {
        return administrator;
    }
}