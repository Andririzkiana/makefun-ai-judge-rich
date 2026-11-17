# Entry for make.fun's ai-judge-rich-01 ("Make the AI judge rich"), Python 3.13, standard library only.
#
# The program writes one fixed plan to /output/entry.txt: how an AI agent with $100, a computer with
# internet access and 30 days, and no human help, ends the 30 days with the most money. The sealed gate
# requires UTF-8 text of 1 to 1,000 Unicode code points with at least one non-whitespace character, and
# the judge reads exactly the bytes written, line ends included -- so the plan below carries no trailing
# line end. The program is deterministic: every run writes the same bytes.
#
# The grader runs `python3 -P -s /bot/main.py` with nothing installed, so everything lives in this one
# file and only the standard library is imported. Outside the grader's container, MAKEFUN_OUTPUT_DIR
# stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Day 1: Pick one vertical — US dental clinics with no online booking. Scrape Google Maps for 3,000 clinics: name, phone, email, booking status. Verify emails with $20 of API credit. The offer: a lapsed-patient reactivation list — 200 cleaned contacts per clinic, ready to message. Start emailing the same afternoon the list is built.",
        "Days 2–30: Send 150 cold emails a day from a $12 domain: '47 patients who stopped booking'. Price $149 per list, $299 with outreach drafts included. Every first email carries a free sample of 10 contacts — proof before payment, paid by Stripe link. Every reply gets a same-day answer and delivery within 48 hours.",
        "The math: 4,000 emails, 2% reply, a quarter of replies buy: 20 sales × $149 ≈ $2,980. Costs stay under $60; the rest of the $100 stays in reserve until the first sale lands, then funds a second vertical: med spas.",
        "Edge: one vertical, one painful problem, proof first. A thousand agents sell generic leads. I sell one clinic its own patients back.",
    ]
)

# The grader provides a writable /output; creating the directory when it is missing only matters for
# local runs against a fresh MAKEFUN_OUTPUT_DIR, and changes nothing about the bytes written.
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
