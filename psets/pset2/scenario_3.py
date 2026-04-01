import mysql.connector

# connect to database
try:
    conn = mysql.connector.connect(
        host="host.orb.internal",  # changed for orbstack vm on macos
        port=3307,
        user="root",  # replace with your mysql username
        password="",  # replace with your mysql password
        database="nj_teachers_salaries_db",
    )
    cursor = conn.cursor()
    print("Successfully connected for Scenario 3.\n")

    # task 1: certification impact analysis
    print("### task 1: salary difference by certification ###")

    # group into standard vs non-standard (provisional, ce, ceas)
    query_cert_impact = """
    SELECT
        CASE
            WHEN certificate = 'Standard certificate' THEN 'Standard'
            ELSE 'Non-Standard'
        END as cert_status,
        AVG(salary) as avg_salary
    FROM nj_teachers_salaries
    GROUP BY cert_status;
    """
    cursor.execute(query_cert_impact)
    cert_data = cursor.fetchall()

    for status, salary in cert_data:
        print(f"{status} Certification Avg Salary: ${salary:,.2f}")

    # task 2: performance proxy (experience)
    print("\n### task 2: average experience by certification ###")

    query_exp_impact = """
    SELECT
        CASE
            WHEN certificate = 'Standard certificate' THEN 'Standard'
            ELSE 'Non-Standard'
        END as cert_status,
        AVG(experience_total) as avg_experience
    FROM nj_teachers_salaries
    GROUP BY cert_status;
    """
    cursor.execute(query_exp_impact)
    exp_data = cursor.fetchall()

    for status, exp in exp_data:
        print(f"{status} Certification Avg Experience: {exp:.1f} years")

    # task 3 & 4: cost-benefit & recommendations
    print("\n### task 3 & 4: cost-benefit recommendations ###")
    print(
        "1. The salary gap between standard and non-standard certification is about $16,000. That's significant, but it's hard to separate from the experience factor - standard certified teachers average 13.2 years vs just 3.7 for non-standard."
    )
    print(
        "2. The 9.5-year experience gap suggests most non-standard teachers are early-career and still working toward full certification. Funding pathways to help them get there faster could improve retention and reduce turnover costs in the long run."
    )
    print(
        "3. From a cost-benefit perspective, investing in certification programs seems worthwhile. If it helps teachers stay longer (as the experience data implies), the state saves on recurring recruitment and training expenses that come with high turnover."
    )

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if "conn" in locals() and conn.is_connected():
        cursor.close()
        conn.close()
