"use client";

import React, { useState, useEffect } from "react";
import { X, AlertCircle, CheckCircle2 } from "lucide-react";
import { api } from "../services/api";
import { UserRole, User as UserType } from "../types";

interface AuthModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSuccess: (user: UserType) => void;
  initialMode?: "login" | "register";
}

export const AuthModal: React.FC<AuthModalProps> = ({
  isOpen,
  onClose,
  onSuccess,
  initialMode = "login",
}) => {
  const [mode, setMode] = useState<"login" | "register" | "recovery">(initialMode);

  // Authentication Fields (Explicitly blank - zero autofill)
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  // Institutional & Organization Fields
  const [fullName, setFullName] = useState("");
  const [role, setRole] = useState<UserRole>("TEACHER");
  const [institution, setInstitution] = useState("");
  const [institutionCode, setInstitutionCode] = useState("");
  const [department, setDepartment] = useState("");
  const [designation, setDesignation] = useState("");

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [recoveryMessage, setRecoveryMessage] = useState<string | null>(null);

  // Reset all state when modal opens or initialMode changes
  useEffect(() => {
    if (isOpen) {
      setMode(initialMode);
      resetAllFields();
    }
  }, [isOpen, initialMode]);

  const resetAllFields = () => {
    setEmail("");
    setPassword("");
    setConfirmPassword("");
    setFullName("");
    setRole("TEACHER");
    setInstitution("");
    setInstitutionCode("");
    setDepartment("");
    setDesignation("");
    setError(null);
    setRecoveryMessage(null);
  };

  const handleTabSwitch = (newMode: "login" | "register" | "recovery") => {
    setMode(newMode);
    setEmail("");
    setPassword("");
    setConfirmPassword("");
    setError(null);
    setRecoveryMessage(null);
  };

  if (!isOpen) return null;

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setRecoveryMessage(null);

    try {
      if (mode === "login") {
        const res = await api.login(email.trim(), password);
        onSuccess(res.user);
        resetAllFields();
        onClose();
      } else if (mode === "register") {
        if (password.length < 8) {
          setError("Password must contain at least 8 characters.");
          setLoading(false);
          return;
        }

        if (password !== confirmPassword) {
          setError("Passwords do not match. Please verify your password entry.");
          setLoading(false);
          return;
        }

        if (!institution.trim()) {
          setError("Please provide your verified college, university, or institute name.");
          setLoading(false);
          return;
        }

        if (!department.trim()) {
          setError("Please specify your academic department or school.");
          setLoading(false);
          return;
        }

        if (!designation) {
          setError("Please select your academic designation.");
          setLoading(false);
          return;
        }

        await api.register({
          email: email.trim(),
          password,
          full_name: fullName.trim(),
          role,
          institution: institution.trim(),
          institution_code: institutionCode.trim() || undefined,
          department: department.trim(),
          designation: designation.trim() || undefined,
        });

        // Automatically authenticate upon successful registration
        const loginRes = await api.login(email.trim(), password);
        onSuccess(loginRes.user);
        resetAllFields();
        onClose();
      } else if (mode === "recovery") {
        if (!email.trim()) {
          setError("Please enter your registered institutional email.");
          setLoading(false);
          return;
        }
        setRecoveryMessage(
          `Password recovery instructions have been dispatched to ${email.trim()}. Please verify your institutional inbox.`
        );
      }
    } catch (err: any) {
      setError(err.message || "Authentication process failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="modal-backdrop" onClick={onClose}>
      <div
        className="modal-card"
        onClick={(e) => e.stopPropagation()}
        style={{ maxWidth: mode === "register" ? "680px" : "440px" }}
      >
        {/* Header */}
        <div className="modal-header">
          <div>
            <h3 className="modal-title">
              {mode === "login" && "Sign In to AI BASED AUTOMATIC QUESTION PAPER DIFFICULTY ANALYZER"}
              {mode === "register" && "Register Account — AI BASED AUTOMATIC QUESTION PAPER DIFFICULTY ANALYZER"}
              {mode === "recovery" && "Account Access Recovery"}
            </h3>
            <p style={{ fontSize: "0.775rem", color: "var(--text-secondary)", marginTop: "2px" }}>
              {mode === "login" && "Access your examination papers, review tables, and analysis."}
              {mode === "register" && "Register with verified university or institutional credentials."}
              {mode === "recovery" && "Reset your password via institutional email verification."}
            </p>
          </div>
          <button
            onClick={() => { resetAllFields(); onClose(); }}
            className="btn btn-secondary btn-icon"
            style={{ width: "28px", height: "28px", borderRadius: "50%" }}
            title="Close"
          >
            <X size={15} />
          </button>
        </div>

        {/* Mode Tabs */}
        <div
          style={{
            display: "flex",
            borderBottom: "1px solid var(--border-light)",
            backgroundColor: "#FAF9F5",
            padding: "0 1.5rem",
          }}
        >
          <button
            type="button"
            onClick={() => handleTabSwitch("login")}
            className={`tab-btn ${mode === "login" ? "active" : ""}`}
          >
            Sign In
          </button>
          <button
            type="button"
            onClick={() => handleTabSwitch("register")}
            className={`tab-btn ${mode === "register" ? "active" : ""}`}
          >
            Register Institution / Faculty
          </button>
          <button
            type="button"
            onClick={() => handleTabSwitch("recovery")}
            className={`tab-btn ${mode === "recovery" ? "active" : ""}`}
          >
            Help
          </button>
        </div>

        {/* Form Body */}
        <div className="modal-body">
          {error && (
            <div className="alert-box alert-error">
              <AlertCircle size={16} style={{ flexShrink: 0, marginTop: "2px" }} />
              <div>{error}</div>
            </div>
          )}

          {recoveryMessage && (
            <div className="alert-box alert-success">
              <CheckCircle2 size={16} style={{ flexShrink: 0, marginTop: "2px" }} />
              <div>{recoveryMessage}</div>
            </div>
          )}

          {mode === "recovery" ? (
            <form onSubmit={handleSubmit} autoComplete="off">
              <div className="form-group">
                <label className="form-label">Registered Institutional Email</label>
                <input
                  type="email"
                  name="recovery_auth_email_no_autofill"
                  autoComplete="off"
                  autoCorrect="off"
                  autoCapitalize="off"
                  spellCheck={false}
                  required
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="name@university.edu"
                  className="form-input"
                />
                <div className="form-hint">
                  Password reset tokens are delivered to your official academic email address.
                </div>
              </div>

              <div style={{ display: "flex", justifyContent: "flex-end", gap: "0.5rem", marginTop: "1.5rem" }}>
                <button type="button" onClick={() => handleTabSwitch("login")} className="btn btn-secondary">
                  Back to Sign In
                </button>
                <button type="submit" disabled={loading} className="btn btn-primary">
                  {loading ? "Sending..." : "Submit Reset Request"}
                </button>
              </div>
            </form>
          ) : (
            <form onSubmit={handleSubmit} autoComplete="off">
              {mode === "register" ? (
                <>
                  {/* Section 1: Academic & Personal Identity */}
                  <div style={{ marginBottom: "1rem" }}>
                    <div style={{ fontSize: "0.75rem", fontWeight: 700, textTransform: "uppercase", letterSpacing: "0.04em", color: "var(--brand-deep)", marginBottom: "0.6rem" }}>
                      1. Academic & User Identity
                    </div>

                    <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "0.75rem" }}>
                      <div className="form-group">
                        <label className="form-label">Full Name & Title *</label>
                        <input
                          type="text"
                          name="academic_full_name_no_autofill"
                          autoComplete="off"
                          autoCorrect="off"
                          spellCheck={false}
                          required
                          value={fullName}
                          onChange={(e) => setFullName(e.target.value)}
                          placeholder="e.g. Dr. Robert Vance"
                          className="form-input"
                        />
                      </div>

                      <div className="form-group">
                        <label className="form-label">Official Institutional Email *</label>
                        <input
                          type="email"
                          name="academic_email_address_no_autofill"
                          autoComplete="off"
                          autoCorrect="off"
                          autoCapitalize="off"
                          spellCheck={false}
                          required
                          value={email}
                          onChange={(e) => setEmail(e.target.value)}
                          placeholder="e.g. r.vance@mit.edu"
                          className="form-input"
                        />
                      </div>
                    </div>

                    <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "0.75rem" }}>
                      <div className="form-group">
                        <label className="form-label">Password (Min 8 Characters) *</label>
                        <input
                          type="password"
                          name="academic_new_password_no_autofill"
                          autoComplete="new-password"
                          autoCorrect="off"
                          autoCapitalize="off"
                          spellCheck={false}
                          required
                          value={password}
                          onChange={(e) => setPassword(e.target.value)}
                          placeholder="••••••••••••"
                          className="form-input"
                        />
                      </div>

                      <div className="form-group">
                        <label className="form-label">Confirm Password *</label>
                        <input
                          type="password"
                          name="academic_confirm_password_no_autofill"
                          autoComplete="new-password"
                          autoCorrect="off"
                          autoCapitalize="off"
                          spellCheck={false}
                          required
                          value={confirmPassword}
                          onChange={(e) => setConfirmPassword(e.target.value)}
                          placeholder="••••••••••••"
                          className="form-input"
                        />
                      </div>
                    </div>

                    <div className="form-group">
                      <label className="form-label">Platform Role Assignment *</label>
                      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "0.5rem" }}>
                        <button
                          type="button"
                          onClick={() => setRole("TEACHER")}
                          className={`btn ${role === "TEACHER" ? "btn-primary" : "btn-secondary"}`}
                          style={{ justifyContent: "center" }}
                        >
                          Faculty / Teacher (Paper Analysis)
                        </button>
                        <button
                          type="button"
                          onClick={() => setRole("RESEARCHER")}
                          className={`btn ${role === "RESEARCHER" ? "btn-primary" : "btn-secondary"}`}
                          style={{ justifyContent: "center" }}
                        >
                          NLP Researcher (Model Evaluation)
                        </button>
                      </div>
                    </div>
                  </div>

                  {/* Section 2: College / Institute / Organization Details */}
                  <div style={{ borderTop: "1px solid var(--border-light)", paddingTop: "1rem" }}>
                    <div style={{ fontSize: "0.75rem", fontWeight: 700, textTransform: "uppercase", letterSpacing: "0.04em", color: "var(--brand-deep)", marginBottom: "0.6rem" }}>
                      2. Institutional Affiliation & Designation
                    </div>

                    <div style={{ display: "grid", gridTemplateColumns: "2fr 1fr", gap: "0.75rem" }}>
                      <div className="form-group">
                        <label className="form-label">College / University / Institute Name *</label>
                        <input
                          type="text"
                          name="academic_institution_name_no_autofill"
                          autoComplete="off"
                          autoCorrect="off"
                          spellCheck={false}
                          required
                          value={institution}
                          onChange={(e) => setInstitution(e.target.value)}
                          placeholder="e.g. Indian Institute of Technology Bombay"
                          className="form-input"
                        />
                      </div>

                      <div className="form-group">
                        <label className="form-label">College / Institute Code</label>
                        <input
                          type="text"
                          name="academic_institution_code_no_autofill"
                          autoComplete="off"
                          autoCorrect="off"
                          spellCheck={false}
                          value={institutionCode}
                          onChange={(e) => setInstitutionCode(e.target.value)}
                          placeholder="e.g. IITB-01"
                          className="form-input"
                        />
                      </div>
                    </div>

                    <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "0.75rem" }}>
                      <div className="form-group">
                        <label className="form-label">Department / School *</label>
                        <input
                          type="text"
                          name="academic_department_name_no_autofill"
                          autoComplete="off"
                          autoCorrect="off"
                          spellCheck={false}
                          required
                          value={department}
                          onChange={(e) => setDepartment(e.target.value)}
                          placeholder="e.g. Computer Science & Engineering"
                          className="form-input"
                        />
                      </div>

                      <div className="form-group">
                        <label className="form-label">Academic Designation / Title *</label>
                        <select
                          name="academic_designation_select_no_autofill"
                          autoComplete="off"
                          required
                          value={designation}
                          onChange={(e) => setDesignation(e.target.value)}
                          className="form-select"
                        >
                          <option value="" disabled>Select Academic Designation</option>
                          <option value="Professor">Professor</option>
                          <option value="Associate Professor">Associate Professor</option>
                          <option value="Assistant Professor">Assistant Professor</option>
                          <option value="Department Chair / HOD">Department Chair / HOD</option>
                          <option value="Dean / Academic Director">Dean / Academic Director</option>
                          <option value="Lecturer / Instructor">Lecturer / Instructor</option>
                          <option value="Research Fellow / Scholar">Research Fellow / Scholar</option>
                        </select>
                      </div>
                    </div>
                  </div>
                </>
              ) : (
                /* Login View */
                <>
                  <div className="form-group">
                    <label className="form-label">Institutional Email Address</label>
                    <input
                      type="email"
                      name="account_login_email_no_autofill"
                      autoComplete="off"
                      autoCorrect="off"
                      autoCapitalize="off"
                      spellCheck={false}
                      required
                      value={email}
                      onChange={(e) => setEmail(e.target.value)}
                      placeholder="name@university.edu"
                      className="form-input"
                    />
                  </div>

                  <div className="form-group">
                    <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                      <label className="form-label">Account Password</label>
                      <button
                        type="button"
                        onClick={() => handleTabSwitch("recovery")}
                        style={{
                          background: "none",
                          border: "none",
                          color: "var(--brand-primary)",
                          fontSize: "0.75rem",
                          cursor: "pointer",
                          fontWeight: 600,
                        }}
                      >
                        Forgot password?
                      </button>
                    </div>
                    <input
                      type="password"
                      name="account_login_password_no_autofill"
                      autoComplete="new-password"
                      autoCorrect="off"
                      autoCapitalize="off"
                      spellCheck={false}
                      required
                      value={password}
                      onChange={(e) => setPassword(e.target.value)}
                      placeholder="••••••••••••"
                      className="form-input"
                    />
                  </div>
                </>
              )}

              <div style={{ marginTop: "1.5rem" }}>
                <button
                  type="submit"
                  disabled={loading}
                  className="btn btn-primary"
                  style={{ width: "100%", padding: "0.65rem", fontSize: "0.875rem" }}
                >
                  {loading
                    ? "Processing..."
                    : mode === "login"
                    ? "Sign In to Workspace"
                    : "Complete Institutional Registration"}
                </button>
              </div>
            </form>
          )}
        </div>
      </div>
    </div>
  );
};
