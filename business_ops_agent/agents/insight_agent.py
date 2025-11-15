from memory.invoice_db import summary_stats

def get_insights():
    stats = summary_stats()
    insights = []

    if stats["overdue"] > 0:
        insights.append(f"{stats['overdue']} overdue invoices. Follow up immediately.")

    if stats["due_soon"] > 0:
        insights.append(f"{stats['due_soon']} invoices due in next 7 days.")

    if not insights:
        insights.append("All invoices up to date.")

    return {"stats": stats, "insights": insights}
