-- Query that gives average response time for each request
SELECT requesttime, currentstatus, Victim_RequesterID_id, deliverytime,
       CASE
           WHEN deliverytime IS NULL THEN NULL
           ELSE JulianDay(deliverytime) - JulianDay(requesttime)
       END AS Response_Time
FROM myapp_request;

-- Query that gives overall mean response time
SELECT AVG(a.Response_Time) AS mean_response_time
FROM (SELECT requesttime, currentstatus, Victim_RequesterID_id, deliverytime,
           CASE
               WHEN deliverytime IS NULL THEN NULL
               ELSE JulianDay(deliverytime) - JulianDay(requesttime)
           END AS Response_Time
    FROM myapp_request) a;

-- Query that gives average response times based on districts
SELECT ad.DistrictName, ad.Coordination, ad.Population, AVG(ad.Response_Time) AS mean_response_time
FROM
(
SELECT *,  CASE
               WHEN deliverytime IS NULL THEN NULL
               ELSE JulianDay(deliverytime) - JulianDay(requesttime)
           END AS Response_Time
FROM myapp_request mr
LEFT JOIN
myapp_victim mv, myapp_district md
         WHERE mr.Victim_RequesterID_id = mv.id AND
         mv.District_DistrictID_id = md.id) ad
GROUP BY ad.DistrictName
