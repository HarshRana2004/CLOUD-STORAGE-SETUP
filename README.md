# CLOUD-STORAGE-SETUP

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: HARSH RANA

*INTERN ID*: CTIS1777

*DOMAIN*: CLOUD COMPUTING

*DURATION*: 6 WEEKS

*MENTOR*: NEELA SANTHOSH KUMAR

**##TASK DESCRIPTION**

## 🚀 Project Overview

This project demonstrates the implementation of a comprehensive cloud storage solution supporting both AWS S3 and Google Cloud Storage platforms. Developed as part of an internship program, this system provides a complete foundation for cloud-based file management with automated deployment, permission configuration, and multi-platform compatibility.

## 🎯 Project Objectives

The primary goal was to create a robust, scalable cloud storage infrastructure that can:
- Seamlessly integrate with major cloud providers (AWS S3 and Google Cloud Storage)
- Automatically configure storage buckets with appropriate permissions
- Provide secure file upload and download capabilities
- Demonstrate best practices in cloud architecture and deployment automation
- Serve as a foundation for enterprise-level storage solutions

## 🏗️ Architecture & Design

### Core Components

**1. Multi-Platform Storage Managers**
- `S3StorageManager`: Handles AWS S3 operations including bucket creation, policy management, and file operations
- `GCSStorageManager`: Manages Google Cloud Storage with IAM policy configuration and blob operations
- Unified interface design for seamless platform switching

**2. Automated Deployment System**
- `deploy.py`: Interactive deployment script with platform selection
- Automated credential validation and error handling
- One-click setup for complete storage infrastructure

**3. Security & Permissions**
- Public read access configuration for web accessibility
- IAM policy management for Google Cloud Storage
- Bucket policy implementation for AWS S3
- Secure credential handling with multiple authentication methods

**4. Testing & Validation**
- Comprehensive credential testing utilities
- Connection validation before deployment
- Error handling and troubleshooting tools

## 🛠️ Technical Implementation

### Technologies Used
- **Python 3.x**: Core programming language
- **Boto3**: AWS SDK for Python
- **Google Cloud Storage Client**: GCS Python library
- **JSON**: Configuration management
- **Environment Variables**: Secure credential handling

### Key Features

**Bucket Management**
- Automatic bucket creation with unique naming
- Location-specific deployment (US, EU, Asia regions)
- Conflict resolution for existing buckets
- Comprehensive error handling and logging

**File Operations**
- Batch file upload capabilities
- Metadata preservation during transfers
- Progress tracking and status reporting
- Support for multiple file formats (text, JSON, binary)

**Permission Configuration**
- Public read access for web applications
- Granular permission control
- Cross-platform permission standardization
- Security best practices implementation

**Deployment Automation**
- Interactive setup wizard
- Platform-specific configuration
- Automated dependency installation
- Rollback capabilities for failed deployments

## 📁 Project Structure

```
Cloud Storage Setup - Task 1/
├── aws_s3_setup.py          # AWS S3 implementation
├── gcs_setup.py             # Google Cloud Storage implementation
├── deploy.py                # Main deployment script
├── local_demo.py            # Local storage demonstration
├── test_credentials.py      # Credential validation utility
├── simple_test.py           # Basic functionality testing
├── requirements.txt         # Python dependencies
├── config.json             # Configuration settings
├── credentials_template    # Credential file template
├── sample_data/           # Example files for testing
│   ├── example.txt        # Sample text file
│   └── data.json         # Sample JSON data
└── README.md             # Project documentation
```

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.x installed
- AWS account with IAM access (for S3)
- Google Cloud Platform account (for GCS)
- Valid API credentials for chosen platform

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone [repository-url]
   cd "Cloud Storage Setup - Task 1"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure credentials**
   
   For AWS S3:
   ```bash
   set AWS_ACCESS_KEY_ID=your_access_key
   set AWS_SECRET_ACCESS_KEY=your_secret_key
   ```
   
   For Google Cloud Storage:
   ```bash
   set GOOGLE_APPLICATION_CREDENTIALS=path\to\service-account-key.json
   ```

4. **Deploy the storage system**
   ```bash
   python deploy.py
   ```

## 🎯 Learning Outcomes

This internship project provided hands-on experience with:

- **Cloud Architecture**: Understanding of distributed storage systems and cloud service integration
- **API Integration**: Working with REST APIs and SDK libraries for major cloud providers
- **Security Implementation**: Implementing proper authentication, authorization, and access control
- **DevOps Practices**: Automated deployment, configuration management, and infrastructure as code
- **Error Handling**: Robust error management and user-friendly troubleshooting
- **Documentation**: Creating comprehensive technical documentation and user guides

## 🔧 Advanced Features

- **Multi-region deployment support**
- **Batch processing capabilities**
- **Comprehensive logging and monitoring**
- **Fallback mechanisms for service failures**
- **Configuration-driven deployment**
- **Cross-platform compatibility testing**

## 📈 Future Enhancements

- Web-based management interface
- Real-time file synchronization
- Advanced security features (encryption, access logs)
- Integration with CI/CD pipelines
- Mobile application support
- Database integration for metadata management

## 🤝 Contributing

This project serves as a foundation for cloud storage implementations and can be extended for various use cases including web applications, mobile backends, and enterprise storage solutions.

---

**Developed as part of Cloud Infrastructure Internship Program**  
*Demonstrating practical implementation of cloud storage solutions with industry best practices*

#OUTPUT

<img width="822" height="364" alt="Image" src="https://github.com/user-attachments/assets/6de72eb4-c246-48ca-8826-4891337ae55b" />
