import datetime
from typing import List

from models.location import Location
from models.reports import Report

__reports: List[Report] = []


async def get_reports() -> List[Report]:
    return list(__reports)


async def add_report(description: str, location: Location) -> object:
    now = datetime.datetime.now()
    report = Report(location=location, description=description, created_date=now)

    __reports.append(report)
    __reports.sort(key=lambda r: r.created_date, reverse=True)

    return report
