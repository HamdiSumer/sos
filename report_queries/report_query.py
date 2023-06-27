import csv
from django.db import connection

query_time_difference = "SELECT requesttime, currentstatus, Victim_RequesterID_id, deliverytime, CASE WHEN deliverytime IS NULL THEN NULL ELSE deliverytime - requesttime END AS Response_Time FROM myapp_request"
query_average_response_time_overall = "SELECT AVG(a.Response_Time) AS mean_response_tim FROM (SELECT requesttime, currentstatus, Victim_RequesterID_id, deliverytime, CASE WHEN deliverytime IS NULL THEN NULL ELSE deliverytime - requesttime AS Response_Time FROM myapp_request) a"
query_average_response_time_by_district = "SELECT ad.DistrictName, ad.Coordination, ad.Population, AVG(ad.Response_Time) AS  FROM ( SELECT *,  CASE WHEN deliverytime IS NULL THEN NULL ELSE deliverytime - requesttime END AS  FROM myapp_request mr LEFT JOIN myapp_victim mv, myapp_district md mr.Victim_RequesterID_id = mv.id AND mv.District_DistrictID_id = md.id) ad ad.DistrictName"

# Run your query
with connection.cursor() as cursor:
    cursor.execute(query_time_difference)
    results = cursor.fetchall()

# Define the CSV file path
csv_file_path = "report_1.csv"

# Save the results as a CSV file
with open(csv_file_path, "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(results)

print("CSV file saved successfully!")