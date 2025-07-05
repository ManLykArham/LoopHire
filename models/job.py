"""
job.py
-------
Defines the Job data model used to store and manipulate job data.
"""

from typing import Optional


class Job:
    """
    Represents a single job listing with relevant fields.
    """

    def __init__(
        self,
        id: str,
        title: str,
        company: Optional[str],
        location: Optional[str],
        created: Optional[str],
        category: Optional[str],
        contract: Optional[str],
        salary: Optional[str],
        url: Optional[str],
        description: Optional[str]
    ):
        self.id = id
        self.title = title
        self.company = company or "N/A"
        self.location = location or "N/A"
        self.created = created or "N/A"
        self.category = category or "N/A"
        self.contract = contract or "N/A"
        self.salary = salary or "N/A"
        self.url = url or "N/A"
        self.description = description or "N/A"

    def to_dict(self) -> dict:
        """
        Converts the Job object into a dictionary for saving to JSON.
        """
        return {
            "id": self.id,
            "title": self.title,
            "company": self.company,
            "location": self.location,
            "created": self.created,
            "category": self.category,
            "contract": self.contract,
            "salary": self.salary,
            "url": self.url,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Creates a Job object from a dictionary (e.g., when loading from JSON).
        """
        return cls(
            id=data.get("id", ""),
            title=data.get("title", "N/A"),
            company=data.get("company"),
            location=data.get("location"),
            created=data.get("created"),
            category=data.get("category"),
            contract=data.get("contract"),
            salary=data.get("salary"),
            url=data.get("url"),
            description=data.get("description")
        )
