import os
import re

import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            os.makedirs("reports/screenshots", exist_ok=True)

            safe_name = re.sub(
                r"[^A-Za-z0-9_.-]+",
                "_",
                item.name,
            )

            screenshot_path = os.path.join(
                "reports",
                "screenshots",
                f"{safe_name}.png",
            )

            page.screenshot(
                path=screenshot_path,
                full_page=True,
            )

            print(
                f"\nFailure screenshot saved: "
                f"{screenshot_path}"
            )