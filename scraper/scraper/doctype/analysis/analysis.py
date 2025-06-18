"""DocType server script for Analysis."""
from __future__ import annotations

from typing import Optional

import frappe
from frappe.model.document import Document


class Analysis(Document):
    """Holds processed metrics for a Scrape Job."""

    @frappe.whitelist()
    def get_latest(self) -> Optional[str]:
        """Return the most recent Plotly graph URL for this job."""
        latest = (
            frappe.get_all(
                "Analysis",
                filters={"scrape_job": self.scrape_job},
                fields=["graph_url"],
                order_by="creation desc",
                limit_page_length=1,
            )
        )
        return latest[0].graph_url if latest else None

# EOF
