# Nepex Agent – Guide

This guide provides detailed instructions for each use case available in the dropdown. It outlines:

- 📥 Required Input Format  
- 📤 Output Structure  
- 💡 Prompt Examples  

---

## ✅ Test Case Generator

Generate structured QA test cases using a user story or feature description.

### 🔸 Required Input:
- User Story OR  
- Feature Description  
- (Optional) Acceptance Criteria

### 🧾 Output Format:
- `Title` 
- `Preconditions`  
- `Test Steps`  
- `Expected Result`  
- `Test Type`: Functional / UI / Negative / Edge / Regression  
- `Priority`: P1 / P2 / P3 / P4

### 💬 Example Prompt:
```
User should be able to log in with valid credentials. Error message should appear on incorrect login.
```

### ✅ Example Output:
```
Test Case: Login with valid and invalid credentials

Preconditions:
1. App is installed and running
2. User has valid and invalid credentials available

Test Steps:
1. Enter valid credentials → Expected: User logs in and sees dashboard
2. Enter incorrect password → Expected: Error message displayed

Test Type: Functional  
Priority: P1
```

---

## 🐞 Bug Report Generator

Generate well-documented bug reports for any application issue.

### 🔸 Required Input:
- Bug Description  
- Observed Behavior  
- (Optional) Environment or Screenshot

### 🧾 Output Format:
- `Title`  
- `Environment`  
- `Steps to Reproduce`  
- `Expected Result`  
- `Actual Result`  
- `Severity` / `Priority`  
- `Suggested Fix` (Optional)

### 💬 Example Prompt:
```
Submit button doesn't respond after clicking. Form hangs on "Please wait."
```

### 🐞 Example Output:
```
Title: 1.18 (2025072101) | Keepr Drive (KD) | iOS – Firmware Update Fails with “Firmware Update Failed” Message Despite 

Environment: Android 14, Chrome 116

Steps to Reproduce:
1. Fill all form fields
2. Click Submit

Expected Result: Confirmation message appears

Actual Result: Infinite loading spinner, no confirmation

Severity: High  
Suggested Fix: Align submit handler with backend response.
```

## 📢 Release Notes Generator

Create QA-friendly or user-facing release notes for new builds.

### 🔸 Required Input:
- List of Features  
- Fixes and Enhancements  
- Known Issues (if any)

### 🧾 Output Format:
- `Version` / Build Number  
- `Release Date`  
- `Introduction` (optional)  
- `New Features`  
- `Enhancements / Improvements`  
- `Bug Fixes / Known Issues`  
- `Steps to Perform Key Features` (if needed)

### 💬 Example Prompt:
```
OTP login added, filter improved in subscription list, fixed dashboard loading issue.
```

### 📢 Example Output:
```
Version: 3.2.0  
Release Date: August 5, 2025  

Introduction:
This release enforces an app update prompt to ensure all users migrate to the latest version.

New Features:
- Mandatory App Update Popup with direct App Store link

Improvements:
- None in this version

Bug Fixes:
- No bugs reported or fixed

Steps to Verify Feature:
1. Launch app with old version → Observe update prompt
2. Tap “Update Now” → Redirect to App Store
3. Update and reopen app → Prompt disappears
```

---

## 📧 QA Email Sign-off Generator

Generate a professional sign-off email after completing test cycles or verifying builds.

### 🔸 Required Input:
- Summary of test coverage  
- Type of testing performed  
- Final status (Pass / Fail / Blockers)

### 🧾 Output Format:
- `Greeting`  
- `Work Summary`  
- `Result`  
- `Next Steps or Sign-off`

### 💬 Example Prompt:
```
Regression complete for build 1.8. All passed, no blockers.
```

### 📧 Example Output:
```
Hi Team,

The regression cycle for Build 1.8 has been successfully completed. All test cases have passed, and there are no blockers.

The build is ready for release.

Best regards,  
QA Team
```
