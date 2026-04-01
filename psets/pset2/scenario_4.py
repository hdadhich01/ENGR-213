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
    print("Successfully connected for Scenario 4.\n")

    # task 1: starting salary analysis (0-5 years)
    print("### task 1: starting salary analysis (0-5 years) ###")

    query_starting_salary = """
    SELECT AVG(salary)
    FROM nj_teachers_salaries
    WHERE experience_total BETWEEN 0 AND 5;
    """
    cursor.execute(query_starting_salary)
    start_avg = cursor.fetchone()[0]
    print(f"Average Salary for New Teachers (0-5 Years): ${start_avg:,.2f}")

    # task 2: salary progression
    print("\n### task 2: salary progression (year 0 to 5) ###")

    query_progression = """
    SELECT experience_total, AVG(salary)
    FROM nj_teachers_salaries
    WHERE experience_total BETWEEN 0 AND 5
    GROUP BY experience_total
    ORDER BY experience_total;
    """
    cursor.execute(query_progression)
    progression_data = cursor.fetchall()

    for year, salary in progression_data:
        print(f"Year {year}: ${salary:,.2f}")

    # task 3: retention factors (proxy via count)
    print("\n### task 3: retention factors (teacher count drop-off) ###")

    # count of teachers at each year - sharp drop indicates attrition
    query_retention = """
    SELECT experience_total, COUNT(*) as teacher_count
    FROM nj_teachers_salaries
    WHERE experience_total BETWEEN 0 AND 10
    GROUP BY experience_total
    ORDER BY experience_total;
    """
    cursor.execute(query_retention)
    retention_data = cursor.fetchall()

    for year, count in retention_data:
        print(f"Year {year}: {count} teachers")

    # task 4: recommendations
    print("\n### task 4: salary structure recommendations ###")
    print(
        "1. The biggest drop-off happens between year 5 and year 6 - teacher count falls from 10,872 to 8,462, a 22% decline in a single year. This suggests year 5-6 is the critical retention window, not years 3-5. A retention bonus or milestone incentive at year 5 could help stem this loss."
    )
    print(
        "2. Salary growth from year 1 to year 2 is almost flat - just $244. Meanwhile, teacher count drops by nearly 2,700 in that same period. Bumping the year 2 raise could help retain teachers through that early transition when many leave."
    )
    print(
        "3. Interestingly, after year 6 the numbers start climbing back up through year 10. Teachers who make it past the 6-year mark seem more likely to stay long-term. This reinforces the idea that early-career retention efforts (years 1-6) are where the investment matters most."
    )

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if "conn" in locals() and conn.is_connected():
        cursor.close()
        conn.close()
