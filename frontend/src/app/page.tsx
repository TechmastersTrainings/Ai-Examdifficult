"use client";

import { useEffect, useState } from "react";
import {
  ShieldCheck,
  GraduationCap,
  Microscope,
  Cpu,
  Layers,
  FileCheck2,
  Activity,
  CheckCircle2,
  AlertCircle,
  ArrowRight,
  Database,
  Terminal,
} from "lucide-react";

interface HealthData {
  status: string;
  project_name: string;
  version: string;
  environment: string;
  timestamp: string;
  system_info: {
    python_version?: string;
    platform?: string;
    debug_mode?: boolean;
  };
  database_status: string;
}

export default function Home() {
  const [health, setHealth] = useState<HealthData | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [latencyMs, setLatencyMs] = useState<number | null>(null);

  const fetchHealth = async () => {
    setLoading(true);
    setError(null);
    const start = performance.now();
    try {
      const res = await fetch("http://127.0.0.1:8000/api/v1/health", {
        cache: "no-store",
      });
      if (!res.ok) {
        throw new Error(`HTTP Error: ${res.status}`);
      }
      const data: HealthData = await res.json();
      setLatencyMs(Math.round(performance.now() - start));
      setHealth(data);
    } catch (err: unknown) {
      setError(
        err instanceof Error
          ? err.message
          : "Backend offline (start FastAPI on port 8000)"
      );
      setHealth(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchHealth();
  }, []);

  return (
    <main
      style={{
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        padding: "40px 24px 80px 24px",
        maxWidth: "1280px",
        margin: "0 auto",
        position: "relative",
        zIndex: 1,
      }}
    >
      {/* Header Navigation */}
      <header
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          paddingBottom: "32px",
          borderBottom: "1px solid var(--border-subtle)",
          marginBottom: "48px",
        }}
      >
        <div style={{ display: "flex", alignItems: "center", gap: "14px" }}>
          <div
            style={{
              width: "44px",
              height: "44px",
              borderRadius: "12px",
              background: "var(--primary-gradient)",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              boxShadow: "0 0 20px rgba(99, 102, 241, 0.4)",
            }}
          >
            <Cpu size={24} color="#ffffff" />
          </div>
          <div>
            <h2 style={{ fontSize: "1.15rem", fontWeight: "700" }}>
              CognitivePulse AI
            </h2>
            <p style={{ fontSize: "0.8rem", color: "var(--text-secondary)" }}>
              Question Paper Difficulty & Bloom&apos;s Analyzer
            </p>
          </div>
        </div>

        {/* Live Backend Connection Badge */}
        <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
          <div
            className={`badge ${
              health ? "badge-success" : error ? "badge-primary" : "badge-cyan"
            }`}
            style={{ padding: "6px 14px", cursor: "pointer" }}
            onClick={fetchHealth}
            title="Click to re-ping API"
          >
            <span
              style={{
                width: "8px",
                height: "8px",
                borderRadius: "50%",
                backgroundColor: health ? "#10b981" : "#ef4444",
                boxShadow: health ? "0 0 10px #10b981" : "0 0 10px #ef4444",
                display: "inline-block",
              }}
            />
            {loading
              ? "Checking API..."
              : health
              ? `FastAPI Online (${latencyMs}ms)`
              : "FastAPI Offline"}
          </div>

          <a
            href="http://127.0.0.1:8000/docs"
            target="_blank"
            rel="noopener noreferrer"
            className="btn-secondary"
            style={{ padding: "8px 16px", fontSize: "0.85rem" }}
          >
            <Terminal size={15} />
            Swagger Docs
          </a>
        </div>
      </header>

      {/* Hero Section */}
      <section style={{ textAlign: "center", marginBottom: "64px" }}>
        <div
          className="badge badge-primary"
          style={{ marginBottom: "20px", padding: "6px 14px" }}
        >
          Phase 2 Foundation Initialized
        </div>
        <h1
          style={{
            fontSize: "clamp(2.2rem, 5vw, 3.6rem)",
            lineHeight: "1.15",
            marginBottom: "20px",
            maxWidth: "960px",
            margin: "0 auto 20px auto",
          }}
        >
          AI-Based Question Paper{" "}
          <span className="text-gradient">Difficulty Analyzer</span> &{" "}
          <span className="text-gradient-cyan">Bloom&apos;s Taxonomy</span>
        </h1>
        <p
          style={{
            fontSize: "1.15rem",
            color: "var(--text-secondary)",
            maxWidth: "760px",
            margin: "0 auto 36px auto",
            lineHeight: "1.6",
          }}
        >
          A research-oriented, production-ready platform that extracts
          examination questions from PDF and DOCX papers, predicts their 6-level
          cognitive demand, estimates empirical difficulty, and produces
          auditable institutional analytics.
        </p>

        <div
          style={{
            display: "flex",
            justifyContent: "center",
            gap: "16px",
            flexWrap: "wrap",
          }}
        >
          <button
            className="btn-primary"
            onClick={fetchHealth}
            id="run-diagnostics-btn"
          >
            <Activity size={18} />
            Test API Health Endpoint
          </button>
          <a
            href="http://127.0.0.1:8000/api/v1/health"
            target="_blank"
            rel="noopener noreferrer"
            className="btn-secondary"
          >
            View Raw JSON
            <ArrowRight size={16} />
          </a>
        </div>
      </section>

      {/* Live Health & Diagnostics Card */}
      <section style={{ marginBottom: "56px" }}>
        <div
          className="glass-panel"
          style={{
            padding: "32px",
            position: "relative",
            overflow: "hidden",
          }}
        >
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              marginBottom: "24px",
              flexWrap: "wrap",
              gap: "12px",
            }}
          >
            <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
              <Activity size={22} color="var(--primary-500)" />
              <h2 style={{ fontSize: "1.3rem" }}>Live Service Diagnostics</h2>
            </div>
            <span style={{ fontSize: "0.85rem", color: "var(--text-muted)" }}>
              Data Source:{" "}
              <code className="code-pill">GET /api/v1/health</code>
            </span>
          </div>

          {loading ? (
            <div
              style={{
                padding: "40px",
                textAlign: "center",
                color: "var(--text-secondary)",
              }}
            >
              Contacting backend service at http://127.0.0.1:8000...
            </div>
          ) : health ? (
            <div
              style={{
                display: "grid",
                gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))",
                gap: "20px",
              }}
            >
              <div
                style={{
                  background: "rgba(0, 0, 0, 0.25)",
                  padding: "18px",
                  borderRadius: "12px",
                  border: "1px solid var(--border-subtle)",
                }}
              >
                <div
                  style={{
                    fontSize: "0.8rem",
                    color: "var(--text-secondary)",
                    marginBottom: "6px",
                  }}
                >
                  System Status
                </div>
                <div
                  style={{
                    display: "flex",
                    alignItems: "center",
                    gap: "8px",
                    color: "var(--status-success)",
                    fontWeight: "600",
                    fontSize: "1.1rem",
                  }}
                >
                  <CheckCircle2 size={18} />
                  Operational
                </div>
              </div>

              <div
                style={{
                  background: "rgba(0, 0, 0, 0.25)",
                  padding: "18px",
                  borderRadius: "12px",
                  border: "1px solid var(--border-subtle)",
                }}
              >
                <div
                  style={{
                    fontSize: "0.8rem",
                    color: "var(--text-secondary)",
                    marginBottom: "6px",
                  }}
                >
                  API Version / Env
                </div>
                <div
                  style={{
                    fontSize: "1.1rem",
                    fontWeight: "600",
                    color: "var(--text-primary)",
                  }}
                >
                  v{health.version} ({health.environment})
                </div>
              </div>

              <div
                style={{
                  background: "rgba(0, 0, 0, 0.25)",
                  padding: "18px",
                  borderRadius: "12px",
                  border: "1px solid var(--border-subtle)",
                }}
              >
                <div
                  style={{
                    fontSize: "0.8rem",
                    color: "var(--text-secondary)",
                    marginBottom: "6px",
                  }}
                >
                  Python Runtime
                </div>
                <div
                  style={{
                    fontSize: "1.1rem",
                    fontWeight: "600",
                    color: "var(--text-primary)",
                  }}
                >
                  {health.system_info.python_version || "3.11.2"}
                </div>
              </div>

              <div
                style={{
                  background: "rgba(0, 0, 0, 0.25)",
                  padding: "18px",
                  borderRadius: "12px",
                  border: "1px solid var(--border-subtle)",
                }}
              >
                <div
                  style={{
                    fontSize: "0.8rem",
                    color: "var(--text-secondary)",
                    marginBottom: "6px",
                  }}
                >
                  Database State
                </div>
                <div
                  style={{
                    fontSize: "1.1rem",
                    fontWeight: "600",
                    color: "#f59e0b",
                  }}
                >
                  {health.database_status}
                </div>
              </div>
            </div>
          ) : (
            <div
              style={{
                padding: "24px",
                background: "rgba(239, 68, 68, 0.1)",
                border: "1px solid rgba(239, 68, 68, 0.3)",
                borderRadius: "12px",
                color: "#fca5a5",
                display: "flex",
                alignItems: "center",
                gap: "12px",
              }}
            >
              <AlertCircle size={22} color="#ef4444" />
              <div>
                <strong>Backend service not responding:</strong> {error}. Run{" "}
                <code className="code-pill">
                  uvicorn backend.app.main:app --reload
                </code>{" "}
                to start the backend.
              </div>
            </div>
          )}
        </div>
      </section>

      {/* Mandatory Roles Overview */}
      <section style={{ marginBottom: "56px" }}>
        <h2 style={{ fontSize: "1.6rem", marginBottom: "8px" }}>
          Three Mandatory User Roles
        </h2>
        <p
          style={{
            color: "var(--text-secondary)",
            marginBottom: "28px",
            fontSize: "0.95rem",
          }}
        >
          Enforced through unified authentication and role-based access control
          (RBAC) without data leakage.
        </p>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(320px, 1fr))",
            gap: "24px",
          }}
        >
          {/* Admin */}
          <div className="glass-panel" style={{ padding: "28px" }}>
            <div
              style={{
                width: "42px",
                height: "42px",
                borderRadius: "10px",
                background: "rgba(239, 68, 68, 0.15)",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                marginBottom: "16px",
              }}
            >
              <ShieldCheck size={22} color="#f87171" />
            </div>
            <h3 style={{ fontSize: "1.2rem", marginBottom: "8px" }}>Admin</h3>
            <p
              style={{
                fontSize: "0.88rem",
                color: "var(--text-secondary)",
                marginBottom: "16px",
                lineHeight: "1.5",
              }}
            >
              System governance, user lifecycle management, audit logs, model
              version promotion, and error monitoring.
            </p>
            <ul
              style={{
                listStyle: "none",
                fontSize: "0.82rem",
                color: "var(--text-secondary)",
                display: "flex",
                flexDirection: "column",
                gap: "8px",
              }}
            >
              <li>• Provisioned via secure CLI setup script</li>
              <li>• Manages user activation & role assignments</li>
              <li>• System failure inspection without secret leakage</li>
            </ul>
          </div>

          {/* Teacher / Faculty */}
          <div className="glass-panel" style={{ padding: "28px" }}>
            <div
              style={{
                width: "42px",
                height: "42px",
                borderRadius: "10px",
                background: "rgba(99, 102, 241, 0.15)",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                marginBottom: "16px",
              }}
            >
              <GraduationCap size={22} color="#818cf8" />
            </div>
            <h3 style={{ fontSize: "1.2rem", marginBottom: "8px" }}>
              Teacher / Faculty
            </h3>
            <p
              style={{
                fontSize: "0.88rem",
                color: "var(--text-secondary)",
                marginBottom: "16px",
                lineHeight: "1.5",
              }}
            >
              Uploads examination papers, verifies extracted questions, triggers
              Bloom&apos;s & difficulty inference, and exports reports.
            </p>
            <ul
              style={{
                listStyle: "none",
                fontSize: "0.82rem",
                color: "var(--text-secondary)",
                display: "flex",
                flexDirection: "column",
                gap: "8px",
              }}
            >
              <li>• Isolated ownership: cannot view other teachers&apos; papers</li>
              <li>• Editable question boundaries & teacher overrides</li>
              <li>• Downloadable PDF and CSV analysis reports</li>
            </ul>
          </div>

          {/* Researcher */}
          <div className="glass-panel" style={{ padding: "28px" }}>
            <div
              style={{
                width: "42px",
                height: "42px",
                borderRadius: "10px",
                background: "rgba(6, 182, 212, 0.15)",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                marginBottom: "16px",
              }}
            >
              <Microscope size={22} color="#22d3ee" />
            </div>
            <h3 style={{ fontSize: "1.2rem", marginBottom: "8px" }}>
              Researcher
            </h3>
            <p
              style={{
                fontSize: "0.88rem",
                color: "var(--text-secondary)",
                marginBottom: "16px",
                lineHeight: "1.5",
              }}
            >
              Audits authorized research datasets, benchmarks baselines against
              advanced models, and inspects verified evaluation metrics.
            </p>
            <ul
              style={{
                listStyle: "none",
                fontSize: "0.82rem",
                color: "var(--text-secondary)",
                display: "flex",
                flexDirection: "column",
                gap: "8px",
              }}
            >
              <li>• Access to dataset provenance, licensing, and splits</li>
              <li>• Confusion matrices, Macro-F1, and ablation runs</li>
              <li>• Held-out test sets locked against data leakage</li>
            </ul>
          </div>
        </div>
      </section>

      {/* Core Technical Pipelines */}
      <section style={{ marginBottom: "56px" }}>
        <h2 style={{ fontSize: "1.6rem", marginBottom: "8px" }}>
          Core Architectural Pipelines
        </h2>
        <p
          style={{
            color: "var(--text-secondary)",
            marginBottom: "28px",
            fontSize: "0.95rem",
          }}
        >
          Rigorous separation between document processing, machine learning
          inference, and persistent reporting.
        </p>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))",
            gap: "20px",
          }}
        >
          <div
            style={{
              background: "var(--bg-surface)",
              padding: "24px",
              borderRadius: "14px",
              border: "1px solid var(--border-subtle)",
            }}
          >
            <Layers size={22} color="#6366f1" style={{ marginBottom: "12px" }} />
            <h4 style={{ fontSize: "1.05rem", marginBottom: "6px" }}>
              1. Document Parsing
            </h4>
            <p style={{ fontSize: "0.85rem", color: "var(--text-secondary)", lineHeight: "1.5" }}>
              PyMuPDF for PDF documents and python-docx for Word papers. Question
              number detection, section splitting, and marks extraction.
            </p>
          </div>

          <div
            style={{
              background: "var(--bg-surface)",
              padding: "24px",
              borderRadius: "14px",
              border: "1px solid var(--border-subtle)",
            }}
          >
            <Cpu size={22} color="#8b5cf6" style={{ marginBottom: "12px" }} />
            <h4 style={{ fontSize: "1.05rem", marginBottom: "6px" }}>
              2. Bloom&apos;s Classification
            </h4>
            <p style={{ fontSize: "0.85rem", color: "var(--text-secondary)", lineHeight: "1.5" }}>
              Classifies questions across 6 revised Bloom levels: Remember,
              Understand, Apply, Analyze, Evaluate, Create with confidence scores.
            </p>
          </div>

          <div
            style={{
              background: "var(--bg-surface)",
              padding: "24px",
              borderRadius: "14px",
              border: "1px solid var(--border-subtle)",
            }}
          >
            <Database size={22} color="#06b6d4" style={{ marginBottom: "12px" }} />
            <h4 style={{ fontSize: "1.05rem", marginBottom: "6px" }}>
              3. Difficulty Estimation
            </h4>
            <p style={{ fontSize: "0.85rem", color: "var(--text-secondary)", lineHeight: "1.5" }}>
              Categorizes questions into Easy, Medium, Hard using distinct features
              independent of cognitive levels to preserve research validity.
            </p>
          </div>

          <div
            style={{
              background: "var(--bg-surface)",
              padding: "24px",
              borderRadius: "14px",
              border: "1px solid var(--border-subtle)",
            }}
          >
            <FileCheck2 size={22} color="#10b981" style={{ marginBottom: "12px" }} />
            <h4 style={{ fontSize: "1.05rem", marginBottom: "6px" }}>
              4. Audited Reports
            </h4>
            <p style={{ fontSize: "0.85rem", color: "var(--text-secondary)", lineHeight: "1.5" }}>
              Generates PDF and CSV exports backed by actual database records,
              recording model version, evaluation bounds, and teacher edits.
            </p>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer
        style={{
          marginTop: "auto",
          paddingTop: "32px",
          borderTop: "1px solid var(--border-subtle)",
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          flexWrap: "wrap",
          gap: "16px",
          fontSize: "0.85rem",
          color: "var(--text-muted)",
        }}
      >
        <div>
          CognitivePulse AI © 2026. Developed for rigorous academic NLP research.
        </div>
        <div>
          Sprint Status:{" "}
          <span style={{ color: "#10b981", fontWeight: "600" }}>
            Phase 2: Repository & Application Foundation
          </span>
        </div>
      </footer>
    </main>
  );
}
