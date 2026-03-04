# Security Policy

## Supported Versions

The following versions of H.A.A.P (Halo Azure Access Platform) are currently supported with security updates:

| Version | Supported |
|----------|------------|
| 1.x      | ✅ Yes     |
| < 1.0    | ❌ No      |

---

## Reporting a Vulnerability

If you discover a security vulnerability within this project, please DO NOT open a public issue.

Instead:

1. Email: security@yourcompany.com
2. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Impact assessment
   - Suggested remediation (if known)

You will receive acknowledgment within 48 hours.

We aim to:
- Confirm vulnerability within 5 business days
- Provide remediation timeline
- Release patch as soon as possible

---

## Security Architecture Overview

H.A.A.P is designed with the following security principles:

### 1. Least Privilege
Azure Function uses:
- Managed Identity
- Microsoft Graph Application Permissions:
  - User.Read.All
  - Group.Read.All
  - AppRoleAssignment.Read.All
  - Directory.Read.All

No delegated permissions are used.

---

### 2. Secrets Management
- `local.settings.json` is excluded from source control
- No secrets stored in repository
- Production secrets stored in:
  - Azure Key Vault (recommended)
  - App Settings (if required)

---

### 3. Authentication Model
- Azure Function protected with:
  - Function-level keys OR
  - Azure AD authentication (recommended for production)
- Optional: API Management front-end for additional controls

---

### 4. Logging & Monitoring
- Azure Application Insights enabled
- No sensitive data written to logs
- Correlation IDs recommended for tracing

---

### 5. Network Security (Recommended Production Setup)
- Private Endpoint for Function App
- VNet Integration
- IP restrictions if public

---

## Secure Deployment Requirements

Production environments MUST:

- Use Managed Identity
- Disable basic auth
- Restrict CORS to Halo endpoint
- Require HTTPS
- Enable Azure Defender for Cloud

---

## Compliance Considerations

This solution can support:

- ISO 27001
- SOC 2
- GDPR (no persistent user storage)
- Zero Trust access validation patterns

---

## Disclosure Policy

Security issues will be disclosed responsibly after:
- Patch release
- Customer notification (if required)

---

Thank you for helping keep H.A.A.P secure.
