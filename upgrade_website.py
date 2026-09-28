import os

def create_advanced_website():
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>OmniPortal | BISY2004 Integrated Project Management Portal</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  
  <style>
    :root {
      --primary: #0F172A;
      --primary-light: #1E293B;
      --navy: #1B365D;
      --navy-light: #2A4D7C;
      --accent: #2563EB;
      --accent-hover: #1D4ED8;
      --accent-soft: #EFF6FF;
      --cyan: #0EA5E9;
      --bg: #F8FAFC;
      --card-bg: #FFFFFF;
      --text-main: #0F172A;
      --text-muted: #64748B;
      --text-sub: #475569;
      --border: #E2E8F0;
      --border-subtle: #F1F5F9;
      --success: #10B981;
      --success-soft: #ECFDF5;
      --warning: #F59E0B;
      --warning-soft: #FFFBEB;
      --danger: #EF4444;
      --danger-soft: #FEF2F2;
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
      --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.07), 0 2px 4px -2px rgb(0 0 0 / 0.07);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.08), 0 4px 6px -4px rgb(0 0 0 / 0.04);
      --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.04);
      --radius: 12px;
      --radius-sm: 8px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: var(--bg);
      color: var(--text-main);
      line-height: 1.65;
      -webkit-font-smoothing: antialiased;
    }

    /* Scroll progress bar */
    #progress-bar {
      position: fixed;
      top: 0;
      left: 0;
      height: 3px;
      background: linear-gradient(90deg, #2563EB, #0EA5E9, #10B981);
      width: 0%;
      z-index: 2000;
      transition: width 0.1s ease;
    }

    /* Top Utility Bar */
    .top-bar {
      background: #0B132B;
      color: #94A3B8;
      font-size: 0.75rem;
      padding: 0.4rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(255,255,255,0.08);
    }
    .top-bar-tags { display: flex; gap: 1rem; align-items: center; }
    .status-pulse {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      color: #34D399;
      font-weight: 600;
    }
    .pulse-dot {
      width: 7px;
      height: 7px;
      background: #10B981;
      border-radius: 50%;
      box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7);
      animation: pulse 1.8s infinite;
    }
    @keyframes pulse {
      0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
      70% { box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }
      100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
    }

    /* Main Floating Header */
    header {
      background: rgba(15, 23, 42, 0.92);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      color: white;
      padding: 0.85rem 2rem;
      position: sticky;
      top: 0;
      z-index: 1000;
      border-bottom: 1px solid rgba(255,255,255,0.1);
      box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    }
    .header-content {
      max-width: 1320px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
      color: white;
    }
    .brand-logo {
      width: 36px;
      height: 36px;
      background: linear-gradient(135deg, #2563EB, #0EA5E9);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 1.1rem;
      box-shadow: 0 4px 10px rgba(37, 99, 235, 0.35);
    }
    .brand-text h1 { font-size: 1.15rem; font-weight: 700; letter-spacing: -0.3px; line-height: 1.2; }
    .brand-text p { font-size: 0.75rem; color: #94A3B8; }

    nav { display: flex; gap: 0.35rem; align-items: center; flex-wrap: wrap; }
    nav a {
      color: #CBD5E1;
      text-decoration: none;
      padding: 0.45rem 0.85rem;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 500;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
    }
    nav a:hover, nav a.active {
      color: white;
      background: rgba(255,255,255,0.12);
    }
    .nav-cta {
      background: #2563EB !important;
      color: white !important;
      font-weight: 600 !important;
      padding: 0.45rem 1rem !important;
      margin-left: 0.5rem;
      box-shadow: 0 2px 8px rgba(37, 99, 235, 0.4);
    }
    .nav-cta:hover { background: #1D4ED8 !important; }

    /* Layout Container */
    .container { max-width: 1320px; margin: 2rem auto; padding: 0 1.5rem; }

    /* HERO EXECUTIVE DASHBOARD BANNER */
    .hero-banner {
      background: linear-gradient(135deg, #0F172A 0%, #1E293B 50%, #0F284E 100%);
      border-radius: var(--radius);
      padding: 2.25rem;
      color: white;
      margin-bottom: 2rem;
      box-shadow: var(--shadow-xl);
      border: 1px solid rgba(255,255,255,0.1);
      position: relative;
      overflow: hidden;
    }
    .hero-banner::after {
      content: "";
      position: absolute;
      top: -50%;
      right: -20%;
      width: 450px;
      height: 450px;
      background: radial-gradient(circle, rgba(37,99,235,0.2) 0%, rgba(14,165,233,0) 70%);
      pointer-events: none;
    }
    .hero-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      flex-wrap: wrap;
      gap: 1.5rem;
      position: relative;
      z-index: 1;
    }
    .hero-badge-wrap { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 0.75rem; }
    .hero-tag {
      background: rgba(255,255,255,0.1);
      border: 1px solid rgba(255,255,255,0.15);
      font-size: 0.72rem;
      padding: 0.25rem 0.65rem;
      border-radius: 20px;
      font-weight: 600;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      color: #93C5FD;
    }
    .hero-title {
      font-size: 1.75rem;
      font-weight: 800;
      letter-spacing: -0.5px;
      margin-bottom: 0.5rem;
      line-height: 1.25;
    }
    .hero-subtitle {
      font-size: 0.95rem;
      color: #94A3B8;
      max-width: 720px;
      line-height: 1.5;
    }

    /* Quick KPI Grid inside Hero */
    .hero-kpis {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 1rem;
      margin-top: 1.75rem;
      position: relative;
      z-index: 1;
    }
    .kpi-stat-box {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: var(--radius-sm);
      padding: 1rem;
      backdrop-filter: blur(8px);
      transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .kpi-stat-box:hover {
      transform: translateY(-2px);
      border-color: rgba(37,99,235,0.5);
      background: rgba(255, 255, 255, 0.08);
    }
    .kpi-stat-label {
      font-size: 0.72rem;
      color: #94A3B8;
      text-transform: uppercase;
      font-weight: 600;
      letter-spacing: 0.5px;
    }
    .kpi-stat-val {
      font-size: 1.45rem;
      font-weight: 800;
      color: white;
      margin: 0.25rem 0;
      font-family: 'JetBrains Mono', monospace;
    }
    .kpi-stat-sub { font-size: 0.75rem; color: #38BDF8; font-weight: 500; }

    /* Team Pills Bar */
    .team-bar {
      margin-top: 1.5rem;
      padding-top: 1.25rem;
      border-top: 1px solid rgba(255,255,255,0.1);
      display: flex;
      align-items: center;
      gap: 1rem;
      flex-wrap: wrap;
      font-size: 0.82rem;
    }
    .team-lead-label { color: #94A3B8; font-weight: 600; }
    .team-chips { display: flex; gap: 0.75rem; flex-wrap: wrap; }
    .team-chip {
      background: rgba(255,255,255,0.08);
      border: 1px solid rgba(255,255,255,0.15);
      padding: 0.35rem 0.85rem;
      border-radius: 20px;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.78rem;
    }
    .chip-avatar {
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: #2563EB;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.65rem;
      font-weight: 700;
    }

    /* Content Sections */
    section {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2.25rem;
      margin-bottom: 2.25rem;
      box-shadow: var(--shadow-sm);
      scroll-margin-top: 5.5rem;
      transition: box-shadow 0.2s ease, border-color 0.2s ease;
    }
    section:hover {
      box-shadow: var(--shadow);
      border-color: #CBD5E1;
    }

    .section-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
      border-bottom: 2px solid var(--border-subtle);
      padding-bottom: 1.25rem;
      margin-bottom: 1.5rem;
    }
    .section-header-left { display: flex; align-items: center; gap: 0.75rem; }
    .section-num {
      background: var(--accent-soft);
      color: var(--accent);
      width: 38px;
      height: 38px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 1.1rem;
      border: 1px solid #BFDBFE;
    }
    .section-title h2 { font-size: 1.35rem; color: var(--primary); font-weight: 800; letter-spacing: -0.3px; }
    .section-title p { font-size: 0.82rem; color: var(--text-muted); }
    .lead-badge {
      background: #F1F5F9;
      color: #334155;
      border: 1px solid #E2E8F0;
      padding: 0.35rem 0.75rem;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
    }

    /* Narrative Paragraphs */
    .prose p {
      font-size: 0.92rem;
      color: var(--text-sub);
      line-height: 1.7;
      margin-bottom: 1rem;
    }
    .prose strong { color: var(--primary); font-weight: 700; }

    /* Tables */
    .table-container {
      overflow-x: auto;
      margin: 1.5rem 0;
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      box-shadow: var(--shadow-sm);
    }
    table { width: 100%; border-collapse: collapse; font-size: 0.85rem; }
    th, td { padding: 0.75rem 1rem; text-align: left; border-bottom: 1px solid var(--border); }
    th {
      background: #0F172A;
      color: white;
      font-weight: 600;
      font-size: 0.78rem;
      letter-spacing: 0.3px;
      text-transform: uppercase;
    }
    tbody tr:nth-child(even) { background: #F8FAFC; }
    tbody tr:hover { background: #F1F5F9; }
    td.font-mono { font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; }

    /* Badges */
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
      padding: 0.2rem 0.55rem;
      border-radius: 4px;
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.3px;
      text-transform: uppercase;
    }
    .badge-critical { background: #FEE2E2; color: #991B1B; border: 1px solid #FCA5A5; }
    .badge-high { background: #FFEDD5; color: #9A3412; border: 1px solid #FDBA74; }
    .badge-medium { background: #FEF3C7; color: #92400E; border: 1px solid #FCD34D; }
    .badge-low { background: #ECFDF5; color: #065F46; border: 1px solid #6EE7B7; }
    .badge-primary { background: #EFF6FF; color: #1E40AF; border: 1px solid #BFDBFE; }

    /* Visual Tri-part Analysis Box */
    .analysis-container {
      margin: 1.75rem 0 1rem 0;
      background: #F8FAFC;
      border: 1px solid #CBD5E1;
      border-radius: var(--radius-sm);
      overflow: hidden;
      box-shadow: var(--shadow-sm);
    }
    .analysis-header {
      background: #0F172A;
      color: white;
      padding: 0.75rem 1.25rem;
      font-size: 0.85rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .analysis-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      divide-x: 1px solid var(--border);
    }
    @media (max-width: 868px) {
      .analysis-grid { grid-template-columns: 1fr; }
    }
    .analysis-card {
      padding: 1.25rem;
      background: white;
      border-right: 1px solid var(--border);
      position: relative;
    }
    .analysis-card:last-child { border-right: none; }
    .analysis-card-title {
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      font-weight: 800;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }
    .analysis-card.shows .analysis-card-title { color: #0284C7; }
    .analysis-card.important .analysis-card-title { color: #D97706; }
    .analysis-card.decision .analysis-card-title { color: #059669; }
    .analysis-card p {
      font-size: 0.84rem;
      color: #334155;
      line-height: 1.55;
    }

    /* Diagram Card Frame */
    .diagram-card {
      background: white;
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 1.25rem;
      margin: 1.5rem 0;
      box-shadow: var(--shadow-sm);
    }
    .diagram-card-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1rem;
      padding-bottom: 0.5rem;
      border-bottom: 1px solid var(--border-subtle);
    }
    .diagram-card-head h3 { font-size: 0.95rem; font-weight: 700; color: var(--primary); }
    .diagram-caption {
      font-size: 0.78rem;
      color: var(--text-muted);
      text-align: center;
      margin-top: 0.75rem;
      font-style: italic;
    }

    /* Trello Live Banner */
    .trello-banner {
      background: linear-gradient(135deg, #026AA7 0%, #0079BF 100%);
      border-radius: var(--radius);
      padding: 1.5rem 1.75rem;
      color: white;
      margin: 1.5rem 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1.25rem;
      box-shadow: 0 10px 20px -5px rgba(0, 121, 191, 0.4);
    }
    .trello-left { display: flex; align-items: center; gap: 1rem; }
    .trello-icon-box {
      width: 48px;
      height: 48px;
      background: rgba(255,255,255,0.2);
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      flex-shrink: 0;
    }
    .trello-btn {
      background: white;
      color: #0079BF;
      text-decoration: none;
      padding: 0.65rem 1.25rem;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.85rem;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      box-shadow: var(--shadow);
      transition: all 0.2s ease;
    }
    .trello-btn:hover {
      transform: translateY(-2px);
      box-shadow: var(--shadow-lg);
      background: #F8FAFC;
    }

    /* EVM Live Metrics Card Bar */
    .evm-deck {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
      gap: 0.75rem;
      margin: 1.5rem 0;
    }
    .evm-metric-card {
      background: white;
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 1rem;
      text-align: center;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s ease;
    }
    .evm-metric-card:hover {
      transform: translateY(-2px);
      box-shadow: var(--shadow);
      border-color: #94A3B8;
    }
    .evm-label { font-size: 0.72rem; color: var(--text-muted); text-transform: uppercase; font-weight: 700; }
    .evm-val {
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--primary);
      margin: 0.35rem 0;
      font-family: 'JetBrains Mono', monospace;
    }
    .evm-val.negative { color: var(--danger); }
    .evm-val.warning { color: var(--warning); }
    .evm-val.positive { color: var(--success); }
    .evm-badge { font-size: 0.7rem; font-weight: 600; }

    /* Footer */
    footer {
      background: #0B132B;
      color: #94A3B8;
      padding: 3rem 2rem;
      font-size: 0.85rem;
      border-top: 1px solid rgba(255,255,255,0.08);
      margin-top: 4rem;
    }
    .footer-content {
      max-width: 1320px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1.5rem;
    }
    .footer-brand h4 { color: white; font-size: 1.1rem; margin-bottom: 0.25rem; }
    .footer-links a { color: #38BDF8; text-decoration: none; margin-left: 1rem; }
    .footer-links a:hover { text-decoration: underline; }
  </style>
</head>
<body>

<div id="progress-bar"></div>

<!-- Top Utility Metadata Bar -->
<div class="top-bar">
  <div class="top-bar-tags">
    <span><strong>Unit:</strong> BISY2004 Project Management</span>
    <span>•</span>
    <span><strong>Coursework:</strong> Assessment 2 (Secure Lane)</span>
    <span>•</span>
    <span><strong>Institution:</strong> Australian Institute of Higher Education</span>
  </div>
  <div class="status-pulse">
    <div class="pulse-dot"></div>
    <span>Status: Execution Phase (Week 14 Review Active)</span>
  </div>
</div>

<!-- Sticky Floating Navbar -->
<header>
  <div class="header-content">
    <a href="#" class="brand">
      <div class="brand-logo">OP</div>
      <div class="brand-text">
        <h1>OmniPortal Consolidation</h1>
        <p>Apex Metropolitan University (Scenario C)</p>
      </div>
    </a>
    <nav>
      <a href="#section1">1. Scope &amp; WBS</a>
      <a href="#section2">2. Schedule &amp; Cost</a>
      <a href="#section3">3. Risk &amp; Stakeholders</a>
      <a href="#section4">4. Quality &amp; Change</a>
      <a href="#section5">5. Dashboard &amp; EVM</a>
      <a href="#section6">6. Recommendation</a>
      <a href="https://trello.com/b/6aba6567933223c336fb8dfc/bisy2004-omniportal-student-portal-consolidation-%F0%9F%93%9A" target="_blank" class="nav-cta">
        Trello Board &nearr;
      </a>
    </nav>
  </div>
</header>

<div class="container">

  <!-- HERO EXECUTIVE DASHBOARD -->
  <div class="hero-banner">
    <div class="hero-top">
      <div>
        <div class="hero-badge-wrap">
          <span class="hero-tag">Scenario C</span>
          <span class="hero-tag">Hybrid Agile-Waterfall</span>
          <span class="hero-tag">Group XX Official Submission</span>
        </div>
        <h2 class="hero-title">OmniPortal: University Student Portal Consolidation</h2>
        <p class="hero-subtitle">
          An integrated project management framework consolidating 4 fragmented student-facing legacy systems into a unified, secure cloud portal with zero data loss, sub-1.8s page response, and 100% privacy compliance.
        </p>
      </div>
    </div>

    <!-- Quick Executive KPIs -->
    <div class="hero-kpis">
      <div class="kpi-stat-box">
        <div class="kpi-stat-label">Budget Cap</div>
        <div class="kpi-stat-val">$450,000</div>
        <div class="kpi-stat-sub">BAC Baseline: $385,000</div>
      </div>
      <div class="kpi-stat-box">
        <div class="kpi-stat-label">Project Window</div>
        <div class="kpi-stat-val">24 WEEKS</div>
        <div class="kpi-stat-sub">120 Working Days (Feb–Jul)</div>
      </div>
      <div class="kpi-stat-box">
        <div class="kpi-stat-label">Critical Path</div>
        <div class="kpi-stat-val">86 DAYS</div>
        <div class="kpi-stat-sub">Zero Float Sequence</div>
      </div>
      <div class="kpi-stat-box">
        <div class="kpi-stat-label">Student Records</div>
        <div class="kpi-stat-val">28,000</div>
        <div class="kpi-stat-sub">Target Fidelity: 100.0%</div>
      </div>
      <div class="kpi-stat-box">
        <div class="kpi-stat-label">Uptime SLA</div>
        <div class="kpi-stat-val">99.95%</div>
        <div class="kpi-stat-sub">12k Concurrent Users</div>
      </div>
    </div>

    <!-- Team Members Bar -->
    <div class="team-bar">
      <span class="team-lead-label">Core Project Management Team:</span>
      <div class="team-chips">
        <div class="team-chip">
          <span class="chip-avatar">TA</span>
          <span><strong>Tanvir Ahmed</strong> (238983) — Project Lead &amp; Systems Architect</span>
        </div>
        <div class="team-chip">
          <span class="chip-avatar">MA</span>
          <span><strong>Momen Ahmed</strong> (242048) — Risk, Finance &amp; Governance Lead</span>
        </div>
        <div class="team-chip">
          <span class="chip-avatar">RM</span>
          <span><strong>MD Rejvi Jaman Mafti</strong> (241964) — Quality, Delivery &amp; Tracking Lead</span>
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- SECTION 1 -->
  <!-- ========================================================================= -->
  <section id="section1">
    <div class="section-header">
      <div class="section-header-left">
        <div class="section-num">01</div>
        <div class="section-title">
          <h2>Project Overview, Charter &amp; Scope</h2>
          <p>Institutional business need, purpose, lifecycle governance, and WBS architecture</p>
        </div>
      </div>
      <span class="lead-badge">👤 Lead: Tanvir Ahmed (238983)</span>
    </div>

    <div class="prose">
      <p><strong>Business Need &amp; Problem:</strong> Apex Metropolitan University (28,000 students, 3,200 staff) currently operates four disconnected student-facing portals: a legacy Blackboard LMS, Ellucian Banner SIS for enrolment, TouchNet for fee billing, and Zendesk for student support. Disjointed logins force students across multiple interfaces, generating 4,200 repetitive helpdesk calls per semester, an 18% record desynchronization rate, and $185,000 in annual multi-vendor maintenance contracts.</p>
      
      <p><strong>Project Purpose &amp; SMART Objectives:</strong> The purpose of Project OmniPortal is to consolidate all student-facing administrative and academic workflows into a single cloud-native responsive platform. The four core project objectives are: (1) <strong>Schedule:</strong> Deliver production cutover within 24 calendar weeks (120 working days) prior to Semester 1 enrolment; (2) <strong>Cost:</strong> Restrict total expenditure to the approved $450,000 AUD budget envelope; (3) <strong>Quality &amp; Scope:</strong> Achieve 100% data fidelity migrating 28,000 student academic profiles with zero record loss; and (4) <strong>Performance:</strong> Attain 99.95% system uptime under peak concurrent loads (&lt;1.80s page load at 12,000 sessions).</p>

      <p><strong>Development Lifecycle:</strong> A <strong>Hybrid Agile-Waterfall</strong> methodology is deployed. Predictive Waterfall governance manages charter sign-off, enterprise architecture, security compliance, and final blue-green cutover. Two-week Agile sprints execute iterative UX prototyping, feature coding, and automated ETL data migration scripts.</p>
    </div>

    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th style="width: 50%;">In-Scope Deliverables (100% Boundary)</th>
            <th style="width: 50%;">Explicit Project Exclusions (Out of Scope)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              • Centralized Single Sign-On (SSO) with Multi-Factor Authentication (MFA).<br>
              • Real-time course cart enrolment, timetable scheduler, and fee processing.<br>
              • Automated ETL migration of 28,000 student historical academic profiles.<br>
              • WCAG 2.1 AA accessible web client and responsive mobile interface.
            </td>
            <td>
              • Migration of legacy human resource and employee payroll systems.<br>
              • Development of native iOS/Android binary compiled app store packages.<br>
              • Overhaul of physical student smartcard campus turnstiles.<br>
              • Ongoing operational tier-1 helpdesk staffing beyond hypercare.
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- WBS SVG Diagram Frame -->
    <div class="diagram-card">
      <div class="diagram-card-head">
        <h3>Work Breakdown Structure (WBS) Architecture</h3>
        <span class="badge badge-primary">100% Rule Compliant</span>
      </div>
      <svg viewBox="0 0 1000 320" style="width:100%; max-height:320px; font-family:'Plus Jakarta Sans', sans-serif; font-size:11px;">
        <rect x="360" y="10" width="280" height="45" rx="6" fill="#0F172A"/>
        <text x="500" y="32" fill="#fff" text-anchor="middle" font-weight="700">PROJECT OMNIPORTAL (WBS 0.0)</text>
        <text x="500" y="47" fill="#38BDF8" text-anchor="middle" font-size="9.5">Budget: $450k | Duration: 24 Weeks (120 Days)</text>

        <!-- Connecting lines -->
        <path d="M500,55 L500,70 M85,70 L910,70 M85,70 L85,85 M250,70 L250,85 M415,70 L415,85 M580,70 L580,85 M745,70 L745,85 M910,70 L910,85" stroke="#0F172A" stroke-width="1.5" fill="none"/>

        <!-- Level 1 Boxes -->
        <g transform="translate(10, 85)">
          <rect x="0" y="0" width="150" height="40" rx="6" fill="#1E293B"/>
          <text x="75" y="18" fill="#fff" text-anchor="middle" font-weight="700">1.0 Initiation</text>
          <text x="75" y="32" fill="#94A3B8" text-anchor="middle" font-size="9">15 Days | $16.5k</text>
        </g>
        <g transform="translate(175, 85)">
          <rect x="0" y="0" width="150" height="40" rx="6" fill="#1E293B"/>
          <text x="75" y="18" fill="#fff" text-anchor="middle" font-weight="700">2.0 Requirements</text>
          <text x="75" y="32" fill="#94A3B8" text-anchor="middle" font-size="9">20 Days | $31.2k</text>
        </g>
        <g transform="translate(340, 85)">
          <rect x="0" y="0" width="150" height="40" rx="6" fill="#1E293B"/>
          <text x="75" y="18" fill="#fff" text-anchor="middle" font-weight="700">3.0 Data Migration</text>
          <text x="75" y="32" fill="#94A3B8" text-anchor="middle" font-size="9">25 Days | $39.5k</text>
        </g>
        <g transform="translate(505, 85)">
          <rect x="0" y="0" width="150" height="40" rx="6" fill="#1E293B"/>
          <text x="75" y="18" fill="#fff" text-anchor="middle" font-weight="700">4.0 Core Dev</text>
          <text x="75" y="32" fill="#94A3B8" text-anchor="middle" font-size="9">35 Days | $68.0k</text>
        </g>
        <g transform="translate(670, 85)">
          <rect x="0" y="0" width="150" height="40" rx="6" fill="#1E293B"/>
          <text x="75" y="18" fill="#fff" text-anchor="middle" font-weight="700">5.0 QA &amp; Testing</text>
          <text x="75" y="32" fill="#94A3B8" text-anchor="middle" font-size="9">20 Days | $34.8k</text>
        </g>
        <g transform="translate(835, 85)">
          <rect x="0" y="0" width="150" height="40" rx="6" fill="#1E293B"/>
          <text x="75" y="18" fill="#fff" text-anchor="middle" font-weight="700">6.0 Deployment</text>
          <text x="75" y="32" fill="#94A3B8" text-anchor="middle" font-size="9">15 Days | $24.2k</text>
        </g>

        <!-- Level 2 Sub-packages -->
        <g transform="translate(10, 135)">
          <rect x="0" y="0" width="150" height="165" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
          <text x="10" y="22" font-weight="600" fill="#1E293B">1.1 Charter &amp; Sign-off</text>
          <text x="10" y="46" font-weight="600" fill="#1E293B">1.2 PMP &amp; Risk Plan</text>
          <text x="10" y="70" font-weight="600" fill="#1E293B">1.3 Governance Kickoff</text>
          <rect x="6" y="88" width="138" height="24" rx="4" fill="#FEF3C7" stroke="#FCD34D"/>
          <text x="75" y="104" fill="#92400E" font-weight="700" font-size="9" text-anchor="middle">◆ M1: Charter Signed</text>
        </g>
        <g transform="translate(175, 135)">
          <rect x="0" y="0" width="150" height="165" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
          <text x="10" y="22" font-weight="600" fill="#1E293B">2.1 Requirements Spec</text>
          <text x="10" y="46" font-weight="600" fill="#1E293B">2.2 Privacy / APP Review</text>
          <text x="10" y="70" font-weight="600" fill="#1E293B">2.3 Cloud Spec (AWS)</text>
          <text x="10" y="94" font-weight="600" fill="#1E293B">2.4 API Protocols</text>
          <rect x="6" y="112" width="138" height="24" rx="4" fill="#FEF3C7" stroke="#FCD34D"/>
          <text x="75" y="128" fill="#92400E" font-weight="700" font-size="9" text-anchor="middle">◆ M2: Spec Approved</text>
        </g>
        <g transform="translate(340, 135)">
          <rect x="0" y="0" width="150" height="165" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
          <text x="10" y="22" font-weight="600" fill="#1E293B">3.1 Data Cleansing</text>
          <rect x="6" y="32" width="138" height="24" rx="4" fill="#FEE2E2" stroke="#FCA5A5"/>
          <text x="75" y="48" fill="#991B1B" font-weight="800" font-size="9.5" text-anchor="middle">3.2 Automated ETL*</text>
          <text x="10" y="76" font-weight="600" fill="#1E293B">3.3 Schema Tuning</text>
          <text x="10" y="98" font-weight="600" fill="#1E293B">3.4 Encryption / RBAC</text>
          <rect x="6" y="115" width="138" height="24" rx="4" fill="#FEF3C7" stroke="#FCD34D"/>
          <text x="75" y="131" fill="#92400E" font-weight="700" font-size="9" text-anchor="middle">◆ M3: ETL Ready</text>
        </g>
        <g transform="translate(505, 135)">
          <rect x="0" y="0" width="150" height="165" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
          <text x="10" y="22" font-weight="600" fill="#1E293B">4.1 Sprint 1: SSO/MFA</text>
          <text x="10" y="44" font-weight="600" fill="#1E293B">4.2 Sprint 2: Records</text>
          <text x="10" y="66" font-weight="600" fill="#1E293B">4.3 Sprint 3: Enrolment</text>
          <text x="10" y="88" font-weight="600" fill="#1E293B">4.4 Sprint 4: Payment</text>
          <text x="10" y="110" font-weight="600" fill="#1E293B">4.5 Sprint 5: Mobile UI</text>
          <rect x="6" y="128" width="138" height="24" rx="4" fill="#FEF3C7" stroke="#FCD34D"/>
          <text x="75" y="144" fill="#92400E" font-weight="700" font-size="9" text-anchor="middle">◆ M4: Features Done</text>
        </g>
        <g transform="translate(670, 135)">
          <rect x="0" y="0" width="150" height="165" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
          <text x="10" y="22" font-weight="600" fill="#1E293B">5.1 Load &amp; Stress Test</text>
          <text x="10" y="46" font-weight="600" fill="#1E293B">5.2 Security Pentest</text>
          <text x="10" y="70" font-weight="600" fill="#1E293B">5.3 User Acceptance</text>
          <text x="10" y="94" font-weight="600" fill="#1E293B">5.4 Defect Fixes</text>
          <rect x="6" y="112" width="138" height="24" rx="4" fill="#FEF3C7" stroke="#FCD34D"/>
          <text x="75" y="128" fill="#92400E" font-weight="700" font-size="9" text-anchor="middle">◆ M5: UAT Signed Off</text>
        </g>
        <g transform="translate(835, 135)">
          <rect x="0" y="0" width="150" height="165" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
          <text x="10" y="22" font-weight="600" fill="#1E293B">6.1 User Guides/Media</text>
          <text x="10" y="46" font-weight="600" fill="#1E293B">6.2 Staff Onboarding</text>
          <text x="10" y="70" font-weight="600" fill="#1E293B">6.3 Blue-Green Cutover</text>
          <text x="10" y="94" font-weight="600" fill="#1E293B">6.4 PIR &amp; Lessons</text>
          <rect x="6" y="112" width="138" height="24" rx="4" fill="#FEF3C7" stroke="#FCD34D"/>
          <text x="75" y="128" fill="#92400E" font-weight="700" font-size="9" text-anchor="middle">◆ M6: Closed</text>
        </g>
      </svg>
      <div class="diagram-caption">WBS Breakdown across 6 Functional Work Packages (*Red denotes Critical Path task). Source: diagrams.net (<code>A2_Group_WBS_Diagram.drawio</code>).</div>
    </div>

    <!-- Tri-part Analysis Box -->
    <div class="analysis-container">
      <div class="analysis-header">
        <span>🔍 Section 1 Artefact Interpretation &amp; Management Logic</span>
      </div>
      <div class="analysis-grid">
        <div class="analysis-card shows">
          <div class="analysis-card-title">👁️ What it Shows</div>
          <p>The 100% rule-compliant hierarchical breakdown decomposes project scope into 6 major deliverables, 28 discrete work packages, and 6 formal milestone quality gates.</p>
        </div>
        <div class="analysis-card important">
          <div class="analysis-card-title">⚡ Why it is Important</div>
          <p>It establishes clear work package ownership, boundaries between in-scope features and excluded legacy HR systems, and provides the baseline for ProjectLibre schedule mapping.</p>
        </div>
        <div class="analysis-card decision">
          <div class="analysis-card-title">🎯 Management Decision</div>
          <p>Enforced a strict scope freeze following Milestone 2 sign-off. Any additional functional requests must submit formal Change Requests to prevent uncontrolled scope creep.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- SECTION 2 -->
  <!-- ========================================================================= -->
  <section id="section2">
    <div class="section-header">
      <div class="section-header-left">
        <div class="section-num">02</div>
        <div class="section-title">
          <h2>Schedule, Cost &amp; Resources</h2>
          <p>ProjectLibre Gantt analysis, 86-day critical path, and bottom-up cost model</p>
        </div>
      </div>
      <span class="lead-badge">👤 Lead: Tanvir Ahmed &amp; Momen Ahmed</span>
    </div>

    <div class="prose">
      <p><strong>ProjectLibre Scheduling &amp; Critical Path:</strong> The ProjectLibre schedule models 120 working days across a 24-calendar-week duration (02-Feb-2026 to 17-Jul-2026). The Critical Path spans <strong>1.1 &rarr; 1.2 &rarr; 1.3 &rarr; 2.1 &rarr; 2.3 &rarr; 2.4 &rarr; 3.1 &rarr; 3.2 &rarr; 3.3 &rarr; 4.1 &rarr; 4.2 &rarr; 4.3 &rarr; 4.4 &rarr; 5.1 &rarr; 5.2 &rarr; 5.3 &rarr; 5.4 &rarr; 6.3 &rarr; 6.4</strong>. Any slip along this 86-working-day path directly extends the project completion date beyond Semester 1 enrolment.</p>
    </div>

    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>Milestone</th>
            <th>Deliverable Name</th>
            <th style="text-align: center;">Scheduled Date</th>
            <th style="text-align: center;">Total Float</th>
            <th>Approval Authority</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>M1</strong></td>
            <td>Project Charter &amp; Governance Framework Signed Off</td>
            <td style="text-align: center;" class="font-mono">20-Feb-2026</td>
            <td style="text-align: center;"><span class="badge badge-critical">0 Days</span></td>
            <td>CIO / Project Sponsor</td>
          </tr>
          <tr>
            <td><strong>M2</strong></td>
            <td>Technical Architecture &amp; API Specifications Approved</td>
            <td style="text-align: center;" class="font-mono">20-Mar-2026</td>
            <td style="text-align: center;"><span class="badge badge-critical">0 Days</span></td>
            <td>Lead Solutions Architect</td>
          </tr>
          <tr>
            <td><strong>M3</strong></td>
            <td>Data Cleansing &amp; Automated ETL Scripts Validated</td>
            <td style="text-align: center;" class="font-mono">24-Apr-2026</td>
            <td style="text-align: center;"><span class="badge badge-critical">0 Days</span></td>
            <td>Database &amp; Migration Lead</td>
          </tr>
          <tr>
            <td><strong>M4</strong></td>
            <td>Core Portal Development Feature Complete</td>
            <td style="text-align: center;" class="font-mono">12-Jun-2026</td>
            <td style="text-align: center;"><span class="badge badge-critical">0 Days</span></td>
            <td>Lead Software Engineer &amp; PM</td>
          </tr>
          <tr>
            <td><strong>M5</strong></td>
            <td>UAT &amp; Independent Security Penetration Sign-Off</td>
            <td style="text-align: center;" class="font-mono">10-Jul-2026</td>
            <td style="text-align: center;"><span class="badge badge-critical">0 Days</span></td>
            <td>University Registrar &amp; Security Officer</td>
          </tr>
          <tr>
            <td><strong>M6</strong></td>
            <td>Production Cutover &amp; Final Operational Handover</td>
            <td style="text-align: center;" class="font-mono">17-Jul-2026</td>
            <td style="text-align: center;"><span class="badge badge-critical">0 Days</span></td>
            <td>CIO &amp; Steering Committee</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="prose">
      <p><strong>Cost &amp; Resource Allocation:</strong> Direct internal and contracted labor totals $219,600 (305 resource days across PM, Architect, Devs, DB specialist, and QA). Capital expenditure (Capex) totals $90,500, covering AWS multi-AZ infrastructure ($28,500), Okta SSO licences ($24,000), CREST penetration testing ($16,500), and training media ($9,500). Base Budget at Completion (BAC) is <strong>$385,000 AUD</strong>. Adding a 10% technical Contingency Reserve ($38,500) yields a Cost Baseline of <strong>$423,500 AUD</strong>. A 5% Management Reserve ($19,250) brings total allocated budget to <strong>$442,750 AUD</strong>, leaving $7,250 headroom below the $450,000 institutional cap.</p>
    </div>

    <!-- Tri-part Analysis Box -->
    <div class="analysis-container">
      <div class="analysis-header">
        <span>🔍 Section 2 Artefact Interpretation &amp; Management Logic</span>
      </div>
      <div class="analysis-grid">
        <div class="analysis-card shows">
          <div class="analysis-card-title">👁️ What it Shows</div>
          <p>The ProjectLibre Gantt chart reveals zero total float along the database migration (WBS 3.2) and payment integration (WBS 4.4) sequences, proving they dictate the project finish date.</p>
        </div>
        <div class="analysis-card important">
          <div class="analysis-card-title">⚡ Why it is Important</div>
          <p>It alerts management that non-critical activities (such as staff training guides with 8 days float) can be delayed without risk, whereas any delay in ETL scripts directly threatens the Semester 1 go-live.</p>
        </div>
        <div class="analysis-card decision">
          <div class="analysis-card-title">🎯 Management Decision</div>
          <p>Authorized ring-fenced resource allocation for the Senior Database Engineer and pre-approved the drawdown of $6,800 from contingency reserves if ETL test runs fall more than 3 days behind.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- SECTION 3 -->
  <!-- ========================================================================= -->
  <section id="section3">
    <div class="section-header">
      <div class="section-header-left">
        <div class="section-num">03</div>
        <div class="section-title">
          <h2>Risk, Stakeholder &amp; Communication</h2>
          <p>5×5 Risk matrix scoring, quadrant stakeholder mapping, and communication rhythms</p>
        </div>
      </div>
      <span class="lead-badge">👤 Lead: Momen Ahmed (242048)</span>
    </div>

    <div class="prose">
      <p><strong>Risk Assessment &amp; 5×5 Scoring:</strong> Risks are evaluated using a standard 5×5 matrix where <code>Score = Likelihood (1–5) × Impact (1–5)</code>. Ten active risks are monitored in the Risk Register. The top prioritized risks are:</p>
    </div>

    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Risk Description</th>
            <th style="text-align: center;">L</th>
            <th style="text-align: center;">I</th>
            <th style="text-align: center;">Score</th>
            <th>Priority</th>
            <th>Owner</th>
            <th>Mitigation &amp; Contingency Action</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="font-mono"><strong>R01</strong></td>
            <td>Legacy database schema mismatch &amp; student record corruption</td>
            <td style="text-align: center;">4</td>
            <td style="text-align: center;">5</td>
            <td style="text-align: center;" class="font-mono"><strong>20</strong></td>
            <td><span class="badge badge-critical">Extreme</span></td>
            <td>Momen Ahmed</td>
            <td>Execute staged ETL runs with 10% sandbox sampling; automated checksum validation with instant rollback.</td>
          </tr>
          <tr>
            <td class="font-mono"><strong>R02</strong></td>
            <td>Cloud infrastructure outage during peak enrolment surge (&gt;10k users)</td>
            <td style="text-align: center;">3</td>
            <td style="text-align: center;">5</td>
            <td style="text-align: center;" class="font-mono"><strong>15</strong></td>
            <td><span class="badge badge-critical">Extreme</span></td>
            <td>Tanvir Ahmed</td>
            <td>Configure AWS Elastic Load Balancing and Redis cache; conduct load testing at 250% capacity (15,000 sessions).</td>
          </tr>
          <tr>
            <td class="font-mono"><strong>R03</strong></td>
            <td>Faculty and administrative staff resistance to adopting new portal</td>
            <td style="text-align: center;">4</td>
            <td style="text-align: center;">3</td>
            <td style="text-align: center;" class="font-mono"><strong>12</strong></td>
            <td><span class="badge badge-high">High</span></td>
            <td>MD Rejvi Jaman</td>
            <td>Mobilize 12 departmental 'Change Champions'; deliver 30-min drop-in clinics and interactive micro-videos.</td>
          </tr>
          <tr>
            <td class="font-mono"><strong>R04</strong></td>
            <td>Student PII data breach violating Australian Privacy Principles (APP)</td>
            <td style="text-align: center;">2</td>
            <td style="text-align: center;">5</td>
            <td style="text-align: center;" class="font-mono"><strong>10</strong></td>
            <td><span class="badge badge-high">High</span></td>
            <td>Tanvir Ahmed</td>
            <td>Enforce AES-256 at-rest and TLS 1.3 encryption; mandate independent CREST security penetration audit.</td>
          </tr>
          <tr>
            <td class="font-mono"><strong>R05</strong></td>
            <td>Scope creep driven by conflicting faculty feature customizations</td>
            <td style="text-align: center;">4</td>
            <td style="text-align: center;">3</td>
            <td style="text-align: center;" class="font-mono"><strong>12</strong></td>
            <td><span class="badge badge-high">High</span></td>
            <td>Tanvir Ahmed</td>
            <td>Strict CCB governance; non-standard functional requests deferred to Phase 2 enhancement backlog.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="prose">
      <p><strong>Stakeholder Engagement &amp; Power-Interest Mapping:</strong> Stakeholders are segmented into four distinct engagement strategies:</p>
      <ul style="margin-left: 1.5rem; margin-bottom: 1rem; font-size: 0.9rem; color: var(--text-sub);">
        <li><strong>Manage Closely (High Power, High Interest):</strong> CIO / Project Sponsor (SH01), University Registrar (SH02), and Central IT Security (SH05). Managed through weekly 1-on-1 briefings and formal fortnightly Steering Committee governance.</li>
        <li><strong>Keep Satisfied (High Power, Low Interest):</strong> Academic Senate &amp; Faculty Deans (SH03), TEQSA Regulators (SH08), and University Finance (SH06). Managed via monthly executive summaries and automated audit compliance logs.</li>
        <li><strong>Keep Informed (Low Power, High Interest):</strong> Student Council &amp; 28k Students (SH04), Helpdesk Staff (SH07). Managed through bi-weekly email bulletins, beta focus groups, and live training webinars.</li>
      </ul>
    </div>

    <!-- Tri-part Analysis Box -->
    <div class="analysis-container">
      <div class="analysis-header">
        <span>🔍 Section 3 Artefact Interpretation &amp; Management Logic</span>
      </div>
      <div class="analysis-grid">
        <div class="analysis-card shows">
          <div class="analysis-card-title">👁️ What it Shows</div>
          <p>The 5×5 heat map clusters technical migration (R01, score 20) and peak infrastructure scalability (R02, score 15) in the critical red zone.</p>
        </div>
        <div class="analysis-card important">
          <div class="analysis-card-title">⚡ Why it is Important</div>
          <p>It justifies shifting project expenditure toward automated verification scripts and cloud redundancy rather than superficial cosmetic features.</p>
        </div>
        <div class="analysis-card decision">
          <div class="analysis-card-title">🎯 Management Decision</div>
          <p>Reallocated $16,500 of the Capex budget to commission an external CREST-certified penetration testing firm and scheduled load tests during off-peak hours at 2.5× peak capacity.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- SECTION 4 -->
  <!-- ========================================================================= -->
  <section id="section4">
    <div class="section-header">
      <div class="section-header-left">
        <div class="section-num">04</div>
        <div class="section-title">
          <h2>Quality, Change &amp; Team Structure</h2>
          <p>Quantified quality gates, formal change evaluation (CR-01), and RACI accountability</p>
        </div>
      </div>
      <span class="lead-badge">👤 Lead: MD Rejvi Jaman Mafti (241964)</span>
    </div>

    <div class="prose">
      <p><strong>Quality Assurance &amp; Control Metrics:</strong> Quality is governed by quantifiable acceptance criteria rather than subjective assessments. The six binding project standards are:</p>
    </div>

    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>Quality Objective</th>
            <th>Target Metric / KPI</th>
            <th style="text-align: center;">Threshold</th>
            <th>Verification Method</th>
            <th>Control Action if Breached</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>System Availability</td>
            <td>Uptime during semester terms</td>
            <td style="text-align: center;" class="font-mono"><strong>&ge; 99.95%</strong></td>
            <td>AWS CloudWatch Synthetics</td>
            <td>Failover to standby AWS multi-AZ instance; page on-call DevOps engineer.</td>
          </tr>
          <tr>
            <td>Peak Concurrency</td>
            <td>Response time at 12k sessions</td>
            <td style="text-align: center;" class="font-mono"><strong>&lt; 1.80s</strong></td>
            <td>JMeter automated load suite</td>
            <td>Scale ECS container tasks; optimize Redis query caching.</td>
          </tr>
          <tr>
            <td>Migration Fidelity</td>
            <td>Academic record checksum match</td>
            <td style="text-align: center;" class="font-mono"><strong>100.0%</strong></td>
            <td>Automated SHA-256 hash checks</td>
            <td>Halt migration pipeline, execute automated DB rollback to snapshot.</td>
          </tr>
          <tr>
            <td>Defect Density</td>
            <td>Open defects at UAT sign-off</td>
            <td style="text-align: center;" class="font-mono"><strong>0 P1 / 0 P2</strong></td>
            <td>Jira defect tracker scrub</td>
            <td>Enforce mandatory code freeze dedicated solely to bug remediation.</td>
          </tr>
          <tr>
            <td>Usability</td>
            <td>System Usability Scale (SUS)</td>
            <td style="text-align: center;" class="font-mono"><strong>&ge; 80 / 100</strong></td>
            <td>50-student beta pilot survey</td>
            <td>Execute targeted 3-day UI polish sprint on low-scoring workflows.</td>
          </tr>
          <tr>
            <td>Cybersecurity</td>
            <td>Unresolved vulnerabilities</td>
            <td style="text-align: center;" class="font-mono"><strong>Zero High/Crit</strong></td>
            <td>Independent CREST pentest</td>
            <td>Patch code vulnerabilities within 72 hours; rerun penetration scan.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="prose">
      <p><strong>Change Control Decision (Change Request CR-01):</strong> On 14-Apr-2026, the University Cybersecurity Advisory Board mandated Multi-Factor Authentication (MFA) following updated Australian Cyber Security Centre (ACSC) Essential Eight guidance. The Change Control Board (CCB) conducted impact analysis: (1) <em>Scope:</em> Add Twilio SMS and TOTP authenticator hooks; (2) <em>Schedule:</em> +8 working days in authentication development, absorbed by fast-tracking UI testing in parallel with Sprint 2 (zero delay to go-live); (3) <em>Cost:</em> +$14,500 AUD funded entirely from the $38,500 Contingency Reserve; (4) <em>Risk:</em> Drastically mitigates PII data breach risk R04. The CCB <strong>APPROVED</strong> CR-01.</p>
    </div>

    <!-- Tri-part Analysis Box -->
    <div class="analysis-container">
      <div class="analysis-header">
        <span>🔍 Section 4 Artefact Interpretation &amp; Management Logic</span>
      </div>
      <div class="analysis-grid">
        <div class="analysis-card shows">
          <div class="analysis-card-title">👁️ What it Shows</div>
          <p>The RACI matrix clearly separates single-point accountability (Accountable = PM/CIO) from task execution (Responsible = Technical Leads), preventing overlapping authority.</p>
        </div>
        <div class="analysis-card important">
          <div class="analysis-card-title">⚡ Why it is Important</div>
          <p>It documents that CR-01 was absorbed through formal governance, utilizing pre-planned contingency funds rather than causing an unmanaged scope blow-out.</p>
        </div>
        <div class="analysis-card decision">
          <div class="analysis-card-title">🎯 Management Decision</div>
          <p>Authorized drawing $14,500 from the Contingency Reserve to fund CR-01 while enforcing an immediate scope freeze on all subsequent non-mandatory enhancement requests.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- SECTION 5 -->
  <!-- ========================================================================= -->
  <section id="section5">
    <div class="section-header">
      <div class="section-header-left">
        <div class="section-num">05</div>
        <div class="section-title">
          <h2>Tracking &amp; Project Dashboard</h2>
          <p>Trello Kanban board linkage, Week 14 EVM review, and schedule crashing recovery</p>
        </div>
      </div>
      <span class="lead-badge">👤 Lead: MD Rejvi Jaman Mafti (241964)</span>
    </div>

    <div class="prose">
      <p><strong>Mid-Project Performance Review (Week 14 Status Snapshot):</strong> Project tracking combines Trello sprint boards for daily task workflow (To Do, In Progress, Review/QA, Done) with Earned Value Management (EVM) in Excel to monitor schedule and budget performance against the baseline.</p>
    </div>

    <!-- Live Trello Board Callout Banner -->
    <div class="trello-banner">
      <div class="trello-left">
        <div class="trello-icon-box">📋</div>
        <div>
          <h3 style="font-size: 1.1rem; font-weight: 800; margin-bottom: 0.25rem;">Live Trello Kanban Board (Public Access Active)</h3>
          <p style="font-size: 0.85rem; opacity: 0.9; max-width: 650px;">
            Traceability verified: 20 active cards carrying direct WBS codes across 5 lists (Backlog, To Do, In Progress, Review/Testing, and Done). Inspect active bottleneck card <code>[WBS 3.2]</code>.
          </p>
        </div>
      </div>
      <a href="https://trello.com/b/6aba6567933223c336fb8dfc/bisy2004-omniportal-student-portal-consolidation-%F0%9F%93%9A" target="_blank" class="trello-btn">
        <span>Open Public Trello Board</span>
        <span>&rarr;</span>
      </a>
    </div>

    <!-- EVM KPI Cards Deck -->
    <div class="evm-deck">
      <div class="evm-metric-card">
        <div class="evm-label">Planned Value (PV)</div>
        <div class="evm-val">$225,000</div>
        <span class="evm-badge" style="color:var(--text-muted);">Baseline Wk 14</span>
      </div>
      <div class="evm-metric-card">
        <div class="evm-label">Earned Value (EV)</div>
        <div class="evm-val">$198,000</div>
        <span class="evm-badge" style="color:#2563EB;">51.4% Physical Work</span>
      </div>
      <div class="evm-metric-card">
        <div class="evm-label">Actual Cost (AC)</div>
        <div class="evm-val">$210,000</div>
        <span class="evm-badge" style="color:var(--text-muted);">Incurred Spend</span>
      </div>
      <div class="evm-metric-card">
        <div class="evm-label">Schedule Var (SV)</div>
        <div class="evm-val negative">-$27,000</div>
        <span class="evm-badge" style="color:var(--danger);">10 Days Behind</span>
      </div>
      <div class="evm-metric-card">
        <div class="evm-label">Cost Var (CV)</div>
        <div class="evm-val negative">-$12,000</div>
        <span class="evm-badge" style="color:var(--danger);">Unfavourable</span>
      </div>
      <div class="evm-metric-card">
        <div class="evm-label">SPI (EV/PV)</div>
        <div class="evm-val warning">0.880</div>
        <span class="evm-badge" style="color:var(--warning);">Delay Flagged</span>
      </div>
      <div class="evm-metric-card">
        <div class="evm-label">CPI (EV/AC)</div>
        <div class="evm-val warning">0.943</div>
        <span class="evm-badge" style="color:var(--warning);">Cost Warning</span>
      </div>
    </div>

    <div class="prose">
      <p><strong>Variance Root Cause Analysis &amp; Corrective Action:</strong></p>
      <ul style="margin-left: 1.5rem; margin-bottom: 1rem; font-size: 0.9rem; color: var(--text-sub);">
        <li><strong>Variance Identification:</strong> At Week 14, EV ($198k) lags PV ($225k) by $27,000, yielding an SPI of 0.880 (10 working days behind schedule on critical path task 3.2: Automated ETL Scripts). CPI is 0.943 ($12k cost overrun).</li>
        <li><strong>Root Cause:</strong> Legacy Ellucian Banner tables contained unindexed foreign keys and corrupted historical address fields, causing automated migration scripts to fail checksum tests and require manual data cleansing.</li>
        <li><strong>Corrective Management Action:</strong> (1) <em>Schedule Crashing:</em> Released $6,800 from Contingency Reserve to contract an external Senior ETL Engineer for two weeks; (2) <em>Fast-Tracking:</em> Re-sequenced Sprint 3 course enrolment frontend development using simulated mock data in parallel with backend ETL scripts; (3) <em>Outcome:</em> Recovered 7 of the 10 lost days by Week 16, restoring SPI to 0.96 and safeguarding the critical path.</li>
      </ul>
    </div>

    <!-- Tri-part Analysis Box -->
    <div class="analysis-container">
      <div class="analysis-header">
        <span>🔍 Section 5 Artefact Interpretation &amp; Management Logic</span>
      </div>
      <div class="analysis-grid">
        <div class="analysis-card shows">
          <div class="analysis-card-title">👁️ What it Shows</div>
          <p>The EVM metrics reveal that work progress slipped 12% behind baseline at Week 14 due to an isolated technical bottleneck in legacy database migration.</p>
        </div>
        <div class="analysis-card important">
          <div class="analysis-card-title">⚡ Why it is Important</div>
          <p>It demonstrates that the delay was caught early through objective variance metrics rather than being discovered during deployment.</p>
        </div>
        <div class="analysis-card decision">
          <div class="analysis-card-title">🎯 Management Decision</div>
          <p>Approved an evidence-backed intervention combining schedule crashing ($6.8k contingency spend) and fast-tracking, pulling the project back to on-schedule status without compromising quality.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- SECTION 6 -->
  <!-- ========================================================================= -->
  <section id="section6">
    <div class="section-header">
      <div class="section-header-left">
        <div class="section-num">06</div>
        <div class="section-title">
          <h2>Integration &amp; Final Management Recommendation</h2>
          <p>Cross-domain alignment synthesis and empirical justification for production cutover</p>
        </div>
      </div>
      <span class="lead-badge">👥 Group Collaborative Synthesis</span>
    </div>

    <div class="prose">
      <p><strong>Artefact Integration &amp; Alignment Synthesis:</strong> Project OmniPortal demonstrates rigorous methodological alignment across all six PM knowledge domains. The business problem (fragmented student experience and high support costs) directly informed the Charter purpose and Scope statement. The Scope was partitioned through the WBS into 28 work packages, which were directly transcribed into the ProjectLibre schedule and mirrored on the Trello board. Resource costing derived the $385,000 BAC baseline. The 5×5 Risk Register anticipated database migration failure, which informed the Week 14 EVM variance response and justified the $38,500 Contingency Reserve. Finally, Quality metrics and Change Request CR-01 ensured compliance with federal cybersecurity directives without delaying production cutover.</p>
    </div>

    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>Knowledge Domain</th>
            <th>Primary Artefact</th>
            <th>Integrated Linkage to Subsequent PM Domain</th>
            <th style="text-align: center;">Integrity Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Scope Management</strong></td>
            <td>WBS &amp; Dictionary (<code>A2_Group_WBS_Diagram.drawio</code>)</td>
            <td>Work packages 1.1 to 6.5 map 1:1 into ProjectLibre tasks &amp; Trello cards</td>
            <td style="text-align: center;"><span class="badge badge-low">Verified 100%</span></td>
          </tr>
          <tr>
            <td><strong>Schedule Management</strong></td>
            <td>ProjectLibre Master Gantt (<code>A2_GroupXX_ProjectLibre.pod</code>)</td>
            <td>Critical path dictates sprint priorities and zero-float milestones</td>
            <td style="text-align: center;"><span class="badge badge-low">Verified 100%</span></td>
          </tr>
          <tr>
            <td><strong>Cost Management</strong></td>
            <td>Cost Baseline Model (<code>A2_GroupXX_ProjectData.xlsx</code>)</td>
            <td>Labour and Capex rates establish EVM Planned Value ($385k BAC)</td>
            <td style="text-align: center;"><span class="badge badge-low">Verified 100%</span></td>
          </tr>
          <tr>
            <td><strong>Risk Management</strong></td>
            <td>5×5 Heat Map Matrix (<code>A2_GroupXX_ProjectData.xlsx</code>)</td>
            <td>Risks R01 &amp; R04 fund contingency reserve and security audit scopes</td>
            <td style="text-align: center;"><span class="badge badge-low">Verified 100%</span></td>
          </tr>
          <tr>
            <td><strong>Project Control</strong></td>
            <td>EVM Dashboard &amp; Trello Board Link</td>
            <td>Week 14 SPI/CPI variance triggers crashing &amp; fast-tracking actions</td>
            <td style="text-align: center;"><span class="badge badge-low">Verified 100%</span></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="prose">
      <p><strong>Final Evidence-Based Management Recommendation:</strong> Based on cumulative project evidence, the Project Management Team recommends that the Project Sponsor and University Steering Committee <strong>AUTHORIZE PROCEEDING TO FINAL PRODUCTION CUTOVER (GO-LIVE)</strong>. The project status has transitioned from Amber (Week 14) to <strong>Green (Week 20)</strong> following successful UAT completion and independent security penetration sign-off. The final projected cost at completion (EAC) is <strong>$406,300 AUD</strong>, fully contained within the $450,000 budget ceiling. The residual contingency reserve ($17,200) is released back to university central funds upon successful completion of the 30-day operational hypercare period.</p>
    </div>

    <!-- Tri-part Analysis Box -->
    <div class="analysis-container">
      <div class="analysis-header">
        <span>🔍 Section 6 Artefact Interpretation &amp; Management Logic</span>
      </div>
      <div class="analysis-grid">
        <div class="analysis-card shows">
          <div class="analysis-card-title">👁️ What it Shows</div>
          <p>The project health metrics confirm that all six milestone gates have been validated and critical path risks have been successfully retired.</p>
        </div>
        <div class="analysis-card important">
          <div class="analysis-card-title">⚡ Why it is Important</div>
          <p>It replaces subjective optimism with empirical evidence (zero P1 defects, 100% data fidelity, $43.7k budget headroom), providing executive confidence.</p>
        </div>
        <div class="analysis-card decision">
          <div class="analysis-card-title">🎯 Management Decision</div>
          <p>Formal recommendation to authorize blue-green production cutover on 17-Jul-2026 and initiate legacy software decommissioning to realize $120,000 in annual recurring savings.</p>
        </div>
      </div>
    </div>
  </section>

</div>

<!-- Modern Executive Footer -->
<footer>
  <div class="footer-content">
    <div class="footer-brand">
      <h4>Apex Metropolitan University — Project OmniPortal</h4>
      <p>BISY2004 Project Management | Secure Lane Assessment 2</p>
      <p style="font-size:0.75rem; color:#64748B; margin-top:0.4rem;">
        Tanvir Ahmed (238983) • Momen Ahmed (242048) • MD Rejvi Jaman Mafti (241964)
      </p>
    </div>
    <div class="footer-links">
      <a href="https://github.com/sadiksk07/omniportal-bisy2004" target="_blank">View GitHub Repository</a>
      <a href="https://trello.com/b/6aba6567933223c336fb8dfc/bisy2004-omniportal-student-portal-consolidation-%F0%9F%93%9A" target="_blank">Public Trello Board</a>
      <a href="#section1">Back to Top &uarr;</a>
    </div>
  </div>
</footer>

<script>
  // Reading Progress Bar
  window.addEventListener('scroll', () => {
    const winScroll = document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    document.getElementById('progress-bar').style.width = scrolled + '%';
  });

  // Active Link on Scroll Spy
  const sections = document.querySelectorAll('section');
  const navLinks = document.querySelectorAll('nav a:not(.nav-cta)');

  window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      if (pageYOffset >= sectionTop - 120) {
        current = section.getAttribute('id');
      }
    });
    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === '#' + current) {
        link.classList.add('active');
      }
    });
  });
</script>

</body>
</html>
'''
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Advanced, modern index.html successfully generated!")

if __name__ == "__main__":
    create_advanced_website()
