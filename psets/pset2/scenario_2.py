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
    print("Successfully connected for Scenario 2.\n")

    # task 1: salary and experience analysis (passaic county)
    print("### task 1: passaic county salary vs experience ###")

    query_passaic_trend = """
    SELECT experience_total, AVG(salary)
    FROM nj_teachers_salaries
    WHERE county = 'Passaic'
    GROUP BY experience_total
    ORDER BY experience_total;
    """
    cursor.execute(query_passaic_trend)
    passaic_data = cursor.fetchall()

    # display snippet
    print("Passaic Avg Salary for Years 10-15:")
    for year, salary in passaic_data:
        if 10 <= year <= 15:
            print(f"Year {year}: ${salary:,.2f}")

    # task 2: retention strategy (passaic only, >10 years)
    print("\n### task 2: passaic retention strategy (>10 years experience) ###")

    query_passaic_experienced = """
    SELECT AVG(salary) as avg_salary, COUNT(*) as teacher_count
    FROM nj_teachers_salaries
    WHERE county = 'Passaic' AND experience_total > 10;
    """
    cursor.execute(query_passaic_experienced)
    passaic_exp = cursor.fetchone()
    print(f"Passaic Avg Salary (>10 Years): ${passaic_exp[0]:,.2f}")
    print(f"Passaic Teacher Count (>10 Years): {passaic_exp[1]}")

    # task 3: cross-county comparison
    print("\n### task 3: cross-county comparison (>10 years experience) ###")

    # compare passaic with neighbors (bergen, essex, morris, sussex)
    query_neighbors = """
    SELECT county, AVG(salary) as avg_salary
    FROM nj_teachers_salaries
    WHERE experience_total > 10
    AND county IN ('Passaic', 'Bergen', 'Essex', 'Morris', 'Sussex')
    GROUP BY county
    ORDER BY avg_salary DESC;
    """
    cursor.execute(query_neighbors)
    neighbor_data = cursor.fetchall()

    print("Average Salary for Experienced Teachers (>10 Years):")
    for county, salary in neighbor_data:
        print(f"{county}: ${salary:,.2f}")

    # task 4: recommendations
    print("\n### task 4: retention strategy recommendations ###")
    print(
        "1. Passaic ranks 2nd out of 5 neighboring counties for experienced teachers, with an average salary of $90,709. The gap with Bergen ($93,020) is only about $2,300 - close enough that targeted incentives could close it without a major overhaul."
    )
    print(
        "2. With 8,238 teachers over 10 years of experience, Passaic has a sizable experienced workforce. The salary progression from year 10 ($68k) to year 15 ($84k) shows strong growth of roughly $3,200/year, which likely contributes to retention."
    )
    print(
        "3. To stay competitive, Passaic should focus on maintaining its edge over Essex, Morris, and Sussex while exploring small moves - like milestone bonuses at year 10 or 15 - to close the gap with Bergen and potentially take the lead."
    )

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if "conn" in locals() and conn.is_connected():
        cursor.close()
        conn.close()
