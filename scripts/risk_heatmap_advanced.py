#!/usr/bin/env python3
"""
Advanced IT Risk Heatmap Generator
=====================================
Author: Akshaya | GRC Portfolio
Usage: python risk_heatmap_advanced.py

Generates professional risk visualisation from risk register data.
Install: pip install matplotlib numpy
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
from datetime import datetime

RISKS = [
    {"id": "R-001", "name": "Ransomware Attack", "l": 4, "i": 5, "treatment": "Mitigate", "sector": "All"},
    {"id": "R-002", "name": "Privileged Account\nCompromise", "l": 3, "i": 5, "treatment": "Mitigate", "sector": "Banking"},
    {"id": "R-003", "name": "Third-Party Vendor\nBreach", "l": 3, "i": 5, "treatment": "Mitigate", "sector": "All"},
    {"id": "R-004", "name": "Business Email\nCompromise (BEC)", "l": 4, "i": 4, "treatment": "Mitigate", "sector": "Banking"},
    {"id": "R-005", "name": "Unpatched Critical\nVulnerability", "l": 4, "i": 4, "treatment": "Mitigate", "sector": "All"},
    {"id": "R-006", "name": "Data Breach / GDPR\nViolation", "l": 3, "i": 5, "treatment": "Mitigate", "sector": "All"},
    {"id": "R-007", "name": "Insider Threat /\nIP Theft", "l": 2, "i": 5, "treatment": "Mitigate", "sector": "Defence"},
    {"id": "R-008", "name": "Cloud\nMisconfiguration", "l": 4, "i": 4, "treatment": "Mitigate", "sector": "Tech"},
    {"id": "R-009", "name": "BCP / DR\nFailure", "l": 2, "i": 5, "treatment": "Accept", "sector": "All"},
    {"id": "R-010", "name": "Change Management\nFailure (SOX)", "l": 3, "i": 4, "treatment": "Mitigate", "sector": "Banking"},
    {"id": "R-011", "name": "IT/OT Network\nBreach", "l": 3, "i": 5, "treatment": "Mitigate", "sector": "Energy"},
    {"id": "R-012", "name": "Phishing /\nBEC Attack", "l": 5, "i": 3, "treatment": "Mitigate", "sector": "All"},
]

TREATMENT_COLORS = {
    "Mitigate": "#b8892a",
    "Transfer": "#2a6b6e",
    "Avoid":    "#8b3a4a",
    "Accept":   "#4a7a4a",
}

def get_risk_color(score):
    if score >= 20: return "#c62828"
    elif score >= 15: return "#d84315"
    elif score >= 12: return "#e65100"
    elif score >= 8:  return "#f57c00"
    elif score >= 6:  return "#f9a825"
    else:             return "#388e3c"

def create_dashboard(risks, output="risk_dashboard.png"):
    fig = plt.figure(figsize=(20, 12), facecolor='#0f0e0c')
    gs = fig.add_gridspec(2, 3, hspace=0.38, wspace=0.32,
                          left=0.05, right=0.97, top=0.90, bottom=0.07)

    # ── Plot 1: Risk Scatter Heatmap ──
    ax1 = fig.add_subplot(gs[0, :2])
    ax1.set_facecolor('#1a1814')

    # Risk zone background
    x = np.linspace(0.5, 5.5, 100)
    y = np.linspace(0.5, 5.5, 100)
    X, Y = np.meshgrid(x, y)
    Z = X * Y
    cmap = LinearSegmentedColormap.from_list('risk',
        ['#1b5e20', '#2e7d32', '#f9a825', '#e65100', '#c62828'])
    ax1.contourf(X, Y, Z, levels=20, cmap=cmap, alpha=0.15)

    # Plot risks
    offset_tracker = {}
    for r in risks:
        key = (r['l'], r['i'])
        n = offset_tracker.get(key, 0)
        offset_tracker[key] = n + 1
        ox, oy = n * 0.18, n * 0.18
        score = r['l'] * r['i']
        color = get_risk_color(score)
        ax1.scatter(r['l'] + ox, r['i'] + oy, c=color, s=320, zorder=5,
                   edgecolors='white', linewidths=1.5, alpha=0.95)
        ax1.annotate(r['id'], (r['l'] + ox, r['i'] + oy),
                    xytext=(10, 5), textcoords='offset points',
                    fontsize=7.5, color='white', fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.2', fc=color, alpha=0.75, ec='none'))

    ax1.set_xlim(0.5, 5.7); ax1.set_ylim(0.5, 5.7)
    ax1.set_xlabel('LIKELIHOOD  →', color='#b8892a', fontsize=10, fontweight='bold', labelpad=8)
    ax1.set_ylabel('IMPACT  →', color='#b8892a', fontsize=10, fontweight='bold', labelpad=8)
    ax1.set_title('Risk Heatmap — Inherent Risk Positions', color='#f5f0e8',
                  fontsize=12, fontweight='bold', pad=10)
    ax1.set_xticks(range(1, 6))
    ax1.set_xticklabels(['1 Rare', '2 Unlikely', '3 Possible', '4 Likely', '5 Almost\nCertain'],
                        color='#8a8579', fontsize=8)
    ax1.set_yticks(range(1, 6))
    ax1.set_yticklabels(['1 Negligible', '2 Minor', '3 Moderate', '4 Major', '5 Critical'],
                        color='#8a8579', fontsize=8)
    ax1.tick_params(colors='#8a8579')
    ax1.grid(True, alpha=0.06, color='white', linestyle='--')
    for sp in ax1.spines.values(): sp.set_edgecolor('#2a2820')

    level_patches = [
        mpatches.Patch(fc='#c62828', label='Critical (≥20)'),
        mpatches.Patch(fc='#e65100', label='High (12–19)'),
        mpatches.Patch(fc='#f57c00', label='Medium (6–11)'),
        mpatches.Patch(fc='#388e3c', label='Low (<6)'),
    ]
    ax1.legend(handles=level_patches, loc='lower right',
              facecolor='#1a1814', labelcolor='white', fontsize=8,
              edgecolor='#3a3830', title='Risk Level', title_fontsize=8)

    # ── Plot 2: Risk Score Bar Chart ──
    ax2 = fig.add_subplot(gs[0, 2])
    ax2.set_facecolor('#1a1814')
    sorted_r = sorted(risks, key=lambda x: x['l']*x['i'], reverse=True)[:10]
    scores = [r['l']*r['i'] for r in sorted_r]
    labels = [r['id'] for r in sorted_r]
    colors_list = [get_risk_color(s) for s in scores]
    bars = ax2.barh(range(len(labels)), scores, color=colors_list,
                   alpha=0.85, edgecolor='#2a2820', linewidth=0.5)
    ax2.set_yticks(range(len(labels)))
    ax2.set_yticklabels(labels, color='#c8c0b0', fontsize=8.5)
    ax2.set_xlabel('Risk Score', color='#b8892a', fontsize=9)
    ax2.set_title('Top Risks — Priority Order', color='#f5f0e8', fontsize=11, fontweight='bold', pad=10)
    for bar, score in zip(bars, scores):
        ax2.text(bar.get_width()+0.2, bar.get_y()+bar.get_height()/2,
                str(score), va='center', color='white', fontsize=8, fontweight='bold')
    for x_val, color, label in [(20,'#c62828','Critical'), (12,'#e65100','High'), (6,'#f9a825','Medium')]:
        ax2.axvline(x=x_val, color=color, linestyle='--', alpha=0.4, linewidth=1)
    ax2.tick_params(colors='#8a8579')
    ax2.set_facecolor('#1a1814')
    for sp in ax2.spines.values(): sp.set_edgecolor('#2a2820')
    ax2.grid(True, alpha=0.06, axis='x', color='white', linestyle='--')
    ax2.invert_yaxis()

    # ── Plot 3: Treatment Distribution Pie ──
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.set_facecolor('#1a1814')
    treatment_counts = {}
    for r in risks:
        treatment_counts[r['treatment']] = treatment_counts.get(r['treatment'], 0) + 1
    labels_p = list(treatment_counts.keys())
    sizes_p = list(treatment_counts.values())
    colors_p = [TREATMENT_COLORS.get(l, '#666') for l in labels_p]
    wedges, texts, autotexts = ax3.pie(sizes_p, labels=labels_p, colors=colors_p,
                                        autopct='%1.0f%%', startangle=90,
                                        pctdistance=0.75, labeldistance=1.15,
                                        wedgeprops=dict(edgecolor='#1a1814', linewidth=2))
    for t in texts: t.set_color('#c8c0b0'); t.set_fontsize(9)
    for at in autotexts: at.set_color('white'); at.set_fontsize(8); at.set_fontweight('bold')
    ax3.set_title('Risk Treatment Distribution', color='#f5f0e8', fontsize=11, fontweight='bold', pad=10)

    # ── Plot 4: Sector Distribution ──
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.set_facecolor('#1a1814')
    sector_counts = {}
    for r in risks:
        sector_counts[r['sector']] = sector_counts.get(r['sector'], 0) + 1
    sectors = list(sector_counts.keys())
    s_counts = list(sector_counts.values())
    s_colors = ['#b8892a','#2a6b6e','#8b3a4a','#4a7a4a','#7b5ea7','#3a5a8a']
    bars2 = ax4.bar(sectors, s_counts,
                    color=s_colors[:len(sectors)], alpha=0.85,
                    edgecolor='#2a2820', linewidth=0.5)
    ax4.set_title('Risks by Sector', color='#f5f0e8', fontsize=11, fontweight='bold', pad=10)
    ax4.set_ylabel('Count', color='#b8892a', fontsize=9)
    ax4.tick_params(colors='#8a8579', axis='both')
    for bar in bars2:
        ax4.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.05,
                str(int(bar.get_height())), ha='center', va='bottom',
                color='white', fontsize=9, fontweight='bold')
    for sp in ax4.spines.values(): sp.set_edgecolor('#2a2820')
    ax4.set_facecolor('#1a1814')
    ax4.grid(True, alpha=0.06, axis='y', color='white')

    # ── Plot 5: Risk Level Summary ──
    ax5 = fig.add_subplot(gs[1, 2])
    ax5.set_facecolor('#1a1814')
    ax5.axis('off')
    critical = sum(1 for r in risks if r['l']*r['i'] >= 20)
    high     = sum(1 for r in risks if 12 <= r['l']*r['i'] < 20)
    medium   = sum(1 for r in risks if 6 <= r['l']*r['i'] < 12)
    low      = sum(1 for r in risks if r['l']*r['i'] < 6)
    summary_data = [
        ('🔴 CRITICAL', critical, '#c62828'),
        ('🟠 HIGH',     high,     '#e65100'),
        ('🟡 MEDIUM',   medium,   '#f57c00'),
        ('🟢 LOW',      low,      '#388e3c'),
    ]
    ax5.set_title('Risk Summary', color='#f5f0e8', fontsize=11, fontweight='bold', pad=10)
    for idx, (label, count, color) in enumerate(summary_data):
        y_pos = 0.75 - idx * 0.22
        ax5.text(0.05, y_pos+0.08, label, transform=ax5.transAxes,
                fontsize=11, color=color, fontweight='bold', va='center')
        ax5.text(0.75, y_pos+0.08, str(count), transform=ax5.transAxes,
                fontsize=22, color=color, fontweight='bold', va='center')
        ax5.plot([0.05, 0.95], [y_pos-0.03, y_pos-0.03],
                transform=ax5.transAxes, color='#2a2820', linewidth=0.8)
    ax5.text(0.5, 0.03, f'Total: {len(risks)} risks assessed',
            transform=ax5.transAxes, ha='center', color='#8a8579', fontsize=9)

    fig.suptitle(
        f'IT Risk Dashboard  |  Generated {datetime.now().strftime("%d %B %Y")}',
        color='#f5f0e8', fontsize=14, fontweight='bold', y=0.96
    )
    plt.savefig(output, dpi=150, bbox_inches='tight',
               facecolor='#0f0e0c', edgecolor='none')
    plt.close()
    print(f"✅ Dashboard saved: {output}")
    print(f"   Critical: {critical} | High: {high} | Medium: {medium} | Low: {low}")

if __name__ == '__main__':
    create_dashboard(RISKS)
