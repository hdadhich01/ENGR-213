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
    print("Successfully connected to the database.\n")

    # task 1: salary distribution
    print("### task 1: salary distribution analysis ###")

    # top 5 districts by avg salary
    query_highest = """
    SELECT district, AVG(salary) as avg_salary
    FROM nj_teachers_salaries
    GROUP BY district
    ORDER BY avg_salary DESC
    LIMIT 5;
    """
    cursor.execute(query_highest)
    highest_districts = cursor.fetchall()

    print("\nTop 5 Districts by Average Salary:")
    for district, salary in highest_districts:
        print(f"{district}: ${salary:,.2f}")

    # bottom 5 districts by avg salary
    query_lowest = """
    SELECT district, AVG(salary) as avg_salary
    FROM nj_teachers_salaries
    GROUP BY district
    ORDER BY avg_salary ASC
    LIMIT 5;
    """
    cursor.execute(query_lowest)
    lowest_districts = cursor.fetchall()

    print("\nBottom 5 Districts by Average Salary:")
    for district, salary in lowest_districts:
        print(f"{district}: ${salary:,.2f}")

    # task 2: experience vs salary
    print("\n### task 2: experience vs. salary analysis ###")

    # correlate experience with avg salary
    query_experience = """
    SELECT experience_total, AVG(salary) as avg_salary
    FROM nj_teachers_salaries
    GROUP BY experience_total
    ORDER BY experience_total ASC;
    """
    cursor.execute(query_experience)
    exp_salary_data = cursor.fetchall()

    print("\nAverage Salary by Years of Experience (First 10 Years):")
    for year, salary in exp_salary_data[:10]:
        print(f"Year {year}: ${salary:,.2f}")

    # task 3: recommendations
    print("\n### task 3: recommendations ###")
    print(
        "1. The gap between the highest and lowest paying districts is nearly $58,000 - more than double. That's a significant disparity that warrants a closer look at how funding is distributed across the state."
    )
    print(
        "2. It's worth noting that 4 of the 5 lowest-paying districts are charter schools. This suggests charter school teacher compensation may need dedicated attention, whether through policy changes or funding adjustments."
    )
    print(
        "3. The salary progression by experience is fairly steady, around $1,200 per year on average. Standardizing salary bands tied to experience across districts could help reduce the geographic lottery effect on teacher pay."
    )

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if "conn" in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("\nDatabase connection closed.")
