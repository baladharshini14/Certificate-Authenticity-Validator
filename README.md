# Certificate Authenticity Validator

## Project Overview

Certificate Authenticity Validator is a web-based application used to verify whether a certificate is genuine or fake.

The system allows users to upload certificate PDF files and verifies the certificate details by comparing extracted information with stored database records.

## Technologies Used

- Frontend: HTML, CSS
- Backend: Python Flask
- Database: MySQL
- PDF Processing: PyPDF2

## Features

- User Login
- Dashboard
- Certificate PDF Upload
- PDF Text Extraction
- Certificate Verification
- Genuine Certificate Detection
- Fake Certificate Detection
- Admin Dashboard
- Verification Records

## Project Workflow

1. User logs into the system
2. Uploads certificate PDF
3. System extracts certificate details using PyPDF2
4. Extracted data is compared with MySQL database records
5. Result is displayed as Genuine or Fake Certificate

## Modules

### 1. Login Module
Provides secure user authentication.

### 2. Dashboard Module
Displays certificate statistics and system information.

### 3. Certificate Verification Module
Checks uploaded certificates and identifies authenticity.

### 4. Admin Module
Manages certificate records and verification details.

## Future Enhancements

- OCR-based image certificate verification
- QR Code based verification
- Cloud database integration
- Verification history tracking

## Conclusion

This project helps organizations reduce manual certificate verification time and prevents fake certificate usage.